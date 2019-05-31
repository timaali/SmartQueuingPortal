import { SelectServiceComponent } from './select-service/select-service.component';
import { SelectCounterComponent } from './select-counter/select-counter.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DashboardComponent } from './dashboard/dashboard.component';
import { FormsComponent } from './forms/forms.component';
import { ButtonsComponent } from './buttons/buttons.component';
import { TablesComponent } from './tables/tables.component';
import { IconsComponent } from './icons/icons.component';
import { TypographyComponent } from './typography/typography.component';
import { AlertsComponent } from './alerts/alerts.component';
import { AccordionsComponent } from './accordions/accordions.component';
import { BadgesComponent } from './badges/badges.component';
import { ProgressbarComponent } from './progressbar/progressbar.component';
import { BreadcrumbsComponent } from './breadcrumbs/breadcrumbs.component';
import { PaginationComponent } from './pagination/pagination.component';
import { DropdownComponent } from './dropdown/dropdown.component';
import { TooltipsComponent } from './tooltips/tooltips.component';
import { CarouselComponent } from './carousel/carousel.component';
import { TabsComponent } from './tabs/tabs.component';
import { ServicesComponent } from './services/services.component';
import { TellersComponent } from './tellers/tellers.component';
import { CreateComponent } from './create/create.component';
import { UpdateComponent } from './update/update.component';
import { TicketsComponent } from './tickets/tickets.component';
import { BookComponent } from './book/book.component';
import { LoginComponent } from './login/login.component';
import { CounterServiceComponent } from './counter-service/counter-service.component';

const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'forms', component: FormsComponent },
  { path: 'buttons', component: ButtonsComponent },
  { path: 'tables', component: TablesComponent },
  { path: 'icons', component: IconsComponent },
  { path: 'typography', component: TypographyComponent },
  { path: 'alerts', component: AlertsComponent },
  { path: 'accordions', component: AccordionsComponent },
  { path: 'badges', component: BadgesComponent },
  { path: 'progressbar', component: ProgressbarComponent },
  { path: 'breadcrumbs', component: BreadcrumbsComponent },
  { path: 'pagination', component: PaginationComponent },
  { path: 'dropdowns', component: DropdownComponent },
  { path: 'tooltips', component: TooltipsComponent },
  { path: 'carousel', component: CarouselComponent },
  { path: 'tabs', component: TabsComponent },
  { path: 'services', component: ServicesComponent },
  { path: 'tellers', component: TellersComponent },
  { path: 'create/:component/:counter_id', component: CreateComponent },
  { path: 'update/:update/:id', component: UpdateComponent },
  { path: 'tickets/:ticket_id', component: TicketsComponent },
  { path: 'book/:teller_id', component: BookComponent },
  { path: 'cancelticket/:ticket_id', component: TicketsComponent },
  { path: 'login', component: LoginComponent },
  { path: 'selectService', component: SelectServiceComponent },
  { path: 'selectCounter/:serviceId', component: SelectCounterComponent },
  { path: 'CounterService/:serviceId', component: CounterServiceComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
