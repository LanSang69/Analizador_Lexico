import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConcatenarComponent } from './concatenar.component';

describe('ConcatenarComponent', () => {
  let component: ConcatenarComponent;
  let fixture: ComponentFixture<ConcatenarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ConcatenarComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ConcatenarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
