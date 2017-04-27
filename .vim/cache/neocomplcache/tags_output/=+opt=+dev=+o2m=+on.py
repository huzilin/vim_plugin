!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
alias	/opt/dev/o2m/on.py	/^                alias = arg$/;"	v
insertSQL	/opt/dev/o2m/on.py	/^        insertSQL = "insert into `{tableName}` {selectSQL}".format(tableName=eachTable, selectSQL=selectSQL)$/;"	v
job	/opt/dev/o2m/on.py	/^        job = thread_pool.submit(producer, tableName, insertSQL)$/;"	v
jobs	/opt/dev/o2m/on.py	/^    jobs = []$/;"	v
mysqlCharset	/opt/dev/o2m/on.py	/^                mysqlCharset = arg$/;"	v
mysqlDb	/opt/dev/o2m/on.py	/^                mysqlDb = arg$/;"	v
mysqlHost	/opt/dev/o2m/on.py	/^                mysqlHost = arg$/;"	v
mysqlPasswd	/opt/dev/o2m/on.py	/^                mysqlPasswd = arg$/;"	v
mysqlPassword	/opt/dev/o2m/on.py	/^                mysqlPassword = arg$/;"	v
mysqlPort	/opt/dev/o2m/on.py	/^                mysqlPort = int(arg)$/;"	v
mysqlUser	/opt/dev/o2m/on.py	/^                mysqlUser = arg$/;"	v
oracleConn	/opt/dev/o2m/on.py	/^    oracleConn = cx_Oracle.connect(oracleDSN,threaded=True)$/;"	v
oracleCursor	/opt/dev/o2m/on.py	/^    oracleCursor = oracleConn.cursor()$/;"	v
oracleDSN	/opt/dev/o2m/on.py	/^    oracleDSN = "{user}\/{password}@{host}:{port}\/{sid}".format(user = oracleUser, password = oraclePassword, host = oracleHost, port = oraclePort, sid = oracleSid)$/;"	v
oracleHost	/opt/dev/o2m/on.py	/^                oracleHost = arg$/;"	v
oraclePassword	/opt/dev/o2m/on.py	/^                oraclePassword = arg$/;"	v
oraclePort	/opt/dev/o2m/on.py	/^                oraclePort = arg$/;"	v
oracleSid	/opt/dev/o2m/on.py	/^                oracleSid = arg$/;"	v
oracleUser	/opt/dev/o2m/on.py	/^                oracleUser = arg$/;"	v
producer	/opt/dev/o2m/on.py	/^def producer(tableName, insertSQL):$/;"	f
row	/opt/dev/o2m/on.py	/^    row = oracleCursor.fetchall()$/;"	v
selectSQL	/opt/dev/o2m/on.py	/^        selectSQL = oracleCursor.fetchall()[0][0]$/;"	v
sql	/opt/dev/o2m/on.py	/^        sql = "SELECT 'select ' || LISTAGG(column_name, ', ') WITHIN GROUP(ORDER BY COLUMN_ID) || ' from `{alias}`.`{tableName}`' FROM (SELECT COLUMN_ID, '\\"' || column_name || '\\"' as column_name from user_tab_cols WHERE table_name='{tableName}')".format(tableName = eachTable, alias = alias)$/;"	v
sqlplusPath	/opt/dev/o2m/on.py	/^                sqlplusPath = arg$/;"	v
tableInsertSQL	/opt/dev/o2m/on.py	/^    tableInsertSQL = []$/;"	v
tableList	/opt/dev/o2m/on.py	/^    tableList = []$/;"	v
threadNum	/opt/dev/o2m/on.py	/^                threadNum = int(arg)$/;"	v
thread_pool	/opt/dev/o2m/on.py	/^    thread_pool = ThreadPoolExecutor(max_workers=threadNum)$/;"	v
usage	/opt/dev/o2m/on.py	/^def usage():$/;"	f
