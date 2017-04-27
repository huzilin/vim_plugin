package utils

import (
	"archive/tar"
	"compress/bzip2"
	"compress/gzip"
	"fmt"
	"io"
	"os"
	"path"
)

func decompressBzip2(compressedFilePath string, targetPath string) {
	os.MkdirAll(targetPath, os.ModePerm)

	cf, err := os.Open(compressedFilePath)
	Check(err)
	defer cf.Close()

	bz2f := bzip2.NewReader(cf)

	tr := tar.NewReader(bz2f)

	for {
		hdr, err := tr.Next()
		if err == io.EOF {
			break
		}
		Check(err)

		if hdr.Typeflag != tar.TypeDir {
			os.MkdirAll(targetPath+"/"+path.Dir(hdr.Name), os.ModePerm)
			targetFilePath := targetPath + "/" + hdr.Name
			fw, _ := os.Create(targetFilePath)
			Check(err)
			_, err = io.Copy(fw, tr)
			Check(err)
			fw.Close()
			os.Chmod(targetFilePath, os.FileMode(hdr.Mode))
		}
	}
}

func decompressgzip(compressedFilePath string, targetPath string) {
	os.MkdirAll(targetPath, os.ModePerm)

	cf, err := os.Open(compressedFilePath)
	Check(err)
	defer cf.Close()

	gzf, err := gzip.NewReader(cf)
	Check(err)
	defer gzf.Close()

	tr := tar.NewReader(gzf)

	for {
		hdr, err := tr.Next()
		if err == io.EOF {
			break
		}
		Check(err)

		if hdr.Typeflag != tar.TypeDir {
			os.MkdirAll(targetPath+"/"+path.Dir(hdr.Name), os.ModePerm)
			targetFilePath := targetPath + "/" + hdr.Name
			fw, _ := os.Create(targetFilePath)
			Check(err)
			_, err = io.Copy(fw, tr)
			Check(err)
			fw.Close()
			os.Chmod(targetFilePath, os.FileMode(hdr.Mode))
		}
	}
}

func Decompress(compressedFilePath string, targetPath string) {
	baseName := path.Base(compressedFilePath)
	extName := path.Ext(baseName)
	switch extName {
	case ".gz":
		decompressgzip(compressedFilePath, targetPath)
	case ".bz2":
		decompressBzip2(compressedFilePath, targetPath)
	default:
		fmt.Println("Not supported decompress this file type!")
		os.Exit(1)
	}
}
