import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UnirAFNsComponent } from './unir-afns.component';

describe('UnirAFNsComponent', () => {
  let component: UnirAFNsComponent;
  let fixture: ComponentFixture<UnirAFNsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [UnirAFNsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(UnirAFNsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
