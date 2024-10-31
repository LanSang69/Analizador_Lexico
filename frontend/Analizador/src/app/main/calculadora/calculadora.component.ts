import { Component, EventEmitter, Output, ViewEncapsulation } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';
import { CalculadoraService } from './CalculadoraService';

@Component({
  selector: 'app-calculadora',
  templateUrl: './calculadora.component.html',
  styleUrls: ['./calculadora.component.css', '../main.component.css', '../toastr.css'], // Corrected from styleUrl to styleUrls
  encapsulation: ViewEncapsulation.None
})
export class CalculadoraComponent {
  expresion: string = '';
  afd: string = '';
  selectedFile: File | null = null;
  @Output() events = new EventEmitter<{ success: boolean, postfijo: string, resultado: number }>();

  constructor(
    private calculadora: CalculadoraService, 
    private toastr: ToastrService, 
    private router: Router
  ) {}

  async onSubmit(): Promise<void> {
    if (!this.selectedFile || !this.expresion) {
      this.showError('Proporciona una expresión y un archivo.');
      return;
    }

    try {
      this.afd = await this.txt_to_string(this.selectedFile);
      this.obtenerResultado(this.expresion, this.afd);
    } catch (error) {
      this.showError('Failed to read the file.');
      console.error('File reading error:', error);
    }
  }

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
      console.log('Archivo:', this.selectedFile.name);
    }
  }

  txt_to_string(file: File): Promise<string> {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result as string);
      reader.onerror = (error) => reject(error);
      reader.readAsText(file);
    });
  }

  obtenerResultado(expresion: string, afd: string) {
    this.calculadora.calculadora(afd, expresion).subscribe(
      data => {
        this.events.emit({ success: true, postfijo: data.postfijo, resultado: data.result });
        this.showSuccess('Calculation successful!');
      },
      error => {
        this.events.emit({ success: false, postfijo: '', resultado: 0 });
        this.showError('Calculation failed.');
      }
    );
  }

  emptyValues(){
    this.expresion = "";
  }

  showSuccess(message: string) {
    this.toastr.success(message);
  }

  showError(message: string) {
    this.toastr.error(message);
  }
}
