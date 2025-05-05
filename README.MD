# 🚕 Urban Routes - Pruebas Automatizadas

Este repositorio contiene pruebas automatizadas para verificar la funcionalidad de la plataforma **Urban Routes**, incluyendo la selección de tarifa, ingreso de teléfono, adición de tarjeta de crédito, y solicitudes adicionales como manta, pañuelos y helados.

---

## 🗂 Estructura del Proyecto

```
qa-project-Urban-Routes-es/
│
├── data.py               # Datos de prueba: URL, direcciones, teléfono, tarjeta, mensaje
├── main.py               # Lógica de pruebas y clases de Page Object + tests con pytest
├── phone_code.py         # Función retrieve_phone_code para extraer el código de verificación
└── README.md             # Documentación de uso y estructura
```

### 📌 Contenido de los Archivos

---

#### `data.py`

Contiene todos los **datos estáticos** necesarios para las pruebas:

- `urban_routes_url`: URL del entorno de prueba
- `address_from`, `address_to`: Dirección de origen y destino
- `phone_number`: Teléfono de prueba
- `card_number`, `card_code`: Datos simulados de una tarjeta de crédito
- `message_for_driver`: Mensaje que se envía al conductor

---

#### `main.py`

Contiene:

- La clase `UrbanRoutesPage`: encapsula los selectores, acciones y verificaciones de la interfaz.
- La clase `TestUrbanRoutes`: define las pruebas unitarias organizadas por flujo:
  - Configura la ruta
  - Selecciona la tarifa "Comfort"
  - Ingresa número de teléfono y confirma con código
  - Añade tarjeta de crédito
  - Envía mensaje al conductor
  - Solicita manta y pañuelos
  - Añade helados
  - Verifica aparición del modal "Buscar automóvil"

Usa `pytest` y `selenium` con WebDriver de Chrome.

---

#### `phone_code.py`

Contiene la función:

```python
def retrieve_phone_code(driver) -> str
```

Que extrae el **código de verificación de teléfono** interceptando los logs de red (performance logs) del navegador, necesario para validar el login vía SMS.

---

## ⚙️ Instalación

1. Clona el repositorio:

```
git clone https://github.com/tu_usuario/urban_routes_tests.git
cd urban_routes_tests
```

2. Crea y activa un entorno virtual:

```
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```
pip install -r requirements.txt
```

---

## ▶️ Ejecución de Pruebas

Asegúrate de tener el navegador y WebDriver configurados correctamente (por ejemplo, ChromeDriver si usas Chrome).

Ejecuta las pruebas con:

```
pytest tests/
```

O para ver los resultados con más detalle:

```
pytest -v tests/
```

---

## ✅ Funcionalidades Probadas
- Ingreso del campo "Desde"
- Ingreso del campo "Hasta"
- Selección de "Pedir taxi"
- Selección de tarifa "Comfort"
- Ingreso de número de teléfono
- Ingreso de datos de tarjeta de crédito
- Mensaje adicional para el conductor
- Selección de servicios extra:
  - Manta y Pañuelos
  - Helados

---

## 📦 Requisitos

- Python 3.8+
- `selenium`
- `pytest`

---

## ✍️ Autor

- Frankin Estiven Suarez Minayo
- Sprint 8 Tripleten

---
