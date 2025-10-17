import { Component,Input } from '@angular/core';


@Component({
  selector: 'app-card',
  standalone: true,
  imports: [],
  templateUrl: './card.html',
  styleUrls: ['./card.css']
})
export class Card {
  @Input() imgSrc: string = '';
  @Input() title : string = '';
  @Input() description : string = '';
  @Input() price: string = '';
}
