from jinja2 import Environment, PackageLoader
import parsley
from ometa.runtime import ParseError, EOFError

from .log import get_logger


html_env = Environment(loader=PackageLoader('svpm', 'html_templates'))


def convert_usfm_to_html(config_path):
    pass
