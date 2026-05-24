# Sistema de Gestión de Base de Datos para Centro Comercial

[![Access](https://img.shields.io/badge/Database-MS%20Access%20%28.accdb%29-blue?style=flat-square&logo=microsoftaccess)](https://products.office.com/access)
[![SQL](https://img.shields.io/badge/Language-SQL-orange?style=flat-square)](https://en.wikipedia.org/wiki/SQL)
[![Mermaid Diagrams](https://img.shields.io/badge/Diagrams-Mermaid%20JS-success?style=flat-square)](https://mermaid.js.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](file:///C:/Users/elitebook%20hp/Desktop/Compu%20III/Trabajo%203/Centro-comercial/LICENSE)

Este repositorio contiene la solución completa de diseño e implementación de una base de datos centralizada y robusta para la **Gestión Integral de Arriendos, Locales y Personal** de un centro comercial de gran envergadura. 

El proyecto resuelve la problemática de fragmentación de datos de la administración del mall (anteriormente operada con planillas Excel desarticuladas y archivadores físicos), consolidando toda la operación en una única fuente de verdad técnica y comercial bajo normas rigurosas de integridad relacional.

---

## Estructura del Repositorio

El repositorio está organizado con un enfoque profesional de ingeniería de software y bases de datos:

*   **[`Centro_comercial.accdb`](file:///C:/Users/elitebook%20hp/Desktop/Compu%20III/Trabajo%203/Centro-comercial/Centro_comercial.accdb)**: Base de datos física totalmente configurada y funcional en Microsoft Access. Contiene las tablas normalizadas, relaciones complejas con integridad referencial y las llaves primarias/foráneas correspondientes.
*   **[`Centro_comercial_ER.md`](file:///C:/Users/elitebook%20hp/Desktop/Compu%20III/Trabajo%203/Centro-comercial/Centro_comercial_ER.md)**: Documentación conceptual, lógica y física detallada. Incluye diagramas interactivos en Mermaid (Notación de Chen y Patas de Gallo), diccionario de datos completo y los esquemas DDL en SQL (3NF).
*   **[`Tarea_DIA_Valenzuela_Nuche.dia`](file:///C:/Users/elitebook%20hp/Desktop/Compu%20III/Trabajo%203/Centro-comercial/Tarea_DIA_Valenzuela_Nuche.dia)**: Archivo original del modelado Entidad-Relación conceptual en formato comprimido de la herramienta de diagramación DIA.
*   **[`Descripción_del_problema.docx`](file:///C:/Users/elitebook%20hp/Desktop/Compu%20III/Trabajo%203/Centro-comercial/Descripci%C3%B3n_del_problema.docx)**: Documento de requerimientos originales del negocio que detalla los dolores operacionales de la administración, las entidades a modelar y las reglas de negocio críticas.

---

## Arquitectura de la Base de Datos

El diseño de la base de datos se estructuró a partir de los requerimientos de negocio y se refinó hasta lograr una arquitectura física optimizada.

### 1. Modelo Conceptual (Notación de Chen)
Representa las entidades esenciales y sus interacciones de negocio.
*   **Entidades Fuertes**: `Local` (inmuebles), `Empresa` (arrendatarios) y `Servicio` (suministros básicos y de valor agregado).
*   **Entidades Débiles**: `Empleado` (dependencia existencial de la empresa contratante).
*   **Jerarquías (Especializaciones Disyuntas Totales)**:
    *   **Locales**: Especializados en `Local Comercial`, `Local de Esparcimiento` (con aforo de seguridad) y `Local de Comidas` (con especialidades gastronómicas).
    *   **Personal**: Clasificación en `Vendedor` y `Jefe de Local`.

### 2. Modelo Lógico Relacional (Notación de Patas de Gallo)
Resuelve las herencias mediante la estrategia **TPT (Table Per Type)**, permitiendo una correspondencia 1:1 limpia e indexada entre superclases y subclases, y normaliza todos los atributos compuestos y multivaluados (tales como características de locales, fechas de pago y facturación de servicios dinámicos) en tablas satélites independientes en **Tercera Forma Normal (3NF)**.

> [!NOTE]
> Para visualizar el diagrama relacional completo en formato interactivo, revisa la sección 3 del archivo de documentación **[`Centro_comercial_ER.md`](file:///C:/Users/elitebook%20hp/Desktop/Compu%20III/Trabajo%203/Centro-comercial/Centro_comercial_ER.md#L217)**.

---

## Reglas de Negocio Implementadas

El modelo físico garantiza a nivel de esquema e integridad referencial el cumplimiento estricto de las políticas corporativas del mall:

*   **Lealtad y Exclusividad de Contratos**: Una empresa externa puede arrendar múltiples locales (relación 1:N), pero cada local individual está limitado a un único arrendatario activo a la vez para evitar colisiones contractuales.
*   **Seguridad de Personal y Operaciones**: Un empleado pertenece contractualmente a una única empresa y solo puede prestar servicios físicos en un local arrendado por esa misma organización. El diseño de llaves foráneas cruzadas previene el 'préstamo' no autorizado de personal entre empresas competidoras dentro del recinto.
*   **Integridad de Infraestructura Física**: Se aplican restricciones a nivel de columna (`CHECK`) para asegurar que no existan locales registrados con superficie cero o costos de arriendo base negativos, protegiendo la valoración comercial del mall.

---

## Tecnologías y Visualización

### Requisitos del Sistema
1.  **Base de Datos**: Microsoft Access 2010 o superior (para abrir y operar el archivo `.accdb`).
2.  **Visualizador Markdown**: Editor con soporte para Mermaid JS (como VS Code con extensión *Markdown Preview Mermaid Support*, u Obsidian) para renderizar los diagramas interactivos en `Centro_comercial_ER.md`.

> [!TIP]
> Si estás visualizando la documentación desde GitHub, la plataforma renderizará automáticamente los bloques de código `mermaid` como diagramas vectoriales interactivos y de alta resolución.
