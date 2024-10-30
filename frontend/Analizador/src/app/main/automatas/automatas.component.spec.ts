import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AutomatasComponent } from './automatas.component';

describe('AutomatasComponent', () => {
  let component: AutomatasComponent;
  let fixture: ComponentFixture<AutomatasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AutomatasComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AutomatasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
