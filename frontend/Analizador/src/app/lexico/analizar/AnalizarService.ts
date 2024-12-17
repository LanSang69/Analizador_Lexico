import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AnalizarService {

  private baseUrl = 'http://localhost:8000'; // Django server URL

  constructor(private http: HttpClient, private router:Router) {}

  analizar(table:string, sigma:string): Observable<any> {
    const url = `${this.baseUrl}/analizar/`;  
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });

    const body = { table, sigma };

    return this.http.post(url, body, { headers });
  }
}
