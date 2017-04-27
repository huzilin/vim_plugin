!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
ERROR	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    ERROR = _EPOLLERR | _EPOLLHUP$/;"	v	class:IOLoop
IOLoop	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^class IOLoop(Configurable):$/;"	c
NONE	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    NONE = 0$/;"	v	class:IOLoop
PeriodicCallback	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^class PeriodicCallback(object):$/;"	c
PollIOLoop	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^class PollIOLoop(IOLoop):$/;"	c
READ	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    READ = _EPOLLIN$/;"	v	class:IOLoop
TimeoutError	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^class TimeoutError(Exception):$/;"	c
WRITE	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    WRITE = _EPOLLOUT$/;"	v	class:IOLoop
_EPOLLERR	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    _EPOLLERR = 0x008$/;"	v	class:IOLoop
_EPOLLET	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    _EPOLLET = (1 << 31)$/;"	v	class:IOLoop
_EPOLLHUP	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    _EPOLLHUP = 0x010$/;"	v	class:IOLoop
_EPOLLIN	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    _EPOLLIN = 0x001$/;"	v	class:IOLoop
_EPOLLONESHOT	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    _EPOLLONESHOT = (1 << 30)$/;"	v	class:IOLoop
_EPOLLOUT	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    _EPOLLOUT = 0x004$/;"	v	class:IOLoop
_EPOLLPRI	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    _EPOLLPRI = 0x002$/;"	v	class:IOLoop
_EPOLLRDHUP	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    _EPOLLRDHUP = 0x2000$/;"	v	class:IOLoop
_Timeout	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^class _Timeout(object):$/;"	c
__init__	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def __init__(self, callback, callback_time, io_loop=None):$/;"	m	class:PeriodicCallback
__init__	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def __init__(self, deadline, callback, io_loop):$/;"	m	class:_Timeout
__le__	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def __le__(self, other):$/;"	m	class:_Timeout	file:
__lt__	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def __lt__(self, other):$/;"	m	class:_Timeout	file:
__slots__	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    __slots__ = ['deadline', 'callback']$/;"	v	class:_Timeout
_current	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    _current = threading.local()$/;"	v	class:IOLoop
_instance_lock	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    _instance_lock = threading.Lock()$/;"	v	class:IOLoop
_run	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def _run(self):$/;"	m	class:PeriodicCallback
_run_callback	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def _run_callback(self, callback):$/;"	m	class:IOLoop
_schedule_next	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def _schedule_next(self):$/;"	m	class:PeriodicCallback
add_callback	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def add_callback(self, callback, *args, **kwargs):$/;"	m	class:IOLoop
add_callback	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def add_callback(self, callback, *args, **kwargs):$/;"	m	class:PollIOLoop
add_callback_from_signal	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def add_callback_from_signal(self, callback, *args, **kwargs):$/;"	m	class:IOLoop
add_callback_from_signal	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def add_callback_from_signal(self, callback, *args, **kwargs):$/;"	m	class:PollIOLoop
add_future	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def add_future(self, future, callback):$/;"	m	class:IOLoop
add_handler	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def add_handler(self, fd, handler, events):$/;"	m	class:IOLoop
add_handler	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def add_handler(self, fd, handler, events):$/;"	m	class:PollIOLoop
add_timeout	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def add_timeout(self, deadline, callback):$/;"	m	class:IOLoop
add_timeout	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def add_timeout(self, deadline, callback):$/;"	m	class:PollIOLoop
clear_current	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def clear_current():$/;"	m	class:IOLoop
close	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def close(self, all_fds=False):$/;"	m	class:IOLoop
close	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def close(self, all_fds=False):$/;"	m	class:PollIOLoop
configurable_base	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def configurable_base(cls):$/;"	m	class:IOLoop
configurable_default	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def configurable_default(cls):$/;"	m	class:IOLoop
current	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def current():$/;"	m	class:IOLoop
handle_callback_exception	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def handle_callback_exception(self, callback):$/;"	m	class:IOLoop
initialize	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def initialize(self):$/;"	m	class:IOLoop
initialize	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def initialize(self, impl, time_func=None):$/;"	m	class:PollIOLoop
initialized	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def initialized():$/;"	m	class:IOLoop
install	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def install(self):$/;"	m	class:IOLoop
instance	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def instance():$/;"	m	class:IOLoop
log_stack	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def log_stack(self, signal, frame):$/;"	m	class:IOLoop
make_current	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def make_current(self):$/;"	m	class:IOLoop
remove_handler	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def remove_handler(self, fd):$/;"	m	class:IOLoop
remove_handler	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def remove_handler(self, fd):$/;"	m	class:PollIOLoop
remove_timeout	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def remove_timeout(self, timeout):$/;"	m	class:IOLoop
remove_timeout	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def remove_timeout(self, timeout):$/;"	m	class:PollIOLoop
run	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^        def run():$/;"	f	function:IOLoop.run_sync
run_sync	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def run_sync(self, func, timeout=None):$/;"	m	class:IOLoop
set_blocking_log_threshold	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def set_blocking_log_threshold(self, seconds):$/;"	m	class:IOLoop
set_blocking_signal_threshold	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def set_blocking_signal_threshold(self, seconds, action):$/;"	m	class:IOLoop
set_blocking_signal_threshold	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def set_blocking_signal_threshold(self, seconds, action):$/;"	m	class:PollIOLoop
signal	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    signal = None$/;"	v
start	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def start(self):$/;"	m	class:IOLoop
start	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def start(self):$/;"	m	class:PeriodicCallback
start	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def start(self):$/;"	m	class:PollIOLoop
stop	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def stop(self):$/;"	m	class:IOLoop
stop	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def stop(self):$/;"	m	class:PeriodicCallback
stop	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def stop(self):$/;"	m	class:PollIOLoop
time	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def time(self):$/;"	m	class:IOLoop
time	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def time(self):$/;"	m	class:PollIOLoop
timedelta_to_seconds	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def timedelta_to_seconds(td):$/;"	m	class:_Timeout
update_handler	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def update_handler(self, fd, events):$/;"	m	class:IOLoop
update_handler	/usr/lib/python2.7/dist-packages/tornado/ioloop.py	/^    def update_handler(self, fd, events):$/;"	m	class:PollIOLoop
