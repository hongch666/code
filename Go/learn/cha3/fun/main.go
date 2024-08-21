package main

import "fmt"

func kToC(k float64) float64 {
	k -= 273.15
	return k
}

func main() {
	k := 294.0
	c := kToC(k)
	fmt.Println(k, " ", c)
}
