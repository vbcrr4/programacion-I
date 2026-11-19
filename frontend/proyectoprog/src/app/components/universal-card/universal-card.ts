import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-universal-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './universal-card.html',
  styleUrl: './universal-card.css'
})
export class UniversalCard {
  @Input() variant: 'default' | 'gradient' | 'glass' | 'transparent' = 'default';
  @Input() size: 'sm' | 'md' | 'lg' | 'xl' | 'full' = 'lg';
  @Input() padding: 'xs' | 'sm' | 'md' | 'lg' | 'xl' | '2xl' = 'lg';
  @Input() centered: boolean = true;
  @Input() hoverable: boolean = false;
  @Input() borderRadius: 'sm' | 'md' | 'lg' | 'xl' | '2xl' = 'xl';
  @Input() customClass: string = '';

  get cardClasses(): string {
    const classes = [
      'universal-card',
      `variant-${this.variant}`,
      `size-${this.size}`,
      `padding-${this.padding}`,
      `radius-${this.borderRadius}`,
    ];

    if (this.centered) {
      classes.push('centered');
    }

    if (this.hoverable) {
      classes.push('hoverable');
    }

    if (this.customClass) {
      classes.push(this.customClass);
    }

    return classes.join(' ');
  }
}
