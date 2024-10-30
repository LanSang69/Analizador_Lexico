import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class RegexService {

  private baseUrl = 'http://localhost:8000'; // Django server URL

  constructor(private http: HttpClient, private router:Router) {}

  getAFN(regex:string): Observable<any> {
    const url = `${this.baseUrl}/regex_to_afn/`;  
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });

    const body = { regex };

    return this.http.post(url, body, { headers });
  }
}
