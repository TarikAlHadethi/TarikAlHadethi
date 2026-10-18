"""Renders the profile tiles as PNGs with Chrome (2x, transparent corners).

Each tile is a solid object in its own project's colours, so it reads the same on
GitHub's light and dark pages. Fonts and the hero follow tarikalhadethi.com.
    python make.py <out dir>
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
os.makedirs(OUT, exist_ok=True)

BASE = """<!doctype html><meta charset=utf-8><style>
@font-face{font-family:Lora;src:url(lora.woff2) format("woff2");font-weight:400 700}
@font-face{font-family:Inst;src:url(instrument-sans.woff2) format("woff2");font-weight:400 700}
@font-face{font-family:Mono;src:url(jetbrains-mono.woff2) format("woff2");font-weight:400 700}
html,body{margin:0;background:transparent}
.t{position:relative;width:%(w)dpx;height:%(h)dpx;border-radius:26px;overflow:hidden;box-sizing:border-box;padding:30px 32px;
   font-family:Inst,Segoe UI,sans-serif;background:%(bg)s;color:%(fg)s}
.lab{font:600 11.5px Mono,monospace;letter-spacing:.14em;text-transform:uppercase;opacity:.62}
.name{font:600 34px/1.05 Lora,Georgia,serif;letter-spacing:-.01em;margin:10px 0 8px;display:flex;align-items:center;gap:12px}
.name img{width:38px;height:38px;border-radius:10px}
.line{font-size:15.5px;line-height:1.45;opacity:.8;max-width:%(lw)dpx}
.shot{position:absolute;border-radius:12px;box-shadow:0 18px 50px rgba(0,0,0,.28),0 0 0 1px rgba(0,0,0,.08)}
</style><div class=t>%(body)s</div>"""

def render(name, w, h, bg, fg, body, lw=360):
    html = BASE % dict(w=w, h=h, bg=bg, fg=fg, body=body, lw=lw)
    p = os.path.join(HERE, f"_{name}.html")
    open(p, "w", encoding="utf-8").write(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=2",
                    "--default-background-color=00000000", f"--window-size={w},{h}",
                    f"--screenshot={os.path.join(OUT, name + '.png')}", "file:///" + p.replace("\\", "/")],
                   stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, check=True)

def head(label, title, line, logo=None):
    img = f'<img src="img/{logo}.svg">' if logo else ""
    return f'<div class=lab>{label}</div><div class=name>{img}{title}</div><div class=line>{line}</div>'

# hero: the site's paper, ink and T tile; the four marks laid on it like cards on a desk
icons = "".join(f'<img src="img/{n}.svg" style="position:absolute;width:86px;height:86px;border-radius:21px;'
                f'left:{x}px;top:{y}px;transform:rotate({r}deg);box-shadow:0 14px 30px rgba(27,22,16,.22)">'
                for n, x, y, r in (("longtable", 600, 58, -9), ("clarus", 700, 40, 6), ("upchirp", 628, 158, 7), ("catsentry", 730, 148, -5)))
render("hero", 880, 290, "linear-gradient(160deg,#ece2d0,#e1d5be)", "#1b1610", f"""
<div style="display:flex;align-items:center;gap:16px;margin-top:6px">
  <div style="width:58px;height:58px;border-radius:17px;background:#1b1610;color:#f8f3ea;display:grid;place-items:center;font:600 32px Lora">T</div>
  <div style="font:600 50px/1 Lora;letter-spacing:-.015em">Tarik Al Hadethi</div></div>
<div style="font-size:19px;line-height:1.5;margin-top:22px;max-width:520px;color:#3a3127">Software engineer in Dubai. I build end to end, and I work directly with the people who use what I build<span style="color:#0099ff">.</span></div>
<div style="display:flex;gap:8px;margin-top:22px;flex-wrap:wrap;max-width:540px">
 {''.join(f'<span style="font:500 12.5px Mono;padding:6px 11px;border-radius:99px;background:#f6f0e5;color:#6a6154">{c}</span>' for c in ("Director, Clarus LLC", "Cyber Security · 2028", "Python · TypeScript · Rust"))}
