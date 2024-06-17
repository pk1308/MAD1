import os
import sys

from loguru import logger
from shared.functions import (deploy_mkdocs, get_git_status_files,
                              update_my_docs)

logger.remove()
logger.add(sys.stdout, colorize=True, format="{time} | {level} | {message}")



if __name__ == "__main__":

    repo_path = os.getcwd()
    files = get_git_status_files(repo_path)
    logger.info(files)

    try:
        files = get_git_status_files(repo_path)
        update_my_docs()
        logger.info("successful update")

    except Exception as e:
        logger.error(f"cant update {e}")
    logger.info("deploy mk docs ")

    deploy_mkdocs()
    logger.info("deployed mk docs ")
