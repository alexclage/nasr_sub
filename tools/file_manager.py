import logging
import os, shutil

logger = logging.getLogger(__name__)

def file_deleter(file_path):

    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            os.rmdir(file_path)
    except Exception as e:
        logger.error('Failed to delete %s. Reason: %s' % (file_path, e))
        raise e