!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
colSQL	/opt/dev/o2m/o2m_t.py	/^        colSQL = "SELECT LISTAGG(column_name, '||''{fieldsTerminated}''||') WITHIN GROUP(ORDER BY COLUMN_ID) FROM (SELECT column_id,'''{enclosed}''||'||column_name||'||''{enclosed}''' as column_name fROM user_tab_cols WHERE table_name='{tableName}' ORDER BY 2 DESC)".format(fieldsTerminated = fieldsTerminated, enclosed = enclosed, tableName = eachTable)	$/;"	v
enclosed	/opt/dev/o2m/o2m_t.py	/^                enclosed = arg$/;"	v
eventList	/opt/dev/o2m/o2m_t.py	/^    eventList = []$/;"	v
fieldsTerminated	/opt/dev/o2m/o2m_t.py	/^                fieldsTerminated = arg$/;"	v
lock	/opt/dev/o2m/o2m_t.py	/^    lock = threading.Lock()$/;"	v
mysqlCharset	/opt/dev/o2m/o2m_t.py	/^                mysqlCharset = arg$/;"	v
mysqlConn	/opt/dev/o2m/o2m_t.py	/^        mysqlConn = MySQLdb.connect(host=mysqlHost,port=mysqlPort,user=mysqlUser,passwd=mysqlPassword,db=mysqlDb,charset=mysqlCharset)$/;"	v
mysqlConnList	/opt/dev/o2m/o2m_t.py	/^    mysqlConnList = []$/;"	v
mysqlConsumer	/opt/dev/o2m/o2m_t.py	/^def mysqlConsumer(pipe, producerWaitEvent, p2cQueue, cursor):$/;"	f
mysqlCursor	/opt/dev/o2m/o2m_t.py	/^        mysqlCursor = mysqlConn.cursor()$/;"	v
mysqlCursor	/opt/dev/o2m/o2m_t.py	/^        mysqlCursor = mysqlCursorList[each]$/;"	v
mysqlCursorList	/opt/dev/o2m/o2m_t.py	/^    mysqlCursorList = []$/;"	v
mysqlDb	/opt/dev/o2m/o2m_t.py	/^                mysqlDb = arg$/;"	v
mysqlHost	/opt/dev/o2m/o2m_t.py	/^                mysqlHost = arg$/;"	v
mysqlPassword	/opt/dev/o2m/o2m_t.py	/^                mysqlPassword = arg$/;"	v
mysqlPort	/opt/dev/o2m/o2m_t.py	/^                mysqlPort = int(arg)$/;"	v
mysqlUser	/opt/dev/o2m/o2m_t.py	/^                mysqlUser = arg$/;"	v
oracleConn	/opt/dev/o2m/o2m_t.py	/^    oracleConn = cx_Oracle.connect(oracleDSN)$/;"	v
oracleCursor	/opt/dev/o2m/o2m_t.py	/^    oracleCursor = oracleConn.cursor()$/;"	v
oracleDSN	/opt/dev/o2m/o2m_t.py	/^    oracleDSN = "{user}\/{password}@{host}:{port}\/{sid}".format(user = oracleUser, password = oraclePassword, host = oracleHost, port = oraclePort, sid = oracleSid)$/;"	v
oracleHost	/opt/dev/o2m/o2m_t.py	/^                oracleHost = arg$/;"	v
oraclePassword	/opt/dev/o2m/o2m_t.py	/^                oraclePassword = arg$/;"	v
oraclePort	/opt/dev/o2m/o2m_t.py	/^                oraclePort = arg$/;"	v
oracleProducer	/opt/dev/o2m/o2m_t.py	/^def oracleProducer(tableQueue, p2cQueue, lock, producerWaitEvent, pipe, sqlplusPath, user, password, cursor):$/;"	f
oracleSid	/opt/dev/o2m/o2m_t.py	/^                oracleSid = arg$/;"	v
oracleUser	/opt/dev/o2m/o2m_t.py	/^                oracleUser = arg$/;"	v
p2cQueue	/opt/dev/o2m/o2m_t.py	/^        p2cQueue = p2cQueueList[each]$/;"	v
p2cQueueList	/opt/dev/o2m/o2m_t.py	/^    p2cQueueList = []$/;"	v
pipe	/opt/dev/o2m/o2m_t.py	/^        pipe = pipeList[each]$/;"	v
pipeList	/opt/dev/o2m/o2m_t.py	/^    pipeList = []$/;"	v
pipeName	/opt/dev/o2m/o2m_t.py	/^        pipeName = str(each) + ".pipe"$/;"	v
process	/opt/dev/o2m/o2m_t.py	/^    process = []$/;"	v
processNum	/opt/dev/o2m/o2m_t.py	/^                processNum = int(arg)$/;"	v
producerWaitEvent	/opt/dev/o2m/o2m_t.py	/^        producerWaitEvent = eventList[each]$/;"	v
row	/opt/dev/o2m/o2m_t.py	/^        row = oracleCursor.fetchall()$/;"	v
selectOutSQL	/opt/dev/o2m/o2m_t.py	/^        selectOutSQL = "SELECT "$/;"	v
sqlplusPath	/opt/dev/o2m/o2m_t.py	/^                sqlplusPath = arg$/;"	v
tableAndSQLList	/opt/dev/o2m/o2m_t.py	/^    tableAndSQLList = []$/;"	v
tableList	/opt/dev/o2m/o2m_t.py	/^    tableList = ["A_RCVBL_FLOW","A_RCVED_FLOW","A_RCVED_PL_FLOW"]$/;"	v
tableQueue	/opt/dev/o2m/o2m_t.py	/^    tableQueue = Queue(len(tableAndSQLList))$/;"	v
usage	/opt/dev/o2m/o2m_t.py	/^def usage():$/;"	f
