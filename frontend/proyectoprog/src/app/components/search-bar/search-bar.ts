import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-search-bar',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './search-bar.html',
  styleUrls: ['./search-bar.css']
})
export class SearchBar {
  query: string = '';

  @Output() search = new EventEmitter<string>();

  onSearch() {
    // emite el texto de búsqueda hacia el padre
    this.search.emit(this.query?.trim() ?? '');
  }
}
