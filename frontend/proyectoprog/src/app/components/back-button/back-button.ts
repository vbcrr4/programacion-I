import { Component, Input } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-back-button',
  imports: [RouterLink],
  templateUrl: './back-button.html',
  styleUrl: './back-button.css'
})
export class BackButton {
  @Input() link: string=""

}
