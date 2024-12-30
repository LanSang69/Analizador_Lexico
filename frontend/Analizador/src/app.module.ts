import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app/app-routing.module';
import { AppComponent } from './app/app.component';
import { MainComponent } from './app/lexico/main.component';
import { OptionsComponent } from './app/lexico/options/options.component';
import { CrearBasicoComponent } from './app/lexico/crear-basico/crear-basico.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ToastrModule } from 'ngx-toastr';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { RegexToAFNComponent } from './app/lexico/regex-to-afn/regex-to-afn.component';
import { AnalizarComponent } from './app/lexico/analizar/analizar.component';
import { CalculadoraComponent } from './app/lexico/calculadora/calculadora.component';
import { MenuComponent } from './app/menu/menu.component';
import { SintacticoComponent } from './app/sintactico/sintactico.component';
import { OptionsComponentS } from './app/sintactico/options/options.component';
import { AnalizarGramaticaComponent } from './app/sintactico/analizar-gramatica/analizar-gramatica.component';
import { AnalizarCadenaComponent } from './app/sintactico/analizar-cadena/analizar-cadena.component';


@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    OptionsComponent,
    CrearBasicoComponent,
    RegexToAFNComponent,
    AnalizarComponent,
    CalculadoraComponent,
    MenuComponent,
    SintacticoComponent,
    OptionsComponentS,
    AnalizarGramaticaComponent,
    AnalizarCadenaComponent,
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
    provideClientHydration(),
    provideHttpClient(withFetch()),
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
