package main

import "fmt"

func main() {
	var a *int
	fmt.Println(a)
	var f func(a, b int) int
	fmt.Println(f)
	var b []string
	for _, i := range b {
		fmt.Println(i)
	}
	fmt.Println(len(b))
}
