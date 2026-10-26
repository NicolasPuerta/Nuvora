# Nuvora --- Issues iniciales

> Plan inicial de trabajo para convertir la idea de Nuvora en un MVP de
> finanzas personales.
>
> **Objetivo:** construir primero un motor financiero confiable; después
> incorporar importaciones e integraciones externas. Los números de
> issue son propuestos: GitHub asignará los números reales al crearlos.

## Milestones

  -----------------------------------------------------------------------
  Milestone               Objetivo                Issues propuestos
  ----------------------- ----------------------- -----------------------
  M0 --- Definición del   Acordar alcance, modelo #1--#3
  producto                financiero y decisiones 
                          técnicas                

  M1 --- Fundamentos      Ejecutar el proyecto    #4--#7
  técnicos                localmente con Docker y 
                          pruebas                 

  M2 --- Motor financiero Administrar cuentas y   #8--#12
                          movimientos             
                          correctamente           

  M3 --- Frontend y       Consultar movimientos y #13--#16
  dashboards              visualizar métricas     

  M4 --- Importación      Importar archivos y     #17--#19
                          evitar duplicados       
  -----------------------------------------------------------------------

## M0 --- Definición del producto

### Issue 1 --- Definir alcance del MVP

**Labels:** `product`, `documentation`\
**Prioridad:** crítica

#### Objetivo

Documentar qué funcionalidades tendrá la primera versión y qué queda
fuera.

#### Tareas

-   Definir el usuario objetivo inicial.
-   Establecer funcionalidades incluidas en el MVP.
-   Definir criterios de éxito.
-   Documentar las funcionalidades pospuestas: APIs bancarias, IA y
    puntaje crediticio oficial.

#### Criterios de aceptación

-   [ ] Existe `docs/product-scope.md`.
-   [ ] El alcance incluido y excluido está explícito.
-   [ ] Los criterios de éxito del MVP son verificables.

### Issue 2 --- Definir modelo de dominio financiero

**Labels:** `backend`, `architecture`\
**Prioridad:** crítica\
**Dependencia:** Issue 1

#### Objetivo

Definir cómo representa Nuvora el dinero y sus movimientos.

#### Tareas

-   Definir cuentas, transacciones, categorías y transferencias.
-   Definir estados de transacción.
-   Definir el tratamiento de monedas y precisión decimal.
-   Establecer reglas para calcular ingresos, gastos y saldos.
-   Documentar devoluciones, reversos y operaciones pendientes.

#### Criterios de aceptación

-   [ ] Existe `docs/data-model.md`.
-   [ ] El documento incluye entidades, relaciones y ejemplos.
-   [ ] Las reglas financieras están documentadas sin ambigüedades.

### Issue 3 --- Definir arquitectura y estándares

**Labels:** `architecture`, `documentation`\
**Prioridad:** alta

#### Objetivo

Acordar cómo se organiza y desarrolla el código.

#### Tareas

-   Definir monorepositorio y estructura de carpetas.
-   Establecer convenciones de nombres y manejo de errores.
-   Definir estándares de Python, TypeScript y pruebas.
-   Documentar decisiones arquitectónicas iniciales.

#### Criterios de aceptación

-   [ ] Existe `docs/architecture.md`.
-   [ ] La estructura inicial está documentada.
-   [ ] Las decisiones principales y sus motivos están registrados.

## M1 --- Fundamentos técnicos

### Issue 4 --- Inicializar repositorio y estructura del proyecto

**Labels:** `infra`, `chore`

#### Objetivo

Crear la estructura base del repositorio.

#### Tareas

-   Crear carpetas `frontend/`, `backend/` y `docs/`.
-   Añadir `.gitignore`.
-   Añadir `.env.example` sin secretos reales.
-   Crear instrucciones iniciales para desarrolladores.

#### Criterios de aceptación

-   [ ] El repositorio tiene una estructura consistente.
-   [ ] Los archivos de entorno sensibles están excluidos de Git.
-   [ ] Un desarrollador puede entender cómo iniciar el proyecto.

### Issue 5 --- Configurar FastAPI y PostgreSQL con Docker Compose

**Labels:** `backend`, `infra`\
**Dependencia:** Issue 4

#### Objetivo

Permitir levantar localmente la API y la base de datos.

#### Tareas

-   Crear servicio FastAPI.
-   Configurar PostgreSQL.
-   Configurar variables de entorno.
-   Añadir healthchecks.
-   Implementar endpoint `/health`.
-   Exponer documentación OpenAPI en desarrollo.

