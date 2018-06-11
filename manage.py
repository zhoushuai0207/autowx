#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    project_path = os.path.dirname(os.getcwd())
    print(project_path)
    print(sys.path)
    if project_path not in sys.path:
        sys.path.append(project_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wxapp.settings")
    print(sys.path)
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
