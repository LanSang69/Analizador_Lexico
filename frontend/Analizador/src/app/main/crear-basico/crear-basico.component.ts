import { Component,  EventEmitter,  Output,  ViewEncapsulation } from '@angular/core';
import { crear_basico } from './crear_basico';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-crear-basico',
  templateUrl: './crear-basico.component.html',
  styleUrls: ['./crear-basico.component.css', '../main.component.css', '../toastr.css'],
  encapsulation: ViewEncapsulation.None // Disable view encapsulation
})
export class CrearBasicoComponent {
  @Output() created = new EventEmitter<boolean>();
  @Output() number = new EventEmitter<number>();
  @Output() description = new EventEmitter<string>();
  simboloInferior: string = '';
  simboloSuperior: string = '';
  info: string = '';

  constructor(private crear_basico:crear_basico, private toastr: ToastrService) { }

  onSubmit(){
    this.crearBasico();
    this.emptyValues();
    this.created.emit(true);
  }

  crearBasico(){
    this.crear_basico.crearBasico(this.simboloInferior, this.simboloSuperior)
      .subscribe(
        response => {
          console.log(response);
          this.showSuccess(response.message);
          this.number.emit(response.id);
          this.description.emit(response.description);
        },

        error => {
          console.log(error);
          this.showError(error.error.message);
        }
      );
  }

  showSuccess(mesage: string) {
    this.toastr.success(mesage);
  }

  showError(mesage: string) {
    this.toastr.error(mesage);
  }

  emptyValues(){
    this.simboloInferior = '';
    this.simboloSuperior = '';
    this.info = '';
  }

}
