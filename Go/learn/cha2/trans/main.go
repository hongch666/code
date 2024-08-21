package main

import (
	"fmt"
	"strconv"
)

func main() {
	a := 123.534
	fmt.Println(int(a))
	fmt.Println("abcd " + strconv.Itoa(int(a)) + " haha")
}
