import { Component, Input, OnInit, ViewEncapsulation} from '@angular/core';

@Component({
  selector: 'app-spinner',
  templateUrl: './spinner.component.html',
  styleUrls: ['./spinner.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class SpinnerComponent implements OnInit {

  @Input() showProgress:boolean = false;
  constructor() { }

  ngOnInit() {
  }

}
