import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class resetService {

  private baseUrl = 'http://localhost:8000'; // Django server URL

  constructor(private http: HttpClient, private router:Router) {}

  resetAutomatas(): Observable<any> {
    const url = `${this.baseUrl}/set_empty/`;  // Django view URL
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });

    const body = {};

    return this.http.post(url, body, { headers });
  }
}
