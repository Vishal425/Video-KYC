
import {Component, Inject} from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { HttpClient, HttpClientModule } from '@angular/common/http';

/**
 * @title Dialog Overview
 */

 export interface DialogData {
  gender: any;
  age: any;
  pan: any;
  dob: any;
  adhar: any;
  name: any;
  otp:any;
}
@Component({
  selector: 'app-modal-pop-up',
  templateUrl: './modal-pop-up.component.html',
  styleUrls: ['./modal-pop-up.component.css']
})

export class ModalPopUpComponent {
  name: any;
  adhar: any;
  dob: any;
  pan: any;
  age:any;
  gender:any;
  otp:any;
  showMask:boolean = false;
  informtn: { accessKey1: string; caseId1: string; MobileNo: string; statuscode: string; };


  constructor(
    public dialogRef: MatDialogRef<ModalPopUpComponent>,  @Inject(MAT_DIALOG_DATA) public data: DialogData,private http:HttpClient
  ) {
    console.log("data",data)

  }

  onNoClick(): void {
    this.dialogRef.close();
  }

  
  submitotp() {
    console.log("called.22.",this.data)
    this.showMask = true;
    const  paramObj={
        name:this.data.name,
        adhar:this.data.adhar,
        dob:this.data.dob,
        pan:this.data.pan,
        age:this.data.age,
        gender:this.data.gender,
        otp:this.otp
      }
 
    console.log("called.22.",paramObj)
        this.http.post('http://192.168.1.120:8000/test/sample', paramObj).subscribe(
        (data) => {
          console.log("data....>>", data)
          if(data){
             this.showMask = false;
            this.dialogRef.close(data);
            this.otp=undefined;
          }
        })
  }

}
