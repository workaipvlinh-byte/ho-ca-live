# Hồ Cá Live

Game nuôi cá cho TikTok LIVE. Người xem comment là có một con cá mang tên mình thả xuống hồ, ngồi xem càng lâu thì cá càng to. Tặng quà thì được cá xịn hơn, quà to nhất được làm chủ hồ. Có giọng đọc tiếng Việt chào tên từng người và cảm ơn quà. Nhạc nền do game tự tạo nên không dính bản quyền.

Mã nguồn game nằm ở `nguon/ho-ca-khung.html`, phần server ở `server.ts`.

## Tính năng nổi bật

### Ai cũng có cá riêng

- Comment lần đầu: hồ thả một con cá thường (koi, cá vàng hoặc cá nóc) mang tên và avatar của bạn.
- Gõ "ăn": rơi 3 hạt thức ăn mà chỉ cá của bạn ăn được, 15 giây một lần. Đủ 12 hạt thì cá lớn thêm một nấc, nên gõ ăn liên tục cũng chỉ được khoảng một nấc mỗi phút.
- Thả tim: rơi thức ăn chung cho cả hồ.
- Ở lại xem: cứ 5 phút cá lớn thêm một nấc, mỗi nấc to thêm 14%. Hai phút không tương tác thì cá dạt ra vùng xa, im lâu nữa thì ngủ thành cá li ti.
- Cá được nhớ theo username qua các buổi live. Buổi sau người xem quay lại, cá vẫn còn nguyên cỡ cũ.

### Quà đổi ra cá

| Xu | Cá |
|---:|---|
| 1 | Cá Vàng Bướm |
| 8 | Cá Bướm Ngũ Sắc |
| 38 | Koi Ngọc |
| 68 | Koi Hoàng Kim |
| 99 | Cá Mập Trắng |
| 188 | Kim Long (mỗi hồ chỉ 1 con) |
| 299 | Cá Voi Xanh |
| 388 | Hồng Long (mỗi hồ chỉ 1 con) |
| 999 | Rồng Thần |
| 1666 | Phượng Hoàng |
| 4888 | Long Vương, làm chủ hồ |

Tên người chơi đổi màu theo độ chịu chơi: trắng, cam, vàng, đỏ rồi huyền thoại. Chỉ Vua hồ và 3 con cá quà to nhất được phát sáng, nên phát sáng vẫn hiếm. Follow được gắn nơ hồng, share được vương miện bạc.

### Sự kiện giữ người xem

- Đua cá 3 chọi 3 mỗi 10 phút, đua trên một kênh nước riêng. Lúc gom đội có nhạc EDM 128 BPM dồn trống, lúc đua thì drop, xong lại về nhạc đàn tranh.
- Giờ vàng: cứ 10 phút mở 2 phút, cá được gắn vây bạc.
- Cá VIP ngẫu nhiên mỗi 15 phút.
- Cá Chép Cầu Vồng: cả phòng gom đủ quà thì một con cá chép khổng lồ nhảy qua hồ kèm cầu vồng.
- Hồ đổi sáng, hoàng hôn, đêm theo giờ trên máy. Ban đêm có tiếng dế.

### Giọng đọc tiếng Việt

- Giọng Edge TTS (Nam Minh), lỗi thì tự chuyển sang Google.
- Chào người vào live và người comment lần đầu, không bỏ sót ai. Mỗi 6 giây đọc một lượt, tối đa 6 tên.
- Quà được ưu tiên đọc trước, kèm một câu chúc gia đình. Quà từ 99 xu trở lên lần nào cũng được cảm ơn.
- Ai comment cầu mong gì (sức khỏe, tiền bạc...) thì được chúc đúng chủ đề đó.
- Lúc rảnh thì nhắc luật, hỏi han theo giờ, rủ comment, nhắc share kèm tên người vừa tương tác.
- Số trong tên được đọc thành chữ, tên tục bị đọc thành "bạn". Giọng không bao giờ tự đọc nguyên văn comment. Muốn đọc comment nào thì chủ kênh bấm 🔊 ở trang điều khiển.

### Trang điều khiển cho chủ kênh

