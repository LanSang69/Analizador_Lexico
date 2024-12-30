import { Component, OnInit, Inject, PLATFORM_ID, Renderer2 } from '@angular/core';
import { CadenaService } from '../Services/analizarC';
import { MatrixService } from '../Services/matrixService';
import { ToastrService } from 'ngx-toastr';
import { isPlatformBrowser } from '@angular/common';

@Component({
  selector: 'app-analizar-cadena',
  templateUrl: './analizar-cadena.component.html',
  styleUrl: './analizar-cadena.component.css'
})
export class AnalizarCadenaComponent  implements OnInit {
  sigma:string = ""
  table:any = []
  tokens: { [key: string]: string } = {};
  isBrowser: boolean;

  constructor(
    @Inject(PLATFORM_ID) private platformId: Object,
    private analizarC: CadenaService,
    private sharedM: MatrixService,
    private toastr: ToastrService
  ) {
    this.isBrowser = isPlatformBrowser(this.platformId);
  }

  ngOnInit() {
    this.sharedM.currentArray.subscribe((array) => {
      this.tokens = array;
      console.log(this.tokens);
    });
  }

  async onSubmit(): Promise<void> {
    if (!this.sigma) {
      this.showError('Proporciona una expresión');
      return;
    }

    try {
      console.log(this.sigma);
      this.analizarGramatica();
    }catch (error) {
      console.error('Error en el proceso:', error);
    }

  }

  analizarGramatica(){
    const sigma = this.sigma;
    const matrix = this.tokens;

      this.analizarC.getTable(sigma, matrix).subscribe(
        response => {
          console.log(response);
          if(response.data.valid){
            this.table = response.data.tabla;
            console.log(this.table);
            this.printTable();
            this.showSuccess("La cadena pertenece a la gramática");
          }else{
            this.showError("La cadena NO pertenece a la gramática");
          }
        },
        error => {
          console.error("Error:", error);
        }
      );
}

printTable() {
  const tabla = document.getElementById("tableA") as HTMLElement;
  if (!tabla) {
    console.error("Table element with id 'tableA' not found.");
    return;
  }

  // Clear the table
  while (tabla.firstChild) {
    tabla.removeChild(tabla.firstChild);
  }

  // Validate table data
  if (!this.table || !Array.isArray(this.table) || this.table.length < 3) {
    console.error("Invalid table data. Ensure 'this.table' is a valid 2D array.");
    return;
  }

  // Add rows to the table with a staggered delay
  for (let i = 0; i < this.table[0].length; i++) {
    setTimeout(() => {
      const row = document.createElement("tr");

      const pila = document.createElement("td");
      const cadena = document.createElement("td");
      const destino = document.createElement("td");

      pila.textContent = this.table[0][i] || ""; // Safeguard against undefined
      cadena.textContent = this.table[1][i] || "";
      destino.textContent = this.table[2][i] || "";

      row.appendChild(pila);
      row.appendChild(cadena);
      row.appendChild(destino);

      tabla.appendChild(row);
    }, i * 300); // Stagger delay: 300ms * iteration index
  }
}


showSuccess(mesage: string) {
  this.toastr.success(mesage);
}

showError(mesage: string) {
  this.toastr.error(mesage);
}

}