</div>{icons}""")

render("longtable", 880, 330, "#f8f6f3", "#24312c",
       head("Open source · live at longtable.chat", "Longtable", "Your team, their AIs and your client, at one table. Every AI answers; the table gives one.", "longtable")
       + '<img class=shot src="img/longtable.png" style="left:430px;top:46px;width:600px">', lw=330)

render("clarus", 436, 330, "radial-gradient(120% 90% at 80% 0%,#3a2a12,#120d07 70%)", "#f6e9cf",
       head("Commercial · Windows", "Clarus", "Screenshots and screen recording, built alone from GPU capture to Stripe.", "clarus")
       + '<img class=shot src="img/clarus-app.png" style="left:46px;top:168px;width:420px;box-shadow:0 18px 50px rgba(0,0,0,.6),0 0 0 1px rgba(255,255,255,.08)">', lw=340)

render("sams", 436, 330, "linear-gradient(150deg,#ece9fb,#dfeef1)", "#1b1f2a",
       head("Client project · UOWD Media Studio", "Studio booking", "Live 14 days after the handover. 25 students now test it with real bookings.")
       + '<img class=shot src="img/sams-today.png" style="left:46px;top:168px;width:420px">', lw=340)

render("upchirp", 436, 330, "radial-gradient(110% 90% at 85% 0%,#24502f,#10241a 70%)", "#eaefd1",
       head("Open source · with a friend", "Upchirp", "Ask a radar what it saw: an AI agent over offline sensor data.", "upchirp")
       + '<img class=shot src="img/upchirp-live.png" style="left:46px;top:168px;width:440px;box-shadow:0 18px 50px rgba(0,0,0,.55),0 0 0 1px rgba(234,239,209,.12)">', lw=340)

render("catsentry", 436, 330, "radial-gradient(110% 90% at 85% 0%,#4b3424,#241a15 70%)", "#fbefe4",
       head("Open source · Python", "Cat Sentry", "Messages me when the cat gets down at night. Silent when only people move.", "catsentry")
       + '<img class=shot src="img/catsentry-demo.png" style="left:46px;top:168px;width:440px;box-shadow:0 18px 50px rgba(0,0,0,.55),0 0 0 1px rgba(251,239,228,.1)">', lw=340)

rows = "".join(f'<div style="display:flex;justify-content:space-between;font:500 13.5px Mono;padding:9px 0;border-top:1px solid rgba(248,243,234,.12)">'
               f'<span style="opacity:.7">{a}</span><span>{b} <span style="color:#7fc7ff">→ {c}</span></span></div>'
               for a, b, c in (("2x2 max pool", "8.82", "2.55 ms"), ("stride-2 deconvolution", "5.71", "1.54 ms"), ("direct convolution", "237.6", "211.6 ms")))
render("tract", 436, 330, "#1b1610", "#f8f3ea", f"""<div class=lab>Open source · sonos/tract</div>
<div style="display:flex;align-items:baseline;gap:12px;margin:8px 0 2px"><span style="font:600 76px/1 Lora">6</span>
<span style="font-size:16px;line-height:1.35;opacity:.85">pull requests merged into<br>Sonos's ONNX inference engine</span></div>
<div style="margin-top:16px">{rows}</div>""")

posts = "".join(f'<div style="font:500 16px/1.35 Lora;padding:10px 0;border-top:1px solid rgba(27,22,16,.12)">{t}</div>'
                for t in ("The benchmark I nearly published", "Three green tests that tested nothing", "Nine emails to a live product"))
render("writing", 436, 330, "#f6f0e5", "#1b1610", f"""<div class=lab>Writing · tarikalhadethi.com</div>
<div style="display:flex;align-items:baseline;gap:12px;margin:8px 0 2px"><span style="font:600 76px/1 Lora">12</span>
<span style="font-size:16px;line-height:1.35;opacity:.8">write-ups on bugs, measurements<br>and my own mistakes</span></div>
<div style="margin-top:12px">{posts}</div>""")
print("ok")
