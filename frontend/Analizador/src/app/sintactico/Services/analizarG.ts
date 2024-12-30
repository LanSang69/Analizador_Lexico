import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class GramaticaService {

  private baseUrl = 'http://localhost:8000/ll1'; // Django server URL

  constructor(private http: HttpClient, private router:Router) {}

  getGrammar(gramatica: string): Observable<any> {
    const url = `${this.baseUrl}/get_reglas/`;  
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });

    const body = { gramatica };

    return this.http.post(url, body, { headers });
  }
}
