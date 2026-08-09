#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import io
import json
from youtube_search import YoutubeSearch

# Force UTF-8 encoding for stdout/stderr
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Search YouTube
results = YoutubeSearch('arsenal', max_results=10).to_dict()

# Print results with proper formatting
print(f"Found {len(results)} results:\n")
print("=" * 80)

for i, video in enumerate(results, 1):
    print(f"\n{i}. {video.get('title', 'No title')}")
    print(f"   Channel: {video.get('channel', 'N/A')}")
    print(f"   Duration: {video.get('duration', 'N/A')}")
    print(f"   Views: {video.get('views', 'N/A')}")
    print(f"   URL: https://youtube.com{video.get('url_suffix', '')}")
    print("-" * 80)

# Save to JSON
with open('youtube_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n✅ Saved results to youtube_results.json")