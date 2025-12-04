# examples/json_prompt_test.py
from dotenv import load_dotenv
import os, requests, json, re

load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')
if not API_KEY:
    raise SystemExit('OPENAI_API_KEY not set')

URL = 'https://api.openai.com/v1/chat/completions'
headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}

system = 'You are a concise summarizer. Use ONLY provided CONTEXT. If info not in CONTEXT, return {"bullets": [], "note":"Not found"}. Always return valid JSON.'
context = 'Python — язык программирования, широко используемый для анализа данных и веб-разработки.'
user = f'CONTEXT:\\n{context}\\nQuestion: Summarize into up to 3 bullets, each ≤20 words. Return exactly JSON: {{\"bullets\": [...], \"sources\": []}}'

payload = {
    'model': 'gpt-4o-mini',
    'messages': [
        {'role': 'system', 'content': system},
        {'role': 'user', 'content': user}
    ],
    'max_tokens': 200,
    'temperature': 0.0
}

r = requests.post(URL, headers=headers, json=payload, timeout=30)
r.raise_for_status()
raw = r.json()
raw_text = (raw.get('choices') or [{}])[0].get('message', {}).get('content') or raw.get('choices', [{}])[0].get('text') or ''
print("RAW RESPONSE:\n", raw_text)

# Try parse JSON directly
try:
    obj = json.loads(raw_text)
    print("\nParsed JSON OK:", json.dumps(obj, indent=2, ensure_ascii=False))
except Exception as e:
    print("\nJSON parse error:", e)
    m = re.search(r'\{.*\}', raw_text, flags=re.S)
    if m:
        try:
            obj2 = json.loads(m.group(0))
            print("\nRecovered JSON:", json.dumps(obj2, indent=2, ensure_ascii=False))
        except Exception as e2:
            print("Recovery failed:", e2)
