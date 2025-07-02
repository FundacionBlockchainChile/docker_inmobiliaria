# Inmobiliaria Docker App

Una aplicación web de ejemplo que demuestra el uso de Docker y Docker Compose con una arquitectura de tres capas:

- Frontend (Nginx)
- Backend (Python/Flask)
- Base de datos (PostgreSQL)

## Estructura del Proyecto

```
docker_inmobiliaria/
├── html/               # Frontend
│   └── index.html     # Página web principal
├── nginx/             # Configuración de Nginx
│   └── Dockerfile     # Dockerfile para el servidor web
├── backend/           # API REST
│   ├── app.py        # Aplicación Flask
│   ├── requirements.txt # Dependencias de Python
│   └── Dockerfile    # Dockerfile para el backend
└── docker-compose.yml # Orquestación de servicios
```

## Requisitos

- Docker
- Docker Compose

## Instalación y Ejecución

1. Clonar el repositorio:

```bash
git clone [URL_DEL_REPOSITORIO]
cd docker_inmobiliaria
```

2. Iniciar los servicios:

```bash
docker-compose up -d
```

3. Acceder a la aplicación:

- Frontend: http://localhost:8080
- API: http://localhost:5001/api/propiedades

## Arquitectura

### Frontend (Nginx)

- Sirve una página web estática
- Se comunica con el backend a través de la API REST
- Puerto: 8080

### Backend (Python/Flask)

- API REST para gestionar propiedades
- Se conecta con PostgreSQL
- Puerto: 5001
- Endpoints:
  - GET /api/propiedades: Lista todas las propiedades

### Base de Datos (PostgreSQL)

- Almacena los datos de las propiedades
- Persistencia mediante volúmenes de Docker
- Puerto: 5432 (interno)

## Comunicación entre Servicios

Los servicios se comunican entre sí de la siguiente manera:

1. El frontend hace peticiones HTTP al backend a través de la API REST
2. El backend procesa las peticiones y se comunica con PostgreSQL
3. PostgreSQL almacena y recupera los datos solicitados
4. Los datos fluyen de vuelta al frontend a través de la API

## Desarrollo

Para modificar la base de datos, puedes conectarte usando:

```bash
docker exec -it docker_inmobiliaria-db-1 psql -U admin -d inmobiliaria
```

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request
