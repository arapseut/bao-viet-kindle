# Báo Việt cho Kindle

Mỗi sáng (5:30 giờ Việt Nam), GitHub Actions dùng [Calibre](https://calibre-ebook.com) gom tin mới
từ VnExpress, Tuổi Trẻ, Thanh Niên, Dân trí và BBC Tiếng Việt thành một tờ báo AZW3 có mục lục
và bìa trang nhất, rồi đăng lên GitHub Pages để Kindle tải bằng Trình duyệt.

Dùng cá nhân. Bản quyền nội dung bài báo thuộc các tòa soạn.

- `bao-viet.recipe`: công thức Calibre (chạy được cả trên máy tính: `ebook-convert bao-viet.recipe Bao-Viet.azw3`).
- `make_page.py`: tạo trang tải đơn giản cho Trình duyệt Kindle.
- `.github/workflows/bao-viet.yml`: lịch chạy hằng ngày.

Bìa học theo [Dayfold](https://github.com/HacDan/dayfold). Font [Playfair Display](https://fonts.google.com/specimen/Playfair+Display)
và [Literata](https://fonts.google.com/specimen/Literata) (SIL Open Font License) được tải lúc chạy.

## Cài một lần
1. **Settings → Secrets and variables → Actions → New repository secret**: tên `BAO_PATH`, giá trị là một chuỗi ngẫu nhiên.
2. **Actions → Bao Viet hang ngay → Run workflow** (chạy lần đầu để tạo nhánh `gh-pages`).
3. **Settings → Pages**: Source = *Deploy from a branch*, Branch = `gh-pages` / `(root)` → Save.
4. Trên Kindle: Trình duyệt → mở `https://<tài khoản>.github.io/bao-viet-kindle/<BAO_PATH>/` → đánh dấu trang.
