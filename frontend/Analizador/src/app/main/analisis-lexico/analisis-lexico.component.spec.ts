import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnalisisLexicoComponent } from './analisis-lexico.component';

describe('AnalisisLexicoComponent', () => {
  let component: AnalisisLexicoComponent;
  let fixture: ComponentFixture<AnalisisLexicoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AnalisisLexicoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AnalisisLexicoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
