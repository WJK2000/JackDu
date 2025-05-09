
import logging, sys, pathlib
LOG_DIR = pathlib.Path('logs')
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[logging.FileHandler(LOG_DIR/'run.log', encoding='utf-8'),
              logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger('mini')
