import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class ConcatenarService {

  private baseUrl = 'http://localhost:8000'; // Django server URL

  constructor(private http: HttpClient, private router:Router) {}

  concatenar(id1: number, id2: number): Observable<any> {
    const url = `${this.baseUrl}/concatenar/`;  
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });

    const body = { id1, id2 };

    return this.http.post(url, body, { headers });
  }
}
