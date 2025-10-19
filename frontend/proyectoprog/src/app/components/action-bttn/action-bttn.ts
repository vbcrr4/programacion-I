import { Component, Input, Output, EventEmitter } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-action-bttn',
  imports: [RouterLink],
  templateUrl: './action-bttn.html',
  standalone:true,
  styleUrl: './action-bttn.css'
})
export class ActionBttn {
@Input() link: string=""
@Input() bttn_icon: string=""
@Input() label: string = 'Acción';
@Output() buttonClick = new EventEmitter<void>();

onClick() {
  this.buttonClick.emit();
}

}
