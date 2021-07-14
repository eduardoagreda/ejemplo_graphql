import os 

ip_run   = "0.0.0.0"
port_run = "8000"
settings = "app.settings"

run_code = f"gunicorn app.asgi:application --bind {ip_run}:{port_run} -k uvicorn.workers.UvicornWorker -e DJANGO_SETTINGS_MODULE={settings}"

os.system(run_code)