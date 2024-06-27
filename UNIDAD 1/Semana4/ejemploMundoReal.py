# hospital.py

class Paciente:
    def _init_(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def _str_(self):
        return f"Paciente: {self.nombre} {self.apellido}, Edad: {self.edad}"


class Doctor:
    def _init_(self, nombre, apellido, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.pacientes = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def mostrar_pacientes(self):
        for paciente in self.pacientes:
            print(paciente)


class Hospital:
    def _init_(self, nombre):
        self.nombre = nombre
        self.doctores = []

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def mostrar_doctores(self):
        for doctor in self.doctores:
            print(f"Doctor: {doctor.nombre} {doctor.apellido}, Especialidad: {doctor.especialidad}")
            doctor.mostrar_pacientes()


# nombre de paciente añado
hospital = Hospital("Hospital General")

paciente1 = Paciente("Juan", "Pérez", 30)
paciente2 = Paciente("María", "González", 25)

doctor1 = Doctor("Dr. Pérez", "Cardiólogo", "Cardiología")
doctor2 = Doctor("Dr. González", "Pediatra", "Pediatría")

doctor1.agregar_paciente(paciente1)
doctor2.agregar_paciente(paciente2)

hospital.agregar_doctor(doctor1)
hospital.agregar_doctor(doctor2)

print("Doctores del hospital:")
hospital.mostrar_doctores()