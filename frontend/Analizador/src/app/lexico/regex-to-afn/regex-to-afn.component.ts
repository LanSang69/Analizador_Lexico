import { Component,  EventEmitter,  Output,  ViewEncapsulation } from '@angular/core';
import { RegexService } from './RegexService';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';

@Component({
  selector: 'app-regex-to-afn',
  templateUrl: './regex-to-afn.component.html',
  styleUrls: ['./regex-to-afn.component.css', '../main.component.css', '../toastr.css'],
  encapsulation: ViewEncapsulation.None // Disable view encapsulation
})
export class RegexToAFNComponent {
  regex: string = '';
  @Output() id = new EventEmitter<number>();

  constructor(private regexToAFN: RegexService, private toastr: ToastrService, private router: Router) {}


  onSubmit(){
    this.getAFN();
    this.emptyValues();
  }


  getAFN() {
    console.log(this.regex);
    this.regexToAFN.getAFN(this.regex).subscribe(
      response => {
        this.showSuccess(response.message);
        this.id.emit(response.id);
      },
      error => {
        this.showError(error.error.message);
        console.error("Error during AFN creation:", error); 
      }
    );
  }

  emptyValues(){
    this.regex = "";
  }

  showSuccess(message: string) {
    this.toastr.success(message);
  }

  showError(message: string) {
    this.toastr.error(message);
  }
}
