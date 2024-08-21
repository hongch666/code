package main

import (
	"fmt"
	"math/rand"
	"strings"
)

func main() {
	fmt.Println(123)

	var s1 = "nbnbnbnb"
	var s2 = strings.Contains(s1, "nb")

	fmt.Println(s2)
	fmt.Println(1 < 2)

	if s1 == "nb" && s2 {
		fmt.Println("yes")
	} else if s1 == "sb" {
		fmt.Println("mid")
	} else {
		fmt.Println("no")
	}

	switch s1 {
	case "sbsbsb":
		fmt.Println("case 1")
	case "nbnbnbnb":
		fmt.Println("case 2")
		fallthrough
	default:
		fmt.Println("default")
	}

	var count = 5
	for count > 0 {
		fmt.Println(count)
		count--
	}

	switch num := rand.Intn(10); num {
	case 1:
		println(num)
	case 2:
		println(2)
	default:
		println("other")
	}
}
