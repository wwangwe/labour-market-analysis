from .base import *

if config('PRODUCTION_ENV', cast=bool):
    from .production import *
else:
    from .development import *
