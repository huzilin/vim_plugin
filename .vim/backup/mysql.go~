package utils

import (
	"bytes"
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"os"
	"os/exec"
	"path"
	"strconv"
	"strings"
)

var (
	grantsCode string
)

func FindMySQLInstallDir() (string, error) {
	var cmd = exec.Command("which", "mysqld")
	var out bytes.Buffer
	cmd.Stdout = &out
	err := cmd.Run()
	if err != nil {
		return "", err
	}

	var mysqldPath = out.String()
	if strings.Compare(mysqldPath, "") == 0 {
		return "", nil
	}

	cmd = exec.Command("dirname", mysqldPath)
	out.Reset()
	cmd.Stdout = &out
	err = cmd.Run()
	if err != nil {
		return "", err
	}

	var mysqlBinPath = out.String()
	cmd = exec.Command("dirname", mysqlBinPath)
	out.Reset()
	cmd.Stdout = &out
	err = cmd.Run()
	if err != nil {
		return "", err
	}

	return strings.TrimSuffix(out.String(), "\n"), nil
}

func Check(e error) {
	if e != nil {
		fmt.Println(e)
		panic(e)
	}
}

func InitMySQLConfigFile(port int, user string, password string,
	mysqlDir string, sandbox string, filename string, retChan chan error) {

	context := fmt.Sprintf(config, user, password, port, sandbox, port, user, port, sandbox, port, mysqlDir, sandbox, sandbox, sandbox, port, port)
	f, err := os.Create(filename)
	defer f.Close()

	Check(err)
	_, err = f.WriteString(context)
	Check(err)
	err = f.Sync()
	Check(err)

	retChan <- err
}

func GetMySQLVersion(mysqlDir string) (int, int, int, error) {
	var mysql_config = mysqlDir + "/bin/mysql_config"
	var options = "--version"
	var cmd = exec.Command(mysql_config, options)
	var out bytes.Buffer
	cmd.Stdout = &out
	var err = cmd.Run()
	if err != nil {
		return 0, 0, 0, err
	} else {
		var versions = strings.Split(strings.TrimSuffix(out.String(), "\n"), ".")
		major, _ := strconv.Atoi(versions[0])
		minor, _ := strconv.Atoi(versions[1])
		rev, _ := strconv.Atoi(versions[2])
		return major, minor, rev, nil
	}
}

func MySQLInstallDB(version bool, mysqlDir string, dataDir string, cnfPath string, retChan chan error) {
	var cmdPath string
	var option1 string
	var option2 string

	var share_dir = mysqlDir + "/share"

	if version {
		cmdPath = "bin/mysqld"

		option1 = "--defaults-file=" + cnfPath
		option2 = "--initialize-insecure"
	} else {
		cmdPath = "scripts/mysql_install_db"

		option1 = "--basedir=" + mysqlDir
		option2 = "--datadir=" + dataDir
	}

	var option3 = "--lc-messages-dir=" + share_dir

	var cmd = exec.Command(cmdPath, option1, option2, option3)

	cmd.Dir = mysqlDir

	cmd.Stderr = os.Stdout
	err := cmd.Run()
	Check(err)
	retChan <- err
}

func MySQLInstallMultiDBs(mysqlDir string, installPath string, mysqlPackagePath string, instanceDir2Port map[string]int) {
	fmt.Println("Installing all MySQLs...")
	/*** judge weather need to decompress MySQL ***/
	if mysqlPackagePath != "" {
		Decompress(mysqlPackagePath, installPath)
		mysqlDecompressPath := strings.Split(path.Base(mysqlPackagePath), ".tar")[0]
		cmd := exec.Command("ln", "-s", mysqlDecompressPath, installPath+"/mysql")
		err := cmd.Run()
		Check(err)
	}

	/*** judge version ***/
	verP1, verP2, verP3, err := GetMySQLVersion(mysqlDir)
	Check(err)

	/*** install grants file ***/
	var version bool

	if (verP1*256*256 + verP2*256 + verP3) >= (5*256*256 + 7*256) {
		version = true
	} else {
		version = false
	}

	retChan := make(chan error, 12)

	/*** Install MySQL and config ***/
	for dir, port := range instanceDir2Port {
		dataDir := dir + "/data"
		tmpDir := dir + "/tmp"
		cnfPath := dir + "/my.sandbox.cnf"
		os.MkdirAll(dataDir, 0777)
		os.MkdirAll(tmpDir, 0777)
		InitMySQLConfigFile(port, "dbscale", "dbscale", mysqlDir, dir, cnfPath, retChan)
		go MySQLInstallDB(version, mysqlDir, dataDir, cnfPath, retChan)
	}

	/** check return channel **/
	for i := 0; i < 12; i++ {
		err := <-retChan
		Check(err)
	}
}

