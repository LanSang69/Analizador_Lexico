import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AutomatasComponent } from './main/automatas/automatas.component';
import { MainComponent } from './main/main.component';

const routes: Routes = [
  { path: 'home', component: MainComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
