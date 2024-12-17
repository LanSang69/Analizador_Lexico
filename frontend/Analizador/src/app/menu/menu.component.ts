import { Component, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent {
  previousComponent:string = "";
  @Output() componentSelected = new EventEmitter<string>();
  constructor() {}

  onChangeIdButtons(isVisible: boolean): void {
    const element = document.getElementById('buttons-container') as HTMLElement;
    if (isVisible) {
      element.classList.add("visible");
      element.classList.remove("hidden");
    } else {
      element.classList.add("hidden");
      element.classList.remove("visible");
    }
  }

  selectComponent(component: string):void {
    if(this.previousComponent === component) {
      component = "";
      this.resetStyles();
    }
    this.componentSelected.emit(component);
    this.previousComponent = component;
    console.log(component);
  }

  resetStyles():void{
    const buttons = document.querySelectorAll('#buttons-container button');
    buttons.forEach(button => {
      (button as HTMLButtonElement).blur();
    });
  }
}
