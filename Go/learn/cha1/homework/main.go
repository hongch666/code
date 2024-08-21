package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("Spaceline         Days Trip type  Price")
	fmt.Println("=======================================")
	// fmt.Println("Space Adventures    24 Round-trip $ 100")
	count := 10
	for count > 0 {
		num1 := rand.Intn(3)
		spaceline := ""
		switch num1 {
		case 0:
			spaceline = "Space Adventures"
		case 1:
			spaceline = "SpaceX"
		case 2:
			spaceline = "Virgin Galactic"
		default:
			spaceline = "no"
		}

		num2 := rand.Intn(2)
		trip_type := ""
		switch num2 {
		case 0:
			trip_type = "Round-trip"
		case 1:
			trip_type = "One-way"
		default:
			trip_type = "no"
		}

		v := rand.Intn(15) + 16
		days := 62100000 / v / (3600 * 24)

		price := rand.Intn(15) + 36

		if num2 == 0 {
			days *= 2
			price *= 2
		}

		fmt.Printf("%-16v  %4v %-10v $%4v\n", spaceline, days, trip_type, price)

		count--
	}

	// fmt.Println(rand.Intn(3))
}
