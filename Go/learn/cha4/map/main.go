package main

import "fmt"

func main() {
	a := map[string]int{
		"nb": 123,
		"sb": 456,
	}
	fmt.Println(a["sb"])
	a["nb"] = 23
	fmt.Println(a["nb"])
	if _, ok := a["nb1"]; ok {
		fmt.Println(a["nb1"])
	} else {
		fmt.Println("key not exit")
	}
	delete(a, "sb")
	fmt.Println(a)
	b := make(map[float64]int, 3)
	fmt.Println(len(b))
	for key, value := range a {
		fmt.Println(key, value)
	}
	var set_arr = []float64{
		3.2, 4, 3.5, 323,
	}
	set := make(map[float64]bool)
	for _, t := range set_arr {
		set[t] = true
	}
	if set[3.2] {
		fmt.Println(3.2)
	}
}