func InitMySQLScripts(mysqlDirPath string, instanceDir string, port int, scriptsDict map[string]string) {

	backQuotes := "`"
	scriptsDict["start"] = fmt.Sprintf(startScript, mysqlDirPath, instanceDir, port, backQuotes, backQuotes, backQuotes, backQuotes)

	scriptsDict["stop"] = fmt.Sprintf(stopScript, mysqlDirPath, instanceDir, port)

	scriptsDict["send_kill"] = fmt.Sprintf(sendKillScript, instanceDir, port, backQuotes, backQuotes)

	scriptsDict["use"] = fmt.Sprintf(useScript, mysqlDirPath, mysqlDirPath, mysqlDirPath, mysqlDirPath, instanceDir, mysqlDirPath, port, "`", "`", "`", "+%%Y-%%m-%%d %%H:%%M:%%S", "`")
}

func InitMySQLScript4All(installPath string, scriptsDict map[string]string) {
	startAllMySQLScript := `#!/bin/bash
instanceScript=%sfind %s -maxdepth 3 -mindepth 2 -type f -name start%s
for i in $instanceScript;
do
    $i $@
done
`
	backQuotes := "`"
	scriptsDict["startallmysql"] = fmt.Sprintf(startAllMySQLScript, backQuotes, installPath, backQuotes)
	stopAllMySQLScript := `#!/bin/bash
echo -e "Stopping All MySQL Instances...\c"
instanceScript=%sfind %s -maxdepth 3 -mindepth 2 -type f -name stop%s
for i in $instanceScript;
do
    $i $@
done
echo -e "done!"
`
	scriptsDict["stopallmysql"] = fmt.Sprintf(stopAllMySQLScript, backQuotes, installPath, backQuotes)
}

func InstallMySQLScripts(mysqlDirPath string, installPath string, instanceDir2Port map[string]int) {
	fmt.Println("Installing MySQL Scripts...")
	mysqlScriptsDict := make(map[string]string)
	mysqlScript4AllDict := make(map[string]string)

	/*** Install startscripts ***/
	for instanceDir, port := range instanceDir2Port {
		InitMySQLScripts(mysqlDirPath, instanceDir, port, mysqlScriptsDict)
		for scriptName, script := range mysqlScriptsDict {
			scriptFilePath := instanceDir + "/" + scriptName
			scriptFile, err := os.Create(scriptFilePath)
			Check(err)
			_, err = scriptFile.Write([]byte(script))
			Check(err)
			scriptFile.Chmod(0744)
			scriptFile.Close()
		}
	}

	/*** Install scripts4all ***/
	InitMySQLScript4All(installPath, mysqlScript4AllDict)
	for scriptName, script := range mysqlScript4AllDict {
		scriptFilePath := installPath + "/" + scriptName
		scriptFile, err := os.Create(scriptFilePath)
		Check(err)
		_, err = scriptFile.Write([]byte(script))
		Check(err)
		scriptFile.Chmod(0744)
		scriptFile.Close()
	}

	/*** Install Grant scripts */
	grantsCode = MySQLInstallGrantFile(mysqlDirPath, installPath)
}

func StartMySQL(installPath string) {
	fmt.Println("Starting MySQL...")
	cmd := exec.Command(installPath + "/startallmysql")
	cmd.Stderr = os.Stdout
	cmd.Dir = installPath
	err := cmd.Run()
	Check(err)
}

