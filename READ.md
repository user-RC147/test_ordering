# Система обліку замовлень

Тестове завдання — модуль обліку замовлень для бізнес-системи.

Реалізовано у двох варіантах:
- **Django Monolith** — серверний рендеринг (Jinja + Tailwind): [репозиторій](https://github.com/user-RC147/test_ordering.git)
- **Django REST Framework + Vue 3 SPA** — цей репозиторій: [репозиторій](https://github.com/user-RC147/test_order_rest.git)

---

## Стек технологій

**Бекенд:**
- Python 3.14
- Django 6.0
- Django REST Framework
- PostgreSQL
- Docker / docker-compose
- drf-spectacular (Swagger / OpenAPI)

**Фронтенд:**
- Vue 3 (Composition API, `<script setup>`)
- Pinia
- Vue Router
- Axios
- Tailwind CSS v4

---

## Реалізований функціонал

- Створення клієнта, товару, замовлення
- Список замовлень із фільтрацією по клієнту
- Автоматичний розрахунок суми замовлення на основі товарів і кількості
- Перегляд деталей замовлення
- Документування REST API через Swagger (OpenAPI)
- Запуск через Docker

**Бізнес-правила:**
- Не можна створити замовлення без клієнта
- У замовленні має бути хоча б один товар
- Сума розраховується автоматично через `@property` на рівні моделі

---

## Архітектурні рішення

### Бекенд — Clean Architecture

Кожен модуль ізольований і має чіткий ланцюжок відповідальності:

```
Model → Repository → Selector → Service → DTO → Serializer → ViewSet
```

| Шар | Відповідальність |
|---|---|
| Model | Опис структури таблиці БД |
| Repository | Запис даних (create, update, delete) |
| Selector | Читання даних (get, filter, exists) |
| Service | Бізнес-логіка та оркестрація |
| DTO | Передача даних між шарами |
| Serializer | Валідація вхідних даних від клієнта |
| ViewSet | HTTP вхідна точка |

**Чому такий підхід:** кожен шар має єдину відповідальність. Service не знає про HTTP. Repository не читає дані. View не містить бізнес-логіки. Це дозволяє легко тестувати і розширювати кожен шар окремо.

### Фронтенд — Модульна архітектура

Потік даних: `View → Store → API → Axios → Django`

| Шар | Відповідальність |
|---|---|
| `api/axios.js` | Глобальний Axios клієнт (baseURL) |
| `modules/orderings/api/` | Функції запитів до Django |
| `modules/orderings/stores/` | Pinia stores (стан + try/catch) |
| `modules/orderings/components/` | Дурні компоненти (props/emits) |
| `modules/orderings/views/` | Сторінки-екрани (ініціатори даних) |

---

## Структура проекту

```
test_order_rest/
├── backend/
│   ├── apps/
│   │   └── orderings/
│   │       ├── models/
│   │       │   ├── client_model.py
│   │       │   ├── product_model.py
│   │       │   ├── order_model.py
│   │       │   └── order_item_model.py
│   │       ├── dto/
│   │       │   ├── client_dto.py
│   │       │   ├── product_dto.py
│   │       │   ├── order_dto.py
│   │       │   └── order_item_dto.py
│   │       ├── repositories/
│   │       │   ├── client_repo.py
│   │       │   ├── product_repo.py
│   │       │   ├── order_repo.py
│   │       │   └── order_item_repo.py
│   │       ├── selectors/
│   │       │   ├── client_selector.py
│   │       │   ├── product_selector.py
│   │       │   └── order_selector.py
│   │       ├── services/
│   │       │   ├── client_service.py
│   │       │   ├── product_service.py
│   │       │   └── order_service.py
│   │       └── api/
│   │           ├── serializers/
│   │           │   ├── client_serializer.py
│   │           │   ├── product_serializer.py
│   │           │   ├── order_serializer.py
│   │           │   └── order_item_serializer.py
│   │           └── views/
│   │               ├── client_view.py
│   │               ├── product_view.py
│   │               └── order_view.py
│   ├── config/
│   │   ├── settings.py
│   │   └── urls.py
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   └── src/
│       ├── api/
│       │   └── axios.js
│       ├── modules/
│       │   └── orderings/
│       │       ├── api/
│       │       │   ├── client_api.js
│       │       │   ├── product_api.js
│       │       │   └── order_api.js
│       │       ├── stores/
│       │       │   ├── useClientStore.js
│       │       │   ├── useProductStore.js
│       │       │   └── useOrderStore.js
│       │       ├── components/
│       │       │   ├── CreateClientModal.vue
│       │       │   └── CreateProductModal.vue
│       │       └── views/
│       │           ├── orders/
│       │           ├── clients/
│       │           └── products/
│       ├── router/
│       │   └── index.js
│       └── main.js
│
├── Dockerfile
├── docker-compose.yml
└── .dockerignore
```

---

## API Endpoints

| Метод | URL | Опис |
|---|---|---|
| GET | `/api/orderings/clients/` | Список клієнтів |
| POST | `/api/orderings/clients/` | Створити клієнта |
| GET | `/api/orderings/products/` | Список товарів |
| POST | `/api/orderings/products/` | Створити товар |
| GET | `/api/orderings/orders/` | Список замовлень |
| GET | `/api/orderings/orders/?client_id=1` | Замовлення по клієнту |
| POST | `/api/orderings/orders/` | Створити замовлення |
| GET | `/api/orderings/orders/{id}/` | Деталі замовлення |

Повна документація: `http://localhost:8000/api/docs/swagger/`

---

## Інструкція запуску

### Через Docker (рекомендовано)

**1. Клонуй репозиторій:**
```bash
git clone https://github.com/user-RC147/test_order_rest.git
cd test_order_rest
```

**2. Створи файл `backend/.env`:**
```env
SECRET_KEY=django-insecure-6wsz(+)9p)e$c1q5vno=g_=c71ubchb4$a1)1fq4gaahwt*b-0
ALLOWED_HOSTS=127.0.0.1,localhost
DEBUG=True
ENGINE=postgres
DB_NAME=order_rest_db
DB_USER=admin
DB_PASSWORD=admin
DB_HOST=db
DB_PORT=5432
```

**3. Запусти:**
```bash
docker compose up --build
```

**4. Створи суперюзера (в окремому терміналі):**
```bash
docker compose exec web python manage.py createsuperuser
```

**5. Відкрий у браузері:**
- Фронтенд: http://localhost:5173
- Swagger: http://localhost:8000/api/docs/swagger/
- Django Admin: http://localhost:8000/admin/

### Зупинити контейнери:
```bash
docker compose down
```

### Видалити дані БД:
```bash
docker compose down -v
```

---

### Локальний запуск (без Docker)

**Бекенд:**
```bash
cd backend
python -m venv venvOrderAccounting/venvOrderRest
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Фронтенд:**
```bash
cd frontend
npm install
npm run dev
```
