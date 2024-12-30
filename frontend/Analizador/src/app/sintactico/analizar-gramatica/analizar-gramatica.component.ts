import { Component, OnInit, Inject, PLATFORM_ID, Renderer2 } from '@angular/core';
import { GramaticaService } from '../Services/analizarG';
import { LexicoService } from '../Services/analizarL';
import { ToastrService } from 'ngx-toastr';
import { isPlatformBrowser } from '@angular/common';
import { MatrixService } from '../Services/matrixService';

@Component({
  selector: 'app-analizar-gramatica',
  templateUrl: './analizar-gramatica.component.html',
  styleUrl: './analizar-gramatica.component.css'
})
export class AnalizarGramaticaComponent {
  tokens: { [key: string]: string } = {};
  Vt = [];
  Vn = [];
  StatesDetails = [];
  LR0: any[] = [];
  renglones: number = -1;
  isBrowser: boolean;

  constructor(
    @Inject(PLATFORM_ID) private platformId: Object,
    private analizarG: GramaticaService,
    private analizarL: LexicoService,
    private toastr: ToastrService,
    private renderer: Renderer2,
    private sharedM: MatrixService
  ) {
    this.isBrowser = isPlatformBrowser(this.platformId);
  }

  EnviarGrammatica() {
    const gramatica = document.getElementById('gramatica') as HTMLInputElement;
    const tablaLR0 = document.getElementById('TablLR0') as HTMLDivElement;
    const terminales = document.getElementById('terminales') as HTMLDivElement;
    const noTerminales = document.getElementById('no-terminales') as HTMLDivElement;
    const button = document.getElementById('saveB') as HTMLButtonElement;

    tablaLR0.classList.remove('hidden');
    terminales.classList.remove('hidden');
    noTerminales.classList.remove('hidden');
    if (button.classList.contains('hideB')) {
      button.classList.toggle('hideB');
    }
    this.analizarGramatica(gramatica.value);
  }

  analizarGramatica(gramatica: string) {
    console.log(gramatica);
    this.analizarG.getGrammar(gramatica).subscribe(
      response => {
        console.log(response);
        this.Vt = response.data.terminals;
        this.Vn = response.data.nonTerminals;
        this.StatesDetails = response.data.details;
        this.LR0 = response.data.table;
        this.renglones = response.data.renglones;
        this.populateTables();
        this.showSuccess(response.message);
      },
      error => {
        console.error("Error:", error);
      }
    );
  }

  populateTables() {
    let i: number;
    const terminales = document.getElementById('tableT') as HTMLTableElement;
    const noTerminales = document.getElementById('tableNT') as HTMLTableElement;
    // Clear previous table content
    while (terminales.firstChild) {
      terminales.removeChild(terminales.firstChild);
    }
    while (noTerminales.firstChild) {
      noTerminales.removeChild(noTerminales.firstChild);
    }

    i = 0;
    this.Vt.forEach(terminal => {
      setTimeout(() => {
      const row = document.createElement('tr');
      const cell = document.createElement('td');
      const cell2 = document.createElement('td');

      cell.textContent = terminal;
      const input = document.createElement('input');
      input.style.width = "100px";
      cell2.appendChild(input);
      row.appendChild(cell);
      row.appendChild(cell2);

      terminales.appendChild(row);
      }, i * 200);
      i++;
    });

    i = 0;
    this.Vn.forEach(nonTerminal => {
      setTimeout(() => {
      const row = document.createElement('tr');
      const cell = document.createElement('td');
      cell.textContent = nonTerminal;
      row.appendChild(cell);
      noTerminales.appendChild(row);
      },i*200);
      i++;
    });

    this.populateLR0();
  }

  populateLR0() {
    const states = document.getElementById("states") as HTMLElement;
    const tableHead = document.getElementById("tableLR0Head") as HTMLElement;
    const tableBody = document.getElementById("tableLR0Body") as HTMLElement;

    // Clear previous table content
    states.innerHTML = "";
    while (tableHead.firstChild) {
      tableHead.removeChild(tableHead.firstChild);
    }
    while (tableBody.firstChild) {
      tableBody.removeChild(tableBody.firstChild);
    }

    let i = 0;
    this.StatesDetails.forEach((state) => {
      setTimeout(() => {
      const p = document.createElement('p');
      p.innerHTML = state;
      states.appendChild(p);
      }, i * 400);
      i++;
    });

    const row = document.createElement('tr');
    const cell = document.createElement('th');
    cell.textContent = "Estados";
    row.appendChild(cell);

    this.Vt.forEach((terminal) => {
      const cell = document.createElement('th');
      cell.textContent = terminal;
      row.appendChild(cell);
    });

    this.Vn.forEach((nonterminal) => {
      const cell = document.createElement('th');
      cell.textContent = nonterminal;
      row.appendChild(cell);
    });

    tableHead.appendChild(row);
    for (let i = 0; i <= this.renglones; i++) {
      setTimeout(() => {
      const row2 = document.createElement('tr');
      const cell = document.createElement('td');
      cell.textContent = i.toString();
      row2.appendChild(cell);

      this.Vt.forEach((terminal) => {
        const cell = document.createElement('td');
        if (this.LR0[i][terminal]) {
          cell.textContent = this.LR0[i][terminal];
        }
        else {
          cell.textContent = " ";
        }
        row2.appendChild(cell);
      });

      this.Vn.forEach((nonterminal) => {
        const cell = document.createElement('td');
        if (this.LR0[i][nonterminal]) {
          cell.textContent = this.LR0[i][nonterminal];
        }
        else {
          cell.textContent = " ";
        }
        row2.appendChild(cell);
      });
      tableBody.appendChild(row2);
      }, i*200);
    }

  }

  showSuccess(mesage: string) {
    this.toastr.success(mesage);
  }

  showError(mesage: string) {
    this.toastr.error(mesage);
  }

  analizarSigma(str: string) {
    this.analizarL.getGrammar(str).subscribe(
      response => {
        this.createAnalisis(response.data.descripcion);
        this.showSuccess(response.message);
      },
      error => {
        console.error("Error:", error);
      }
    );
  }

  seleccionarS() {
    const sigma = document.getElementById('sigma') as HTMLInputElement;
    this.analizarSigma(sigma.value);
  }

  createAnalisis(description: string) {
    const container = document.getElementById('dinamicContainer');
    if (container) {
      while (container.firstChild) {
        container.removeChild(container.firstChild);
      }
    }
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
          (gridItems[i] as HTMLElement).style.width = '200px';
          (gridItems[i] as HTMLElement).style.height = '25vh';
        }
      }
    }
  }

  setTokens() {
    const matrix: { [key: string]: string } = {};
    const table = document.getElementById('tableT') as HTMLTableElement;
    const rows = table.rows;

    for (let i = 0; i < rows.length; i++) {
      const row = rows[i];
      const cells = row.cells;
      const terminal = cells[0].textContent!;
      const input = cells[1].children[0] as HTMLInputElement;
      matrix[input.value] = terminal;
    }

    this.tokens = matrix;
    this.sharedM.updateArray(matrix);
    this.showSuccess('Tokens actualizados');
    console.log(this.tokens);
  }

}
