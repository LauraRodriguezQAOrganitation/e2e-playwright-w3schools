## Proyecto QA Manual y Automatizado de la web W3School

En este proyecto se realiza un proceso de aseguramiento de la calidad (QA) como parte de la formación, combinando pruebas manuales y automatizadas: https://w3schools.com"
El proyecto se ha realizado en equipo siguiendo metodología ágil Scrum y BDD para el diseño de las pruebas antes del desarrollo, siguiendo buenas prácticas de testing.

## Alcance del Proyecto

El proyecto se enfoca en la validación de funcionalidades clave del sitio W3Schools, tales como:
- Navegación principal
- Acceso a secciones educativas
- Interacción con ejemplos y juegos educativos
- Verificación de elementos visibles y contenido principal

## Plan de Pruebas, resultados y reporte de errores: [Ver Plan de Pruebas](https://github.com/LauraRodriguezQAOrganitation/e2e-playwright-w3schools/blob/main/PlanDePruebas.md)
En este documento se detalla el plan de pruebas, las funcionalidades probadas, el resultado de las pruebas ejecutadas y el reporte de errores.

## Automatización E2E - Tecnologías

- ![Python](https://img.shields.io/badge/Python-3.12%2B-blue)  
- ![Playwright](https://img.shields.io/badge/Playwright-v1.48-green)

## Resultados de las pruebas automatizadas

Se ha configurado un flujo de integración continua con github actions que ejecuta las pruebas automatizadas después de cada cambio en el repositorio y una vez a la semana al final de cada sprint. Puede consultar en este enlace el resultado de la ultima ejecucion de pruebas y descargar el reporte HTML desde a seccion **Actions** del repositorio.

El proyecto fue realizado en equipo, aplicando **metodología ágil Scrum** y **BDD (Behavior Driven Development)** para el diseño de los casos de prueba, siguiendo las buenas prácticas vistas durante el curso.

---
 reporte de los resultados de las pruebas: (https://github.com/LauraRodriguezQAOrganitation/e2e-playwright-w3schools/tree/main/tests)


## Requisitos del Proyecto

### Python 3.12

Descarga e instala Python versión 3.12 desde su web oficial (https://www.python.org/downloads/)
Asegurate que Python se añade al PATH durante la instalación.

### Instalar Dependencias

Una vez instalado Python:
Clona este repositorio.

Accede a la carpeta del proyecto.
Ejecuta en la terminal:

``
pip install -r requirements.txt
``

``
playwright install
``

### Ejecutar los tests en local
Accede a la carpeta del proyecto.

Ejecuta en la terminal:

`pytest --headed`

## Debug y Trazas
Durante el desarrollo se utilizaron herramientas de depuración como Playwright Inspector, page.pause() y generación de trazas para análisis de fallos.