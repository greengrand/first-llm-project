from dotenv import load_dotenv
import os
import requests
import time
import json
import random

load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')
if not API_KEY:
    raise SystemExit('OPENAI_API_KEY not set')

URL = 'https://api.openai.com/v1/chat/completions'
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def post_with_retry(url, headers, payload, tries=4, initial_delay=1, backoff=2):
    """
    Simple retry for 429 rate limits with exponential backoff + small jitter.
    Returns the last response (may be 429).
    """
    last_resp = None
    for i in range(tries):
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=30)
            last_resp = r
        except Exception as e:
            # Network error — retry on exception except on last try
            print(f"Request exception: {e}")
            if i == tries - 1:
                raise
            wait = initial_delay * (backoff ** i) + random.uniform(0, 0.5)
            print(f"Sleeping {wait:.1f}s before retrying (exception)...")
            time.sleep(wait)
            continue

        if r.status_code == 429:
            # rate-limited — backoff and retry
            wait = initial_delay * (backoff ** i) + random.uniform(0, 0.5)
            print(f"Rate limited (429). Sleeping {wait:.1f}s and retrying... (attempt {i+1}/{tries})")
            time.sleep(wait)
            continue
        # any other status — return immediately
        return r
    # exhausted retries — return last response (likely 429) so caller can handle it
    return last_resp

temperatures = [0.0, 0.2, 0.7, 1.0]
prompt = 'Напиши короткое (1-2 предложения) приветствие для пользователя, упомяни слово Python.'

results = []
for t in temperatures:
    payload = {
        'model': 'gpt-4o-mini',
        'messages': [
            {'role': 'system', 'content': 'You are a concise assistant.'},
            {'role': 'user', 'content': prompt}
        ],
        'max_tokens': 60,
        'temperature': t
    }
    start = time.time()
    r = post_with_retry(URL, headers, payload, tries=4)
    elapsed = time.time() - start
    if r is None:
        text = 'ERROR: no response (requests failed)'
    elif r.status_code != 200:
        text = f'ERROR {r.status_code}: {r.text}'
    else:
        data = r.json()
        text = (data.get('choices') or [{}])[0].get('message', {}).get('content') or data.get('choices', [{}])[0].get('text')
    entry = {'temperature': t, 'time': round(elapsed,2), 'response': text}
    results.append(entry)
    print(f"\n=== temperature={t} (time {entry['time']}s) ===\n{entry['response']}\n")

# save results to file
out_path = 'logs/temperature_test_results.json'
os.makedirs('logs', exist_ok=True)
with open(out_path, 'w', encoding='utf8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"Saved results to {out_path}")
