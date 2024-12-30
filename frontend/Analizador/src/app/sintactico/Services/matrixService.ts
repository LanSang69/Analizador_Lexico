import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class MatrixService {
    private arraySource = new BehaviorSubject<{ [key: string]: string }>({});
    currentArray = this.arraySource.asObservable(); 
  
    updateArray(newArray: { [key: string]: string }) {
      this.arraySource.next(newArray);
    }
  
}
