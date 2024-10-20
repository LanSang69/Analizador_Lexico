import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app/app-routing.module';
import { AppComponent } from './app/app.component';
import { MainComponent } from './app/main/main.component';
import { OptionsComponent } from './app/main/options/options.component';
import { CrearBasicoComponent } from './app/main/crear-basico/crear-basico.component';
import { ConcatenarComponent } from './app/main/concatenar/concatenar.component';
import { CerraduraPositivaComponent } from './app/main/cerradura-positiva/cerradura-positiva.component';
import { CerraduraKleeneComponent } from './app/main/cerradura-kleene/cerradura-kleene.component';
import { OpcionalComponent } from './app/main/opcional/opcional.component';
import { UnirAFNsComponent } from './app/main/unir-afns/unir-afns.component';
import { ConvertirComponent } from './app/main/convertir/convertir.component';
import { AnalisisLexicoComponent } from './app/main/analisis-lexico/analisis-lexico.component';
import { WelcomeComponent } from './app/main/welcome/welcome.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ToastrModule } from 'ngx-toastr';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    OptionsComponent,
    CrearBasicoComponent,
    ConcatenarComponent,
    CerraduraPositivaComponent,
    CerraduraKleeneComponent,
    OpcionalComponent,
    UnirAFNsComponent,
    ConvertirComponent,
    AnalisisLexicoComponent,
    WelcomeComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule, 
    ToastrModule.forRoot(),
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
