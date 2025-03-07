import cv2

cap = cv2.VideoCapture(0)
success, img = cap.read()

if not success:
    print("Failed to access camera.")
else:
    cv2.imshow("Test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cap.release()
