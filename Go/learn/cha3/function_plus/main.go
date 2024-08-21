package main

import (
	"fmt"
	"math/rand"
)

type k float64

func te() k {
	return k(rand.Intn(151) + 150)
}

func cout(sample int, sensor func() k) {
	for i := 0; i < sample; i++ {
		k := sensor()
		fmt.Println(k)
	}
}

var f = func() {
	fmt.Println("yes")
}

func main() {
	n := te
	fmt.Println(n())
	cout(3, te)
	f()
	func() {
		fmt.Println("no")
	}()
}
