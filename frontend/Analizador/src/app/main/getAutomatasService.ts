import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class getAutomatasService {
  private baseUrl = 'http://localhost:8000'; 

  constructor(private http: HttpClient) {}

  getAutomata(): Observable<any> {
    const url = `${this.baseUrl}/get_session_data/`; 
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.get(url, { headers });
  }
}
