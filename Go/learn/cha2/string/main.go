package main

import "fmt"

func main() {
	a := `ed23d2\n
	dwedw`
	println(a)

	var c1 rune = 960
	var c2 rune = 24144
	c3 := 'A'
	fmt.Printf("%v %v\n", c1, c2)
	fmt.Printf("%c %c\n", c1, c2)
	fmt.Println(c3)
	s1 := "dewdf"
	fmt.Printf("%c\n", s1[2])
	for i, c := range s1 {
		fmt.Printf("%v %c\n", i, c)
	}
}
