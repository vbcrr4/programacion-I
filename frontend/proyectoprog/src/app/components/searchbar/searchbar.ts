import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { InputField } from '../input/input';
import { ButtonField } from '../button/button';

@Component({
  selector: 'app-searchbar',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, InputField, ButtonField],
  templateUrl: './searchbar.html',
  styleUrls: ['./searchbar.css']
})
export class SearchbarComponent {
  @Input() namePlaceholder: string = 'Buscar por nombre...';
  @Input() categoryPlaceholder: string = 'Buscar por categoría...';
  @Output() searchSubmit = new EventEmitter<any>();

  searchForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.searchForm = this.fb.group({
      name: [''],
      category: ['']
    });
  }

  onSearch(): void {
    this.searchSubmit.emit(this.searchForm.value);
  }
}
