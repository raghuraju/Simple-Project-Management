import os

from django.conf import settings

def get_upload_to_path(suffix):
	return os.path.join(settings.MEDIA_ROOT, suffix) 

