# django-htmx-tailwind

A basic Django template which uses HTMX and Tailwind

## Instalation

### - Download Tailwind CLI:

Download the [tailwind executable](https://github.com/tailwindlabs/tailwindcss/releases) for your platform. If you are on macOS or Linux you need to give the file execute permissions.

```bash
# CLI example for Linux
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64
chmod +x tailwindcss-linux-x64
mv tailwindcss-linux-x64 tailwindcss
```

### - Run the Tailwind watcher

```bash
./tailwindcss -i static/css/input.css -o static/css/output.css --watch
```

### - Run Django's server

```bash
# Create a virtualenv
virtualenv env

# Enable environment

#Linux
source .env/bin/activate
#Windows
./env/Scripts/activate

# Instal dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver
```

## Production

Before running your website in production, you should minfy the Tailwind output to reduce the file size that needs to be downloaded

```bash
./tailwindcss -i static/css/input.css -o static/css/output.css --minify
```
