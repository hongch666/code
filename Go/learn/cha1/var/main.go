package main

import (
	"fmt"
	"math/rand"
)

var n = "package"

func main() {
	const a = 123
	var b = 666
	var (
		c1 = 678
		c2 = 789
	)
	c1++
	b = 66
	fmt.Println(a)
	fmt.Printf("nb %-4v nb\n", b)
	fmt.Printf("%v %v\n", c1, c2)
	var num = rand.Intn(10) + 1
	fmt.Println(num)
	count := 10
	fmt.Println(count)
	fmt.Println(n)
}
