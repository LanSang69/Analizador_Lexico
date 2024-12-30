import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OptionsComponentS } from './options.component';

describe('OptionsComponent', () => {
  let component: OptionsComponentS;
  let fixture: ComponentFixture<OptionsComponentS>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [OptionsComponentS]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(OptionsComponentS);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
