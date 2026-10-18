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
    img = f'<img src="img/{logo}">' if logo else ""
    return f'<div class=lab>{label}</div><div class=name>{img}{title}</div><div class=line>{line}</div>'

# hero: the site's paper, ink and T tile; the four marks laid on it like cards on a desk
icons = "".join(f'<img src="img/{n}.{"png" if n == "sams" else "svg"}" style="position:absolute;width:86px;height:86px;border-radius:21px;'
                f'left:{x}px;top:{y}px;transform:rotate({r}deg);box-shadow:0 14px 30px rgba(27,22,16,.22)">'
                for n, x, y, r in (("longtable", 600, 58, -9), ("clarus", 700, 40, 6), ("upchirp", 628, 158, 7), ("sams", 730, 148, -5)))
render("hero", 880, 290, "linear-gradient(160deg,#ece2d0,#e1d5be)", "#1b1610", f"""
<div style="display:flex;align-items:center;gap:16px;margin-top:6px">
  <div style="width:58px;height:58px;border-radius:17px;background:#1b1610;color:#f8f3ea;display:grid;place-items:center;font:600 32px Lora">T</div>
  <div style="font:600 50px/1 Lora;letter-spacing:-.015em">Tarik Al Hadethi</div></div>
<div style="font-size:19px;line-height:1.5;margin-top:22px;max-width:520px;color:#3a3127">Software engineer in Dubai. I build end to end, and I work directly with the people who use what I build<span style="color:#0099ff">.</span></div>
<div style="display:flex;gap:8px;margin-top:22px;flex-wrap:wrap;max-width:540px">
 {''.join(f'<span style="font:500 12.5px Mono;padding:6px 11px;border-radius:99px;background:#f6f0e5;color:#6a6154">{c}</span>' for c in ("Director, Clarus LLC", "Cyber Security · 2028", "Python · TypeScript · Rust"))}
</div>{icons}""")

LT_HEAD = head("Open source · live at longtable.chat", "Longtable", "Your team, their AIs and your client, at one table. Every AI answers; the table gives one.", "longtable.svg")
# A: the app itself
render("longtable", 880, 330, "#f8f6f3", "#24312c",
       LT_HEAD + '<img class=shot src="img/longtable-app.png" style="left:388px;top:40px;width:600px">', lw=330)
# B: zoomed in on the table's one answer and the client's side
render("longtable-b", 880, 330, "#f8f6f3", "#24312c",
       LT_HEAD + '<img class=shot src="img/longtable-answer.png" style="left:372px;top:44px;width:640px">', lw=310)

