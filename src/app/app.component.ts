import { Component, OnInit } from '@angular/core';
// import * as studentsData from '../app/example.json'
import { AppModule } from '../app/app.module'
import { ApiService } from './core/api.service';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { ModalPopUpComponent } from './modal-pop-up/modal-pop-up.component';
// import { Spinner } from './core/loader/spinner';
// import 'rxjs/add/operator/toPromise';

// interface Student {  
//   adharname: String;  
//   adhardob: String;  
//   adhargender: String;  
//   inputname: String;  
// }  

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  // providers: [Spinner]
})
// export class DialogElementsExampleDialog {}
export class AppComponent implements OnInit {
  
  data: any;
  errorMessage: any;
  name: any;
  adhar: any;
  dob: any;
  pan: any;
  age:any;
  gender:any;
  otp:any;
  openpopup: boolean = false;
  contact:boolean= true;
  displayform:boolean= false;
  students: any;
  img: string;
  videoimg:any;
  info: any;
  informtn: { accessKey1: string; caseId1: string; MobileNo: string; statuscode: string; };
  showMask:boolean = false;
  // students: Student= studentsData;

  constructor(private apiService: ApiService,private http:HttpClient
    ,public dialog: MatDialog,
    //  private spinner: Spinner
    // public dialog: MatDialog
    ) { }
  obj:any;

  ngOnInit():void {
    // this.img="data:image/png;base64,"+this.ajit;
//   this.informtn= {
//     "accessKey1": "14c92f6a-6572-4bab-a563-a981d45b0900",
//     "caseId1": "20062022150517",
//     "MobileNo": "9049402755",
//     "statuscode": "101"
// }



//  console.log("stu",this.students.adhardob);

    }
    openDialog() {
      // this.dialog.open(AppComponent);
    }
  submitinfo() {
    // this.spinner.show();
    this.showMask = true;
    const  paramObj={
        name:this.name,
        adhar:this.adhar,
        dob:this.dob,
        pan:this.pan,
        age:this.age,
        gender:this.gender
      }  
        this.http.post('http://192.168.1.120:8000/test', paramObj).subscribe(
        (data) => {
          console.log("data", data)
          this.info =data;
          if(this.info.statuscode === '101'){
          this.showMask = false;
           alert('Adhaar Number is link with Mobile and otp sent to register mobile number') 
           this.openMatDialog();
          }else{this.showMask = false;
            alert('Error/Insufficient Credits')

          }
        })

      //   setTimeout(()=>{
      //     this.showMask = false;
      //   },3000)
      // this.openMatDialog();

  }

  openMatDialog(){
    const dialogRef = this.dialog.open(ModalPopUpComponent, {
      width: '250px',
      data: {name: this.name, adhar:this.adhar,
        dob:this.dob,
        pan:this.pan,
        age:this.age,
        gender:this.gender},
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log("result..",result)
      if(result){
      this.students = result;
        this.img="data:image/png;base64,"+this.students.imgsrc;
         console.log("img",this.img)
         this.videoimg="data:image/png;base64,"+this.students.videoimg;
          this.displayform = true;
          this.contact = false;
      }
    });
  }

goBack(){this.displayform = false;
  this.contact = true;}

}
