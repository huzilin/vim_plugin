!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
alias	/opt/dev/o2m/job/od.py	/^                alias = arg$/;"	v
cnfName	/opt/dev/o2m/job/od.py	/^        cnfName = eachTable + ".job"$/;"	v
colList	/opt/dev/o2m/job/od.py	/^        colList = oracleCursor.fetchall()[0][0]$/;"	v
jobCnfN	/opt/dev/o2m/job/od.py	/^        jobCnfN = jobCnf.replace("spk",spk).replace("tableName", eachTable).replace("colList", colList)$/;"	v
mysqlCharset	/opt/dev/o2m/job/od.py	/^                mysqlCharset = arg$/;"	v
mysqlDb	/opt/dev/o2m/job/od.py	/^                mysqlDb = arg$/;"	v
mysqlHost	/opt/dev/o2m/job/od.py	/^                mysqlHost = arg$/;"	v
mysqlPasswd	/opt/dev/o2m/job/od.py	/^                mysqlPasswd = arg$/;"	v
mysqlPassword	/opt/dev/o2m/job/od.py	/^                mysqlPassword = arg$/;"	v
mysqlPort	/opt/dev/o2m/job/od.py	/^                mysqlPort = int(arg)$/;"	v
mysqlUser	/opt/dev/o2m/job/od.py	/^                mysqlUser = arg$/;"	v
oracleConn	/opt/dev/o2m/job/od.py	/^    oracleConn = cx_Oracle.connect(oracleDSN,threaded=True)$/;"	v
oracleCursor	/opt/dev/o2m/job/od.py	/^    oracleCursor = oracleConn.cursor()$/;"	v
oracleDSN	/opt/dev/o2m/job/od.py	/^    oracleDSN = "{user}\/{password}@{host}:{port}\/{sid}".format(user = oracleUser, password = oraclePassword, host = oracleHost, port = oraclePort, sid = oracleSid)$/;"	v
oracleHost	/opt/dev/o2m/job/od.py	/^                oracleHost = arg$/;"	v
oraclePassword	/opt/dev/o2m/job/od.py	/^                oraclePassword = arg$/;"	v
oraclePort	/opt/dev/o2m/job/od.py	/^                oraclePort = arg$/;"	v
oracleSid	/opt/dev/o2m/job/od.py	/^                oracleSid = arg$/;"	v
oracleUser	/opt/dev/o2m/job/od.py	/^                oracleUser = arg$/;"	v
producer	/opt/dev/o2m/job/od.py	/^def producer(tableName, insertSQL):$/;"	f
sqk	/opt/dev/o2m/job/od.py	/^        sqk = oracleCursor.fetchall()[0][0]$/;"	v
sql	/opt/dev/o2m/job/od.py	/^        sql = "SELECT LISTAGG(column_name, ', ') WITHIN GROUP(ORDER BY COLUMN_ID) FROM (SELECT COLUMN_ID, '\\"' || column_name || '\\"' as column_name from user_tab_cols WHERE table_name='{tableName}')".format(tableName = eachTable)$/;"	v
sqlplusPath	/opt/dev/o2m/job/od.py	/^                sqlplusPath = arg$/;"	v
tableList	/opt/dev/o2m/job/od.py	/^    tableList = ["P_SMS_SEND", "A_INV_IO", "O_PAY_DAY", "D_METER_ERR", "O_CONS_PQ_AMT", "NEW_SA_MSG_RECEIVE_HIS", "A_INV", "RT_WORKITEMINST"]$/;"	v
threadNum	/opt/dev/o2m/job/od.py	/^                threadNum = int(arg)$/;"	v
usage	/opt/dev/o2m/job/od.py	/^def usage():$/;"	f
