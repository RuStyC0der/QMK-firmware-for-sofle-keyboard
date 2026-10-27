import re, sys
from xml.sax.saxutils import escape

src = open(sys.argv[1]).read()
out = sys.argv[2]

def split_args(s):
    args, depth, cur = [], 0, ''
    for ch in s:
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
        if ch == ',' and depth == 0:
            args.append(cur.strip()); cur = ''
        else:
            cur += ch
    if cur.strip():
        args.append(cur.strip())
    return args

layers = []
for name, body in re.findall(r'\[(_\w+)\]\s*=\s*LAYOUT\((.*?)\n\s*\)', src, re.S):
    body = re.sub(r'/\*.*?\*/', '', body, flags=re.S)
    layers.append((name.lstrip('_'), split_args(body)))

NAMES = {'GRV':'`','MINUS':'-','EQUAL':'=','LBRC':'[','RBRC':']','SCLN':';','QUOT':"'",'BSLS':'\\',
 'COMM':',','DOT':'.','SLSH':'/','BSPC':'⌫','ENT':'⏎','TAB':'⇥','SPC':'Space','LSFT':'⇧','RSFT':'⇧',
 'LGUI':'⌘','RGUI':'⌘','LALT':'⌥','RALT':'⌥','LCTL':'⌃','RCTL':'⌃','ESC':'Esc','MUTE':'Mute',
 'UP':'↑','DOWN':'↓','LEFT':'←','RGHT':'→','RIGHT':'→','PGUP':'PgUp','PGDN':'PgDn','HOME':'Home',
 'END':'End','INS':'Ins','PSCR':'PrtSc','APP':'Menu','DEL':'Del','CAPS':'Caps','MNXT':'⏭','MPRV':'⏮',
 'MPLY':'⏯','VOLU':'Vol+','VOLD':'Vol−','WSCH':'Search','UNDO':'Undo','CUT':'Cut','COPY':'Copy',
 'PASTE':'Paste','BRIU':'Bri+','BRID':'Bri−'}
SHIFTED = {'1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':')',
 'MINUS':'_','EQUAL':'+','LBRC':'{','RBRC':'}','SCLN':':','BSLS':'|'}
MODS = {'LGUI':'⌘','RGUI':'⌘','LALT':'⌥','RALT':'⌥','LSFT':'⇧','RSFT':'⇧','LCTL':'⌃','RCTL':'⌃'}

def kc(s):
    s = s.strip().replace('KC_','')
    return NAMES.get(s, s)

def label(k):
    """returns (main, sub, kind)"""
    if k == '_______': return ('▽', '', 'trans')
    if k == 'XXXXXXX': return ('', '', 'none')
    if k == 'QK_GESC': return ('Esc', '`', 'norm')
    m = re.fullmatch(r'(\w)(?:GUI|ALT|SFT|CTL)_T\((.*)\)', k)
    m = re.fullmatch(r'([LR])(GUI|ALT|SFT|CTL)_T\((.*)\)', k)
    if m: return (kc(m.group(3)), MODS[m.group(1)+m.group(2)], 'modtap')
    m = re.fullmatch(r'LT\((\d),(.*)\)', k)
    if m: return (kc(m.group(2)), 'L'+m.group(1), 'layer')
    m = re.fullmatch(r'MO\((\d)\)', k)
    if m: return ('L'+m.group(1), 'hold', 'layer')
    m = re.fullmatch(r'TG\((\d)\)', k)
    if m: return ('L'+m.group(1), 'toggle', 'layer')
    m = re.fullmatch(r'LSFT\(KC_(\w+)\)', k)
    if m: return (SHIFTED.get(m.group(1), '⇧'+kc(m.group(1))), '', 'norm')
    m = re.fullmatch(r'RGUI\((.*)\)', k)
    if m: return ('⌘'+kc(m.group(1)), '', 'combo')
    if k.startswith('TD('): return ('TD', 'search', 'combo')
    if k == 'M0': return ('M0', 'macro', 'combo')
    if k == 'SE_REQ': return ('SysRq', '', 'norm')
    if k == 'KC_MUTE': return ('Mute', 'enc', 'enc')
    return (kc(k), '', 'norm')

# slot index (per row) -> grid column. 14 columns: 0-5 left, 6 enc, 7 mid, 8-13 right
def columns(row, n):
    if row < 3:   # 6 + mid + 6
        return list(range(0, 6)) + [7] + list(range(8, 14))
    if row == 3:  # 6 + enc + mid + 6
        return list(range(0, 6)) + [6, 7] + list(range(8, 14))
    return list(range(1, 6)) + [7] + list(range(8, 13))  # thumb row

ROW_LENS = [13, 13, 13, 14, 11]

