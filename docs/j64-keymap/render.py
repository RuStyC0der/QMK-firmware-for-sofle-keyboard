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

COL = {
 'norm':  ('#2b303b', '#e8eaf0'),
 'modtap':('#1f3a5f', '#cfe3ff'),
 'layer': ('#6b3f12', '#ffd9a8'),
 'combo': ('#46285f', '#ecd5ff'),
 'enc':   ('#164a3a', '#c4f5e1'),
 'trans': ('#1a1d24', '#555b69'),
 'none':  ('#111318', '#111318'),
}

K, G, PAD = 54, 6, 24
W = PAD*2 + 14*(K+G)
LAYER_H = 5*(K+G) + 50
H = PAD*2 + 4*LAYER_H + 70

p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="-apple-system, Helvetica, Arial, sans-serif">',
     f'<rect width="{W}" height="{H}" fill="#0d0f14"/>',
     f'<text x="{PAD}" y="{PAD+14}" font-size="22" font-weight="700" fill="#fff">Sofle Choc · J64 keymap</text>',
     f'<text x="{PAD}" y="{PAD+34}" font-size="12" fill="#8b92a3">rustyc0der/sofle/choc/keymaps/j64 — generated from keymap.c</text>']

y0 = PAD + 56
for li, (name, keys) in enumerate(layers):
    p.append(f'<text x="{PAD}" y="{y0+14}" font-size="15" font-weight="700" fill="#ffb454">L{li} · {name}</text>')
    yy = y0 + 24
    i = 0
    for r, n in enumerate(ROW_LENS):
        cols = columns(r, n)
        for c in cols:
            kk = keys[i]; i += 1
            main, sub, kind = label(kk)
            bg, fg = COL[kind]
            x, y = PAD + c*(K+G), yy + r*(K+G)
            stroke = '#000' if kind == 'none' else '#3a4050'
            p.append(f'<rect x="{x}" y="{y}" width="{K}" height="{K}" rx="8" fill="{bg}" stroke="{stroke}"/>')
            if main:
                fs = 18 if len(main) <= 1 else 14 if len(main) <= 3 else 11
                ty = y + (K/2 + 6 if not sub else K/2 + 1)
                p.append(f'<text x="{x+K/2}" y="{ty}" font-size="{fs}" font-weight="600" fill="{fg}" text-anchor="middle">{escape(main)}</text>')
            if sub:
                p.append(f'<text x="{x+K/2}" y="{y+K-8}" font-size="10" fill="{fg}" opacity="0.75" text-anchor="middle">{escape(sub)}</text>')
    assert i == len(keys), (name, i, len(keys))
    y0 += LAYER_H

# legend
lx, ly = PAD, H - 40
for kind, text in [('norm','key'),('modtap','mod-tap (hold = mod)'),('layer','layer'),('combo','⌘-combo / macro / tap-dance'),('enc','encoder press'),('trans','transparent')]:
    bg, fg = COL[kind]
    p.append(f'<rect x="{lx}" y="{ly}" width="18" height="18" rx="4" fill="{bg}" stroke="#3a4050"/>')
    p.append(f'<text x="{lx+26}" y="{ly+13}" font-size="12" fill="#c0c5d2">{escape(text)}</text>')
    lx += 26 + len(text)*7 + 24
p.append(f'<text x="{PAD}" y="{H-8}" font-size="11" fill="#8b92a3">Encoder: L0 Vol±, L1 Bri±</text>')
p.append('</svg>')
open(out, 'w').write('\n'.join(p))
print('wrote', out, len(layers), 'layers')
