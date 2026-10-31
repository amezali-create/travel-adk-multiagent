# Travel ADK Multiagent

Laboratorio UCV de sistema multiagente de viajes con Google ADK.

[![CI Pipeline](https://github.com/amezali-create/travel-adk-multiagent/actions/workflows/ci.yml/badge.svg)](https://github.com/amezali-create/travel-adk-multiagent/actions/workflows/ci.yml)

## Agentes

- Travel Coordinator Agent
- Web Search Agent
- Itinerary Agent
- Budget Agent
- Risk Reviewer Agent
- Local Culture Agent (reto del laboratorio)

```
Usuario
   │
   v
Travel Coordinator Agent
   │-- Web Search Agent      (Google Search)
   │-- Itinerary Agent
   │-- Budget Agent          (tool: estimate_trip_budget)
   │-- Risk Reviewer Agent   (tool: assess_basic_travel_risks)
   │-- Local Culture Agent   (tool: get_local_culture_info)
   v
Respuesta final consolidada
```

### Reto: Local Culture Agent

Recomienda platos típicos, explica costumbres locales y sugiere frases útiles para el viajero.
Es subagente del coordinador y usa la tool `get_local_culture_info`, con datos de Cusco, Lima,
Arequipa, Buenos Aires y París. Si el destino no está en la base, la tool devuelve
`not_found` y el agente responde con conocimiento general avisando que debe verificarse.

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate        # En Git Bash de Windows: source .venv/Scripts/activate
pip install poetry
poetry install
```

## Variables de entorno

Crear archivo `.env` a partir de `.env.example`:

```bash
GOOGLE_API_KEY="TU_API_KEY"
```

El archivo `.env` está en `.gitignore`: nunca se sube a GitHub.

## Ejecutar agente por consola

```bash
poetry run adk run travel_assistant
```

## Ejecutar agente web

```bash
poetry run adk web --port 8000
```

Abrir:

```text
http://localhost:8000
```

## Ejecutar pruebas

```bash
poetry run pytest
```

## Ejecutar lint

```bash
poetry run ruff check .
```

## Modelo utilizado

Los agentes usan `gemini-3.1-flash-lite` (el modelo Flash normal respondía con errores 503 por alta demanda y tiene un límite diario bajo en el plan gratuito). La guía original indicaba `gemini-2.0-flash`, pero
Google retiró ese modelo el 1 de junio de 2026, por lo que ya no responde.

## Flujo Git

```text
feature/travel-multiagent  ->  develop  ->  main
```

En cada Pull Request y en cada push a `develop` o `main` se ejecuta GitHub Actions: Ruff,
Pytest con cobertura y análisis de SonarQube Cloud.
