import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnalizarGramaticaComponent } from './analizar-gramatica.component';

describe('AnalizarGramaticaComponent', () => {
  let component: AnalizarGramaticaComponent;
  let fixture: ComponentFixture<AnalizarGramaticaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AnalizarGramaticaComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AnalizarGramaticaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
