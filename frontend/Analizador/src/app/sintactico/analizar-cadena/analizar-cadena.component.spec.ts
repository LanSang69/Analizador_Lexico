import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnalizarCadenaComponent } from './analizar-cadena.component';

describe('AnalizarCadenaComponent', () => {
  let component: AnalizarCadenaComponent;
  let fixture: ComponentFixture<AnalizarCadenaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AnalizarCadenaComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AnalizarCadenaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
