"""Tạo trang tải đơn giản cho Trình duyệt Kindle (không JavaScript, chữ to)."""
import os
import sys
from datetime import datetime

THU = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ Nhật']

out = sys.argv[1]
now = datetime.now()
ngay = '%s, %02d/%02d/%d' % (THU[now.weekday()], now.day, now.month, now.year)
size = os.path.getsize(os.path.join(out, 'Bao-Viet.azw3')) / 1024 / 1024
has_mobi = os.path.exists(os.path.join(out, 'Bao-Viet.mobi'))
mobi = ('<p><a class="small" href="Bao-Viet.mobi">Tải bản MOBI (nếu bản trên không tải được)</a></p>'
        if has_mobi else '')

html = f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex, nofollow">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Báo Việt – {ngay}</title>
<style>
  body {{ font-family: Georgia, serif; margin: 24px; color: #000; background: #fff; text-align: center; }}
  h1 {{ font-size: 2.6em; margin: 0.2em 0 0; }}
  .date {{ font-size: 1.3em; letter-spacing: 0.05em; border-top: 4px double #000; border-bottom: 1px solid #000;
           padding: 0.3em 0; margin: 0.5em 0 1em; }}
  a.btn {{ display: block; font-size: 1.6em; font-weight: bold; color: #fff; background: #000;
           padding: 0.8em; margin: 0.6em 0; text-decoration: none; }}
  a.small {{ font-size: 1.1em; color: #000; }}
  img {{ width: 60%; border: 1px solid #000; }}
  .note {{ font-size: 1em; color: #333; margin-top: 1.5em; }}
</style>
</head>
<body>
<h1>Báo Việt</h1>
<div class="date">{ngay.upper()}</div>
<a class="btn" href="Bao-Viet.azw3">⬇ Tải báo hôm nay ({size:.1f} MB)</a>
{mobi}
<p><img src="bia.jpg" alt="Trang nhất"></p>
<p class="note">Tải xong, báo nằm trong Thư viện Kindle. Báo mới có lúc khoảng 6 giờ sáng.</p>
</body>
</html>
'''
with open(os.path.join(out, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html ok')
