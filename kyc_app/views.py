# from bitarray import test
from re import U
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import datetime
import json
# from sympy import print_rcode



@csrf_exempt
def sample(request):
    # Opening JSON file
    with open('example.json', 'r') as openfile:
        json_object = json.load(openfile)
    accessKey1 = json_object['accessKey1']
    caseId1 = json_object['caseId1']
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    u_name = body['name']
    u_age= body['age']
    u_gender= body['gender']
    u_otp = body['otp']
    u_pan = body['pan']
    u_adhar = body['adhar']
    print(u_age)
    print(u_otp)
    # accessKey1,caseId1 = test(request)
    # print(accessKey1)
    url4 = 'http://192.168.1.61//VGDocverify/VGKVerify.asmx/GetAadhaarFile'
    headers = {'Content-Type': 'application/json'}
    data4 =  {"obj":[{
        "UserId": "3",
        "VerificationKey": "KARZA123",
        "Longitude": "21",
        "Latitude": "77",
        "Accuracy": "85",
        "App_Mode": "a",
        "Request From": "Mob",
        "Device_Id": "456",
        "DeviceInfo": "",
        "APICode": "get-aadhaar-file",
        "OTP":u_otp,
        "shareCode":"1234",
        "accessKey": accessKey1,
        "caseId": caseId1

    }]}               
    response  = requests.post(url4, data=json.dumps(data4), 
                                headers=headers)
    data4= response.text
    print(data4)

    import cv2
    import math
    import time
    import pandas as pd
    import os
    from deepface import DeepFace
    import base64

    def getFaceBox(net, frame,conf_threshold = 0.75):
        frameOpencvDnn = frame.copy()
        frameHeight = frameOpencvDnn.shape[0]
        frameWidth = frameOpencvDnn.shape[1]
        blob = cv2.dnn.blobFromImage(frameOpencvDnn,1.0,(300,300),[104, 117, 123], True, False)

        net.setInput(blob)
        detections = net.forward()
        bboxes = []

        for i in range(detections.shape[2]):
            confidence = detections[0,0,i,2]
            if confidence > conf_threshold:
                x1 = int(detections[0,0,i,3]* frameWidth)
                y1 = int(detections[0,0,i,4]* frameHeight)
                x2 = int(detections[0,0,i,5]* frameWidth)
                y2 = int(detections[0,0,i,6]* frameHeight)
                bboxes.append([x1,y1,x2,y2])
                cv2.rectangle(frameOpencvDnn,(x1,y1),(x2,y2),(0,255,0),int(round(frameHeight/150)),8)

        return frameOpencvDnn , bboxes



    faceProto = r"opencv_face_detector.pbtxt"
    faceModel = r"opencv_face_detector_uint8.pb"

    ageProto = r"age_deploy.prototxt"
    ageModel = r"age_net.caffemodel"

    genderProto = r"gender_deploy.prototxt"
    genderModel = r"gender_net.caffemodel"

    MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
    ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)','(33,37)', '(38-43)', '(48-53)', '(60-100)']
    genderList = ['Male', 'Female']


    #load the network
    ageNet = cv2.dnn.readNet(ageModel,ageProto)
    genderNet =  cv2.dnn.readNet(genderModel, genderProto)
    faceNet = cv2.dnn.readNet(faceModel, faceProto)

    cap = cv2.VideoCapture(0)
    padding = 20

    capture_duration = 10
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

    start_time = time.time()
    # ret , frame = cap.read()
    while cv2.waitKey(1) < 0:
        #read frame
        t = time.time()
        hasFrame , frame = cap.read()

        if not hasFrame:
            cv2.waitKey()
            break
        #creating a smaller frame for better optimization
        small_frame = cv2.resize(frame,(0,0),fx = 0.5,fy = 0.5)

        frameFace ,bboxes = getFaceBox(faceNet,small_frame)
        if not bboxes:
            print("No face Detected, Checking next frame")
            continue
        for bbox in bboxes:
            face = small_frame[max(0,bbox[1]-padding):min(bbox[3]+padding,frame.shape[0]-1),
                    max(0,bbox[0]-padding):min(bbox[2]+padding, frame.shape[1]-1)]
            blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
            genderNet.setInput(blob)
            genderPreds = genderNet.forward()
            gender = genderList[genderPreds[0].argmax()]
    #         i = genderpreds[0].argmax()
    #         gender = genderList[i]
            x1 = ("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))
            print(x1)

            ageNet.setInput(blob)
            agePreds = ageNet.forward()
            age = ageList[agePreds[0].argmax()]
            print("Age Output : {}".format(agePreds))
            y1 = ("Age : {}, conf = {:.3f}".format(age, agePreds[0].max()))
            print(y1)

            label = "{},{}".format(gender, age)
            frame1 = cv2.putText(frameFace, label, (bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow("Age Gender Demo", frameFace)
        print("time : {:.3f}".format(time.time() - t))
        if ( int(time.time() - start_time) < capture_duration ):
            out.write(frame)
        #         cv2.imshow('frame',frame1)
        else:
            break
    cap.release()
    cv2.destroyAllWindows() 

    import cv2
    capture = cv2.VideoCapture('output.avi')
    frameNr = 0
    while (True):
        success, frame = capture.read()
        if success:
            cv2.imwrite('frametest.jpg', frame)
        else:
            break
        frameNr = frameNr+1

            # Read the input image
    img = cv2.imread('frametest.jpg')

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
        faces = img[y:y + h, x:x + w]
    #     cv2.imshow("face",faces)
        cv2.imwrite('extracted_face.jpg', faces)

    # Display the output
    cv2.imwrite('detected.jpg', img)
    # cv2.imshow('img', img)
    cv2.waitKey()    

    capture.release()

    #extract base64 from video img
    with open("frametest.jpg", "rb") as img_file:
        videoimg = base64.b64encode(img_file.read()).decode("utf-8")

    imgdata = base64.b64decode(data4.split(':{"')[4].split('},')[2].split(',')[0].split(':')[1].replace('"',''))
    filename = 'adharimage.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    # Read the input frame
    img = cv2.imread('adharimage.jpg')
    
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        faces = img[y:y + h, x:x + w]
        #cv2.imshow("face",faces)
        cv2.imwrite('input_face.jpg', faces)
        

    # Display the output
    cv2.imwrite('input_detected.jpg', img)
    #cv2.imshow('img', img)
    cv2.waitKey()


    #img1_path = face extracted from the image inputed by user
    #img2_path = face extracted from the video taken from webcam
    # face_verification = DeepFace.verify(img1_path = "input_face.jpg", img2_path = "extracted_face.jpg" ,enforce_detection=False)
    # age_gender_verification = DeepFace.analyze(img_path = "extracted_face.jpg", actions = ['age', 'gender', 'race', 'emotion'], enforce_detection=False)
    face_verification = DeepFace.verify(img1_path = "input_face.jpg", img2_path = "extracted_face.jpg"  ,model_name = 'VGG-Face', distance_metric = 'cosine', enforce_detection = False, detector_backend = 'opencv')
    age_gender_verification = DeepFace.analyze(img_path = "extracted_face.jpg", actions = ['age', 'gender'] , models = None, enforce_detection = False, detector_backend = 'opencv', prog_bar = True)
    print(face_verification)
    print(age_gender_verification)

    print("Level 1 verification")

    print("Name : ", u_name)

    # face match
    if (face_verification["verified"]==True):
        print("Face matched")
    else:
        print("Face not matched")

    # age match
    print("Input age : ", u_age)
    print("Detected age : ", age_gender_verification["age"])
    a=age_gender_verification["age"]
    b=int(u_age)
    s=100-(((abs(b-a))/((a+b)/2))*100)
    #print(s)
    if (s>=50):
        print("Age verified" + " , " + "match percentage :",s )
    else:
        print("age not verified" + " , " + "match percentage :",s)

    # # gender match
    # print("Input gender : ", u_gender)
    # print("Detected gender : ", age_gender_verification["gender"])
    # c=(age_gender_verification["gender"])
    # if(c=="Man"):
    #     c="male"
    # else:
    #     c="female"

    # d=u_gender
    # if (c.lower()==d.lower()):
    #     print("Gender verified")
    # else:
    #     print("Gender not verified")
    imgsrc = data4.split(':{"')[4].split('},')[2].split(',')[0].split(':')[1].replace('"','')
    adharname = data4.split(':{"')[2].split(',')[2].split(':')[1].replace('"','')
    adhardob = data4.split(':{"')[2].split(',')[3].split(':')[1].replace('"','')
    adhargender=data4.split(':{"')[2].split(',')[4].split(':')[1].replace('"','')
    inputname = data4.split(':{"')[5].split(':')[1].split(',')[0].replace('"','')
    namematchpercent = data4.split(':{"')[5].split(':')[2].split(',')[0]
    face_verified = face_verification['verified']
    face_match_percent = (1 - face_verification['distance'])*100
    detectedage = age_gender_verification['age']
    detectedgender = age_gender_verification['gender']
    output = {"adharname": adharname,"adhardob": adhardob,"adhargender": adhargender,'inputname':inputname,'inputage':u_age,'inputgender':u_gender,
         'pan':u_pan,'adhar':u_adhar,'namematchpercent':namematchpercent,'face_verified':face_verified,'face_match_percent':face_match_percent,
         'detectedage':detectedage,'detectedgender':detectedgender,'imgsrc':imgsrc,'videoimg':videoimg,'agematchpercent':s}
    j_data = json.dumps(output)
    df = pd.DataFrame(output,index = [0])
    df.to_csv('Customer_data.csv', mode='a', index=False,header = False)



    return HttpResponse(j_data, content_type='application/json')

    
    # Driver code to test above method
    # d = sample() 
    # print(d)   


import json
import requests
@csrf_exempt
def test(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    u_name = body['name']
    u_age= body['age']
    u_gender= body['gender']
    u_pan = body['pan']
    u_adhar = body['adhar']
    u_dob = body['dob']
    print("name",u_name)
    print("dob",u_dob)

    
    url = 'http://192.168.1.61//VGDocverify/VGKVerify.asmx/Aadhaar'
    headers = {'Content-Type': 'application/json'}
    data =  {"obj":[{"UserId": "3","VerificationKey": "KARZA123","Longitude": "21","Latitude": "77","Accuracy": "85",
                    "App_Mode": "a","Request From": "Mob","Device_Id": "456","DeviceInfo": "", 
                    "APICode": "aadhaar-consent", "Name": u_name}]}
    response  = requests.post(url, data=json.dumps(data), 
                                headers=headers)
    data = response.text
    accessKey1=data.split('{')[2].split(',')[1].split(':')[1].replace('"','')
    caseId1 = data.split('{')[3].split(':')[1].replace('"}}','').replace('"','')

    url2 = 'http://192.168.1.61//VGDocverify/VGKVerify.asmx/PanAadhaarProfile'
    headers = {'Content-Type': 'application/json'}
    data2 =  {"obj":[{
        "UserId": "3",
        "VerificationKey": "KARZA123",
        "Longitude": "21",
        "Latitude": "77",
        "Accuracy": "85",
        "App_Mode": "a",
        "Request From": "Mob",
        "Device_Id": "456",
        "DeviceInfo": "",
        "APICode": "pan-aadhaar-profile",
        "aadhaarNo": u_adhar,
        "pan": u_pan,
        "monthYearOfBirth": datetime.datetime.strptime(u_dob, "%Y-%m-%d").strftime('%m-%Y'),
        "consent": "Y",
        "accessKey": accessKey1,
        "caseId": caseId1

    }]}

    response  = requests.post(url2, data=json.dumps(data2),  headers=headers)
    data2 = response.text
    print('panadharprofile',data2)

    url3 = 'http://192.168.1.61//VGDocverify/VGKVerify.asmx/GetAadhaarOTP'
    headers = {'Content-Type': 'application/json'}
    data3 =  {"obj":[{
        "UserId": "3",
        "VerificationKey": "KARZA123",
        "Longitude": "21",
        "Latitude": "77",
        "Accuracy": "85",
        "App_Mode": "a",
        "Request From": "Mob",
        "Device_Id": "456",
        "DeviceInfo": "",
        "APICode": "get-aadhaar-otp",
        "aadhaarNo": u_adhar,
        "accessKey": accessKey1,
        "caseId": caseId1

    }]}
                
    response  = requests.post(url3, data=json.dumps(data3),   headers=headers)
    data3 = response.text 
    print('otpdata',data3)
    # test.accessKey1=accessKey1
    # test.caseId1=caseId1
    j_data = json.dumps({"accessKey1": accessKey1,"caseId1": caseId1,"MobileNo":data2.split('result')[1].split(',')[0].replace('":{','').replace('}','')[-11:-1],"statuscode":data3.split('statusCode')[1].split(':')[1][0:3]})
    with open("example.json", "w") as outfile:
        outfile.write(j_data)
    # return accessKey1,caseId1
    return HttpResponse(j_data, content_type='application/json')


# import json
# import requests
# @csrf_exempt

# def otp(request):
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
#     u_name = body['name']
#     u_age= body['age']
#     u_gender= body['gender']
#     u_otp = body['otp']
#     print(u_age)
#     print(u_otp)
#     # list = test(request)
#     # accessKey1=test.accessKey1
#     # caseId1=test.caseId1
    
#     # print('accesskey',accessKey1)
#     url4 = 'http://192.168.1.61//VGDocverify/VGKVerify.asmx/GetAadhaarFile'
#     headers = {'Content-Type': 'application/json'}
#     data4 =  {"obj":[{
#         "UserId": "3",
#         "VerificationKey": "KARZA123",
#         "Longitude": "21",
#         "Latitude": "77",
#         "Accuracy": "85",
#         "App_Mode": "a",
#         "Request From": "Mob",
#         "Device_Id": "456",
#         "DeviceInfo": "",
#         "APICode": "get-aadhaar-file",
#         "OTP":u_otp,
#         "shareCode":"1234",
#         "accessKey": '05083f6a-8cff-4a3d-89d4-c2d60331a55c',
#         "caseId": '17062022140746'

#     }]}               
#     response  = requests.post(url4, data=json.dumps(data4), 
#                                 headers=headers)
#     data4= response.text
#     print('adhardata',data4)
#     return render(request,'nam.html')
