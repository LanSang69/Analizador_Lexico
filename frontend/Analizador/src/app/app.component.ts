import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-root',
  encapsulation: ViewEncapsulation.None,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css', './lexico/toastr.css']
})
export class AppComponent {
  selectedComponent = "sintactico";
  title = 'Analizador';
  constructor(){}

  selectOnMain(component: string) {
    this.selectedComponent = component;
  }
}