CLAUDE_D = "m4.7144 15.9555 4.7174-2.6471.079-.2307-.079-.1275h-.2307l-.7893-.0486-2.6956-.0729-2.3375-.0971-2.2646-.1214-.5707-.1215-.5343-.7042.0546-.3522.4797-.3218.686.0608 1.5179.1032 2.2767.1578 1.6514.0972 2.4468.255h.3886l.0546-.1579-.1336-.0971-.1032-.0972L6.973 9.8356l-2.55-1.6879-1.3356-.9714-.7225-.4918-.3643-.4614-.1578-1.0078.6557-.7225.8803.0607.2246.0607.8925.686 1.9064 1.4754 2.4893 1.8336.3643.3035.1457-.1032.0182-.0728-.164-.2733-1.3539-2.4467-1.445-2.4893-.6435-1.032-.17-.6194c-.0607-.255-.1032-.4674-.1032-.7285L6.287.1335 6.6997 0l.9957.1336.419.3642.6192 1.4147 1.0018 2.2282 1.5543 3.0296.4553.8985.2429.8318.091.255h.1579v-.1457l.1275-1.706.2368-2.0947.2307-2.6957.0789-.7589.3764-.9107.7468-.4918.5828.2793.4797.686-.0668.4433-.2853 1.8517-.5586 2.9021-.3643 1.9429h.2125l.2429-.2429.9835-1.3053 1.6514-2.0643.7286-.8196.85-.9046.5464-.4311h1.0321l.759 1.1293-.34 1.1657-1.0625 1.3478-.8804 1.1414-1.2628 1.7-.7893 1.36.0729.1093.1882-.0183 2.8535-.607 1.5421-.2794 1.8396-.3157.8318.3886.091.3946-.3278.8075-1.967.4857-2.3072.4614-3.4364.8136-.0425.0304.0486.0607 1.5482.1457.6618.0364h1.621l3.0175.2247.7892.522.4736.6376-.079.4857-1.2142.6193-1.6393-.3886-3.825-.9107-1.3113-.3279h-.1822v.1093l1.0929 1.0686 2.0035 1.8092 2.5075 2.3314.1275.5768-.3218.4554-.34-.0486-2.2039-1.6575-.85-.7468-1.9246-1.621h-.1275v.17l.4432.6496 2.3436 3.5214.1214 1.0807-.17.3521-.6071.2125-.6679-.1214-1.3721-1.9246L14.38 17.959l-1.1414-1.9428-.1397.079-.674 7.2552-.3156.3703-.7286.2793-.6071-.4614-.3218-.7468.3218-1.4753.3886-1.9246.3157-1.53.2853-1.9004.17-.6314-.0121-.0425-.1397.0182-1.4328 1.9672-2.1796 2.9446-1.7243 1.8456-.4128.164-.7164-.3704.0667-.6618.4008-.5889 2.386-3.0357 1.4389-1.882.929-1.0868-.0062-.1579h-.0546l-6.3385 4.1164-1.1293.1457-.4857-.4554.0608-.7467.2307-.2429 1.9064-1.3114Z"
OPENAI_D = "M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"
def ai(kind, size):
    d, fill = (CLAUDE_D, "#D97757") if kind == "claude" else (OPENAI_D, "#1f2a26")
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" style="display:block;flex:none"><path d="{d}" fill="{fill}"/></svg>'
MARK = ('<svg width="26" height="26" viewBox="0 0 64 64"><rect x="7.04" y="22.4" width="49.92" height="19.2" rx="9.6" fill="#24312c"/>'
        '<circle cx="17.92" cy="13.66" r="4.16" fill="#b67166"/><circle cx="32" cy="13.66" r="4.16" fill="#5b8abb"/><circle cx="46.08" cy="13.66" r="4.16" fill="#9777af"/>'
        '<circle cx="17.92" cy="50.34" r="4.16" fill="#9777af"/><circle cx="32" cy="50.34" r="4.16" fill="#438a73"/><circle cx="46.08" cy="50.34" r="4.16" fill="#b67166"/></svg>')

