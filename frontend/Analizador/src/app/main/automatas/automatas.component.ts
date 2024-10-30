import { Component, OnInit, Inject, PLATFORM_ID, Renderer2, Output, EventEmitter } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';

@Component({
  selector: 'app-automatas',
  templateUrl: './automatas.component.html',
  styleUrls: ['./automatas.component.css'], // Corrected from 'styleUrl' to 'styleUrls'
})
export class AutomatasComponent implements OnInit {
  constructor(
    @Inject(PLATFORM_ID) private platformId: Object,
    private renderer: Renderer2 // Inject Renderer2
  ) {}

  cuadrosNum: number = 0;
  @Output() cuadrosNumChange: EventEmitter<number> = new EventEmitter<number>();

  ngOnInit() {
    this.addGridClass();
    this.emitNum(); // Emit initial count on init if necessary
  }

  countChilds() {
    if (isPlatformBrowser(this.platformId)) {
      const container = document.getElementById('dinamicContainer');
      if (container) {
        this.cuadrosNum = container.children.length;
      }
    }
  }

  emitNum() {
    this.countChilds();
    this.cuadrosNumChange.emit(this.cuadrosNum);
  }

  addNewChild() {
    // Logic to add a child element
    this.emitNum();
  }

  removeChild() {
    // Logic to remove a child element
    this.emitNum();
  }

  addGridClass() {
    this.countChilds();
    if (isPlatformBrowser(this.platformId)) {
      const container = document.getElementById('dinamicContainer');
      if (container) {
        container.classList.remove(
          'dinamicGrid-2',
          'dinamicGrid-3',
          'dinamicGrid-4',
          'dinamicGrid-5',
          'dinamicGrid-6'
        ); // Remove previous grid classes

        if (this.cuadrosNum === 1) {
          container.classList.add('dinamicGrid-1');
        } else if (this.cuadrosNum === 2) {
          container.classList.add('dinamicGrid-2');
        } else if (this.cuadrosNum === 3) {
          container.classList.add('dinamicGrid-3');
        } else if (this.cuadrosNum === 4) {
          container.classList.add('dinamicGrid-4');
        } else if(this.cuadrosNum == 5){
          container.classList.add('dinamicGrid-5');
        } else {
          container.classList.add('dinamicGrid-6');
        }
      }
    }
  }
}
