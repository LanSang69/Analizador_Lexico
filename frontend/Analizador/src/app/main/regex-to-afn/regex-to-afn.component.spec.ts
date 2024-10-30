import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegexToAFNComponent } from './regex-to-afn.component';

describe('RegexToAFNComponent', () => {
  let component: RegexToAFNComponent;
  let fixture: ComponentFixture<RegexToAFNComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [RegexToAFNComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RegexToAFNComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