def lt_tree():
    people = [("M", "Maya", "#c75f4e", "claude", "Opus 5.5", 420), ("S", "Sam", "#4b7fc1", "claude", "Sonnet 5.5", 597), ("P", "Priya", "#4d9a68", "codex", "GPT-5.5", 774)]
    TX, TY = 597, 236
    out = ['<svg style="position:absolute;left:0;top:0" width="880" height="380">']
    for _, _, _, kind, _, x in people:
        col = "#e9a183" if kind == "claude" else "#5fc49b"
        out.append(f'<path d="M{x},178 C{x},212 {TX},204 {TX},{TY}" fill="none" stroke="{col}" stroke-width="2" opacity=".85"/>')
        out.append(f'<line x1="{x}" y1="86" x2="{x}" y2="116" stroke="#cfd3cc" stroke-width="1.5"/>')
    out.append(f'<line x1="{TX}" y1="318" x2="{TX}" y2="332" stroke="#cfd3cc" stroke-width="1.5"/>')
    out.append('</svg>')
    for ini, name, colr, kind, model, x in people:
        out.append(f'<div style="position:absolute;left:{x-30}px;top:30px;width:60px;text-align:center">'
                   f'<div style="position:relative;width:34px;height:34px;margin:0 auto;border-radius:50%;background:{colr};color:#fff;font:600 15px Inst;display:grid;place-items:center">{ini}'
                   f'<span style="position:absolute;right:-1px;bottom:-1px;width:10px;height:10px;border-radius:50%;background:#3fae6a;box-shadow:0 0 0 2px #f8f6f3"></span></div>'
                   f'<div style="font:500 12px Inst;margin-top:5px;color:#3b4642">{name}</div></div>')
        bg, bd = ("#fde8dc", "#f2cdb9") if kind == "claude" else ("#dcf4e9", "#b9e5d1")
        maker = "Claude" if kind == "claude" else "ChatGPT"
        out.append(f'<div style="position:absolute;left:{x-72}px;top:118px;width:144px;height:58px;box-sizing:border-box;border-radius:12px;background:{bg};border:1px solid {bd};padding:9px 11px">'
                   f'<div style="display:flex;align-items:center;gap:6px">{ai(kind, 15)}<span style="font:500 11px Inst;color:#6b6f6a">{maker}</span>'
                   f'<span style="margin-left:auto;width:8px;height:8px;border-radius:50%;background:#3fae6a"></span></div>'
                   f'<div style="font:600 14.5px Inst;color:#1f2a26;margin-top:4px">{model}</div></div>')
    out.append(f'<div style="position:absolute;left:{TX-82}px;top:{TY}px;width:164px;height:82px;box-sizing:border-box;border-radius:14px;background:#fff;'
               f'box-shadow:0 8px 24px rgba(36,49,44,.12),0 0 0 1px rgba(36,49,44,.06);text-align:center;padding-top:9px">'
               f'<div style="font:600 9.5px Mono;letter-spacing:.14em;color:#7b807a">THE TABLE</div><div style="display:flex;justify-content:center;margin:5px 0 3px">{MARK}</div>'
               f'<div style="font:500 13px Inst;color:#1f2a26">Claude Sonnet 5.5</div></div>')
    for name, colr, x in (("Elena Ruiz", "#a8608d", TX - 64), ("Tom Becker", "#2f8d87", TX + 64)):
        out.append(f'<div style="position:absolute;left:{x-58}px;top:334px;width:116px;height:30px;box-sizing:border-box;border-radius:99px;background:#fff;'
                   f'box-shadow:0 0 0 1px rgba(36,49,44,.1);display:flex;align-items:center;gap:7px;padding:0 10px 0 5px">'
                   f'<span style="width:20px;height:20px;border-radius:50%;background:{colr};flex:none"></span>'
                   f'<span style="font:500 11px/1.1 Inst;color:#1f2a26">{name}<br><span style="color:#8a8f88;font-size:9.5px">Client</span></span></div>')
    return "".join(out)

# C: the tree, drawn here: three people, their AIs, the table and two clients
render("longtable-c", 880, 488, "#f8f6f3", "#24312c",
       head("Open source · longtable.chat", "Longtable", "Your team, their AIs and your client, at one table. Every AI answers; the table gives one.", "longtable.svg")
       + '<img src="img/longtable-tree3.png" style="position:absolute;left:350px;top:22px;width:490px">', lw=280)

KEY = lambda k: f'<span style="font:600 10px Mono;color:#d9cdb6;background:#2a251d;border:1px solid #3a3326;border-radius:5px;padding:2px 5px">{k}</span>'
ICONS = {"Area": '<path d="M4 7V4h3M17 4h3v3M20 17v3h-3M7 20H4v-3" fill="none" stroke="#f1d9a6" stroke-width="1.8" stroke-linecap="round"/>',
         "Record": '<circle cx="12" cy="12" r="8" fill="none" stroke="#f1d9a6" stroke-width="1.8"/><circle cx="12" cy="12" r="3.5" fill="#f1d9a6"/>',
         "Scrolling": '<path d="M12 4v16M8 8l4-4 4 4M8 16l4 4 4-4" fill="none" stroke="#f1d9a6" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>',
         "Extract text": '<path d="M4 7V4h3M17 4h3v3M20 17v3h-3M7 20H4v-3M9 9h6M12 9v7" fill="none" stroke="#f1d9a6" stroke-width="1.8" stroke-linecap="round"/>'}
