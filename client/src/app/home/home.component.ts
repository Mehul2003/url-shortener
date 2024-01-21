import { Component, OnInit } from '@angular/core';
import { PathService } from '../path.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  short: String = ""

  constructor(private ps: PathService) {}

  generate(url: String): void {
    this.short = this.ps.generateCombo();;

    console.log(this.ps.getEndpoint(this.short))
    this.ps.createShortcut(this.short, url).subscribe(res => console.log(res))
  }

}
