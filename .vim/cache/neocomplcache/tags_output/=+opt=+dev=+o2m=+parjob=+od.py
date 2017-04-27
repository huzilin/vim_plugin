!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
cnfName	/opt/dev/o2m/parjob/od.py	/^        cnfName = eachTable + ".job"$/;"	v
jobCnfN	/opt/dev/o2m/parjob/od.py	/^        jobCnfN = jobCnf.replace("tableName", eachTable).replace("colList", colList)$/;"	v
oracleConn	/opt/dev/o2m/parjob/od.py	/^    oracleConn = cx_Oracle.connect(oracleDSN,threaded=True)$/;"	v
oracleCursor	/opt/dev/o2m/parjob/od.py	/^    oracleCursor = oracleConn.cursor()$/;"	v
oracleDSN	/opt/dev/o2m/parjob/od.py	/^    oracleDSN = "{user}\/{password}@{host}:{port}\/{sid}".format(user = oracleUser, password = oraclePassword, host = oracleHost, port = oraclePort, sid = oracleSid)$/;"	v
sql	/opt/dev/o2m/parjob/od.py	/^        sql = "select no_where || ' partition(' || dt.partition_name || ') t' from (select 'select \/*+ parallel(t,2) *\/ ' || listagg || ' from ' || table_name no_where from (select table_name, LISTAGG(column_name, ',') WITHIN GROUP(ORDER BY COLUMN_ID) LISTAGG from (select table_name, column_id, column_name as column_name from user_tab_columns where table_name = '{tableName}' order by 2 desc) group by table_name)), user_tab_partitions dt where dt.table_name = '{tableName}';".format(tableName = eachTable)$/;"	v
tableList	/opt/dev/o2m/parjob/od.py	/^    tableList = ["P_SMS_SEND", "A_INV_IO", "O_PAY_DAY", "D_METER_ERR", "O_CONS_PQ_AMT", "NEW_SA_MSG_RECEIVE_HIS", "A_INV", "RT_WORKITEMINST"]$/;"	v
usage	/opt/dev/o2m/parjob/od.py	/^def usage():$/;"	f
