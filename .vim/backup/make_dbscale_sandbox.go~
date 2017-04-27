package main

import (
	"flag"
	"fmt"
	utils "github.com/louishust/dbscale_sandbox/utils"
	"os"
	"os/user"
	"strings"
)

var (
	installPath        *string
	mysqlDirPath       *string
	mysqlPackagePath   *string
	mysqlStartPort     *int
	dbscalePackagePath *string
	dbscalePort        *int
	dirPortMap         = make(map[string]int)
)

func init_options() {
	var curUser, _ = user.Current()
	var defaultInstallPath = curUser.HomeDir + "/sandboxes"
	var defaultStartPort = 3210
	var defaultDBSalePort = 13001
	installPath = flag.String("install-path", defaultInstallPath, "path to install")
	mysqlDirPath = flag.String("mysql-dir", "", "mysql installed directory, if not declare, sandbox will auto find")
	mysqlPackagePath = flag.String("mysql-package-path", "", "mysql package path")
	mysqlStartPort = flag.Int("mysql-start-port", defaultStartPort, "mysql start port")
	dbscalePackagePath = flag.String("dbscale-package-path", "", "DBScale package path")
	dbscalePort = flag.Int("dbscale-port", defaultDBSalePort, "DBScale port")
}

func parse_options() {
	flag.Parse()
	args := flag.Args()
	if len(args) != 0 {
		flag.Usage()
		os.Exit(1)
	}

	if *dbscalePackagePath == "" {
		fmt.Println("dbscale-package-path must be declare!")
		os.Exit(1)
	}

	/** check dbscale package path */
	fileinfo, err := os.Stat(*dbscalePackagePath)
	if err != nil {
		fmt.Println("dbscale-package-path:" + *dbscalePackagePath + " no such file!")
		os.Exit(1)
	} else if fileinfo.IsDir() {
		fmt.Println("dbscale-package-path:" + *dbscalePackagePath + "should be a file but not a directory!")
		os.Exit(1)
	} else if !strings.HasSuffix(fileinfo.Name(), "gz") && !strings.HasSuffix(fileinfo.Name(), ".bz2") {
		fmt.Println("dbscale-package-path:" + *dbscalePackagePath + "should be gz or bz2 file!")
		os.Exit(1)
	}

	if *mysqlPackagePath != "" {
		*mysqlDirPath = *installPath + "/mysql"
	} else if *mysqlDirPath != "" {
	} else {
		*mysqlDirPath, _ = utils.FindMySQLInstallDir()
		if *mysqlDirPath == "" {
			fmt.Println("Can not find MySQL install directory!")
			os.Exit(1)
		}
	}
}

func exists(path string) (bool, error) {
	_, err := os.Stat(path)
	if err == nil {
		return true, nil
	}
	if os.IsNotExist(err) {
		return false, nil
	}
	return true, err
}

func init_directories() {
	rep1Dir := *installPath + "/rep_mysql_sandbox1"
	rep2Dir := *installPath + "/rep_mysql_sandbox2"
	authDir := *installPath + "/auth_mysql_sandbox"

	ret1, _ := exists(rep1Dir)
	ret2, _ := exists(rep2Dir)
	ret3, _ := exists(authDir)

	if ret1 || ret2 || ret3 {
		fmt.Println(rep1Dir + " or " + rep2Dir + " or " + authDir + " already exists!!!")
		os.Exit(1)
	}

	os.MkdirAll(rep1Dir, 0777)
	os.MkdirAll(rep2Dir, 0777)
	os.MkdirAll(authDir, 0777)

	dirPortMap[authDir+"/master"] = *mysqlStartPort
	dirPortMap[authDir+"/slave"] = *mysqlStartPort + 1
	dirPortMap[rep1Dir+"/master"] = *mysqlStartPort + 2
	dirPortMap[rep1Dir+"/slave"] = *mysqlStartPort + 3
	dirPortMap[rep2Dir+"/master"] = *mysqlStartPort + 4
	dirPortMap[rep2Dir+"/slave"] = *mysqlStartPort + 5
}

func main() {
	init_options()
	parse_options()
	init_directories()
	utils.InstallAndStartMySQL(*mysqlDirPath, *installPath, *mysqlPackagePath, dirPortMap)
	utils.InstallAndStartScale(*mysqlDirPath, *dbscalePackagePath, *installPath, *mysqlStartPort, *dbscalePort)
	fmt.Println("DBScale Sandbox installed successfully!")
}