- Ô nhập username TikTok và nút Kết nối.
- Danh sách comment, bấm 🔊 để stage đọc "Bạn X nói: ...".
- Ô "Đọc ngay" để tự gõ câu cho giọng đọc, câu này được đọc trước mọi thứ.
- Đổi tên hồ. Tên được lưu lại, tắt máy mở lại vẫn còn.
- Nút giả lập để thử khi chưa live: comment, 100 tim, từng mức quà, follow, share, bốc cá VIP, đua cá ngay, sang buổi live mới.
- Chế độ "Live giả" chạy tự động với 30, 300 hoặc 500 người xem để xem hồ đông trông ra sao.
- Đổi cảnh ngày / hoàng hôn / đêm bằng tay, hoặc để theo giờ thật.
- Chọn giọng Edge Nam Minh hoặc giọng trình duyệt, có nút tắt tiếng.
- Từ cấm trong comment bị che thành `***`.

## Cài đặt

Cần một máy Windows có TikTok LIVE Studio. Không cần biết code.

### 1. Cài Node.js

1. Vào https://nodejs.org, tải bản **LTS** (bản 20.19 trở lên).
2. Mở file vừa tải, bấm Next tới hết. Giữ nguyên các lựa chọn mặc định.
3. Kiểm tra: mở Command Prompt, gõ `node -v`. Hiện ra số phiên bản (ví dụ `v22.x.x`) là được.

### 2. Tải game về

Cách dễ nhất: trên trang GitHub này, bấm nút xanh **Code**, chọn **Download ZIP**, rồi giải nén ra một thư mục, ví dụ `D:\ho-ca-live`.

Nếu máy có Git thì gõ:

```
git clone https://github.com/workaipvlinh-byte/ho-ca-live.git
```

### 3. Chạy lần đầu

1. Vào thư mục game, bấm đúp `BAT-LIVE.bat`.
2. Lần đầu nó tự cài thư viện, mất khoảng 1–2 phút (cần mạng).
3. Xong thì trình duyệt tự mở trang điều khiển `http://localhost:3000`.

Từ lần sau chỉ cần bấm đúp `BAT-LIVE.bat` là chạy, không phải cài lại.

## Lên live

1. Bấm đúp `BAT-LIVE.bat`. Giữ cửa sổ đen này mở suốt buổi live, tắt nó là game tắt.
2. Mở TikTok LIVE Studio, thêm nguồn **Link** với địa chỉ `http://lvh.me:3000/?view=stage`, kích thước 1080 × 1920.
3. Bắt đầu live.
4. Ở trang điều khiển, nhập username TikTok của kênh, bấm **Kết nối**.

Giọng đọc và nhạc nền phát từ trang stage trong LIVE Studio, nên người xem nghe được. Trang điều khiển im lặng. Muốn nghe thử giọng ở trang điều khiển thì bấm **🔊 Thử giọng**.

Chưa live mà muốn thử: bấm các nút giả lập ở trang điều khiển, trang stage cũng nhận được.

## Gặp lỗi

- Bấm `BAT-LIVE.bat` báo không nhận ra `npm`: chưa cài Node.js, hoặc cài xong chưa khởi động lại máy.
- Trang không mở được / báo cổng 3000 đang bận: đang có game khác chạy. Tắt cửa sổ `BAT-LIVE.bat` của game kia rồi mở lại. Mỗi lúc chỉ chạy được một game.
- Live không nghe giọng: kiểm tra nguồn Link trong LIVE Studio có bật âm thanh không, và địa chỉ phải có `?view=stage`.
- Kết nối không được: kênh phải đang live thì mới kết nối được.

## Sửa game

Cả game chạy trong một file `index.html` (canvas, WebGL, three.js). File này được tạo ra từ khung, nên đừng sửa thẳng:

1. Sửa `nguon/ho-ca-khung.html`.
2. Chạy `python nguon/build.py` (cần Python 3) để ghép ảnh trong `public/assets/` vào `index.html`.

`server.ts` lo kết nối TikTok (`tiktok-live-connector`), đẩy sự kiện xuống trang qua SSE và đọc giọng qua `/api/tts`. Server chỉ nghe ở `127.0.0.1`, người khác cùng Wi-Fi không điều khiển được.
