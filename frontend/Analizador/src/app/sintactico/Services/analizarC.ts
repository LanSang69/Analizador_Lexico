import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class CadenaService {

  private baseUrl = 'http://localhost:8000/ll1'; // Django server URL

  constructor(private http: HttpClient, private router:Router) {}

  getTable(sigma:String, matrix: any): Observable<any> {
    const url = `${this.baseUrl}/get_tabla/`;  
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });

    const body = { sigma,matrix };

    return this.http.post(url, body, { headers });
  }
}
