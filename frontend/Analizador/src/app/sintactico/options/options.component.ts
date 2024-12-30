import { Component, Output, EventEmitter, Input } from '@angular/core';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-options-sintactico',
  templateUrl: './options.component.html',
  styleUrls: ['./options.component.css']
})

export class OptionsComponentS {
  constructor(private toastr:ToastrService){}
  @Output() componentSelected = new EventEmitter<string>();
  @Output() resetAutomatas = new EventEmitter<boolean>();
  @Output() eliminateE = new EventEmitter<boolean>();
  @Output() eliminated = new EventEmitter<string>();
  @Input() selected:string[] = [];

  selectComponent(component: string) {
    this.componentSelected.emit(component);
    console.log(component);
  }

  showSuccess(mesage: string) {
    this.toastr.info(mesage);
  }

  showError(mesage: string) {
    this.toastr.error(mesage);
  }

}
