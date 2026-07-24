#!/usr/bin/env python3
import html, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "info-card.svg")
W, H = 480, 376
PAD = 20
TITLEBAR_H = 30
KEY_X = PAD
VAL_X = PAD + 92
LINE_H = 20.5
ROWS = [
    ("host",),
    ("kv", "Now", "Computer Engineering Student @ KEC"),
    ("kv", "Loc", "Kathmandu, Nepal"),
    ("kv", "Open", "AI/ML, full-stack, and product engineering"),
    ("gap",),
    ("sec", "Stack"),
    ("kv", "Frontend", "React, Next.js, TypeScript, Tailwind"),
    ("kv", "Backend", "Node.js, Supabase, PostgreSQL, Docker"),
    ("kv", "AI / ML", "LLM workflows, XGBoost, prompt systems"),
    ("gap",),
    ("sec", "Projects"),
    ("bul", "Mergy — repository analytics"),
    ("bul", "Monex — currency intelligence"),
    ("bul", "Aether — ambient productivity"),
    ("bul", "Nocturne — VS Code theme"),
    ("gap",),
    ("sec", "Focus"),
    ("kv", "Build", "Clean systems, sharp UX, real-world impact"),
]
def esc(s): return html.escape(s)
def rise(inner, delay): return f'<g opacity="0" transform="translate(0,5)">{inner}<animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.4s" fill="freeze"/><animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="{delay:.2f}s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/></g>'
parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">']
parts.append(f'<defs><linearGradient id="ibg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#111722"/><stop offset="1" stop-color="#0d1117"/></linearGradient></defs>')
parts.append(f'<rect width="{W}" height="{H}" rx="12" fill="url(#ibg)"/>')
parts.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#30363d"/>')
parts.append(f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="#30363d"/>')
for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dotcol}"/>')
parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="#7d8590" font-size="12" text-anchor="middle">aarjan@github: ~$ neofetch</text>')
y = TITLEBAR_H + 30
i = 0
for row in ROWS:
    kind = row[0]
    if kind == "gap":
        y += LINE_H * 0.55
        continue
    if kind == "host":
        inner = f'<text x="{KEY_X}" y="{y:.1f}" font-size="14" font-weight="700"><tspan fill="#22c55e">aarjan</tspan><tspan fill="#7d8590">@</tspan><tspan fill="#a78bfa">github</tspan></text><line x1="{KEY_X+96}" y1="{y-4:.1f}" x2="{W-PAD}" y2="{y-4:.1f}" stroke="#30363d" stroke-opacity="0.8"/>'
    elif kind == "sec":
        title = esc(row[1])
        inner = f'<text x="{KEY_X}" y="{y:.1f}" fill="#60a5fa" font-size="12.5" font-weight="700">&#8212; {title}</text><line x1="{KEY_X + 12 + len(row[1])*8}" y1="{y-4:.1f}" x2="{W-PAD}" y2="{y-4:.1f}" stroke="#30363d" stroke-opacity="0.8"/>'
    elif kind == "kv":
        key, val = esc(row[1]), esc(row[2])
        inner = f'<text x="{KEY_X}" y="{y:.1f}" fill="#8b5cf6" font-size="12.5" font-weight="700">{key}</text><text x="{VAL_X}" y="{y:.1f}" fill="#c9d1d9" font-size="12.5">{val}</text>'
    elif kind == "bul":
        txt = esc(row[1])
        inner = f'<circle cx="{KEY_X+3}" cy="{y-4:.1f}" r="2.5" fill="#22c55e"/><text x="{KEY_X+14}" y="{y:.1f}" fill="#c9d1d9" font-size="12.5">{txt}</text>'
    else:
        continue
    parts.append(rise(inner, 0.15 + i*0.06))
    y += LINE_H
    i += 1
parts.append("</svg>")
open(OUT, "w").write("".join(parts))
