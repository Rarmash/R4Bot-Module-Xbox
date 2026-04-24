# R4Bot-Module-Xbox

Внешний Xbox-модуль для [R4Bot](https://github.com/Rarmash/R4Bot).

## Что делает
- добавляет `/xbox stats`
- добавляет `/xbox connect`
- привязывает Xbox-профиль к Discord-учётной записи
- показывает основную статистику Xbox-профиля
- использует runtime services из `bot.r4_services`

## Секреты
API-ключ Xbox хранится в:

```json
{
  "api_key": "YOUR_XBOX_API_KEY"
}
```

Файл должен лежать в:

```txt
config/secrets/xbox.json
```

## Требования
- R4Bot `>= 2.0`
- runtime context с `bot.r4_services`
- сервисы `firebase`, `secrets`
- установленный пакет `xbox-python-api`

## Структура
- `module.json` — метаданные модуля
- `cog.py` — Discord cog
- `xbox.secrets.example.json` — пример файла секретов
- `requirements.txt` — зависимости для IDE и локальной проверки

## Установка в R4Bot
```powershell
python manage_modules.py install github:Rarmash/R4Bot-Module-Xbox@master --enable
```

## Разработка
Для нормальной подсветки импортов в IDE и локальной проверки модуля рекомендуется установить зависимости:

```powershell
python -m pip install -r requirements.txt
```



