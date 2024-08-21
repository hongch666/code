package main

import "fmt"

/* type report struct {
	sol         int
	temperature temperature
	location    location
} */

type report struct {
	sol int
	temperature
	location
}

type temperature struct {
	high, low celsius
}

type location struct {
	lat, long float64
}

type celsius float64

func (t temperature) average() float64 {
	return float64(t.high) + float64(t.low)
}

func main() {
	b := location{-4.5, 137.4}
	t := temperature{high: -1.0, low: -78.0}
	report := report{
		sol:         15,
		temperature: t,
		location:    b,
	}
	fmt.Printf("%+v\n", report)
	fmt.Println(t.average())
	fmt.Println(report.average())
}
