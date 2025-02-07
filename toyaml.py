import json
import yaml
import requests

url = "https://script.google.com/macros/s/AKfycbzkHvVaplMOJp9tkEoJTX7-X0hy6o6IQz94tm4xyUBaA-Pf50LuEtwqOCgbHmModBDc5A/exec"

response = requests.get(url)
data = response.json()

with open('_data/seminars.yml', 'w', encoding='utf8') as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False)
