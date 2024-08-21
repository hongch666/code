package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	files, err := ioutil.ReadDir("..")
	if err != nil {
		fmt.Println(err)
		defer os.Exit(1)
		fmt.Println(666)
	}

	for _, file := range files {
		fmt.Println(file.Name())
	}

	defer func() {
		if e := recover(); e != nil {
			fmt.Println(e)
		}
	}()

	panic("fuck")
}
