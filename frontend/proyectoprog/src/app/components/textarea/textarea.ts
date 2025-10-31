import { NgIf } from '@angular/common';
import { Component, Input, Output, EventEmitter, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-textarea',
  imports: [NgIf],
  templateUrl: './textarea.html',
  styleUrls: ['./textarea.css']
})
export class TextArea {
  @Input() placeholder: string = 'Escribe aquí...';
  @Input() maxRows: number = 5;
  @Input() minRows: number = 1;
  @Input() value: string = '';
  @Input() type: 'search' | 'comment' = 'comment'; // Por defecto para comentarios
  @Output() valueChange = new EventEmitter<string>();
  @Output() search = new EventEmitter<string>(); // Solo para búsqueda
  
  @ViewChild('textareaRef') textareaRef!: ElementRef;

  onInput(event: any) {
    this.value = event.target.value;
    this.valueChange.emit(this.value);
    this.autoResize();
    
    // Emitir búsqueda en tiempo real si es tipo search
    if (this.type === 'search') {
      this.search.emit(this.value);
    }
  }

  onKeyPress(event: KeyboardEvent) {
    if (this.type === 'search' && event.key === 'Enter') {
      this.search.emit(this.value);
    }
  }

  private autoResize() {
    const textarea = this.textareaRef.nativeElement;
    textarea.style.height = 'auto';
    
    const lineHeight = parseInt(getComputedStyle(textarea).lineHeight);
    const newHeight = Math.min(
      textarea.scrollHeight,
      lineHeight * this.maxRows
    );
    
    textarea.style.height = newHeight + 'px';
  }

  // Método para limpiar el campo
  clear() {
    this.value = '';
    this.valueChange.emit('');
    this.autoResize();
  }
}