import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class crear_basico {

  private baseUrl = 'http://localhost:8000'; // Django server URL

  constructor(private http: HttpClient) {}

  crearBasico(inferior: string, superior: string): Observable<any> {
    const url = `${this.baseUrl}/crear_basico/`;  // Django view URL
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });

    const body = { inferior, superior };

    return this.http.post(url, body, { headers });
  }
}
