package main

import (
	"fmt"
	"math/big"
	"time"
)

func main() {
	fmt.Println("nb")
	a := 1.0 / 3
	fmt.Println(a)
	fmt.Printf("%v\n", a)
	fmt.Printf("%f\n", a)
	fmt.Printf("%.3f\n", a)
	fmt.Printf("%4.1f\n", a)
	fmt.Printf("%04.1f\n", a)

	fmt.Printf("%T\n", a)
	var red, green, blue uint8 = 0, 141, 213
	fmt.Printf("color: #%02x%02x%02x;\n", red, green, blue)

	future := time.Unix(12622780800, 0)
	fmt.Println(future)

	num1 := big.NewInt(299792)
	num2 := big.NewFloat(86400)
	fmt.Println(num1, num2)

	num3 := new(big.Int)
	num3.SetString("24000000000000000000000000", 10)
	fmt.Println(num3)

	num4 := new(big.Int)
	num4.Div(num3, num1)
	fmt.Println(num4)
}
