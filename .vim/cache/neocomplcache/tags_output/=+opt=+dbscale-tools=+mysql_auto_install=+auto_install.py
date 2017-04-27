!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
Install_Or_Init_Error	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^class Install_Or_Init_Error(Exception):$/;"	c
New_SSHClient	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^class New_SSHClient(paramiko.SSHClient):$/;"	c
SSH_CMD_With_Report_Error	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^class SSH_CMD_With_Report_Error(SSH_CMD):$/;"	c
__init__	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    def __init__(self):$/;"	m	class:New_SSHClient
__init__	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    def __init__(self, value):$/;"	m	class:Install_Or_Init_Error
__init__	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    def __init__(self,error_dic,ip,user,password,port,cmd,db_port,need_stdout = False):$/;"	m	class:SSH_CMD_With_Report_Error
__str__	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    def __str__(self):$/;"	m	class:Install_Or_Init_Error	file:
all_info	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    all_info = get_server_and_cnf_info()$/;"	v	class:SSH_CMD_With_Report_Error
cnf_info_dic	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    cnf_info_dic = all_info['cnf_info_dic']$/;"	v	class:SSH_CMD_With_Report_Error
error	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    error = 0$/;"	v	class:SSH_CMD_With_Report_Error
error_dic	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^error_dic={101:u"Basedir's parent directory has a file.",102:u"The installation package decompression directory file or directory exists ",103:u"Basedir's location has a file or directory.",104:u"Decompression failed.",105:u"Modify the unzipped directory permissions to fail.",106:u"Failed to create soft links.",107:u"Modify the basedir permission to fail.",201:u"Failed to create datadir.",202:u"Modify the datadir permission to fail.",203:u"Failed to create the directory with the socket",204:u"Modify the socket's directory permissions",205:u"Failed to create the redo_log's directory.",206:u"Modify the redo_log directory permissions to fail.",207:u"Failed to create the undo's directory.",208:u"Modify the undo directory permissions to fail.",209:u"Failed to create the error_log's directory.",210:u"Modify the error_log's directory permissions to fail",211:u"Failed to create directory of pid.",212:u"Modify the pid's directory permissions to fail.",213:u"Failed to create directory of tmp.",214:u"Modify the tmp's directory permissions to fail.",215:u"Failed to create directory of log_bin's directory.",216:u"Modify the log bin's directory permissions to fail.",217:u"Database initialization failed.",218:u"Failed to copy the configuration file to the specified directory.",219:u"Modify the configuration file permissions to fail.",220:u"Modify server_id failure.",221:u"Failed to start the database or timeout.",222:u"Failed to create a db_user.",223:u"Reset master to fail."}$/;"	v
exec_command	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    def exec_command(self, command, bufsize=-1, timeout=None, get_pty=False):$/;"	m	class:New_SSHClient
fuzzy_list	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    fuzzy_list = ['-','_']$/;"	v	class:SSH_CMD_With_Report_Error
local_init_mysql_sh	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    local_init_mysql_sh = run_dir + '\/init_mysql.sh'$/;"	v	class:SSH_CMD_With_Report_Error
main_dic	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    main_dic = all_info['main_dic']$/;"	v	class:SSH_CMD_With_Report_Error
modify_options_dic	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    modify_options_dic = {'interactive_timeout':'31536000','wait_timeout':'31536000','server_id':''}$/;"	v	class:SSH_CMD_With_Report_Error
mysql_install_dic	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    mysql_install_dic = {}$/;"	v	class:SSH_CMD_With_Report_Error
mysql_install_list	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    mysql_install_list = list()$/;"	v	class:SSH_CMD_With_Report_Error
mysql_install_list	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    mysql_install_list = mysql_install_dic.keys()$/;"	v	class:SSH_CMD_With_Report_Error
raise_error	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    def raise_error(self):$/;"	m	class:SSH_CMD_With_Report_Error
rsync_dic	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    rsync_dic = {}$/;"	v	class:SSH_CMD_With_Report_Error
rsync_list	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    rsync_list = list()$/;"	v	class:SSH_CMD_With_Report_Error
rsync_list	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    rsync_list = rsync_dic.keys()$/;"	v	class:SSH_CMD_With_Report_Error
rsync_num	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    rsync_num= len(rsync_list)$/;"	v	class:SSH_CMD_With_Report_Error
run	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    def run(self):$/;"	m	class:SSH_CMD_With_Report_Error
run_dir	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    run_dir = os.getcwd()$/;"	v	class:SSH_CMD_With_Report_Error
run_dir	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^run_dir = os.getcwd()$/;"	v
run_max_thread	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    run_max_thread = 2$/;"	v	class:SSH_CMD_With_Report_Error
server_info_dic	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    server_info_dic = all_info['server_info_dic']$/;"	v	class:SSH_CMD_With_Report_Error
server_list	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    server_list = all_info['server_list']$/;"	v	class:SSH_CMD_With_Report_Error
string_contrast	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    def string_contrast(str1,str2,fuzzy_list):$/;"	m	class:SSH_CMD_With_Report_Error
thread	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    thread = list()$/;"	v	class:SSH_CMD_With_Report_Error
thread_num	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    thread_num = 0$/;"	v	class:SSH_CMD_With_Report_Error
try_times	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^    try_times = 1$/;"	v	class:SSH_CMD_With_Report_Error
usage	/opt/dbscale-tools/mysql_auto_install/auto_install.py	/^def usage():$/;"	f
