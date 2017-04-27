package utils

import (
	"fmt"
	"os"
)

func InitScript4All(installPath string, scriptsDict map[string]string) {
	startAllScript := `#!/bin/bash
SBDIR="%s"
$SBDIR/startallmysql
$SBDIR/dbscale-start.sh
`
	scriptsDict["startall"] = fmt.Sprintf(startAllScript, installPath)
	stopAllScript := `#!/bin/bash
SBDIR="%s"
$SBDIR/dbscale-stop.sh
$SBDIR/stopallmysql
`
	scriptsDict["stopall"] = fmt.Sprintf(stopAllScript, installPath)
}

func InstallScripts4All(installPath string) {
	script4AllDict := make(map[string]string)

	/*** Install startallscript ***/
	InitScript4All(installPath, script4AllDict)
	for scriptName, script := range script4AllDict {
		scriptFilePath := installPath + "/" + scriptName
		scriptFile, err := os.Create(scriptFilePath)
		Check(err)
		_, err = scriptFile.Write([]byte(script))
		Check(err)
		scriptFile.Chmod(0744)
		scriptFile.Close()
	}
}
