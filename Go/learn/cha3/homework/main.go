package main

import "fmt"

func cTof(t float64) float64 {
	return float64(32 + 9*t/5)
}

func fToc(t float64) float64 {
	return float64((t - 32) * 5 / 9)
}

func drawLine() {
	fmt.Println("====================")
}

func drawUnitcf() {
	fmt.Println("| ℃        | ℉     ")
}

func drawUnitfc() {
	fmt.Println("| ℉        | ℃     ")
}

func drawLinecf(t float64) {
	fmt.Printf("| %-9.1f| %-9.1f\n", t, cTof(t))
}

func drawLinefc(t float64) {
	fmt.Printf("| %-9.1f| %-9.1f\n", t, fToc(t))
}

func drawTable(line func(t float64), unit func()) {
	drawLine()
	unit()
	drawLine()
	var i float64
	for i = -40; i <= 100; i += 5 {
		line(i)
	}
	drawLine()
}

func main() {
	drawTable(drawLinecf, drawUnitcf)
	drawTable(drawLinefc, drawUnitfc)
}
