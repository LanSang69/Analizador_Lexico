import { Component, Output, EventEmitter } from '@angular/core';
import { resetService } from './resetService';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-options',
  templateUrl: './options.component.html',
  styleUrls: ['./options.component.css']
})

export class OptionsComponent {
  constructor(private reset:resetService, private toastr:ToastrService){}
  @Output() componentSelected = new EventEmitter<string>();
  @Output() resetAutomatas = new EventEmitter<boolean>();

  selectComponent(component: string) {
    this.componentSelected.emit(component);
    console.log(component);
  }

  resetAll(){
    this.reset.resetAutomatas()
      .subscribe(
        response => {
          this.showSuccess(response.message);
          this.resetAutomatas.emit(true);
        },
        error => {
          this.showError(error.error.message);
        }
      );
  }

  showSuccess(mesage: string) {
    this.toastr.info(mesage);
  }

  showError(mesage: string) {
    this.toastr.error(mesage);
  }

}