#### Criterios de aceptación

-   [ ] `docker compose up --build` inicia los servicios.
-   [ ] La API responde en `/health`.
-   [ ] `/docs` funciona en desarrollo.
-   [ ] No hay credenciales reales en el repositorio.

### Issue 6 --- Configurar calidad de código y pruebas automatizadas

**Labels:** `quality`, `ci`\
**Dependencia:** Issue 4

#### Objetivo

Detectar errores de estilo y pruebas fallidas antes de integrar cambios.

#### Tareas

-   Configurar Ruff o Flake8, Pylint y Pytest para Python.
-   Configurar ESLint, Prettier y pruebas del frontend.
-   Configurar integración continua para pull requests.
-   Documentar los comandos de validación local.

#### Criterios de aceptación

-   [ ] Las herramientas pueden ejecutarse localmente.
-   [ ] La CI ejecuta las validaciones pertinentes.
-   [ ] Una prueba fallida hace fallar el pipeline.

### Issue 7 --- Configurar SQLAlchemy y Alembic

**Labels:** `backend`, `database`\
**Dependencia:** Issue 5

#### Objetivo

Configurar persistencia y migraciones versionadas.

#### Tareas

-   Configurar conexión a PostgreSQL.
-   Definir sesiones y configuración de SQLAlchemy.
-   Inicializar Alembic.
-   Documentar cómo generar y ejecutar migraciones.

#### Criterios de aceptación

-   [ ] La API se conecta a PostgreSQL.
-   [ ] Una migración de prueba se puede aplicar.
-   [ ] El esquema de base de datos se gestiona mediante Alembic.

## M2 --- Motor financiero

### Issue 8 --- Implementar autenticación y aislamiento de usuarios

**Labels:** `backend`, `security`

#### Objetivo

Proteger los recursos de cada usuario.

#### Tareas

-   Elegir un mecanismo de autenticación adecuado.
-   Implementar registro e inicio de sesión.
-   Proteger los endpoints.
-   Validar propiedad de los recursos en cada operación.
-   Añadir pruebas de acceso cruzado entre usuarios.

#### Criterios de aceptación

-   [ ] Los endpoints privados requieren autenticación.
-   [ ] Un usuario no puede consultar ni modificar recursos de otro
    usuario.
-   [ ] Los errores de autenticación y autorización son controlados.
-   [ ] Las pruebas cubren intentos de acceso indebido.

### Issue 9 --- Implementar cuentas financieras

**Labels:** `backend`, `feature`\
**Dependencias:** Issues 2 y 7

#### Objetivo

Permitir que cada usuario administre sus cuentas financieras internas.

#### Tareas

-   Crear cuentas.
-   Listar cuentas del usuario autenticado.
-   Consultar el detalle de una cuenta.
-   Actualizar datos.
-   Archivar cuentas sin eliminar el historial.
-   Validar nombre, tipo y moneda.

#### Criterios de aceptación

-   [ ] Las cuentas se persisten en PostgreSQL.
-   [ ] Cada cuenta pertenece a un usuario.
-   [ ] Se aplican validaciones y controles de acceso.
-   [ ] Los endpoints están documentados y probados.

### Issue 10 --- Implementar categorías de movimientos

**Labels:** `backend`, `feature`\
**Dependencias:** Issues 2 y 7

#### Objetivo

Clasificar los movimientos por categorías.

#### Tareas

-   Definir categorías iniciales de ingresos y gastos.
-   Permitir consultar las categorías disponibles.
-   Permitir categorías personalizadas si forman parte del alcance
    acordado.
-   Validar el tipo de categoría.

#### Criterios de aceptación

-   [ ] Las categorías están tipadas y validadas.
-   [ ] Se impide usar categorías fuera del ámbito autorizado.
-   [ ] Existen pruebas de las reglas de categoría.

### Issue 11 --- Implementar registro de transacciones

**Labels:** `backend`, `feature`\
**Dependencias:** Issues 9 y 10

#### Objetivo

Crear y consultar movimientos financieros.

#### Tareas

-   Implementar creación, consulta, edición y anulación de movimientos.
-   Registrar importe, moneda, fecha, descripción, cuenta, categoría y
    tipo.
-   Validar relaciones y datos requeridos.
-   Utilizar precisión decimal para importes monetarios.

#### Criterios de aceptación

