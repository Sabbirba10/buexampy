#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exam.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?") from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
import imgkit

config = imgkit.config(
    wkhtmltoimage='/nix/store/...-wkhtmltopdf-*/bin/wkhtmltoimage'
)  # You may need to check the exact path with `which wkhtmltoimage`
imgkit.from_url('http://google.com', 'out.jpg', config=config)
