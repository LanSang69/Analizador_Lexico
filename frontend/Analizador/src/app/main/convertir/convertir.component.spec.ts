import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConvertirComponent } from './convertir.component';

describe('ConvertirComponent', () => {
  let component: ConvertirComponent;
  let fixture: ComponentFixture<ConvertirComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ConvertirComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ConvertirComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