-   [ ] Las transacciones se guardan y consultan correctamente.
-   [ ] Los importes no se almacenan mediante `float`.
-   [ ] Las relaciones entre usuario, cuenta y categoría se validan.
-   [ ] Existen pruebas unitarias y de integración.

### Issue 12 --- Implementar reglas de consistencia financiera

**Labels:** `backend`, `testing`\
**Dependencia:** Issue 11

#### Objetivo

Asegurar que los totales financieros no sean engañosos.

#### Tareas

-   Definir el tratamiento de transferencias entre cuentas propias.
-   Definir el tratamiento de devoluciones y reversos.
-   Distinguir operaciones pendientes y confirmadas cuando corresponda.
-   Implementar cálculos de ingresos, gastos y flujo neto.
-   Documentar el tratamiento de múltiples monedas.

#### Criterios de aceptación

-   [ ] Una transferencia propia no se cuenta como ingreso ni gasto
    consolidado.
-   [ ] Las devoluciones y reversos no duplican ni distorsionan los
    totales.
-   [ ] Los cálculos tienen pruebas con casos límite.
-   [ ] Las reglas están documentadas.

## M3 --- Frontend y dashboards

### Issue 13 --- Inicializar frontend con React y TypeScript

**Labels:** `frontend`, `infra`

#### Objetivo

Crear la base de la aplicación web.

#### Tareas

-   Configurar Vite y TypeScript.
-   Configurar Tailwind CSS.
-   Definir enrutamiento.
-   Configurar cliente HTTP.
-   Organizar componentes y funcionalidades.
-   Configurar lint y formato.

#### Criterios de aceptación

-   [ ] El frontend inicia localmente.
-   [ ] La estructura está organizada por funcionalidades.
-   [ ] Puede comunicarse con FastAPI.
-   [ ] Las herramientas de calidad funcionan.

### Issue 14 --- Implementar interfaz de cuentas y movimientos

**Labels:** `frontend`, `feature`\
**Dependencias:** Issues 9, 10, 11 y 13

#### Objetivo

Permitir administrar cuentas y movimientos desde la interfaz.

#### Tareas

-   Crear vistas de cuentas.
-   Crear listado de movimientos.
-   Crear formulario de ingresos y gastos.
-   Mostrar estados de carga, éxito y error.
-   Validar formularios en el cliente sin reemplazar las validaciones
    del backend.

#### Criterios de aceptación

-   [ ] El usuario puede realizar las operaciones principales desde la
    interfaz.
-   [ ] Los errores se muestran claramente.
-   [ ] La interfaz se adapta a pantallas móviles y de escritorio.

### Issue 15 --- Implementar dashboard financiero

**Labels:** `frontend`, `analytics`\
**Dependencias:** Issues 12 y 13

#### Objetivo

Visualizar la situación financiera del usuario.

#### Tareas

-   Mostrar ingresos, gastos y flujo neto.
-   Mostrar evolución temporal.
-   Mostrar distribución por categoría.
-   Añadir filtros por período y cuenta.
-   Definir el comportamiento cuando no hay datos.

#### Criterios de aceptación

-   [ ] Los totales provienen de cálculos verificables.
-   [ ] Los filtros actualizan los datos correctamente.
-   [ ] Los estados vacíos y errores están contemplados.
-   [ ] Los datos de monedas diferentes no se suman sin una conversión
    explícita.

### Issue 16 --- Implementar presupuestos y seguimiento de gastos

**Labels:** `frontend`, `backend`, `feature`\
**Dependencias:** Issues 10, 12 y 15

#### Objetivo

Permitir definir presupuestos y comparar el gasto real con los límites.

#### Tareas

-   Crear presupuestos por período y categoría.
-   Consultar gasto acumulado.
-   Mostrar porcentaje utilizado y saldo presupuestario.
-   Definir reglas para avisos de presupuesto excedido.

#### Criterios de aceptación

-   [ ] Los cálculos respetan período, categoría y moneda.
-   [ ] Los presupuestos se aíslan por usuario.
-   [ ] Las alertas se generan a partir de reglas explícitas.

## M4 --- Importación de movimientos

### Issue 17 --- Diseñar formato de importación CSV

**Labels:** `backend`, `import`\
**Dependencias:** Issues 2 y 11

#### Objetivo

Definir un formato consistente para importar movimientos desde
extractos.

#### Tareas

-   Definir columnas requeridas y opcionales.
-   Definir formatos de fecha e importes.
-   Definir moneda y tipo de movimiento.
-   Crear archivos de ejemplo.
-   Documentar el tratamiento de filas inválidas.

