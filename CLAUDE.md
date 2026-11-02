# Hồ Cá Live: ghi chú cho Claude

> Luật chung ở `E:\VibeCode\CLAUDE.md`. File này chỉ nói riêng game Hồ Cá.

## Cấu trúc (khác `_base`)

- Toàn bộ game nằm trong **một file** `index.html` (canvas + WebGL + three.js r128 từ cdnjs). Thư mục `src/` của `_base` không dùng.
- Sửa game: sửa `nguon/ho-ca-khung.html` (khung, ảnh để chỗ `__BG__`, `__LOTUS__`, `__RACE__`), rồi chạy `python nguon/build.py` để ghép ảnh ở `public/assets/` vào `index.html`.
- `server.ts` giữ nguyên của `_base`: kết nối TikTok, SSE `/api/tiktok/events`, `/api/control` (speak, setName, reset, custom = `race` | `vip`), `/api/test/emit`, giọng `/api/tts`.
- `?view=stage` = trang LIVE Studio: phát giọng Edge + nhạc nền tự tạo (Web Audio). Trang điều khiển `/` im lặng, có nút giả lập (bắn qua `/api/test/emit` nên trang stage cũng nhận).
- Tên hồ = "Tên kênh" của `_base` (`setName`, lưu `settings.json`).

## Luật chơi chính

- Comment → thả cá (cá thường 1 màu: koi / cá vàng / cá nóc). Gõ "ăn" → 3 hạt chỉ cá mình ăn được (15 giây/lần); 12 hạt = +1 nấc, nên gõ ăn tối đa ~1 nấc/phút. Thả tim cũng rơi thức ăn chung.
- Ở lại xem: cá lớn 1 nấc mỗi 5 phút (bản thử 40 giây), mỗi nấc +14%. Ít tương tác 2 phút → dạt lên vùng xa; im lâu → ngủ thành cá li ti. Cá được nhớ qua các buổi live (localStorage `hoca-memory` trên trang stage, theo username).
- Quà (xu): 1 Cá Vàng Bướm · 8 Cá Bướm Ngũ Sắc · 38 Koi Ngọc · 68 Koi Hoàng Kim · 99 Cá Mập Trắng · 188 Kim Long (chỉ 1) · 299 Cá Voi Xanh · 388 Hồng Long (chỉ 1) · 999 Rồng Thần · 1666 Phượng Hoàng · 4888 Long Vương (chủ hồ).
- Màu tên: thường trắng < cam < vàng < đỏ < huyền thoại. Chỉ Vua hồ + 3 cá quà to nhất phát sáng.
- Follow → nơ hồng; share → vương miện bạc. Giờ vàng 10 phút mở 2 phút (vây bạc). Cá Chép Cầu Vồng (thay Rồng 7 màu, chủ kênh chê xấu): cả phòng đủ quà thì cá chép khổng lồ nhảy qua hồ + cầu vồng; xem thử bằng `?test=carp`. Cá VIP ngẫu nhiên mỗi 15 phút. Đua cá 3 chọi 3 mỗi 10 phút (kênh đua riêng).
- Ngày / hoàng hôn / đêm theo giờ máy.

## Giọng đọc (học từ Đi Chùa)

- Thời gian: chạy từ server (`SERVED`) = số live thật; mở file trực tiếp = bản thử chạy nhanh (`TK(demo, real)`).
- Tên đọc qua `speakable()` (số thành chữ, tách tên dính, tên bậy = "bạn"). Không bao giờ tự đọc nội dung comment.
- Chào: người vào live + người comment lần đầu vào `greetQueue` (tối đa 300, không bỏ ai), 6 giây 1 lượt, tối đa 6 tên (2 câu x 3 tên). Câu chào có `keep` nên không bị coi là cũ.
- Quà: lên đầu hàng, kèm 1 câu chúc gia đình (`LINES.family`). Mỗi người 30 giây 1 lần (quà ≥99 xu luôn cảm ơn); hàng quà dài thì quà nhỏ chỉ đọc câu ngắn. Sau 2 câu quà liền thì cho 1 câu chào chen vào. Không đọc tên quà tiếng Anh.
- Comment có lời cầu (mong/cầu/xin + chủ đề) → chúc đúng chủ đề, mỗi người 10 phút, cả phòng 20 giây 1 lần.
- Giọng rảnh mới chen câu: nhắc luật / hỏi han theo giờ (`LINES.chat`) / câu hỏi kéo comment, 45 giây kiểm tra 1 lần; chúc chung 2 phút; nhắc chia sẻ kèm tên 3 người vừa tương tác 5 phút.
- Trang điều khiển: danh sách comment, bấm 🔊 thì stage đọc "Bạn X nói: ..."; ô "Đọc ngay" tự gõ câu (đi qua `/api/control` speak, lên đầu hàng).
- Avatar vẽ trên canvas lớp chữ (không đọc ngược pixel) nên không cần proxy.
- Đua cá: nhạc EDM 128 BPM tự tạo (dồn trống lúc gom đội, drop lúc đua), nhạc đàn tranh tắt dần rồi về lại khi xong.

## Quyết định của chủ kênh

- Nền hồ: `public/assets/nen-ho-1080.webp` (thác dời vào giữa). Kênh đua: `kenh-dua-1080.webp`.
- Bảng gỗ tên hồ + khẩu hiệu "Ở lại xem càng lâu, cá càng to!" nền vàng đậm.
- Không dùng bài nhạc có bản quyền: nhạc nền tự tạo (đàn tranh ngũ cung + tiếng suối, đêm có dế).
- Không làm quay số / rương may rủi. Không ghi giới hạn giả.
