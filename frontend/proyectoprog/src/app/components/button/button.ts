import { Component, Input as AngularInput, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-button',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './button.html',
  styleUrl: './button.css'
})
export class ButtonField {
  @AngularInput() variant: 'primary' | 'secondary' | 'danger' | 'success' | 'outline' = 'primary';
  @AngularInput() size: 'sm' | 'md' | 'lg' = 'md';
  @AngularInput() type: 'button' | 'submit' | 'reset' = 'button';
  @AngularInput() disabled: boolean = false;
  @AngularInput() loading: boolean = false;
  @AngularInput() fullWidth: boolean = false;
  @AngularInput() iconStart: string = '';
  @AngularInput() iconEnd: string = '';
  @AngularInput() routerLink: string = '';
  @AngularInput() customClass: string = '';
  @AngularInput() label: string = '';
  @Output() buttonClick = new EventEmitter<MouseEvent>();

  onClick(event: MouseEvent): void {
    if (!this.disabled && !this.loading) {
      this.buttonClick.emit(event);
    }
  }

  get buttonClasses(): string {
    const classes = [
      'app-button',
      `variant-${this.variant}`,
      `size-${this.size}`,
    ];

    if (this.fullWidth) {
      classes.push('full-width');
    }

    if (this.loading) {
      classes.push('loading');
    }

    if (this.customClass) {
      classes.push(this.customClass);
    }

    return classes.join(' ');
  }

  get isLink(): boolean {
    return !!this.routerLink;
  }
}