# ---- print theme: white page, black text, kinds distinguishable without colour ----
# kind: (fill, stroke, stroke-width, dash, text)
STYLE = {
 'norm':   ('#ffffff', '#222', 1.6, '',    '#000'),
 'modtap': ('#e3ecf8', '#222', 1.6, '',    '#000'),
 'layer':  ('#ffd9a0', '#000', 3.2, '',    '#000'),
 'combo':  ('#eddcf7', '#222', 1.8, '6 3', '#000'),
 'enc':    ('#cdeedd', '#000', 3.0, '',    '#000'),
 'trans':  ('none',    '#aaa', 1.2, '2 3', '#aaa'),
 'none':   ('url(#hatch)', '#888', 1.2, '', '#000'),
}

W, H = 1754, 1240          # A4 landscape, 150 dpi units
PAD = 40
GAPX = 40
LW = (W - 2*PAD - GAPX) / 2
KW_PITCH = LW / 14
KW, KH = KW_PITCH - 6, 62
KP_Y = KH + 6
BLOCK_H = 34 + 5*KP_Y

p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="-apple-system, Helvetica, Arial, sans-serif">',
     '<defs><pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
     '<rect width="8" height="8" fill="#f3f3f3"/><line x1="0" y1="0" x2="0" y2="8" stroke="#bbb" stroke-width="2"/></pattern></defs>',
     f'<rect width="{W}" height="{H}" fill="#fff"/>',
     f'<text x="{PAD}" y="{PAD+26}" font-size="34" font-weight="700" fill="#000">Sofle Choc · J64 keymap</text>',
     f'<text x="{PAD}" y="{PAD+52}" font-size="16" fill="#444">rustyc0der/sofle/choc/keymaps/j64 · 4 layers · generated from keymap.c</text>']

top = 130
GAPY = 46
for li, (name, keys) in enumerate(layers):
    bx = PAD + (li % 2) * (LW + GAPX)
    by = top + (li // 2) * (BLOCK_H + GAPY)
    p.append(f'<text x="{bx}" y="{by+22}" font-size="22" font-weight="800" fill="#000">L{li} · {name}</text>')
    p.append(f'<line x1="{bx}" y1="{by+30}" x2="{bx+LW}" y2="{by+30}" stroke="#000" stroke-width="1.5"/>')
    yy = by + 40
    i = 0
    for r, n in enumerate(ROW_LENS):
        for c in columns(r, n):
            kk = keys[i]; i += 1
            main, sub, kind = label(kk)
            fill, stroke, sw, dash, fg = STYLE[kind]
            x, y = bx + c*KW_PITCH, yy + r*KP_Y
            rx = KW/2 if kind == 'enc' else 9
            da = f' stroke-dasharray="{dash}"' if dash else ''
            p.append(f'<rect x="{x:.1f}" y="{y}" width="{KW:.1f}" height="{KH}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}/>')
            cx = x + KW/2
            if main:
                fs = 24 if len(main) <= 1 else 19 if len(main) <= 3 else 14
                ty = y + (KH/2 + 8 if not sub else KH/2 - 1)
                p.append(f'<text x="{cx:.1f}" y="{ty}" font-size="{fs}" font-weight="700" fill="{fg}" text-anchor="middle">{escape(main)}</text>')
            if sub:
                p.append(f'<text x="{cx:.1f}" y="{y+KH-9}" font-size="13" font-weight="600" fill="{fg}" text-anchor="middle">{escape(sub)}</text>')
    assert i == len(keys), (name, i, len(keys))

# legend + notes
ly = top + 2*BLOCK_H + GAPY + 50
p.append(f'<line x1="{PAD}" y1="{ly-14}" x2="{W-PAD}" y2="{ly-14}" stroke="#000" stroke-width="1.5"/>')
lx = PAD
for kind, text in [('norm','key'),('modtap','mod-tap: tap = letter, hold = mod'),('layer','layer key'),
                   ('combo','⌘-combo / macro / tap-dance'),('enc','encoder press'),('trans','transparent (▽)'),('none','unused')]:
    fill, stroke, sw, dash, fg = STYLE[kind]
    da = f' stroke-dasharray="{dash}"' if dash else ''
    rx = 11 if kind == 'enc' else 5
    p.append(f'<rect x="{lx}" y="{ly}" width="22" height="22" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}/>')
    p.append(f'<text x="{lx+30}" y="{ly+17}" font-size="15" fill="#000">{escape(text)}</text>')
    lx += 30 + len(text)*8.2 + 26
notes = [
 'Home-row mods (L0): A ⌘  S ⌥  D ⇧  F ⌃   |   J ⌃  K ⇧  L ⌥  ; ⌘',
 'Thumb: left Space = tap Space / hold L1 (Raise) · right L2 key = hold for Lower · L3 (Game) toggles from the Lower layer',
 'Encoder: L0 volume ±, L1 brightness ± · press = Mute',
 '⌘→ ⌘↓ ⌘← ⌘↑ ⌘PgUp = Right-GUI combos in the centre column',
]
for n, t in enumerate(notes):
    p.append(f'<text x="{PAD}" y="{ly+60+n*26}" font-size="16" fill="#111">{escape(t)}</text>')
p.append('</svg>')
open(out, 'w').write('\n'.join(p))
print('wrote', out)
