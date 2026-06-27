import { Component, Input, Output, EventEmitter,  } from '@angular/core';

@Component({
  selector: 'app-calfiestrellas',
  templateUrl: './calfiestrellas.html',
  styleUrls: ['./calfiestrellas.css']
})
export class CalifiEstrellas {
  @Input() calificacion: number = 0;
  @Input() tamaño: 'sm' | 'md' | 'lg' = 'md';
  @Input() editable: boolean = true;
  @Output() calificacionChange = new EventEmitter<number>();

  estrellas = [1, 2, 3, 4, 5];
  calificacionTemporal: number = 0;

  calificar(puntuacion: number) {
    if (this.editable) {
      this.calificacion = puntuacion;
      this.calificacionChange.emit(this.calificacion);
    }
  }

  hoverStar(puntuacion: number) {
    if (this.editable) {
      this.calificacionTemporal = puntuacion;
    }
  }

  resetTemporal() {
    if (this.editable) {
      this.calificacionTemporal = this.calificacion;
    }
  }

  getTamanoClase(): string {
    switch (this.tamaño) {
      case 'sm': return 'estrella-sm';
      case 'lg': return 'estrella-lg';
      default: return 'estrella-md';
    }
  }
  // Agrega este método a la clase existente
getTextoCalificacion(): string {
  const textos = {
    0: 'Sin calificar',
    1: 'Muy malo',
    2: 'Malo',
    3: 'Regular',
    4: 'Bueno',
    5: 'Excelente'
  };
  return textos[this.calificacion as keyof typeof textos] || 'Sin calificar';
}
}