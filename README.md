# Место

Небольшой демонстрационный магазин на Django: каталог с фильтрацией, корзина в сессии, оформление демо-заказа и админка товаров.

## Запуск в Docker

```powershell
docker compose up --build
```

Откройте http://localhost:8000. Контейнер автоматически применяет миграции и добавляет стартовые товары. Данные SQLite сохраняются в Docker volume `shop_data`.

## Проверки

```powershell
python manage.py test
```

## Публикация в GHCR

Workflow `.github/workflows/ghcr.yml` запускает тесты, а затем публикует `ghcr.io/<owner>/<repository>` при push в `main`, публикации тега `v*.*.*` или ручном запуске workflow. Для публикации у репозитория должны быть разрешены GitHub Actions и запись пакетов.