"""The profile as one paper card, cut into rows so each row is its own link.
Every row shares the card's colour and edges, so stacked they read as one piece.
    python card.py <out dir>
"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
W = 880
PAPER, INK, SOFT, LINE = "#f4eee3", "#1b1610", "#6f6556", "#e2d8c6"

FONTS = """@font-face{font-family:Lora;src:url(lora.woff2) format("woff2");font-weight:400 700}
@font-face{font-family:Inst;src:url(instrument-sans.woff2) format("woff2");font-weight:400 700}
@font-face{font-family:Mono;src:url(jetbrains-mono.woff2) format("woff2");font-weight:400 700}"""

def shot(name, h, body, top=False, bottom=False):
    r = "20px"   # GitHub leaves a few pixels between stacked images, so every row is its own rounded card
    html = (f'<!doctype html><meta charset=utf-8><style>{FONTS}html,body{{margin:0;background:transparent}}'
            f'.c{{width:{W}px;height:{h}px;box-sizing:border-box;background:{PAPER};color:{INK};border-radius:{r};'
            f'font-family:Inst,Segoe UI,sans-serif;position:relative;overflow:hidden}}</style><div class=c>{body}</div>')
    p = os.path.join(HERE, f"_{name}.html"); open(p, "w", encoding="utf-8").write(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=3",
                    "--default-background-color=00000000", f"--window-size={W},{h}",
                    f"--screenshot={os.path.join(OUT, name + '.png')}", "file:///" + p.replace("\\", "/")],
                   stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, check=True)

# header: the site's T tile and serif name, nothing else competing with it
shot("c-head", 196, f"""
<div style="position:absolute;left:44px;top:42px;display:flex;align-items:center;gap:16px">
  <div style="width:52px;height:52px;border-radius:15px;background:{INK};color:#f8f3ea;display:grid;place-items:center;font:600 29px Lora">T</div>
  <div style="font:600 44px/1 Lora;letter-spacing:-.015em">Tarik Al Hadethi</div></div>
<div style="position:absolute;left:44px;top:120px;font-size:18px;line-height:1.5;color:#3a3127;max-width:600px">
  Software engineer in Dubai. I build end to end, and I work directly with the people who use what I build<span style="color:#0099ff">.</span></div>
<div style="position:absolute;right:44px;top:50px;text-align:right;font:500 12px/1.9 Mono;letter-spacing:.06em;color:{SOFT}">
  DIRECTOR, CLARUS LLC<br>CYBER SECURITY · 2028<br>PYTHON · TYPESCRIPT · RUST</div>
""", top=True)

ARROW = (f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="{SOFT}" stroke-width="2" stroke-linecap="round" '
         'stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9"/></svg>')
MERGE = ('<svg width="48" height="48" viewBox="0 0 64 64" style="display:block"><rect width="64" height="64" rx="15" fill="#1b1610"/>'
         '<g fill="none" stroke="#f1d9a6" stroke-width="3.6" stroke-linecap="round"><circle cx="22" cy="18" r="5"/><circle cx="22" cy="46" r="5"/>'
         '<circle cx="44" cy="32" r="5"/><path d="M22 23v18M22 23c0 9 9 9 17 9"/></g></svg>')
PEN = ('<svg width="48" height="48" viewBox="0 0 64 64" style="display:block"><rect width="64" height="64" rx="15" fill="#1b1610"/>'
       '<text x="32" y="43" text-anchor="middle" font-family="Lora" font-weight="600" font-size="32" fill="#f8f3ea">T</text></svg>')

def row(name, logo, title, kind, line, last=False):
    lg = logo if logo.startswith("<") else f'<img src="img/{logo}" style="width:48px;height:48px;border-radius:13px;display:block">'
    shot(name, 96, f"""
<div style="position:absolute;left:44px;right:44px;top:0;bottom:0;display:flex;align-items:center;gap:18px">
  <div style="flex:none;border-radius:13px;box-shadow:0 0 0 1px rgba(27,22,16,.08)">{lg}</div>
  <div style="flex:1;min-width:0">
    <div style="display:flex;align-items:baseline;gap:10px"><span style="font:600 22px/1.15 Lora">{title}</span>
      <span style="font:500 11px Mono;letter-spacing:.1em;text-transform:uppercase;color:{SOFT}">{kind}</span></div>
    <div style="font-size:15px;line-height:1.4;color:{SOFT};margin-top:4px">{line}</div></div>
  <div style="flex:none">{ARROW}</div></div>
""", bottom=last)

row("c-longtable", "longtable.svg", "Longtable", "Open source", "A team chat where everyone's own AI answers together, and the client sits at the table too.")
row("c-clarus", "clarus.svg", "Clarus", "Windows app", "Screenshots and screen recording, built alone from GPU capture to Stripe.")
row("c-sams", "sams.png", "SAMS", "Client project", "Equipment booking for the UOWD Media Studio, live 14 days after the handover.")
row("c-upchirp", "upchirp.svg", "Upchirp", "Open source", "Ask a radar what it saw: an AI agent over offline sensor data, built with a friend.")
row("c-catsentry", "catsentry.svg", "Cat Sentry", "Open source", "Local object detection on a home camera. Pings Telegram when the cat is up at night.")
row("c-tract", "tract.svg", "sonos/tract", "Contributor", "Six pull requests merged into Sonos's ONNX inference engine, each one measured.")
row("c-writing", PEN, "Writing", "12 posts", "Write-ups on bugs, measurements and my own mistakes.", last=True)
print("ok")
