import os
import collections
import logging as logging
import logging.config
import yaml
import utility_funcs.search as search

"""
Get configuration from yaml file.  Sets up logging streams as defined in logger.yaml.

Returned values:

root    -   Root logger stream. Standard log stream sent to console and output file.
console -   Logs only to the console
logger  -   For convenience, this is the same as the root stream.

A particular output stream can be gotten by Logger.getLogger("<name>"), where <name>
is the definition of the stream from the YAML file. If it happens that <name> is not
defined in the file, it seems to default to the root stream.
"""

logger = None
root = None
console = None

def update_dict(d, u):
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            default = v.copy()
            default.clear()
            r = update_dict(d.get(k, default), v)
            d[k] = r
        else:
            d[k] = v
    return d

def get_loggers():
    global logger, root, console
    logger =logging.getLogger("root")
    root =logging.getLogger("root")
    console = logging.getLogger("console")

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG',
    override=None
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    path = search.search_for_profile(path)
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        if override is not None:
            config = update_dict(config, override)
        logging.config.dictConfig(config)
        get_loggers()
        logger.info("Using logging configuration file %s"%(path))
    else:
        logging.basicConfig(level=default_level)
        get_loggers()
        logger.info("Unable to open logging configuration file %s, using basic logging"%(path))

# -- Don't need to do configuration more than once...
#if logger is None:
    #setup_logging()

"""
root.fatal("FATAL to root -- This should go to everyone...")
root.error("Error to root -- This should go to everyone...")
root.warning("Warning to root -- This should go to everyone...")
root.info("Info to root -- This should go to everyone...")
root.debug("debug level to root")

console.fatal("FATAL to my_module -- This should go to everyone...")
console.error("Error to my_module -- This should go to everyone...")
console.warning("Warning to my_module -- This should go to everyone...")
console.info("Info to my_module -- This should go to everyone...")
console.debug("debug level to my_module")

undefined = logging.getLogger("undefined")
undefined.fatal("FATAL to xyzzy -- This is an undefined logger...")
undefined.error("Error to xyzzy -- This is an undefined logger...")
undefined.warning("Warning to xyzzy -- This is an undefined logger...")
undefined.info("Info to xyzzy -- This is an undefined logger...")
undefined.debug("Debug level to xyzzy -- This is an undefined logger...")

"""

