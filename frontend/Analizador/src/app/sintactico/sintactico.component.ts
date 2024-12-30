import { Component } from '@angular/core';
import { GramaticaService } from './Services/analizarG';

@Component({
  selector: 'app-sintactico',
  templateUrl: './sintactico.component.html',
  styleUrl: './sintactico.component.css'
})
export class SintacticoComponent {
  constructor(private analizarG:GramaticaService){}

  selectedComponent: string = '';
  vocabulary: string[] = [];
  terminals: string[] = [];
  non_terminals: string[] = [];

  selectOnMain(component: string) {
    this.selectedComponent = component;
  }
}
