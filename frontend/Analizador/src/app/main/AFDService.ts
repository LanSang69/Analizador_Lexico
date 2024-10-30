import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AFDService {

  private baseUrl = 'http://localhost:8000'; // Django server URL

  constructor(private http: HttpClient, private router:Router) {}

  getString(id: number): Observable<any> {
    const url = `${this.baseUrl}/afn_to_afd/`;  
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });

    const body = { id };

    return this.http.post(url, body, { headers });
  }
}
