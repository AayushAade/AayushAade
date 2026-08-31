#!/usr/bin/env python3
import os
import json
import urllib.request

USERNAME = "AayushAade"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def fetch_json(url):
    headers = {"User-Agent": "GitHub-Stats-Generator"}
    if TOKEN:
        headers["Authorization"] = f"token {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

def get_stats():
    user = fetch_json(f"https://api.github.com/users/{USERNAME}")
    repos = fetch_json(f"https://api.github.com/users/{USERNAME}/repos?per_page=100")
    
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
    total_forks = sum(r.get("forks_count", 0) for r in repos)
    
    lang_counts = {}
    for r in repos:
        lang = r.get("language")
        if lang:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1
            
    total_lang_repos = sum(lang_counts.values()) or 1
    lang_percentages = [
        (lang, count, (count / total_lang_repos) * 100)
        for lang, count in sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)
    ]
    
    return {
        "name": user.get("name") or USERNAME,
        "repos": user.get("public_repos", 0),
        "followers": user.get("followers", 0),
        "stars": total_stars,
        "forks": total_forks,
        "languages": lang_percentages
    }

def generate_stats_svg(stats, output_path):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 195" width="450" height="195" fill="none">
  <defs>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117" />
      <stop offset="100%" stop-color="#161b22" />
    </linearGradient>
  </defs>
  <style>
    .header {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 700; fill: #7aa2f7; }}
    .stat-label {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 13px; font-weight: 500; fill: #c0caf5; }}
    .stat-val {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 13px; font-weight: 700; fill: #7dcfff; }}
    .icon {{ fill: #7aa2f7; }}
  </style>

  <rect width="450" height="195" rx="10" fill="url(#cardGrad)" stroke="#30363d" stroke-width="1" />

  <!-- Title -->
  <g transform="translate(25, 32)">
    <circle cx="6" cy="6" r="4" fill="#7aa2f7" />
    <text x="18" y="10" class="header">GitHub Profile Overview</text>
  </g>

  <!-- Items -->
  <g transform="translate(25, 68)">
    <!-- Stars -->
    <g transform="translate(0, 0)">
      <path class="icon" d="M8 0L10.472 4.908L15.902 5.729L11.951 9.537L12.894 14.938L8 12.4L3.106 14.938L4.049 9.537L0.098 5.729L5.528 4.908L8 0Z" transform="scale(0.85)" />
      <text x="24" y="11" class="stat-label">Total Stars Earned:</text>
      <text x="360" y="11" class="stat-val" text-anchor="end">{stats['stars']}</text>
    </g>

    <!-- Public Repos -->
    <g transform="translate(0, 28)">
      <path class="icon" d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5v-9Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8V1.5Z" transform="scale(0.85)" />
      <text x="24" y="11" class="stat-label">Public Repositories:</text>
      <text x="360" y="11" class="stat-val" text-anchor="end">{stats['repos']}</text>
    </g>

    <!-- Followers -->
    <g transform="translate(0, 56)">
      <path class="icon" d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4.002 4.002 0 0 0-6.899 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM5.5 3.5a2 2 0 1 0 0 4 2 2 0 0 0 0-4Z" transform="scale(0.85)" />
      <text x="24" y="11" class="stat-label">Followers:</text>
      <text x="360" y="11" class="stat-val" text-anchor="end">{stats['followers']}</text>
    </g>

    <!-- Forks -->
    <g transform="translate(0, 84)">
      <path class="icon" d="M5 3.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Zm0 2.122a2.25 2.25 0 1 0-1.5 0v.878A2.25 2.25 0 0 0 5.75 8.5h1.5v2.128a2.251 2.251 0 1 0 1.5 0V8.5h1.5A2.25 2.25 0 0 0 12.5 6.25v-.878a2.25 2.25 0 1 0-1.5 0v.878a.75.75 0 0 1-.75.75h-4.5a.75.75 0 0 1-.75-.75v-.878Z" transform="scale(0.85)" />
      <text x="24" y="11" class="stat-label">Forks &amp; Contributions:</text>
      <text x="360" y="11" class="stat-val" text-anchor="end">{stats['forks']}</text>
    </g>
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

def generate_top_langs_svg(stats, output_path):
    lang_colors = {
        "Python": "#3572A5",
        "JavaScript": "#f1e05a",
        "C++": "#f34b7d",
        "C": "#555555",
        "HTML": "#e34c26",
        "CSS": "#563d7c"
    }

    langs = stats.get("languages", [])[:4]
    
    # Generate progress bar parts
    bar_rects = []
    current_x = 0
    total_bar_width = 390
    for lang, count, pct in langs:
        color = lang_colors.get(lang, "#7aa2f7")
        w = (pct / 100) * total_bar_width
        bar_rects.append(f'<rect x="{current_x:.1f}" y="0" width="{w:.1f}" height="8" fill="{color}" rx="2" />')
        current_x += w

    bars_html = "\n    ".join(bar_rects)

    # Generate legend
    legend_items = []
    for i, (lang, count, pct) in enumerate(langs):
        color = lang_colors.get(lang, "#7aa2f7")
        col = i % 2
        row = i // 2
        x = col * 200
        y = row * 26
        legend_items.append(f"""<g transform="translate({x}, {y})">
      <circle cx="6" cy="6" r="5" fill="{color}" />
      <text x="18" y="10" class="lang-name">{lang}</text>
      <text x="175" y="10" class="lang-pct" text-anchor="end">{pct:.1f}%</text>
    </g>""")

    legend_html = "\n    ".join(legend_items)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 195" width="450" height="195" fill="none">
  <defs>
    <linearGradient id="cardGradLangs" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117" />
      <stop offset="100%" stop-color="#161b22" />
    </linearGradient>
  </defs>
  <style>
    .header {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 700; fill: #7aa2f7; }}
    .lang-name {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 12.5px; font-weight: 500; fill: #c0caf5; }}
    .lang-pct {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12px; font-weight: 600; fill: #7dcfff; }}
  </style>

  <rect width="450" height="195" rx="10" fill="url(#cardGradLangs)" stroke="#30363d" stroke-width="1" />

  <!-- Title -->
  <g transform="translate(25, 32)">
    <circle cx="6" cy="6" r="4" fill="#7aa2f7" />
    <text x="18" y="10" class="header">Most Used Languages</text>
  </g>

  <!-- Progress Bar Container -->
  <g transform="translate(25, 62)">
    <rect width="390" height="8" rx="4" fill="#21262d" />
    {bars_html}
  </g>

  <!-- Language Legend -->
  <g transform="translate(25, 96)">
    {legend_html}
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    os.makedirs("profile", exist_ok=True)
    print("Fetching stats...")
    data = get_stats()
    print("Generating profile/stats.svg...")
    generate_stats_svg(data, "profile/stats.svg")
    print("Generating profile/top-langs.svg...")
    generate_top_langs_svg(data, "profile/top-langs.svg")
    print("Done!")
