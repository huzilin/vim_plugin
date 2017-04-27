!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
conn	/opt/mysql-5.6.28-linux-glibc2.5-x86_64/heartbeat.py	/^conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='123',db="test",charset="utf8")  $/;"	v
cursor	/opt/mysql-5.6.28-linux-glibc2.5-x86_64/heartbeat.py	/^cursor = conn.cursor()$/;"	v
n	/opt/mysql-5.6.28-linux-glibc2.5-x86_64/heartbeat.py	/^        n = cursor.execute("create table t" + str(i) + " (a int)engine=myisam")$/;"	v
n	/opt/mysql-5.6.28-linux-glibc2.5-x86_64/heartbeat.py	/^        n = cursor.execute("drop table if exists t" + str(i))$/;"	v
n	/opt/mysql-5.6.28-linux-glibc2.5-x86_64/heartbeat.py	/^        n = cursor.execute("set @a=ifnull(concat(@a, ', ', 't" + str(i) + "'), 't" + str(i) + "')")$/;"	v
n	/opt/mysql-5.6.28-linux-glibc2.5-x86_64/heartbeat.py	/^    n = cursor.execute("drop table t" + str(i))$/;"	v
