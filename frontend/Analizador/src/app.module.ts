import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app/app-routing.module';
import { AppComponent } from './app/app.component';
import { MainComponent } from './app/main/main.component';
import { OptionsComponent } from './app/main/options/options.component';
import { CrearBasicoComponent } from './app/main/crear-basico/crear-basico.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ToastrModule } from 'ngx-toastr';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { AutomatasComponent } from './app/main/automatas/automatas.component';
import { RegexToAFNComponent } from './app/main/regex-to-afn/regex-to-afn.component';
import { AnalizarComponent } from './app/main/analizar/analizar.component';


@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    OptionsComponent,
    CrearBasicoComponent,
    AutomatasComponent,
    RegexToAFNComponent,
    AnalizarComponent,
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
