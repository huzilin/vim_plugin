!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
alias	/opt/dev/o2m/od.py	/^                alias = arg$/;"	v
insertSQL	/opt/dev/o2m/od.py	/^        insertSQL = "insert into `{tableName}` {selectSQL}".format(tableName=eachTable, selectSQL=selectSQL)$/;"	v
job	/opt/dev/o2m/od.py	/^        job = thread_pool.submit(producer, tableName, insertSQL)$/;"	v
jobs	/opt/dev/o2m/od.py	/^    jobs = []$/;"	v
mysqlCharset	/opt/dev/o2m/od.py	/^                mysqlCharset = arg$/;"	v
mysqlDb	/opt/dev/o2m/od.py	/^                mysqlDb = arg$/;"	v
mysqlHost	/opt/dev/o2m/od.py	/^                mysqlHost = arg$/;"	v
mysqlPasswd	/opt/dev/o2m/od.py	/^                mysqlPasswd = arg$/;"	v
mysqlPassword	/opt/dev/o2m/od.py	/^                mysqlPassword = arg$/;"	v
mysqlPort	/opt/dev/o2m/od.py	/^                mysqlPort = int(arg)$/;"	v
mysqlUser	/opt/dev/o2m/od.py	/^                mysqlUser = arg$/;"	v
oracleConn	/opt/dev/o2m/od.py	/^    oracleConn = cx_Oracle.connect(oracleDSN,threaded=True)$/;"	v
oracleCursor	/opt/dev/o2m/od.py	/^    oracleCursor = oracleConn.cursor()$/;"	v
oracleDSN	/opt/dev/o2m/od.py	/^    oracleDSN = "{user}\/{password}@{host}:{port}\/{sid}".format(user = oracleUser, password = oraclePassword, host = oracleHost, port = oraclePort, sid = oracleSid)$/;"	v
oracleHost	/opt/dev/o2m/od.py	/^                oracleHost = arg$/;"	v
oraclePassword	/opt/dev/o2m/od.py	/^                oraclePassword = arg$/;"	v
oraclePort	/opt/dev/o2m/od.py	/^                oraclePort = arg$/;"	v
oracleSid	/opt/dev/o2m/od.py	/^                oracleSid = arg$/;"	v
oracleUser	/opt/dev/o2m/od.py	/^                oracleUser = arg$/;"	v
producer	/opt/dev/o2m/od.py	/^def producer(tableName, insertSQL):$/;"	f
row	/opt/dev/o2m/od.py	/^    row = oracleCursor.fetchall()$/;"	v
selectSQL	/opt/dev/o2m/od.py	/^        selectSQL = oracleCursor.fetchall()[0][0]$/;"	v
sql	/opt/dev/o2m/od.py	/^        sql = "SELECT 'select ' || LISTAGG(column_name, ', ') WITHIN GROUP(ORDER BY COLUMN_ID) || ' from `{alias}`.`{tableName}`' FROM (SELECT COLUMN_ID, '\\"' || column_name || '\\"' as column_name from user_tab_cols WHERE table_name='{tableName}')".format(tableName = eachTable, alias = alias)$/;"	v
sqlplusPath	/opt/dev/o2m/od.py	/^                sqlplusPath = arg$/;"	v
tableInsertSQL	/opt/dev/o2m/od.py	/^    tableInsertSQL = []$/;"	v
tableList	/opt/dev/o2m/od.py	/^    tableList = []$/;"	v
threadNum	/opt/dev/o2m/od.py	/^                threadNum = int(arg)$/;"	v
thread_pool	/opt/dev/o2m/od.py	/^    thread_pool = ThreadPoolExecutor(max_workers=threadNum)$/;"	v
usage	/opt/dev/o2m/od.py	/^def usage():$/;"	f
