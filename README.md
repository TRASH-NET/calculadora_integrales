# Calculadora de Integración Numérica

Aplicación web para resolver integrales mediante métodos de aproximación numérica utilizando:

- Backend en FastAPI
- Frontend en React + Vite

---

# Tecnologías utilizadas

## Backend

- Python 3.14
- FastAPI
- SymPy
- Uvicorn

## Frontend

- React 19
- TypeScript
- Vite
- TailwindCSS
- Recharts
- shadcn/ui

---

# Estructura del proyecto

```txt
project/
│
├── backend/
│   ├── requirements.txt
│   ├── main.py
│   └── ...
│
├── frontend/
│   ├── package.json
│   ├── src/
│   └── ...
│
└── README.md
```

---

# Requisitos previos

Instalar:

- Python 3.14
- Node.js
- npm (incluido con Node)

Verificar instalaciones:

```bash
python --version
node --version
npm --version
```

---

# Configuración del Backend

Ir a la carpeta backend:

```bash
cd backend
```

## Crear entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar servidor FastAPI

```bash
uvicorn main:app --reload
```

Servidor disponible en:

```txt
http://localhost:8000
```

Documentación automática:

```txt
http://localhost:8000/docs
```

---

# Configuración del Frontend

Abrir otra terminal y entrar al frontend:

```bash
cd frontend
```

---

## Instalar dependencias

```bash
npm install
```

---

## Configurar variables de entorno

Crear archivo:

```txt
frontend/.env
```

Contenido:

```env
VITE_BASE_URL=http://localhost:8000/
```

---

## Ejecutar frontend

```bash
npm run dev
```

Aplicación disponible en:

```txt
http://localhost:5173
```

---

# Métodos numéricos implementados

- Regla del Trapecio
- Regla de Simpson 1/3
- Regla de Simpson 3/8
- Simpson Abierto
- Regla de Boole

---

# Características

- Evaluación simbólica de funciones
- Visualización gráfica interactiva
- Representación de intervalos de aproximación
- Tabla detallada de iteraciones
- Cálculo automático de áreas parciales
- Tooltips matemáticos interactivos

---

# Scripts útiles

## Frontend

### Iniciar entorno de desarrollo

```bash
npm run dev
```

### Generar build de producción

```bash
npm run build
```

### Previsualizar build

```bash
npm run preview
```

---

# Notas importantes

- El backend debe estar ejecutándose antes de iniciar el frontend.
- La URL del backend puede modificarse desde el archivo `.env`.
- Algunas expresiones matemáticas inválidas pueden generar errores de evaluación en SymPy.

---

# Autor

Proyecto desarrollado con FastAPI + React para integración numérica y visualización matemática interactiva.