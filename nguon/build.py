# Ghép ảnh vào khung: python build.py  ->  ghi lại ../index.html (giữ nguyên cách làm hiện tại)
import base64, os
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
s = open(os.path.join(here, 'ho-ca-khung.html'), encoding='utf-8').read()
enc = lambda f: base64.b64encode(open(os.path.join(root, 'public', 'assets', f), 'rb').read()).decode()
s = s.replace("'__BG__'", "'data:image/webp;base64," + enc('nen-ho-1080.webp') + "'").replace("'__LOTUS__'", "'data:image/webp;base64," + enc('la-sen.webp') + "'").replace("'__RACE__'", "'data:image/webp;base64," + enc('kenh-dua-1080.webp') + "'")
head, body = s.split('</style>\n\n<div class="wrap">', 1)
page = '<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n' + head + '  html, body { margin: 0; }\n  [hidden] { display: none !important; }\n</style>\n</head>\n<body>\n<div class="wrap">' + body + '\n</body>\n</html>\n'
open(os.path.join(root, 'index.html'), 'w', encoding='utf-8').write(page)
print('Đã ghi index.html')
