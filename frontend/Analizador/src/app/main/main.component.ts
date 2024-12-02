import { Component, OnInit, Inject, PLATFORM_ID, Renderer2 } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import { getAutomatasService } from './getAutomatasService';
import { ConcatenarService } from './ConcatenarService';
import { ToastrService } from 'ngx-toastr';
import { CerraduraPService } from './CerraduraPService';
import { CerraduraKService } from './CerraduraKService';
import { OpcionalService } from './OpcionalService';
import { UnirService } from './UnirService';
import { Router } from '@angular/router';
import { ChangeDetectorRef } from '@angular/core';
import { AFDService } from './AFDService';
import { GenerarService } from './GenerarService';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  isBrowser: boolean;

  constructor(
    @Inject(PLATFORM_ID) private platformId: Object,
    private renderer: Renderer2,
    private getData: getAutomatasService,
    private concatenar: ConcatenarService,
    private cerraduraP: CerraduraPService,
    private cerraduraK: CerraduraKService,
    private opcional: OpcionalService,
    private unir: UnirService,
    private toastr: ToastrService,
    private router: Router,
    private cdRef: ChangeDetectorRef,
    private afd: AFDService,
    private generar: GenerarService
  ) {
    this.isBrowser = isPlatformBrowser(this.platformId); // Check if running in the browser
  }

  basico_created: boolean = false;
  selectedComponent: string = '';
  cuadrosNum: number = 0;
  automatas = [];
  checkedIds: string[] = [];
  descriptions: { [key: number]: string } = {};
  active = true

  ngOnInit() {
    this.getAutomatas();
    this.addGridClass();
    console.log(this.automatas)
    console.log(this.descriptions)
    for (let i = 0; i < this.automatas.length; i++) {
      console.log(i)
      console.log(this.automatas[i])
      this.createChildren(this.automatas[i]);
    }
  }

  automataEliminated(){
    this.eliminateChildren();
    this.getAutomatas().then(() => {
      for (let i = 0; i < this.automatas.length; i++) {
        this.createChildren(this.automatas[i]);
      }
    }).catch(error => {
      console.error("Error getting automatas:", error);
    });
  }

  updateChecked(event:any){
    event = event.toString();
    console.log(this.checkedIds);
    console.log("eliminando", event);
    if(this.checkedIds.includes(event)){
      const index = this.checkedIds.indexOf(event);
      if (index > -1) {
        this.checkedIds.splice(index, 1);
      }
    }else{
      this.checkedIds.push(event);
    }
  }

  automatasCreated(id: number){
    this.getAutomatas().then(() => {
      this.createChildren(id);
  }).catch(error => {
      console.error("Error getting automatas:", error);
  });
  }

  regexCreated(id: number){
    this.getAutomatas().then(() => {
      this.createChildren(id);
  }).catch(error => {
      console.error("Error getting automatas:", error);
  });
  }

  OnReset(boleano: boolean) {
    if (boleano && this.isBrowser) {
      this.eliminateChildren();
      
      this.basico_created = false;
      this.selectedComponent = '';
      this.cuadrosNum = 0;
      this.automatas = [];
      this.checkedIds = [];
      localStorage.clear();
      this.descriptions = {};
    }
  }

  selectOnMain(component: string) {
    this.selectedComponent = component;
    this.cdRef.detectChanges();
    this.basico_created = false;
    
    if (component === 'concatenar') {
      if (this.checkedIds.length === 2) {
        const id1 = parseInt(this.checkedIds[0], 10);
        const id2 = parseInt(this.checkedIds[1], 10);
        this.concatenarAutomatas(id1, id2);
      } else {
        this.showError('Debe seleccionar dos autómatas para concatenar');
      }
    }else if(component === 'cerraduraPositiva'){
      if (this.checkedIds.length === 1) {
        const id = parseInt(this.checkedIds[0], 10);
        this.cerraduraPositiva(id);
      } else {
        this.showError('Debe seleccionar un autómata para cerradura positiva');
      }
    }else if(component === 'cerraduraKleene'){
      if (this.checkedIds.length === 1) {
        const id = parseInt(this.checkedIds[0], 10);
        this.cerraduraKleene(id);
      } else {
        this.showError('Debe seleccionar un autómata para cerradura de Kleene');
      }
    }else if(component === 'opcional'){
      if (this.checkedIds.length === 1) {
        const id = parseInt(this.checkedIds[0], 10);
        this.cerraduraOpcional(id);
      } else {
        this.showError('Debe seleccionar un autómata para aplicar opcional');
      }
    }
    else if(component === 'unirAfns'){
      if (this.checkedIds.length > 1) {
        let ids: number[] = [];
        this.checkedIds.forEach(element => {
          ids.push(parseInt(element, 10));
        });
        this.unir_automatas(ids);
      } else {
        this.showError('Debe seleccionar más un autómata para unirlos');
      }
    }else if(component === 'convertir'){
      if (this.checkedIds.length === 1) {
        const id = parseInt(this.checkedIds[0], 10);
        this.getFile(id);
      } else {
        this.showError('Debe seleccionar un autómata para convertirlo');
      }
    }else if(component === 'GenerarAFN'){
      if (this.checkedIds.length > 1) {
        let ids: number[] = [];
        this.checkedIds.forEach(element => {
          ids.push(parseInt(element, 10));
        });
        this.gen_automatas(ids);
      } else {
        this.showError('Debe seleccionar más un autómata para unirlos');
      }
    }
  }

  alreadyCreated(event: boolean) {
    if (event) {
      this.basico_created = true;
    }
  }

  getAutomatas(): Promise<void> {
    return new Promise((resolve, reject) => {
      this.getData.getAutomata()
        .subscribe(
          response => {
            this.automatas = [];
            this.descriptions = {};
            this.automatas = response.data; 
            this.descriptions = response.descriptions; 
            resolve();
          },
          error => {
            console.error("Error fetching data:", error);
            reject(error);
          }
        );
    });
  }

  addGridClass() {
    if (isPlatformBrowser(this.platformId)) {
      const container = document.getElementById('dinamicContainer');
      if (container) {
        container.classList.remove(
          'dinamicGrid-1',
          'dinamicGrid-2',
          'dinamicGrid-3',
          'dinamicGrid-4',
          'dinamicGrid-5',
          'dinamicGrid-6'
        ); // Remove previous grid classes

        let counter = this.automatas.length;

        if (counter === 1) {
          container.classList.add('dinamicGrid-1');
        } else if (counter === 2) {
          container.classList.add('dinamicGrid-2');
        } else if (counter === 3) {
          container.classList.add('dinamicGrid-3');
        } else if (counter === 4) {
          container.classList.add('dinamicGrid-4');
        } else if(counter == 5){
          container.classList.add('dinamicGrid-5');
        } else {
          container.classList.add('dinamicGrid-6');
        }
      }
    }
  }

  createChildren(id: number) {
    let counter = this.automatas.length;
    console.log("Creating children: ", id);
    if (isPlatformBrowser(this.platformId)) {
      const container = document.getElementById('dinamicContainer');
      if (container) {
        const div = this.renderer.createElement('div');
        this.renderer.addClass(div, 'grid-item'); 
        this.renderer.setAttribute(div, 'id', `${id}`);
        const lines = this.descriptions[id] ? this.descriptions[id].split('\n') : [];
        lines.forEach(line => {
          const p = this.renderer.createElement('p');
          const text = this.renderer.createText(line);
          this.renderer.appendChild(p, text);
          this.renderer.appendChild(div, p);
        });

        // Create a checkbox input element
        const checkbox = this.renderer.createElement('input');
        this.renderer.setAttribute(checkbox, 'type', 'checkbox');
        this.renderer.setAttribute(checkbox, 'id', `${id}`);
        this.renderer.setStyle(checkbox, 'position', 'absolute');
        this.renderer.setStyle(checkbox, 'bottom', '10px');
        this.renderer.setStyle(checkbox, 'right', '10px');
        this.renderer.setStyle(checkbox, 'cursor', 'pointer');

        checkbox.addEventListener('change', (event: any) => this.onCheckboxChange(event));
        
        this.renderer.appendChild(div, checkbox);

        this.renderer.setStyle(div, 'position', 'relative'); // Ensure the parent div is positioned relatively
        this.renderer.appendChild(container, div); 
        this.addGridClass();
        
        const gridItems = container.getElementsByClassName('grid-item');
        for (let i = 0; i < gridItems.length; i++) {
          (gridItems[i] as HTMLElement).style.width = '301px';
          (gridItems[i] as HTMLElement).style.height = '301px';
        }

        if(counter > 3){
          const gridItems = container.getElementsByClassName('grid-item');
          for (let i = 0; i < gridItems.length; i++) {
            (gridItems[i] as HTMLElement).style.width = '231px';
            (gridItems[i] as HTMLElement).style.height = '231px';
          }
        }

        if(counter > 5){
          const gridItems = container.getElementsByClassName('grid-item');
          for (let i = 0; i < gridItems.length; i++) {
            (gridItems[i] as HTMLElement).style.width = '201px';
            (gridItems[i] as HTMLElement).style.height = '201px';
          }
        }

        if(counter > 9){
          const gridItems = container.getElementsByClassName('grid-item');
          for (let i = 0; i < gridItems.length; i++) {
            (gridItems[i] as HTMLElement).style.width = '181px';
            (gridItems[i] as HTMLElement).style.height = '181px';
          }
        }

        if(counter > 18){
          const gridItems = container.getElementsByClassName('grid-item');
          for (let i = 0; i < gridItems.length; i++) {
            (gridItems[i] as HTMLElement).style.width = '141px';
            (gridItems[i] as HTMLElement).style.height = '141px';
          }
        }
        if(counter > 24){
          const gridItems = container.getElementsByClassName('grid-item');
          for (let i = 0; i < gridItems.length; i++) {
            (gridItems[i] as HTMLElement).style.width = '101px';
            (gridItems[i] as HTMLElement).style.height = '101px';
          }
        }
      }
    }
  } 


  createAnalisis(description:string){
    console.log("Creating children: ", description);
    this.eliminateChildren();
    let counter = this.automatas.length;
    if (isPlatformBrowser(this.platformId)) {
      const container = document.getElementById('dinamicContainer');
      if (container) {
        const div = this.renderer.createElement('div');
        this.renderer.addClass(div, 'grid-item'); 
        this.renderer.setAttribute(div, 'id', `test`);
        const table = this.renderer.createElement('table');
        
        this.renderer.addClass(table, 'table');
        this.renderer.addClass(table, 'table-bordered');
        this.renderer.addClass(table, 'table-hover');
        this.renderer.setStyle(table, 'text-align', 'center');

        const lines = description.split('\n').slice(0, -1);
        const headerRow = this.renderer.createElement('tr');
        const lexemaHeader = this.renderer.createElement('th');
        const tokenHeader = this.renderer.createElement('th');

        // Style header row
        this.renderer.setStyle(headerRow, 'background-color', '#19173B');
        this.renderer.setStyle(headerRow, 'color', '#E7E0D5');

        this.renderer.appendChild(lexemaHeader, this.renderer.createText('LEXEMA'));
        this.renderer.appendChild(tokenHeader, this.renderer.createText('TOKEN'));
        this.renderer.appendChild(headerRow, lexemaHeader);
        this.renderer.appendChild(headerRow, tokenHeader);
        this.renderer.appendChild(table, headerRow);

        lines.forEach(line => {
            let elements = line.split('\t');
            const row = this.renderer.createElement('tr');
            const lexemaCell = this.renderer.createElement('td');
            const tokenCell = this.renderer.createElement('td');
            
            this.renderer.appendChild(lexemaCell, this.renderer.createText(elements[0]));
            this.renderer.appendChild(tokenCell, this.renderer.createText(elements[1]));
            this.renderer.appendChild(row, lexemaCell);
            this.renderer.appendChild(row, tokenCell);
            this.renderer.appendChild(table, row);
        });
        this.renderer.appendChild(div, table);

        this.renderer.setStyle(div, 'position', 'relative'); // Ensure the parent div is positioned relatively
        this.renderer.appendChild(container, div); 
        container.classList.remove(
          'dinamicGrid-1',
          'dinamicGrid-2',
          'dinamicGrid-3',
          'dinamicGrid-4',
          'dinamicGrid-5',
          'dinamicGrid-6'
        );
        this.renderer.addClass(container, 'dinamicGrid-1');
        
        const gridItems = container.getElementsByClassName('grid-item');
        for (let i = 0; i < gridItems.length; i++) {
          (gridItems[i] as HTMLElement).style.width = '300px';
          (gridItems[i] as HTMLElement).style.height = '400px';
        }
      }
    }
  }

  createResult(postfijo:string, result:number){
    console.log("Creating children: ", postfijo, result);
    this.eliminateChildren();
    if (isPlatformBrowser(this.platformId)) {
      const container = document.getElementById('dinamicContainer');
      if (container) {
        const div = this.renderer.createElement('div');
        this.renderer.addClass(div, 'grid-item'); 
        this.renderer.setAttribute(div, 'id', `test`);
        
        const postfijoLabel = this.renderer.createElement('label');
        this.renderer.addClass(postfijoLabel, 'pt-3');
        this.renderer.setAttribute(postfijoLabel, 'for', 'postfijoInput');
        this.renderer.setStyle(postfijoLabel, 'font-weight', 'bold');
        const postfijoLabelText = this.renderer.createText('Postfijo:');
        this.renderer.appendChild(postfijoLabel, postfijoLabelText);

        const postfijoInput = this.renderer.createElement('input');
        this.renderer.addClass(postfijoInput, 'pt-3');
        this.renderer.setAttribute(postfijoInput, 'type', 'text');
        this.renderer.setAttribute(postfijoInput, 'id', 'postfijoInput');
        this.renderer.setAttribute(postfijoInput, 'value', postfijo);
        this.renderer.addClass(postfijoInput, 'form-control');
        this.renderer.setStyle(postfijoInput, 'margin-bottom', '10px');
        this.renderer.setAttribute(postfijoInput, 'readonly', 'true');

        const resultLabel = this.renderer.createElement('label');
        this.renderer.setAttribute(resultLabel, 'for', 'resultInput');
        this.renderer.setStyle(resultLabel, 'font-weight', 'bold');
        const resultLabelText = this.renderer.createText('Resultado:');
        this.renderer.appendChild(resultLabel, resultLabelText);

        const resultInput = this.renderer.createElement('input');
        this.renderer.setAttribute(resultInput, 'type', 'text');
        this.renderer.setAttribute(resultInput, 'id', 'resultInput');
        this.renderer.setAttribute(resultInput, 'value', result.toString());
        this.renderer.addClass(resultInput, 'form-control');
        this.renderer.setAttribute(resultInput, 'readonly', 'true');

        const centeredDiv = this.renderer.createElement('div');
        this.renderer.setStyle(centeredDiv, 'display', 'flex');
        this.renderer.setStyle(centeredDiv, 'flex-direction', 'column');
        this.renderer.setStyle(centeredDiv, 'align-items', 'center');


        this.renderer.appendChild(centeredDiv, postfijoLabel);
        this.renderer.appendChild(centeredDiv, postfijoInput);
        this.renderer.appendChild(centeredDiv, resultLabel);
        this.renderer.appendChild(centeredDiv, resultInput);
        this.renderer.addClass(postfijoInput, 'container');

        this.renderer.appendChild(div, centeredDiv);

        this.renderer.setStyle(div, 'position', 'relative'); // Ensure the parent div is positioned relatively
        this.renderer.appendChild(container, div); 
        container.classList.remove(
          'dinamicGrid-1',
          'dinamicGrid-2',
          'dinamicGrid-3',
          'dinamicGrid-4',
          'dinamicGrid-5',
          'dinamicGrid-6'
        );
        this.renderer.addClass(container, 'dinamicGrid-1');
        
        const gridItems = container.getElementsByClassName('grid-item');
        for (let i = 0; i < gridItems.length; i++) {
          (gridItems[i] as HTMLElement).style.width = '300px';
          (gridItems[i] as HTMLElement).style.height = '400px';
        }
      }
    }
  }

  eliminateChildren() {
    if (isPlatformBrowser(this.platformId)) {
      const container = document.getElementById('dinamicContainer');
      if (container) {
        while (container.firstChild) {
          container.removeChild(container.firstChild);
        }
        this.addGridClass();
      }
    }
  }

