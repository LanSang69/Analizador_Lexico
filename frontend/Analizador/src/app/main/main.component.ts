import { Component } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent {
  selectedComponent: string = '';

  selectOnMain(component: string) {
    this.selectedComponent = component;
  }
}
