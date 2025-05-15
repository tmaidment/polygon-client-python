import urllib.request
import json

contents = urllib.request.urlopen("https://polygon.theedman.com:8000/openapi").read()
parsed = json.loads(contents)
formatted = json.dumps(parsed, indent=2)
with open(".polygon/rest.json", "w") as f:
    f.write(formatted)
