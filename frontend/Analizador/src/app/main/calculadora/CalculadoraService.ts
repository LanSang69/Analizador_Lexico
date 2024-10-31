import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class CalculadoraService {

  private baseUrl = 'http://localhost:8000'; // Django server URL

  constructor(private http: HttpClient, private router:Router) {}

  calculadora(automata:string, expresion:string): Observable<any> {
    const url = `${this.baseUrl}/calculadora/`;  
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });

    const body = { automata, expresion };

    return this.http.post(url, body, { headers });
  }
}
