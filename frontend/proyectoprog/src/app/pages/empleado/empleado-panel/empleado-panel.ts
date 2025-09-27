import { Component } from '@angular/core';
import { RouterLink} from '@angular/router';

@Component({
  selector: 'app-empleado-panel',
  standalone: true, 
  imports: [ RouterLink],
  templateUrl: './empleado-panel.html',
  styleUrls: ['./empleado-panel.css'] 
})
export class EmpleadoPanel {}
