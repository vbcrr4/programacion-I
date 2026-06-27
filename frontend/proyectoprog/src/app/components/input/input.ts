import { Component, Input as AngularInput, forwardRef } from '@angular/core';
import { ControlValueAccessor, NG_VALUE_ACCESSOR, FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-input',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './input.html',
  styleUrl: './input.css',
  providers: [
    {
      provide: NG_VALUE_ACCESSOR,
      useExisting: forwardRef(() => InputField),
      multi: true
    }
  ]
})
export class InputField implements ControlValueAccessor {
  @AngularInput() type: 'text' | 'email' | 'password' | 'number' | 'tel' | 'url' | 'search' = 'text';
  @AngularInput() label: string = '';
  @AngularInput() placeholder: string = '';
  @AngularInput() inputId: string = `input-${Math.random().toString(36).substr(2, 9)}`;
  @AngularInput() disabled: boolean = false;
  @AngularInput() readonly: boolean = false;
  @AngularInput() customClass: string = '';
  @AngularInput() error: boolean = false;
  @AngularInput() errorMessage: string = '';
  @AngularInput() iconStart: string = '';
  @AngularInput() iconEnd: string = '';

  value: string = '';
  onChange: any = () => {};
  onTouched: any = () => {};

  writeValue(value: any): void {
    this.value = value || '';
  }

  registerOnChange(fn: any): void {
    this.onChange = fn;
  }

  registerOnTouched(fn: any): void {
    this.onTouched = fn;
  }

  setDisabledState(isDisabled: boolean): void {
    this.disabled = isDisabled;
  }

  onInputChange(event: Event): void {
    const value = (event.target as HTMLInputElement).value;
    this.value = value;
    this.onChange(value);
  }

  onBlur(): void {
    this.onTouched();
  }

  get inputClasses(): string {
    const classes = ['app-input'];

    if (this.error) {
      classes.push('error');
    }

    if (this.iconStart) {
      classes.push('with-icon-start');
    }

    if (this.iconEnd) {
      classes.push('with-icon-end');
    }

    if (this.customClass) {
      classes.push(this.customClass);
    }

    return classes.join(' ');
  }
}
