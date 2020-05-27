from django.conf import settings
import numpy as np
import cv2

def opencv_dface(path):
    # Read the input image
    print("top path:"+path)

    img = cv2.imread(path,1)

    if (type(img) is np.ndarray):
        print(img.shape)

        factor = 1
        if img.shape[1] > 640:
            factor = 640.0 / img.shape[1]
        elif img.shape[0] > 480:
            factor = 480.0 / img.shape[0]

        if factor != 1:
            w = img.shape[1] * factor
            h = img.shape[0] * factor
            img = cv2.resize(img, (int(w), int(h)))

        baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL  #media folder

        # Load the cascade
        face_cascade = cv2.CascadeClassifier(baseUrl+'haarcascade_frontalface_default.xml')
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imwrite(path, img)

    else:
        print('something error')
        print(path)
