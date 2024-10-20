import { Component,  ViewEncapsulation } from '@angular/core';
import { crear_basico } from './crear_basico';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-crear-basico',
  templateUrl: './crear-basico.component.html',
  styleUrls: ['./crear-basico.component.css', '../main.component.css', '../toastr.css'],
  encapsulation: ViewEncapsulation.None // Disable view encapsulation
})
export class CrearBasicoComponent {
  simboloInferior: string = '';
  simboloSuperior: string = '';
  info: string = '';

  constructor(private crear_basico:crear_basico, private toastr: ToastrService) { }

  onSubmit(){
    this.crearBasico();
  }

  crearBasico(){
    this.crear_basico.crearBasico(this.simboloInferior, this.simboloSuperior)
      .subscribe(
        response => {
          console.log(response);
          this.info = response.data;
          this.showSuccess(response.message);
        },

        error => {
          console.log(error);
        }
      );
  }

  showSuccess(mesage: string) {
    this.toastr.success(mesage);
  }

  showError(mesage: string) {
    this.toastr.error(mesage);
  }

}
