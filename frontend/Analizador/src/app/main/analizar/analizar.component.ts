import { Component, EventEmitter, Output } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';
import { AnalizarService } from './AnalizarService';

@Component({
  selector: 'app-analizar',
  templateUrl: './analizar.component.html',
  styleUrls: ['./analizar.component.css'] // Fixed typo here
})
export class AnalizarComponent {
  sigma: string = '';
  txt: string = '';
  @Output() final_table = new EventEmitter<string>();
  selectedFile: File | null = null;

  constructor(private toastr: ToastrService, private router: Router, private analisis: AnalizarService) {}

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0]; // Get the first selected file
      console.log('Selected file:', this.selectedFile);
    }
  }

  async onSubmit(): Promise<void> {
    if (!this.sigma || !this.selectedFile) {
      this.showError('Please provide both Sigma and a file.');
      return;
    }

    try {
      this.txt = await this.txt_to_string(this.selectedFile);
      this.analizar(this.txt, this.sigma);
    } catch (error) {
      this.showError('Failed to read the file.');
      console.error('File reading error:', error);
    }
  }

  analizar(txt:string, sigma:string) {
    this.analisis.analizar(txt, sigma)
      .subscribe(
        response => {
          this.final_table.emit(response.analisis);
        },
        error => {
          console.error('Error during analysis:', error);
          this.showError(error.error.message);
        }
      );
    
  }

  txt_to_string(file: File): Promise<string> {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result as string);
      reader.onerror = (error) => reject(error);
      reader.readAsText(file);
    });
  }

  emptyValues(): void {
    this.sigma = ''; 
    this.txt = ''; 
    this.selectedFile = null;
  }

  showSuccess(message: string) {
    this.toastr.success(message);
  }

  showError(message: string) {
    this.toastr.error(message);
  }

}
