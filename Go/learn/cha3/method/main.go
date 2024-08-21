package main

import "fmt"

type cel float64
type kel float64

func (k kel) celsius() cel {
	return cel(k - 273.15)
}

func main() {

	var t kel = 20
	t += 10
	var t1 cel = t.celsius()
	fmt.Println(t1)
}
