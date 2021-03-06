#!/usr/bin/python

import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "se.settings")
    from django.core.management import execute_from_command_line
    import se.startup as startup
    startup.run()
    execute_from_command_line(sys.argv)
