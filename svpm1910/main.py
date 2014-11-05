import os
import sys
import argparse

from .log import get_logger
from .html import convert_usfm_to_html

logger = get_logger()


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Configuration file")
    parser.add_argument("--html", action="store_true",
                            help="Convert USFM to HTML format")
    parser.add_argument("--latex", action="store_true",
                            help="Convert USFM to LaTeX format")
    parser.add_argument("--osis", action="store_true",
                            help="Convert USFM to OSIS format")
    args = parser.parse_args()

    if not args.config:
        parser.print_help()
        sys.exit(1)

    config_path = os.path.abspath(args.config)

    if not os.path.exists(config_path):
        logger.error("Configuration doesn't exist: %s" % config_path)
        sys.exit(1)

    if args.html:
        convert_usfm_to_html(config_path)
