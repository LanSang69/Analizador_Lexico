import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class LexicoService {

  private baseUrl = 'http://localhost:8000/ll1'; // Django server URL

  constructor(private http: HttpClient, private router:Router) {}

  getGrammar(sigma: string): Observable<any> {
    const url = `${this.baseUrl}/get_lexico/`;  
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });

    const body = { sigma };

    return this.http.post(url, body, { headers });
  }
}