def mode(name, keys, x, y):
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:180px;height:62px;box-sizing:border-box;border-radius:12px;background:#1b1813;'
            f'border:1px solid rgba(241,217,166,.12);padding:10px 12px;display:flex;gap:10px;align-items:center">'
            f'<div style="width:34px;height:34px;border-radius:9px;background:#0f0d0a;display:grid;place-items:center;flex:none"><svg width="18" height="18" viewBox="0 0 24 24">{ICONS[name]}</svg></div>'
            f'<div><div style="font:600 13px Inst;color:#f6e9cf;margin-bottom:5px">{name}</div><div style="display:flex;gap:3px">{"".join(KEY(k) for k in keys)}</div></div></div>')
CL_HEAD = head("Commercial · Windows", "Clarus", "Screenshots and screen recording, built alone from GPU capture to Stripe.", "clarus.svg")
CL_BG = "radial-gradient(120% 90% at 80% 0%,#3a2a12,#120d07 70%)"
# A: the whole app window, scaled to fit, nothing cut off
render("clarus", 436, 330, CL_BG, "#f6e9cf",
       CL_HEAD + '<img class=shot src="img/clarus-app.png" style="left:118px;top:150px;width:200px;'
       'box-shadow:0 18px 40px rgba(0,0,0,.6),0 0 0 1px rgba(255,255,255,.1)">', lw=340)
# B: the 3D prism from getclarus.dev (its baked prism-spin.webm), turned slightly
GOLD_BG = "radial-gradient(70% 70% at 76% 58%,#3d2b12,#0d0b08 70%)"
render("clarus-b", 436, 330, GOLD_BG, "#f6e9cf",
       CL_HEAD.replace('<img src="img/clarus.svg">', '')
       + '<img src="img/prism-angle.png" style="position:absolute;right:-4px;bottom:-16px;width:212px;filter:drop-shadow(0 24px 30px rgba(0,0,0,.55))">', lw=250)
# C: the same prism facing front, with the shortcut most people press
render("clarus-c", 436, 330, GOLD_BG, "#f6e9cf",
       CL_HEAD.replace('<img src="img/clarus.svg">', '')
       + '<img src="img/prism-front.png" style="position:absolute;right:8px;bottom:-2px;width:196px;filter:drop-shadow(0 24px 30px rgba(0,0,0,.55))">'
       + '<div style="position:absolute;left:32px;bottom:30px;display:flex;gap:6px;align-items:center;font:600 12px Mono;color:#a8987a">'
       + ' <span style="color:#a8987a">+</span> '.join(f'<span style="padding:5px 9px;border-radius:7px;background:#211b12;border:1px solid #3d3220;color:#f1d9a6;box-shadow:0 2px 0 #3d3220">{k}</span>' for k in ("Win", "Shift", "S"))
       + '<span style="margin-left:8px">area capture</span></div>', lw=250)

render("sams", 436, 330, "linear-gradient(150deg,#ece9fb,#dfeef1)", "#1b1f2a",
       head("Client project · UOWD Media Studio", "SAMS", "Live 14 days after the handover. 25 students now test it with real bookings.", "sams.png")
       + '<img class=shot src="img/sams-today.png" style="left:46px;top:168px;width:420px">', lw=340)

render("upchirp", 436, 330, "radial-gradient(110% 90% at 85% 0%,#24502f,#10241a 70%)", "#eaefd1",
       head("Open source · with a friend", "Upchirp", "Ask a radar what it saw: an AI agent over offline sensor data.", "upchirp.svg")
       + '<img class=shot src="img/upchirp-live.png" style="left:46px;top:168px;width:440px;box-shadow:0 18px 50px rgba(0,0,0,.55),0 0 0 1px rgba(234,239,209,.12)">', lw=340)

render("catsentry", 436, 330, "radial-gradient(110% 90% at 85% 0%,#4b3424,#241a15 70%)", "#fbefe4",
       head("Open source · Python", "Cat Sentry", "Local object detection on a home camera. Pings Telegram when the cat is up at night.", "catsentry.svg")
       + '<div style="position:absolute;left:282px;top:40px;width:136px;padding:6px;border-radius:30px;background:#0f0b08;'
         'box-shadow:0 22px 50px rgba(0,0,0,.6),0 0 0 1.5px rgba(251,239,228,.14);transform:rotate(4deg)">'
         '<img src="img/catsentry-phone.png" style="display:block;width:136px;border-radius:22px"></div>', lw=215)

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