concatenarAutomatas(id1: number, id2: number){
  this.concatenar.concatenar(id1, id2)
    .subscribe(
      response => {
        this.eliminateChildren();
        this.checkedIds = [];
        this.getAutomatas().then(() => {
          for (let i = 0; i < this.automatas.length; i++) {
            this.createChildren(this.automatas[i]);
          }
        }).catch(error => {
          console.error("Error getting automatas:", error);
        });
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach((checkbox) => {
          (checkbox as HTMLInputElement).checked = false;
        });
        this.showSuccess(response.message);
      },
      error => {
        this.showError(error.error.message);
      }
    );
}

cerraduraPositiva(id: number){
  this.cerraduraP.cerraduraP(id)
    .subscribe(
      response => {
        this.eliminateChildren();
        this.checkedIds = [];
        this.getAutomatas().then(() => {
          for (let i = 0; i < this.automatas.length; i++) {
            this.createChildren(this.automatas[i]);
          }
        }).catch(error => {
          console.error("Error obteniendo los automatas:", error);
        });
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach((checkbox) => {
          (checkbox as HTMLInputElement).checked = false;
        });
        this.showSuccess(response.message);
      },
      error => {
        this.showError(error.error.message);
      }
    );
}

cerraduraKleene(id: number){
  this.cerraduraK.cerraduraK(id)
    .subscribe(
      response => {
        this.eliminateChildren();
        this.checkedIds = [];
        this.getAutomatas().then(() => {
          for (let i = 0; i < this.automatas.length; i++) {
            this.createChildren(this.automatas[i]);
          }
        }).catch(error => {
          console.error("Error obteniendo los automatas:", error);
        });
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach((checkbox) => {
          (checkbox as HTMLInputElement).checked = false;
        });
        this.showSuccess(response.message);
      },
      error => {
        this.showError(error.error.message);
      }
    );
}

