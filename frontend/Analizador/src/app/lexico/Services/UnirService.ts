import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class UnirService {

  private baseUrl = 'http://localhost:8000'; // Django server URL

  constructor(private http: HttpClient, private router:Router) {}

  unir_automatas(ids: number[]): Observable<any> {
    const url = `${this.baseUrl}/unir/`;  
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });

    const body = { ids };

    return this.http.post(url, body, { headers });
  }
}
