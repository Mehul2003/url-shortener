import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Path } from './path';


@Injectable({
  providedIn: 'root'
})
export class PathService {

  url = 'http://127.0.0.1:8000/path'

  constructor(private http: HttpClient) { }

  getEndpoint(short: String): Observable<Path> {
    return this.http.get<Path>(`${this.url}?id=${short}`);
  }

  createShortcut(short: String, end: String): Observable<Path> {
    let path = {alt: short, endpoint: end}
    return this.http.post<Path>(`${this.url}`, path);
  }

  generateCombo(): String {
    let alphaL = "abcdefghijklmnopqrstuvwxyz";
    let alphaU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    var comb = "";

    let len = Math.round(Math.random() * 2) + 5;
    var curr;
    
    for (let i = 0; i < len; i++) {
      curr = Math.round(Math.random()*25);
      if (Math.round(Math.random()) == 0) {
        comb += alphaL.at(curr);
      }
      else {
        comb += alphaU.at(curr);
      }
    }
    return comb;
  }

}
