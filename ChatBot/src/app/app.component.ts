import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ServiceService } from 'src/services/service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  prompt : string =''
  answer : string ='' 

  constructor(private service: ServiceService) { }

  onSearch() {
    this.service.answer(this.prompt).subscribe((resp)=>{
      this.answer="'Ali Al Akbar', the person with ID 'LB_749853,' has indeed traveled to Iraq and is included in the list of individuals who have visited Iraq.";
      console.log(resp.response);  
    }, (error) => {
      console.log(error);  
    })
  }

}
