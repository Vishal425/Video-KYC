from django.shortcuts import render
from django.http import HttpResponse

import json
# Create your views here.
from deepface import DeepFace
import cv2
def test(request):
    # Convert into grayscale
    try:
        url = r'http://192.168.1.158:9011/KYC/AgeGender/client.jpg'
        # response = requests.get(url)
        # img = Image.open(BytesIO(response.content))
        from skimage import io
        img = io.imread(url)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Load the cascade
        face_cascade = cv2.CascadeClassifier(r'D:\Project Reports\agegender\haarcascade_frontalface_default.xml')

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw rectangle around the faces and crop the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
            faces = img[y:y + h, x:x + w]
        #     cv2.imshow("face",faces)
            cv2.imwrite('extracted_face.jpg', faces)

        

        # face_verification = DeepFace.verify(img1_path = "input_face.jpg", img2_path = "extracted_face.jpg"  ,model_name = 'VGG-Face', distance_metric = 'cosine', model = None, enforce_detection = False, detector_backend = 'opencv', align = True, prog_bar = True, normalization = 'base')
        age_gender_verification = DeepFace.analyze(img_path = 'extracted_face.jpg', actions = ['age', 'gender'] , enforce_detection = False, detector_backend = 'opencv')
        # print(face_verification)
        print(age_gender_verification)
        j_data = json.dumps(age_gender_verification)
        convertedDict = json.loads(j_data)
        j_data1 = {'output':convertedDict}
        j_data1 = json.dumps(j_data1)
        print('j_data1',j_data1)
        # j_data1 ='output=' , j_data
        return HttpResponse(j_data1, content_type='application/json')
    except:
        return HttpResponse('Client Image URL Not found')