cerraduraOpcional(id:number){
  this.opcional.opcional(id)
    .subscribe(
      response => {
        this.eliminateChildren();
        this.checkedIds = [];
        this.getAutomatas().then(() => {
          for (let i = 0; i < this.automatas.length; i++) {
            this.createChildren(this.automatas[i]);
          }
        }).catch(error => {
          console.error("Error obteniendo los automatas:", error);
        });
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach((checkbox) => {
          (checkbox as HTMLInputElement).checked = false;
        });
        this.showSuccess(response.message);
      },
      error => {
        this.showError(error.error.message);
      }
    );
}

unir_automatas(ids:number[]){
    this.unir.unir_automatas(ids)
    .subscribe(response =>{
        this.eliminateChildren();
        this.checkedIds = [];
        this.getAutomatas().then(() => {
          for (let i = 0; i < this.automatas.length; i++) {
            this.createChildren(this.automatas[i]);
          }
        }).catch(error => {
          console.error("Error getting automatas:", error);
        });
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach((checkbox) => {
          (checkbox as HTMLInputElement).checked = false;
        });
        this.showSuccess(response.message);
      },
      error => {
        this.showError(error.error.message);
    })
}


gen_automatas(ids:number[]){
  this.generar.generar(ids)
  .subscribe(response =>{
      this.eliminateChildren();
      this.checkedIds = [];
      this.getAutomatas().then(() => {
        for (let i = 0; i < this.automatas.length; i++) {
          this.createChildren(this.automatas[i]);
        }
      }).catch(error => {
        console.error("Error getting automatas:", error);
      });
      const checkboxes = document.querySelectorAll('input[type="checkbox"]');
      checkboxes.forEach((checkbox) => {
        (checkbox as HTMLInputElement).checked = false;
      });
      this.showSuccess(response.message);
    },
    error => {
      this.showError(error.error.message);
  })
}

