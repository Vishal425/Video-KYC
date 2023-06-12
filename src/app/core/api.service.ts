//  ===========================================================================================================
// Original Author : Akshay Borje
// Creation Date   : 19/01/2021
// Project Name    : Berar Finance
// Module Name	   : Core
// Page Name    : API service

// Modify Author    -   Modify Date   -  Reason Of Modify

// Akshay  B         -   19/01/2021    - Added post to server function.
// Ashwini L         -   27/02/2021    - Added common parameters from master pages to be send to the server in post function.
// Akshay  B         -   10/02/2021    - Modified common parametrs to be send to server. Getting value form session storage.
// Ashwini L         -   03/04/2021    - Set session variables of longitude ,latitude and accuracy.
// ==================================================================================================================================

import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import * as moment from 'moment';
import { catchError } from 'rxjs/operators';
import { ObservableInput } from 'rxjs';

@Injectable()
export class ApiService {
  apiconfig: any;
  path: string;
  obj: any;
  page: any;
  handleError: (err: any, caught: Observable<Object>) => ObservableInput<any>;

  constructor(private http: HttpClient) {

    this.apiconfig = {
      // serviceUrl: 'http://192.168.1.129:5600'
      serviceUrl: 'http://192.168.1.120:8000'
    }
  }

  sendToServer<interfaceType>(path, obj, page) {

    obj.op_br_mst_id = 1;
    obj.longitude = 1;
    obj.latitude = 1;
    obj.accuracy = 1;
    obj.longitude = '111';
    obj.latitude = '111';
    obj.accuracy = '111';
    obj.app_mode = "SYS";
    obj.request_from = "CBS";
    obj.transaction_date = moment(new Date().toLocaleDateString()).format("DD-MM-YYYY"),
    obj.transaction_time = moment(new Date()).format("HH:mm:ss");
    obj.pass_user_id = 1;
    obj.enter_desc = null;

    return this.http.post<interfaceType>(path, obj);
  }

  getFromServer(path, queryParams) {
    return this.http.get(this.apiconfig.serviceUrl + path, { params: queryParams });
  }

//   OCR_Image(type, base64) {
//     var input = {
//       obj: {
//         // "UserId": "3",
//         // "APICode": "ocr/kyc",
//         // "VerificationKey": "KARZA123",
//         // "Longitude": "94.786",
//         // "Latitude": "92.365",
//         // "Accuracy": "14",
//         // "App_Mode": "webservice",
//         // "Request_From": "UAT Server",
//         // "Device_Id": "Machine",
//         // "fileB64": base64,
//         // "maskAadhaar": "false",
//         // "hideAadhaar": "false",
//         // "conf": "true",
//         // "docType": ""
//         "UserId": "3",
//         "APICode": "ocr/kyc",/* kycocr */
//         "VerificationKey": "KARZA123",
//         "Longitude": "94.786",
//         "Latitude": "92.365",
//         "Accuracy": "14",
//         "App_Mode": "webservice",
//         "Request_From": "UAT Server",
//         "Device_Id": "Machine",
//         "fileB64": base64,
//         "maskAadhaar": "false",
//         "hideAadhaar": "false",
//         "conf": "true",
//         "docType": "",

//         // "checkBlur": "false",             //True if you need the quality (blur) score of the KYC card region. Returns a score in range of 0 (poor quality) to 100 (good quality)
//         // "checkBlackAndWhite": "false", //True to check if the KYC card is grayscale / photocopy. Returns boolean output
//         // "checkCutCard": "false",        //True to check if the KYC card is incomplete. Returns boolean output
//         // "checkBrightness": "false"
//       }
//     }
//     return this.http
//       .post(this.apiconfig.serviceUrl + '/karzaApi', input,)
//       .pipe(catchError(this.handleError));
//   }


//   text_Zoop(type, base64) {


//     return this.http
//       .post("http://192.168.1.140:5600/ZoopOne", type)
//       .pipe(catchError(this.handleError));

//   }

//   cibil(type) {
//     return this.http
//       .post("http://192.168.1.140:5600/cibil", type)
//       .pipe(catchError(this.handleError));
//   }
}