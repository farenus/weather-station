# weather-station

firmware micropython dla stacji pogodowej opartej na ESP32-S3, wysyłający pomiary do API.

## Konfiguracja

Skopiuj `src/secrets_config.example.py` do `src/secrets_config.py` i uzupełnij zmienne.

## Zależności

Biblioteka `requests` obsługuje komunikację HTTP.

```bash
uv run mpremote mip install requests
```

## Podziękowania

Sterownik czujnika pochodzi z projektu [robert-hh/BME280](https://github.com/robert-hh/BME280) na licencji MIT.