showSuccess(mesage: string) {
  this.toastr.success(mesage);
}

showError(mesage: string) {
  this.toastr.error(mesage);
}

onCheckboxChange(event: any) {
  const id = event.target.id;
  if (event.target.checked) {
    if (!this.checkedIds.includes(id) && id !== 0) {
      this.checkedIds.push(id);
    }
  } else {
    const index = this.checkedIds.indexOf(id);
    if (index > -1) {
      this.checkedIds.splice(index, 1);
    }
  }

  console.log(event.target.id);
}

setFalse(event:boolean){
  if(!event){
    this.eliminateChildren();
    this.checkedIds = [];
    this.getAutomatas().then(() => {
      for (let i = 0; i < this.automatas.length; i++) {
        this.createChildren(this.automatas[i]);
      }
    }).catch(error => {
      console.error("Error getting automatas:", error);
    });
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach((checkbox) => {
      (checkbox as HTMLInputElement).checked = false;
    });
    this.showSuccess("Elemento agregado con exito");
  }
}


getFile(id:number){
  this.afd.getString(id).subscribe(
    response => {
      this.downloadFile(response.txt);
    },
    error => {
      console.error("Error getting file:", error);
    }
  );
}

downloadFile(content: any) {
  const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
  const url = window.URL.createObjectURL(blob);

  const anchor = document.createElement('a');
  anchor.href = url;

  const fileName = prompt('Enter the file name', 'afd.txt');
  if (fileName) {
    anchor.download = fileName;
    anchor.click();
  }

  window.URL.revokeObjectURL(url); 
}

getTable(event: any){
  this.createAnalisis(event);
}

calcular(event:any){
  if(event.success){
    this.createResult(event.postfijo, event.resultado);
    this.showSuccess("Cálculo exitoso");
  }else{
    this.showError("Error en el cálculo");
  }
}

}