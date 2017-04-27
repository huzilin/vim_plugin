!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
CalledProcessError	/usr/lib/python3.4/subprocess.py	/^class CalledProcessError(SubprocessError):$/;"	c
Close	/usr/lib/python3.4/subprocess.py	/^        def Close(self, CloseHandle=_winapi.CloseHandle):$/;"	m	class:.Handle
DEVNULL	/usr/lib/python3.4/subprocess.py	/^DEVNULL = -3$/;"	v
Detach	/usr/lib/python3.4/subprocess.py	/^        def Detach(self):$/;"	m	class:.Handle
Handle	/usr/lib/python3.4/subprocess.py	/^    class Handle(int):$/;"	c
MAXFD	/usr/lib/python3.4/subprocess.py	/^    MAXFD = 256$/;"	v
MAXFD	/usr/lib/python3.4/subprocess.py	/^    MAXFD = os.sysconf("SC_OPEN_MAX")$/;"	v
PIPE	/usr/lib/python3.4/subprocess.py	/^PIPE = -1$/;"	v
Popen	/usr/lib/python3.4/subprocess.py	/^class Popen(object):$/;"	c
STARTUPINFO	/usr/lib/python3.4/subprocess.py	/^    class STARTUPINFO:$/;"	c
STDOUT	/usr/lib/python3.4/subprocess.py	/^STDOUT = -2$/;"	v
SubprocessError	/usr/lib/python3.4/subprocess.py	/^class SubprocessError(Exception): pass$/;"	c
TimeoutExpired	/usr/lib/python3.4/subprocess.py	/^class TimeoutExpired(SubprocessError):$/;"	c
_PIPE_BUF	/usr/lib/python3.4/subprocess.py	/^    _PIPE_BUF = getattr(select, 'PIPE_BUF', 512)$/;"	v
_PLATFORM_DEFAULT_CLOSE_FDS	/usr/lib/python3.4/subprocess.py	/^_PLATFORM_DEFAULT_CLOSE_FDS = object()$/;"	v
_PopenSelector	/usr/lib/python3.4/subprocess.py	/^        _PopenSelector = selectors.PollSelector$/;"	v	class:.STARTUPINFO
_PopenSelector	/usr/lib/python3.4/subprocess.py	/^        _PopenSelector = selectors.SelectSelector$/;"	v	class:.STARTUPINFO
__all__	/usr/lib/python3.4/subprocess.py	/^__all__ = ["Popen", "PIPE", "STDOUT", "call", "check_call", "getstatusoutput",$/;"	v
__del__	/usr/lib/python3.4/subprocess.py	/^        __del__ = Close$/;"	v	class:.Handle
__del__	/usr/lib/python3.4/subprocess.py	/^    def __del__(self, _maxsize=sys.maxsize):$/;"	m	class:Popen	file:
__enter__	/usr/lib/python3.4/subprocess.py	/^    def __enter__(self):$/;"	m	class:Popen	file:
__exit__	/usr/lib/python3.4/subprocess.py	/^    def __exit__(self, type, value, traceback):$/;"	m	class:Popen	file:
__init__	/usr/lib/python3.4/subprocess.py	/^    def __init__(self, args, bufsize=-1, executable=None,$/;"	m	class:Popen
__init__	/usr/lib/python3.4/subprocess.py	/^    def __init__(self, cmd, timeout, output=None):$/;"	m	class:TimeoutExpired
__init__	/usr/lib/python3.4/subprocess.py	/^    def __init__(self, returncode, cmd, output=None):$/;"	m	class:CalledProcessError
__repr__	/usr/lib/python3.4/subprocess.py	/^        def __repr__(self):$/;"	m	class:.Handle	file:
__str__	/usr/lib/python3.4/subprocess.py	/^        __str__ = __repr__$/;"	v	class:.Handle
__str__	/usr/lib/python3.4/subprocess.py	/^    def __str__(self):$/;"	m	class:CalledProcessError	file:
__str__	/usr/lib/python3.4/subprocess.py	/^    def __str__(self):$/;"	m	class:TimeoutExpired	file:
_active	/usr/lib/python3.4/subprocess.py	/^_active = []$/;"	v
_args_from_interpreter_flags	/usr/lib/python3.4/subprocess.py	/^def _args_from_interpreter_flags():$/;"	f
_check_timeout	/usr/lib/python3.4/subprocess.py	/^    def _check_timeout(self, endtime, orig_timeout):$/;"	m	class:Popen
_child_created	/usr/lib/python3.4/subprocess.py	/^    _child_created = False  # Set here since __del__ checks it$/;"	v	class:Popen
_cleanup	/usr/lib/python3.4/subprocess.py	/^def _cleanup():$/;"	f
_close_fds	/usr/lib/python3.4/subprocess.py	/^        def _close_fds(self, fds_to_keep):$/;"	f	function:Popen._check_timeout
_communicate	/usr/lib/python3.4/subprocess.py	/^        def _communicate(self, input, endtime, orig_timeout):$/;"	f	function:Popen._check_timeout
_eintr_retry_call	/usr/lib/python3.4/subprocess.py	/^def _eintr_retry_call(func, *args):$/;"	f
_execute_child	/usr/lib/python3.4/subprocess.py	/^        def _execute_child(self, args, executable, preexec_fn, close_fds,$/;"	f	function:Popen._check_timeout
_get_devnull	/usr/lib/python3.4/subprocess.py	/^    def _get_devnull(self):$/;"	m	class:Popen
_get_handles	/usr/lib/python3.4/subprocess.py	/^        def _get_handles(self, stdin, stdout, stderr):$/;"	f	function:Popen._check_timeout
_handle_exitstatus	/usr/lib/python3.4/subprocess.py	/^        def _handle_exitstatus(self, sts, _WIFSIGNALED=os.WIFSIGNALED,$/;"	f	function:Popen._check_timeout
_internal_poll	/usr/lib/python3.4/subprocess.py	/^        def _internal_poll(self, _deadstate=None, _waitpid=os.waitpid,$/;"	f	function:Popen._check_timeout
_internal_poll	/usr/lib/python3.4/subprocess.py	/^        def _internal_poll(self, _deadstate=None,$/;"	f	function:Popen._check_timeout
_make_inheritable	/usr/lib/python3.4/subprocess.py	/^        def _make_inheritable(self, handle):$/;"	f	function:Popen._check_timeout
_readerthread	/usr/lib/python3.4/subprocess.py	/^        def _readerthread(self, fh, buffer):$/;"	f	function:Popen._check_timeout
_remaining_time	/usr/lib/python3.4/subprocess.py	/^    def _remaining_time(self, endtime):$/;"	m	class:Popen
_save_input	/usr/lib/python3.4/subprocess.py	/^        def _save_input(self, input):$/;"	f	function:Popen._check_timeout
_translate_newlines	/usr/lib/python3.4/subprocess.py	/^    def _translate_newlines(self, data, encoding):$/;"	m	class:Popen
_try_wait	/usr/lib/python3.4/subprocess.py	/^        def _try_wait(self, wait_flags):$/;"	f	function:Popen._check_timeout
call	/usr/lib/python3.4/subprocess.py	/^def call(*popenargs, timeout=None, **kwargs):$/;"	f
check_call	/usr/lib/python3.4/subprocess.py	/^def check_call(*popenargs, **kwargs):$/;"	f
check_output	/usr/lib/python3.4/subprocess.py	/^def check_output(*popenargs, timeout=None, **kwargs):$/;"	f
closed	/usr/lib/python3.4/subprocess.py	/^        closed = False$/;"	v	class:.Handle
communicate	/usr/lib/python3.4/subprocess.py	/^    def communicate(self, input=None, timeout=None):$/;"	m	class:Popen
dwFlags	/usr/lib/python3.4/subprocess.py	/^        dwFlags = 0$/;"	v	class:.STARTUPINFO
getoutput	/usr/lib/python3.4/subprocess.py	/^def getoutput(cmd):$/;"	f
getstatusoutput	/usr/lib/python3.4/subprocess.py	/^def getstatusoutput(cmd):$/;"	f
hStdError	/usr/lib/python3.4/subprocess.py	/^        hStdError = None$/;"	v	class:.STARTUPINFO
hStdInput	/usr/lib/python3.4/subprocess.py	/^        hStdInput = None$/;"	v	class:.STARTUPINFO
hStdOutput	/usr/lib/python3.4/subprocess.py	/^        hStdOutput = None$/;"	v	class:.STARTUPINFO
kill	/usr/lib/python3.4/subprocess.py	/^        def kill(self):$/;"	f	function:Popen._check_timeout
list2cmdline	/usr/lib/python3.4/subprocess.py	/^def list2cmdline(seq):$/;"	f
mswindows	/usr/lib/python3.4/subprocess.py	/^mswindows = (sys.platform == "win32")$/;"	v
poll	/usr/lib/python3.4/subprocess.py	/^    def poll(self):$/;"	m	class:Popen
send_signal	/usr/lib/python3.4/subprocess.py	/^        def send_signal(self, sig):$/;"	f	function:Popen._check_timeout
terminate	/usr/lib/python3.4/subprocess.py	/^        def terminate(self):$/;"	f	function:Popen._check_timeout
wShowWindow	/usr/lib/python3.4/subprocess.py	/^        wShowWindow = 0$/;"	v	class:.STARTUPINFO
wait	/usr/lib/python3.4/subprocess.py	/^        def wait(self, timeout=None, endtime=None):$/;"	f	function:Popen._check_timeout
