!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
BaseConfigurator	/usr/lib/python3.4/logging/config.py	/^class BaseConfigurator(object):$/;"	c
CONVERT_PATTERN	/usr/lib/python3.4/logging/config.py	/^    CONVERT_PATTERN = re.compile(r'^(?P<prefix>[a-z]+):\/\/(?P<suffix>.*)$')$/;"	v	class:BaseConfigurator
ConfigSocketReceiver	/usr/lib/python3.4/logging/config.py	/^    class ConfigSocketReceiver(ThreadingTCPServer):$/;"	c	function:listen
ConfigStreamHandler	/usr/lib/python3.4/logging/config.py	/^    class ConfigStreamHandler(StreamRequestHandler):$/;"	c	function:listen
ConvertingDict	/usr/lib/python3.4/logging/config.py	/^class ConvertingDict(dict, ConvertingMixin):$/;"	c
ConvertingList	/usr/lib/python3.4/logging/config.py	/^class ConvertingList(list, ConvertingMixin):$/;"	c
ConvertingMixin	/usr/lib/python3.4/logging/config.py	/^class ConvertingMixin(object):$/;"	c
ConvertingTuple	/usr/lib/python3.4/logging/config.py	/^class ConvertingTuple(tuple, ConvertingMixin):$/;"	c
DEFAULT_LOGGING_CONFIG_PORT	/usr/lib/python3.4/logging/config.py	/^DEFAULT_LOGGING_CONFIG_PORT = 9030$/;"	v
DIGIT_PATTERN	/usr/lib/python3.4/logging/config.py	/^    DIGIT_PATTERN = re.compile(r'^\\d+$')$/;"	v	class:BaseConfigurator
DOT_PATTERN	/usr/lib/python3.4/logging/config.py	/^    DOT_PATTERN = re.compile(r'^\\.\\s*(\\w+)\\s*')$/;"	v	class:BaseConfigurator
DictConfigurator	/usr/lib/python3.4/logging/config.py	/^class DictConfigurator(BaseConfigurator):$/;"	c
IDENTIFIER	/usr/lib/python3.4/logging/config.py	/^IDENTIFIER = re.compile('^[a-z_][a-z0-9_]*$', re.I)$/;"	v
INDEX_PATTERN	/usr/lib/python3.4/logging/config.py	/^    INDEX_PATTERN = re.compile(r'^\\[\\s*(\\w+)\\s*\\]\\s*')$/;"	v	class:BaseConfigurator
RESET_ERROR	/usr/lib/python3.4/logging/config.py	/^RESET_ERROR = errno.ECONNRESET$/;"	v
Server	/usr/lib/python3.4/logging/config.py	/^    class Server(threading.Thread):$/;"	c	function:listen
WORD_PATTERN	/usr/lib/python3.4/logging/config.py	/^    WORD_PATTERN = re.compile(r'^\\s*(\\w+)\\s*')$/;"	v	class:BaseConfigurator
__getitem__	/usr/lib/python3.4/logging/config.py	/^    def __getitem__(self, key):$/;"	m	class:ConvertingDict	file:
__getitem__	/usr/lib/python3.4/logging/config.py	/^    def __getitem__(self, key):$/;"	m	class:ConvertingList	file:
__getitem__	/usr/lib/python3.4/logging/config.py	/^    def __getitem__(self, key):$/;"	m	class:ConvertingTuple	file:
__init__	/usr/lib/python3.4/logging/config.py	/^        def __init__(self, host='localhost', port=DEFAULT_LOGGING_CONFIG_PORT,$/;"	m	class:listen.ConfigSocketReceiver
__init__	/usr/lib/python3.4/logging/config.py	/^        def __init__(self, rcvr, hdlr, port, verify):$/;"	m	class:listen.Server
__init__	/usr/lib/python3.4/logging/config.py	/^    def __init__(self, config):$/;"	m	class:BaseConfigurator
_create_formatters	/usr/lib/python3.4/logging/config.py	/^def _create_formatters(cp):$/;"	f
_handle_existing_loggers	/usr/lib/python3.4/logging/config.py	/^def _handle_existing_loggers(existing, child_loggers, disable_existing):$/;"	f
_install_handlers	/usr/lib/python3.4/logging/config.py	/^def _install_handlers(cp, formatters):$/;"	f
_install_loggers	/usr/lib/python3.4/logging/config.py	/^def _install_loggers(cp, handlers, disable_existing):$/;"	f
_listener	/usr/lib/python3.4/logging/config.py	/^_listener = None$/;"	v
_resolve	/usr/lib/python3.4/logging/config.py	/^def _resolve(name):$/;"	f
_strip_spaces	/usr/lib/python3.4/logging/config.py	/^def _strip_spaces(alist):$/;"	f
add_filters	/usr/lib/python3.4/logging/config.py	/^    def add_filters(self, filterer, filters):$/;"	m	class:DictConfigurator
add_handlers	/usr/lib/python3.4/logging/config.py	/^    def add_handlers(self, logger, handlers):$/;"	m	class:DictConfigurator
allow_reuse_address	/usr/lib/python3.4/logging/config.py	/^        allow_reuse_address = 1$/;"	v	class:listen.ConfigSocketReceiver
as_tuple	/usr/lib/python3.4/logging/config.py	/^    def as_tuple(self, value):$/;"	m	class:BaseConfigurator
cfg_convert	/usr/lib/python3.4/logging/config.py	/^    def cfg_convert(self, value):$/;"	m	class:BaseConfigurator
common_logger_config	/usr/lib/python3.4/logging/config.py	/^    def common_logger_config(self, logger, config, incremental=False):$/;"	m	class:DictConfigurator
configure	/usr/lib/python3.4/logging/config.py	/^    def configure(self):$/;"	m	class:DictConfigurator
configure_custom	/usr/lib/python3.4/logging/config.py	/^    def configure_custom(self, config):$/;"	m	class:BaseConfigurator
configure_filter	/usr/lib/python3.4/logging/config.py	/^    def configure_filter(self, config):$/;"	m	class:DictConfigurator
configure_formatter	/usr/lib/python3.4/logging/config.py	/^    def configure_formatter(self, config):$/;"	m	class:DictConfigurator
configure_handler	/usr/lib/python3.4/logging/config.py	/^    def configure_handler(self, config):$/;"	m	class:DictConfigurator
configure_logger	/usr/lib/python3.4/logging/config.py	/^    def configure_logger(self, name, config, incremental=False):$/;"	m	class:DictConfigurator
configure_root	/usr/lib/python3.4/logging/config.py	/^    def configure_root(self, config, incremental=False):$/;"	m	class:DictConfigurator
convert	/usr/lib/python3.4/logging/config.py	/^    def convert(self, value):$/;"	m	class:BaseConfigurator
convert	/usr/lib/python3.4/logging/config.py	/^    def convert(self, value):$/;"	m	class:ConvertingMixin
convert_with_key	/usr/lib/python3.4/logging/config.py	/^    def convert_with_key(self, key, value, replace=True):$/;"	m	class:ConvertingMixin
dictConfig	/usr/lib/python3.4/logging/config.py	/^def dictConfig(config):$/;"	f
dictConfigClass	/usr/lib/python3.4/logging/config.py	/^dictConfigClass = DictConfigurator$/;"	v
ext_convert	/usr/lib/python3.4/logging/config.py	/^    def ext_convert(self, value):$/;"	m	class:BaseConfigurator
fileConfig	/usr/lib/python3.4/logging/config.py	/^def fileConfig(fname, defaults=None, disable_existing_loggers=True):$/;"	f
get	/usr/lib/python3.4/logging/config.py	/^    def get(self, key, default=None):$/;"	m	class:ConvertingDict
handle	/usr/lib/python3.4/logging/config.py	/^        def handle(self):$/;"	m	class:listen.ConfigStreamHandler
importer	/usr/lib/python3.4/logging/config.py	/^    importer = staticmethod(__import__)$/;"	v	class:BaseConfigurator
listen	/usr/lib/python3.4/logging/config.py	/^def listen(port=DEFAULT_LOGGING_CONFIG_PORT, verify=None):$/;"	f
pop	/usr/lib/python3.4/logging/config.py	/^    def pop(self, idx=-1):$/;"	m	class:ConvertingList
pop	/usr/lib/python3.4/logging/config.py	/^    def pop(self, key, default=None):$/;"	m	class:ConvertingDict
resolve	/usr/lib/python3.4/logging/config.py	/^    def resolve(self, s):$/;"	m	class:BaseConfigurator
run	/usr/lib/python3.4/logging/config.py	/^        def run(self):$/;"	m	class:listen.Server
serve_until_stopped	/usr/lib/python3.4/logging/config.py	/^        def serve_until_stopped(self):$/;"	m	class:listen.ConfigSocketReceiver
stopListening	/usr/lib/python3.4/logging/config.py	/^def stopListening():$/;"	f
thread	/usr/lib/python3.4/logging/config.py	/^    thread = None$/;"	v
valid_ident	/usr/lib/python3.4/logging/config.py	/^def valid_ident(s):$/;"	f
value_converters	/usr/lib/python3.4/logging/config.py	/^    value_converters = {$/;"	v	class:BaseConfigurator
