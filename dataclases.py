from dataclasses import dataclass
from typing import Any

# Dataclases - Anotaciones - f String

# se puede implementar este tipo de clases para trabajar con muchos atributos
# utilizando el decorador para ahorrar lineas de codigo

@dataclass
class User:
	username: str
	email: str
	#password: Any # No quiero definir esta clase
	password: Any = 'valor por default'

	def saludar(self):
		print(f"Hola soy el usuario {self.username}")

#if __name__ == '__main__':

	#persona = User("Alan","jajdjdjd@gmail.com")

	#print(persona.username)
	#print(persona.email)

persona = User("Alan","programmer@email.com")

persona.saludar()
print(persona.email)