#### Criterios de aceptación

-   [ ] Existe un CSV de ejemplo.
-   [ ] Existe un esquema documentado.
-   [ ] Los formatos aceptados y rechazados están definidos.

### Issue 18 --- Implementar importador CSV con validación

**Labels:** `backend`, `feature`\
**Dependencia:** Issue 17

#### Objetivo

Validar archivos antes de guardar movimientos.

#### Tareas

-   Recibir y validar archivos.
-   Analizar filas y convertirlas al modelo interno.
-   Informar errores por fila.
-   Permitir revisar el resultado antes de confirmar la importación.
-   Registrar el resultado de la ejecución.

#### Criterios de aceptación

-   [ ] Los archivos inválidos no generan importaciones parciales
    silenciosas.
-   [ ] El resultado informa filas aceptadas, rechazadas e ignoradas.
-   [ ] Los errores no exponen datos sensibles.
-   [ ] Existen pruebas para archivos válidos, inválidos y vacíos.

### Issue 19 --- Implementar deduplicación e historial de importaciones

**Labels:** `backend`, `data-integrity`\
**Dependencia:** Issue 18

#### Objetivo

Evitar que la misma información se registre varias veces.

#### Tareas

-   Guardar el historial de importaciones.
-   Detectar reintentos del mismo archivo.
-   Utilizar identificadores externos cuando existan.
-   Definir reglas de coincidencia para archivos sin identificadores.
-   Informar los movimientos duplicados detectados.

#### Criterios de aceptación

-   [ ] Reprocesar el mismo archivo no duplica movimientos.
-   [ ] El usuario puede consultar el resultado de cada importación.
-   [ ] Los criterios de coincidencia están documentados.
-   [ ] Los posibles duplicados ambiguos pueden revisarse sin eliminar
    movimientos automáticamente.

## Investigación paralela --- Proveedores de Open Finance

### Issue de investigación --- Evaluar proveedores para Colombia

**Labels:** `research`, `finance`, `integration`

Este trabajo puede iniciarse durante el MVP, pero no bloquea el motor
financiero.

#### Objetivo

Comparar proveedores que permitan conectar bancos y otras fuentes
financieras en Colombia.

#### Tareas

-   Comparar cobertura de bancos y tipos de cuentas.
-   Verificar soporte para saldos y movimientos históricos.
-   Consultar frecuencia de sincronización y límites.
-   Solicitar precios para el volumen inicial.
-   Verificar requisitos legales, técnicos y comerciales.
-   Investigar cobertura de Nequi, Daviplata, tarjetas de crédito y
    PayPal por separado.

#### Criterios de aceptación

-   [ ] Existe `docs/provider-research.md`.
-   [ ] Se documentan fuentes y fecha de consulta.
-   [ ] Se distinguen precios públicos, cotizaciones y estimaciones.
-   [ ] Se recomienda un proveedor o se documenta por qué aún no puede
    elegirse.
-   [ ] No se implementa una integración sin confirmar cobertura y
    condiciones.

## Labels iniciales recomendadas

-   `backend`
-   `frontend`
-   `database`
-   `security`
-   `infra`
-   `testing`
-   `feature`
-   `bug`
-   `documentation`
-   `research`
-   `priority: critical`
-   `priority: high`
-   `import`
-   `data-integrity`
-   `analytics`
-   `architecture`
-   `finance`
-   `integration`

## Definition of Done

Un issue se considera terminado cuando:

-   [ ] Cumple todos sus criterios de aceptación.
-   [ ] Incluye pruebas apropiadas.
-   [ ] Pasa las validaciones automáticas de CI.
-   [ ] Está documentado cuando corresponde.
-   [ ] No incluye secretos ni datos financieros reales.
-   [ ] Ha sido revisado y se integra mediante un pull request.

## Orden recomendado de ejecución

1.  Issues 1, 2 y 3: definir producto y reglas.
2.  Issues 4, 5, 6 y 7: preparar el entorno.
3.  Issues 8, 9, 10, 11 y 12: construir el motor financiero.
4.  Issues 13 y 14: construir la interfaz principal.
5.  Issues 15 y 16: crear dashboards y presupuestos.
6.  Issues 17, 18 y 19: habilitar importación.
7.  En paralelo, investigar proveedores de Open Finance sin comprometer
    aún una integración de producción.

**Principio rector:** primero confiabilidad financiera; después
automatización; finalmente inteligencia financiera.
