import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { UniversalCard } from '../../../components/universal-card/universal-card';
import { InputField } from '../../../components/input/input';
import { ButtonField } from '../../../components/button/button';
import { ActionBttn } from '../../../components/action-bttn/action-bttn';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Auth } from '../../../services/auth';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterLink, UniversalCard, InputField, ButtonField,ActionBttn,ReactiveFormsModule],
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class Login{
  constructor(
    private authService: Auth
  ){}

  irLogin(){
    this.authService.login().subscribe({
      next:(res) => {
        alert("Login exitoso");
        console.log("Respuesta login : ", res);

      },
      error:(err) =>{
        alert("Usuario o contraseña invalido");
        console.log("Error en el login",err);
      }
    })
  }
}
