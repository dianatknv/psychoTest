import { BrowserModule } from '@angular/platform-browser';
import { NgModule, ClassProvider } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ParentComponent } from './components/parent/parent.component';
import { ProviderService } from './shared/services/provider.service';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { TestComponent } from './test/test.component';
import {AuthInterceptor} from './AuthInterceptor';
import {FormsModule} from '@angular/forms';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { MainComponent } from './components/main/main.component';
import { ProfileComponent } from './components/profile/profile.component';

@NgModule({
  declarations: [
    AppComponent,
    ParentComponent,
    TestComponent,
    HeaderComponent,
    FooterComponent,
    MainComponent,
    ProfileComponent
  ],
  imports: [
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [
    ProviderService,
    <ClassProvider> {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