func InitGrantScripts(scripts map[string]string) {
	/** get grants options **/
	dbUser := Options["dbUser"]
	rwUser := Options["rwUser"]
	roUser := Options["roUser"]
	remoteAccess := Options["remoteAccess"]
	dbPassword := Options["dbPassword"]
	replUser := Options["replUser"]
	replPassword := Options["replPassword"]

	/** init grants code **/
	grantsMySQLFormat := `set password=password('%s');
grant all on *.* to %s@'%s' identified by '%s' with grant option;
grant all on *.* to %s@'localhost' identified by '%s';
grant SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,INDEX,ALTER, SHOW DATABASES,CREATE TEMPORARY TABLES,LOCK TABLES, EXECUTE on *.* to %s@'localhost' identified by '%s';
grant SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,INDEX,ALTER, SHOW DATABASES,CREATE TEMPORARY TABLES,LOCK TABLES, EXECUTE on *.* to %s@'%s' identified by '%s';
grant SELECT,EXECUTE on *.* to %s@'%s' identified by '%s';
grant SELECT,EXECUTE on *.* to %s@'localhost' identified by '%s';
grant REPLICATION SLAVE on *.* to %s@'%s' identified by '%s';
delete from user where password='';
delete from db where user='';
flush privileges;
create database if not exists test;
reset master;`
	grantsMysql := fmt.Sprintf(grantsMySQLFormat, dbPassword, dbUser, remoteAccess, dbPassword, dbUser, dbPassword, rwUser, dbPassword, rwUser, remoteAccess, dbPassword, roUser, remoteAccess, dbPassword, roUser, dbPassword, replUser, remoteAccess, replPassword)
	scripts["grants.mysql"] = grantsMysql

	/** init grants576 code **/
	grants576MySQLFormat := `use mysql;
set password='%s';
delete from user where user not in ('root', 'mysql.sys', 'mysqlxsys');
flush privileges;
create user %s@'%s' identified by '%s';
grant all on *.* to %s@'%s' with grant option;
create user %s@'localhost' identified by '%s';
grant all on *.* to %s@'localhost';
create user %s@'localhost' identified by '%s';
grant SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,INDEX,ALTER, SHOW DATABASES,CREATE TEMPORARY TABLES,LOCK TABLES, EXECUTE on *.* to %s@'localhost';
create user %s@'%s' identified by '%s';
grant SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,INDEX,ALTER, SHOW DATABASES,CREATE TEMPORARY TABLES,LOCK TABLES, EXECUTE on *.* to %s@'%s';
create user %s@'%s' identified by '%s';
create user %s@'localhost' identified by '%s';
create user %s@'%s' identified by '%s';
grant SELECT,EXECUTE on *.* to %s@'%s';
grant SELECT,EXECUTE on *.* to %s@'localhost';
grant REPLICATION SLAVE on *.* to %s@'%s';
create database if not exists test;
reset master;`
	grants576Mysql := fmt.Sprintf(grants576MySQLFormat, dbPassword, dbUser, remoteAccess, dbPassword, dbUser, remoteAccess, dbUser, dbPassword, dbUser, rwUser, dbPassword, rwUser, rwUser, remoteAccess, dbPassword, rwUser, remoteAccess, roUser, remoteAccess, dbPassword, roUser, dbPassword, replUser, remoteAccess, replPassword, roUser, remoteAccess, roUser, replUser, remoteAccess)
	scripts["grants_5_7_6.mysql"] = grants576Mysql
}

func MySQLInstallGrantFile(mysqlDirPath string, installPath string) string {
	/*** init grants scripts ***/
	scripts := make(map[string]string)
	InitGrantScripts(scripts)

	/*** judge version ***/
	verP1, verP2, verP3, err := GetMySQLVersion(mysqlDirPath)
	Check(err)

	/*** install grants file ***/
	var code string

	if (verP1*256*256 + verP2*256 + verP3) >= (5*256*256 + 7*256 + 6) {
		code = scripts["grants_5_7_6.mysql"]
	} else {
		code = scripts["grants.mysql"]
	}

	grantsFilePath := installPath + "/mysql.grants"

	grantsCode := []byte(code)

	grantsFile, err := os.Create(grantsFilePath)
	Check(err)

	_, err = grantsFile.Write(grantsCode)
	Check(err)

	grantsFile.Close()
	return code
}

func MySQLInitPrivileges(instanceDir2Port map[string]int) {
	fmt.Println("Init MySQL Privileges...")
	for dir, port := range instanceDir2Port {
		socketPath := fmt.Sprintf("%s/mysql_sandbox%d.sock", dir, port)
		dsn := "root:@unix(" + socketPath + ")/mysql"
		stmts := strings.Split(grantsCode, "\n")
		RunOperat(dsn, stmts)
	}
}

func RunOperat(dsn string, stmts []string) {
	db, err := sql.Open("mysql", dsn)
	Check(err)
	for _, each_stmt := range stmts {
		_, err = db.Exec(each_stmt)
		Check(err)
	}
	db.Close()
}

func InstallAndStartMySQL(mysqlDir string, installPath string, mysqlPackagePath string, instanceDir2Port map[string]int) {
	MySQLInstallMultiDBs(mysqlDir, installPath, mysqlPackagePath, instanceDir2Port)

	InstallMySQLScripts(mysqlDir, installPath, instanceDir2Port)

	/** start MySQL */
	StartMySQL(installPath)

	/** execute grants options **/
	MySQLInitPrivileges(instanceDir2Port)
}
