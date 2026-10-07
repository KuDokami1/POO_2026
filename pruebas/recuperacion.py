class alumnos: 
    def __init__(self, nombre, apellido, edad, calificaciones): 
        self._nombre = self.nombre
        self._edad = self.edad
        self._calificaciones = self.calificaciones
        
        def mostrarDatos (self):
            print(f"Nombre: {self._nombre}")
            print(f"Edad: {self._edad}")
            print(f"Calificaciones: {self._calificaciones}")
            
        def estaAprobado (calificaciones):
            promedio = sum(self._calificaciones) / len(self._calificaciones)
            if promedio >= 6:
                print("El alumno está aprobado.")
            else:
                print("El alumno está reprobado.")
        