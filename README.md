# ProyectoItegracionContinua
Proyecto de Asistencia de Personal, se realizara pruebas Pipeline CI con GitHub Actions, Docker y PostgreSQL para el correcto funcionaciomiento, cobertura de analisis de codigo:


# Caracteristicas


# Sistema de Control de Asistencia

# Sin Docker
Aplicación web para registrar estudiantes y controlar su asistencia.

## Características
- Registro de estudiantes
- Control de asistencia con fecha y hora
- Base de datos PostgreSQL
- Interfaz web con Bootstrap

## Requisitos
- Python 3.9+
- PostgreSQL

## Instalación
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt


# Con Docker -- hasta el momento esta funcionado en docker ya que se realizo algunas configuraciones

Aplicación web para gestionar la asistencia de estudiantes construida con Flask y PostgreSQL.

## Requisitos

- Docker
- Docker Compose

## Instalación

```bash
git clone https://github.com/tu-usuario/control-asistencia.git
cd control-asistencia
docker-compose up --build
