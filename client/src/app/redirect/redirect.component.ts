import { Component, OnInit } from '@angular/core';
import { PathService } from '../path.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-redirect',
  templateUrl: './redirect.component.html',
  styleUrls: ['./redirect.component.css']
})
export class RedirectComponent implements OnInit {

  url = "TEST URL";

  constructor(
    private ps: PathService, 
    private route: ActivatedRoute,
    private router: Router
  ) { }
  
  
  ngOnInit(): void {
    this.getEndpoint();
  }

  getEndpoint(): void {
    let short = String(this.route.snapshot.paramMap.get('id'));
    this.ps.getEndpoint(short).subscribe(res => {
      this.url = String(res.endpoint);
      if (String(res) != "Invalid Id") {
        this.url = !this.url.startsWith("http") ? 'https://' + this.url : this.url;

        window.location.replace(this.url);
      }
      else {
        this.router.navigateByUrl('/404');
      }
    });
  }


}
