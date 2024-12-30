import { Component, Output, EventEmitter, Input } from '@angular/core';
import { resetService } from './resetService';
import { ToastrService } from 'ngx-toastr';
import { exit } from 'node:process';

@Component({
  selector: 'app-options',
  templateUrl: './options.component.html',
  styleUrls: ['./options.component.css']
})

export class OptionsComponent {
  constructor(private reset:resetService, private toastr:ToastrService){}
  @Output() componentSelected = new EventEmitter<string>();
  @Output() resetAutomatas = new EventEmitter<boolean>();
  @Output() eliminateE = new EventEmitter<boolean>();
  @Output() eliminated = new EventEmitter<string>();
  @Input() selected:string[] = [];

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

  eliminate(){
    for(let i=0; i<this.selected.length; i++){
      console.log("numero para eliminar", this.selected.length);

      this.reset.eliminate(this.selected[i])
        .subscribe(
          response => {
            console.log(response);
            this.eliminated.emit(response.id);
          },
          error => {
            this.showError(error.error.message);
            console.error('Error occurred while eliminating automata:', error.error.message);
          }
        );
    }
    this.showSuccess("Automatas eliminados");
    this.eliminateE.emit(true);
  }

  showSuccess(mesage: string) {
    this.toastr.info(mesage);
  }

  showError(mesage: string) {
    this.toastr.error(mesage);
  }

}
