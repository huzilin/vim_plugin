!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
DummyExecutor	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^class DummyExecutor(object):$/;"	c
Future	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    Future = _DummyFuture$/;"	v
Future	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    Future = futures.Future$/;"	v
ReturnValueIgnoredError	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^class ReturnValueIgnoredError(Exception):$/;"	c
TracebackFuture	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^class TracebackFuture(Future):$/;"	c
_DummyFuture	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^class _DummyFuture(object):$/;"	c
_NO_RESULT	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^_NO_RESULT = object()$/;"	v
__init__	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def __init__(self):$/;"	m	class:TracebackFuture
__init__	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def __init__(self):$/;"	m	class:_DummyFuture
_check_done	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def _check_done(self):$/;"	m	class:_DummyFuture
_set_done	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def _set_done(self):$/;"	m	class:_DummyFuture
add_done_callback	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def add_done_callback(self, fn):$/;"	m	class:_DummyFuture
cancel	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def cancel(self):$/;"	m	class:_DummyFuture
cancelled	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def cancelled(self):$/;"	m	class:_DummyFuture
chain_future	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^def chain_future(a, b):$/;"	f
copy	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def copy(future):$/;"	f	function:chain_future
done	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def done(self):$/;"	m	class:_DummyFuture
dummy_executor	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^dummy_executor = DummyExecutor()$/;"	v
exc_info	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def exc_info(self):$/;"	m	class:TracebackFuture
exception	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def exception(self, timeout=None):$/;"	m	class:_DummyFuture
futures	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    futures = None$/;"	v
handle_error	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^        def handle_error(typ, value, tb):$/;"	f	function:return_future.wrapper
result	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def result(self):$/;"	m	class:TracebackFuture
result	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def result(self, timeout=None):$/;"	m	class:_DummyFuture
return_future	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^def return_future(f):$/;"	f
run_callback	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^            def run_callback(future):$/;"	f	function:return_future.wrapper.handle_error
run_on_executor	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^def run_on_executor(fn):$/;"	f
running	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def running(self):$/;"	m	class:_DummyFuture
set_exc_info	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def set_exc_info(self, exc_info):$/;"	m	class:TracebackFuture
set_exception	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def set_exception(self, exception):$/;"	m	class:_DummyFuture
set_result	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def set_result(self, result):$/;"	m	class:_DummyFuture
shutdown	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def shutdown(self, wait=True):$/;"	m	class:DummyExecutor
submit	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def submit(self, fn, *args, **kwargs):$/;"	m	class:DummyExecutor
wrapper	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def wrapper(*args, **kwargs):$/;"	f	function:return_future
wrapper	/usr/lib/python2.7/dist-packages/tornado/concurrent.py	/^    def wrapper(self, *args, **kwargs):$/;"	f	function:run_on_executor
