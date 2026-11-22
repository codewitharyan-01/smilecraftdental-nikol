# -*- coding: utf-8 -*-
"""Repair vercel.json — the old constant contained an illegal JSON escape.

`"/(.*)\\.html"` written through a Python string became `"/(.*)\.html"` on disk.
JSON does not permit `\.`, so Vercel rejected the config as invalid JSON.
The .html cache rule is dropped entirely: Vercel's defaults are already correct
for static HTML, and removing it leaves the file free of every backslash.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_PY = os.path.join(ROOT, "_build", "build.py")

NEW = """{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "trailingSlash": false,
  "headers": [
    {
      "source": "/assets/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    },
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
        { "key": "Permissions-Policy", "value": "geolocation=(), microphone=(), camera=()" }
      ]
    }
  ]
}"""

# 1. Prove the current file is broken, and show why.
old_path = os.path.join(ROOT, "vercel.json")
if os.path.exists(old_path):
    raw = open(old_path, encoding="utf-8").read()
    try:
        json.loads(raw)
        print("old vercel.json: parsed OK (no repair needed?)")
    except Exception as e:
        print("old vercel.json: INVALID -> %s" % e)
        for i, line in enumerate(raw.splitlines(), 1):
            if "\\.html" in line:
                print("  offending line %d: %s" % (i, line.strip()))

# 2. Validate the replacement before writing anything.
json.loads(NEW)
print("replacement: parses as valid JSON")

# 3. Patch the generator so a rebuild cannot reintroduce the bug.
src = open(BUILD_PY, encoding="utf-8").read()
marker = 'VERCEL = """'
start = src.index(marker)
end = src.index('"""', start + len(marker)) + 3
src = src[:start] + marker + NEW + '"""' + src[end:]
open(BUILD_PY, "w", encoding="utf-8", newline="\n").write(src)
print("build.py: VERCEL constant replaced")

# 4. Write the corrected file.
with open(old_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(NEW + "\n")
print("vercel.json: rewritten")
