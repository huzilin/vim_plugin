package utils

import (
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
)

func InitDBScaleServiceScript(installPath string) {
	backQuotes := "`"
	serviceScript := fmt.Sprintf(dbscaleServiceScript, installPath, backQuotes, backQuotes, backQuotes, "%s", backQuotes, backQuotes, "%s", backQuotes, backQuotes, backQuotes, backQuotes, "%s", backQuotes, backQuotes, "%s", backQuotes)
	serviceScriptPath := installPath + "/dbscale/dbscale-service.sh"
	err := os.Remove(serviceScriptPath)
	Check(err)
	f, err := os.Create(serviceScriptPath)
	Check(err)
	f.Write([]byte(serviceScript))
	err = f.Chmod(0755)
	Check(err)
	f.Close()
}

func InstallDBScale(dbscalePackagePath string, installPath string) {
	fmt.Println("Installing DBScale...")
	Decompress(dbscalePackagePath, installPath)
	InitDBScaleServiceScript(installPath)
}

func InitDBScaleConfig(dbUser string, dbPassword string, installPath string, mysqlStartPort int, dbscalePort int) string {

	config = fmt.Sprintf(dbscaleConfig, "log/dbscale.log", dbUser, dbPassword, dbscalePort, dbUser, dbPassword, mysqlStartPort, dbUser, dbPassword, mysqlStartPort+1, dbUser, dbPassword, mysqlStartPort+2, dbUser, dbPassword, mysqlStartPort+3, dbUser, dbPassword, dbUser, dbPassword, mysqlStartPort+4, dbUser, dbPassword, mysqlStartPort+5, dbUser, dbPassword, dbUser, dbPassword)
	return config
}

func InstallDBScaleConfig(dbUser string, dbPassword string, installPath string, mysqlStartPort int, dbscalePort int) {
	fmt.Println("Initing DBScale Configure...")
	config := InitDBScaleConfig(dbUser, dbPassword, installPath, mysqlStartPort, dbscalePort)
	configPath := installPath + "/dbscale/dbscale.conf"
	err := ioutil.WriteFile(configPath, []byte(config), 0644)
	Check(err)
}

func StartDBScale(installPath string) {
	fmt.Println("Starting DBScale...")
	cmd := exec.Command(installPath+"/dbscale/dbscale-service.sh", "start")
	cmd.Dir = installPath + "/dbscale"
	cmd.Stderr = os.Stdout
	err := cmd.Run()
	Check(err)
}

func InitDBScaleScripts(installPath string, mysqlDirPath string, dbUser string, dbPassword string, dbscalePort int, DBScaleScript map[string]string) {
	DBScaleScript["dbscale-start.sh"] = installPath + "/dbscale/dbscale-service.sh start"
	DBScaleScript["dbscale-stop.sh"] = installPath + "/dbscale/dbscale-service.sh stop"
	loginScript := "%s/bin/mysql -u%s -p%s -h127.0.0.1 -P%d"
	loginScript = fmt.Sprintf(loginScript, mysqlDirPath, dbUser, dbPassword, dbscalePort)
	DBScaleScript["loginDBScale"] = loginScript
}

func InstallDBscaleScripts(installPath string, mysqlDirPath string, dbUser string, dbPassword string, dbscalePort int) {
	fmt.Println("Installing DBScale Scripts And Sandbox Scripts...")
	/*** init stop&start scripts ***/
	DBScaleScript := make(map[string]string)
	InitDBScaleScripts(installPath, mysqlDirPath, dbUser, dbPassword, dbscalePort, DBScaleScript)

	/*** install DBScale scripts ***/
	for scriptName, script := range DBScaleScript {
		scriptPath := installPath + "/" + scriptName
		scriptf, err := os.Create(scriptPath)
		Check(err)
		scriptf.Write([]byte(script))
		err = scriptf.Chmod(0755)
		Check(err)
		scriptf.Close()
	}
}

func InitPartitionData(dbscalePort int, dbUser string, dbPassword string) {
	fmt.Println("Initing Partition Data...")
	stmts := []string{
		"create table part_tb01 (id int primary key, c1 int, c2 varchar(50)) engine=innodb",
		"create table part_tb02 (id int primary key, c1 int, c2 varchar(50)) engine=innodb",
		"insert into part_tb01 values (1, 1, 'hello world.')",
		"insert into part_tb01 values (2, 2, 'welecome to dbscale.')",
		"insert into part_tb01 values (3, 3, 'this is a demo partition table.')",
		"insert into part_tb01 values (4, 4, 'plz try and have fun.')",
	}
	for i := 5; i < 101; i++ {
		sql := "insert into part_tb01 values (%d, %d, 'this is test text%d')"
		sql = fmt.Sprintf(sql, i, i, i)
		stmts = append(stmts, sql)
	}
	dsn := "%s:%s@tcp(127.0.0.1:%d)/test"
	dsn = fmt.Sprintf(dsn, dbUser, dbPassword, dbscalePort)
	RunOperat(dsn, stmts)
}

func InstallAndStartScale(mysqlDirPath string, dbscalePackagePath string, installPath string, mysqlStartPort int, dbscalePort int) {
	InstallDBScale(dbscalePackagePath, installPath)
	InstallDBScaleConfig(Options["dbUser"], Options["dbPassword"], installPath, mysqlStartPort, dbscalePort)
	StartDBScale(installPath)
	InstallDBscaleScripts(installPath, mysqlDirPath, Options["dbUser"], Options["dbPassword"], dbscalePort)

	InstallScripts4All(installPath)

	InitPartitionData(dbscalePort, Options["dbUser"], Options["dbPassword"])
}
