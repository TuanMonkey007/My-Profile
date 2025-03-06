import uuid
import os
from appCore.constants import *

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(SERVER_CONFIG_UPLOAD_FOLDER_IMAGE, filename)