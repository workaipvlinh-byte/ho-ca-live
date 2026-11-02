# Hồ Cá Live

Game nuôi cá cho TikTok LIVE. Người xem comment là có một con cá của mình thả xuống hồ, ngồi xem càng lâu thì cá càng to. Tặng quà thì được cá xịn hơn, quà to nhất được làm chủ hồ. Có giọng đọc tiếng Việt chào tên từng người và cảm ơn quà, nhạc nền tự tạo nên không dính bản quyền.

## Chơi thế nào

- Comment lần đầu: thả một con cá thường (koi, cá vàng hoặc cá nóc) mang tên bạn.
- Gõ "ăn": rơi 3 hạt thức ăn mà chỉ cá của bạn ăn được, 15 giây một lần. Thả tim thì rơi thức ăn chung cho cả hồ.
- Ở lại xem: cứ 5 phút cá lớn thêm một nấc. Im lâu thì cá dạt ra xa rồi ngủ thành cá li ti. Cá được nhớ qua các buổi live, lần sau vào vẫn còn.
- Tặng quà: mỗi mức xu đổi ra một loài, từ Cá Vàng Bướm (1 xu) tới Rồng Thần, Phượng Hoàng và Long Vương (4888 xu, làm chủ hồ). Kim Long và Hồng Long mỗi hồ chỉ có một con.
- Follow được gắn nơ hồng, share được vương miện bạc.
- Sự kiện chạy theo giờ: giờ vàng 2 phút mỗi 10 phút, đua cá 3 chọi 3 mỗi 10 phút (có nhạc EDM riêng), cá VIP ngẫu nhiên mỗi 15 phút. Cả phòng gom đủ quà thì Cá Chép Cầu Vồng khổng lồ nhảy qua hồ.
- Hồ đổi sáng, hoàng hôn, đêm theo giờ máy. Đêm có tiếng dế.

Giọng đọc (Edge TTS, giọng Nam Minh) chào người mới vào, cảm ơn quà kèm câu chúc, chúc đúng chủ đề khi ai comment cầu mong gì đó. Nó không bao giờ tự đọc nguyên văn comment, tên bậy thì đọc thành "bạn". Muốn đọc comment nào thì chủ kênh bấm 🔊 ở trang điều khiển.

## Chạy

Cần cài Node.js trên máy Windows.

1. Bấm đúp `BAT-LIVE.bat`. Lần đầu tự cài thư viện 1–2 phút, xong tự mở trang điều khiển `http://localhost:3000`.
2. TikTok LIVE Studio → thêm nguồn **Link**: `http://lvh.me:3000/?view=stage`, kích thước 1080 × 1920. Trang này phát giọng đọc + nhạc nền.
3. Bắt đầu live, nhập username vào trang điều khiển, bấm **Kết nối**.

Chưa live mà muốn thử: bấm các nút giả lập ở trang điều khiển. Muốn nghe giọng ngay ở trang điều khiển: bấm **🔊 Thử giọng**.

Giữ cửa sổ `BAT-LIVE.bat` mở suốt buổi live. Chỉ chạy 1 game một lúc (cùng cổng 3000).

## Sửa game

Cả game nằm trong `index.html` (canvas, WebGL, three.js). Đừng sửa thẳng file này: sửa `nguon/ho-ca-khung.html`, rồi chạy `python nguon/build.py` để ghép ảnh trong `public/assets/` vào `index.html`.

`server.ts` lo phần kết nối TikTok (`tiktok-live-connector`), đẩy sự kiện xuống trang qua SSE và đọc giọng qua `/api/tts`. Server chỉ nghe ở `127.0.0.1`, người khác cùng Wi-Fi không điều khiển được.
