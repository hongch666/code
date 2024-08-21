package main

import "fmt"

func main() {
	var a [8]string
	a[0] = "abc"
	a[1] = "cde"
	a[2] = "nb"
	fmt.Println(a[4])
	fmt.Println(a)
	b := [...]string{"nb", "sb", "hello", "go", "code", "666"}
	fmt.Println(b[1])
	for i, s := range b {
		fmt.Println(i, " ", s)
	}
	slice1 := b[0:2]
	slice2 := b[2:6]
	fmt.Println(slice1)
	fmt.Println(slice2)
}
