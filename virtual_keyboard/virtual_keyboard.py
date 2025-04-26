import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller

# Kamera sozlamalari
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Qo‘l aniqlovchi model
detector = HandDetector(detectionCon=0.8)
keyboard = Controller()

# Klaviatura tugmalari
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

ClickedText = ""

# Tugma klassi
class Button():
    def __init__(self, pos, text, size=[80, 80]):
        self.pos = pos
        self.text = text
        self.size = size

# Tugmalarni chizish funksiyasi
def drawALL(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
    return img

# Tugma obyektlarini yaratish
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

# Asosiy sikl
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # Qo‘lni aniqlash

    img = drawALL(img, buttonList)  # Barcha tugmalarni chizish

    if hands:
        lmList = hands[0]['lmList']

        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 0), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

                # Faqat (x, y) koordinatalarini olish
                point1 = lmList[8][:2]
                point2 = lmList[12][:2]
                length, _, _ = detector.findDistance(point1, point2, img)

                if length < 50:
                    keyboard.press(button.text)
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
                    ClickedText += button.text
                    sleep(0.2)

    # Yozilgan matn oynasi
    cv2.rectangle(img, (55, 345), (700, 450), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, ClickedText, (60, 425),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    # Natijani ko‘rsatish
    cv2.imshow('camera', img)
    cv2.waitKey(1)
