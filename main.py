# Trò chơi đoán số
# Máy chọn ngẫu nhiên một số từ 1 đến 50, người chơi có 5 lượt để đoán.

import random

so = random.randint(1, 50)  # Số bí mật của máy
print("Máy đã chọn một số từ 1 đến 50. Bạn có 5 lượt đoán.")

lan = 1  # Lần đoán hiện tại

while True:
    try:
        doan = int(input(f"Lần {lan}/5 - Đoán: "))

        # Nhập số ngoài khoảng 1-50 thì nhập lại, không bị mất lượt
        if doan > 50 or doan < 1:
            print("Hãy nhập số trong khoảng 1 đến 50!")
            continue

        if doan == so:
            print(f"Chính xác! Bạn đã đoán đúng sau {lan} lần!")
            break
        elif doan < so:
            # Đoán thấp hơn số đúng -> gợi ý đoán cao lên
            if lan == 5:
                print("Hết lượt! Số đúng là:", so)
                break
            else:
                print("Cao hơn!")
                lan = lan + 1
        elif doan > so:
            # Đoán cao hơn số đúng -> gợi ý đoán thấp xuống
            if lan == 5:
                print("Hết lượt! Số đúng là:", so)
                break
            else:
                print("Thấp hơn!")
                lan = lan + 1
    except ValueError:
        # Nhập chữ hoặc số thập phân thì báo lỗi, không bị mất lượt
        print("Hãy nhập số nguyên!")
