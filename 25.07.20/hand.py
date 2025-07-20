import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # 손가락 끝(엄지~새끼) 좌표: 4, 8, 12, 16, 20
            for idx in [4, 8, 12, 16, 20]:
                h, w, _ = frame.shape
                x = int(hand_landmarks.landmark[idx].x * w)
                y = int(hand_landmarks.landmark[idx].y * h)
                cv2.circle(frame, (x, y), 10, (0, 0, 0), -1)  # 검은 점

    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC 키
        break

cap.release()
cv2.destroyAllWindows()
# This code captures video from the webcam, processes it to detect hand landmarks using MediaPipe,
if __name__ == "__main__":
    # and draws black dots on the fingertips of detected hands.
    pass
# The program will exit when the ESC key is pressed.
# The code uses OpenCV for video capture and display, and MediaPipe for hand tracking.  
# It draws black dots on the fingertips of detected hands.