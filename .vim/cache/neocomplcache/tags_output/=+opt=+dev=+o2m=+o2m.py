!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
colSQL	/opt/dev/o2m/o2m.py	/^        colSQL = "SELECT LISTAGG(column_name, '||''{fieldsTerminated}''||') WITHIN GROUP(ORDER BY COLUMN_ID) FROM (SELECT column_id,'''{enclosed}''||'||column_name||'||''{enclosed}''' as column_name fROM user_tab_cols WHERE table_name='{tableName}' ORDER BY 2 DESC)".format(fieldsTerminated = fieldsTerminated, enclosed = enclosed, tableName = eachTable)	$/;"	v
enclosed	/opt/dev/o2m/o2m.py	/^                enclosed = arg$/;"	v
fieldsTerminated	/opt/dev/o2m/o2m.py	/^                fieldsTerminated = arg$/;"	v
lock	/opt/dev/o2m/o2m.py	/^    lock = multiprocessing.Lock()$/;"	v
mysqlCharset	/opt/dev/o2m/o2m.py	/^                mysqlCharset = arg$/;"	v
mysqlConsumer	/opt/dev/o2m/o2m.py	/^def mysqlConsumer(pipe, tableName, mysqlHost, mysqlPort, mysqlUser, mysqlPassword, mysqlDb, mysqlCharset):$/;"	f
mysqlDb	/opt/dev/o2m/o2m.py	/^                mysqlDb = arg$/;"	v
mysqlHost	/opt/dev/o2m/o2m.py	/^                mysqlHost = arg$/;"	v
mysqlPassword	/opt/dev/o2m/o2m.py	/^                mysqlPassword = arg$/;"	v
mysqlPort	/opt/dev/o2m/o2m.py	/^                mysqlPort = int(arg)$/;"	v
mysqlUser	/opt/dev/o2m/o2m.py	/^                mysqlUser = arg$/;"	v
oracleConn	/opt/dev/o2m/o2m.py	/^    oracleConn = cx_Oracle.connect(oracleDSN)$/;"	v
oracleCursor	/opt/dev/o2m/o2m.py	/^    oracleCursor = oracleConn.cursor()$/;"	v
oracleDSN	/opt/dev/o2m/o2m.py	/^    oracleDSN = "{user}\/{password}@{host}:{port}\/{sid}".format(user = oracleUser, password = oraclePassword, host = oracleHost, port = oraclePort, sid = oracleSid)$/;"	v
oracleHost	/opt/dev/o2m/o2m.py	/^                oracleHost = arg$/;"	v
oraclePassword	/opt/dev/o2m/o2m.py	/^                oraclePassword = arg$/;"	v
oraclePort	/opt/dev/o2m/o2m.py	/^                oraclePort = arg$/;"	v
oracleProducer	/opt/dev/o2m/o2m.py	/^def oracleProducer(queue, lock, pipe, sqlplusPath, user, password, mysqlHost, mysqlPort, mysqlUser, mysqlPassword, mysqlDb, mysqlCharset):$/;"	f
oracleSid	/opt/dev/o2m/o2m.py	/^                oracleSid = arg$/;"	v
oracleUser	/opt/dev/o2m/o2m.py	/^                oracleUser = arg$/;"	v
pipe	/opt/dev/o2m/o2m.py	/^        pipe = pipeList[each]$/;"	v
pipeList	/opt/dev/o2m/o2m.py	/^    pipeList = []$/;"	v
pipeName	/opt/dev/o2m/o2m.py	/^        pipeName = str(each) + ".pipe"$/;"	v
process	/opt/dev/o2m/o2m.py	/^    process = []$/;"	v
processNum	/opt/dev/o2m/o2m.py	/^                processNum = int(arg)$/;"	v
queue	/opt/dev/o2m/o2m.py	/^    queue = Queue(len(tableAndSQLList))$/;"	v
row	/opt/dev/o2m/o2m.py	/^        row = oracleCursor.fetchall()$/;"	v
selectOutSQL	/opt/dev/o2m/o2m.py	/^        selectOutSQL = "SELECT "$/;"	v
sqlplusPath	/opt/dev/o2m/o2m.py	/^                sqlplusPath = arg$/;"	v
tableAndSQLList	/opt/dev/o2m/o2m.py	/^    tableAndSQLList = []$/;"	v
tableList	/opt/dev/o2m/o2m.py	/^    tableList = ["A_RCVBL_FLOW","A_RCVED_FLOW","A_RCVED_PL_FLOW"]$/;"	v
usage	/opt/dev/o2m/o2m.py	/^def usage():$/;"	f
