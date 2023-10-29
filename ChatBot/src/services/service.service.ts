import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ServiceService {

  constructor(private http: HttpClient) { }

  getData(prompt: string) : Observable<any>{
    return this.http.get<any>('http://127.0.0.1:8000/endpoint');
  }

  answer(prompt: string): Observable<any> {
    const body = { prompt: prompt }; // Create a body object with the required data
    return this.http.post<any>('http://127.0.0.1:8000/answer/', body);
  }
}
