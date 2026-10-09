# Trò chơi đoán số

Trò chơi đoán số chạy trên màn hình dòng lệnh (terminal), viết bằng Python.

Máy chọn ngẫu nhiên một số từ 1 đến 50, bạn có **5 lượt** để đoán. Sau mỗi lần đoán, máy sẽ gợi ý số cần tìm **cao hơn** hay **thấp hơn**.

## Tính năng

- Máy chọn ngẫu nhiên một số từ 1 đến 50
- Giới hạn 5 lượt đoán
- Gợi ý "Cao hơn!" hoặc "Thấp hơn!" sau mỗi lần đoán
- Báo lỗi khi nhập chữ hoặc nhập số ngoài khoảng 1–50 (không bị mất lượt)
- Hiện đáp án khi hết lượt

## Yêu cầu

- [Python](https://www.python.org/downloads/) 3.6 trở lên
- Không cần cài thêm thư viện nào

## Cách chạy

1. Tải code về máy:

   ```
   git clone https://github.com/ten-cua-ban/tro-choi-doan-so.git
   cd tro-choi-doan-so
   ```

2. Chạy chương trình:

   ```
   python main.py
   ```

   (Trên macOS/Linux có thể cần gõ `python3 main.py`.)

## Ví dụ khi chơi

```
Máy đã chọn một số từ 1 đến 50. Bạn có 5 lượt đoán.
Lần 1/5 - Đoán: 25
Cao hơn!
Lần 2/5 - Đoán: 40
Thấp hơn!
Lần 3/5 - Đoán: 33
Chính xác! Bạn đã đoán đúng sau 3 lần!
```

## Kiến thức áp dụng

Đây là dự án luyện tập của mình, sử dụng:

- Thư viện `random` để tạo số ngẫu nhiên
- Vòng lặp `while` và câu điều kiện `if / elif / else`
- Xử lý lỗi bằng `try / except`

## Tác giả

Twilight-Stargazing– [GitHub](https://github.com/Twilight-Stargazing)
