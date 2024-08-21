package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type nt struct {
	L1 float64 `json:"change1"`
	L2 float64 `json:"change2"`
}

func f1(nt1 nt) nt {
	fmt.Println(nt1)
	return nt{0.0, 0.0}
}

func (n nt) m1() float64 {
	return n.L1 + n.L2
}

func main() {
	var a struct {
		L1 float64
		L2 float64
	}
	a.L1 = -4.3
	a.L2 = 4.7
	fmt.Println(a.L1, a.L2)
	var b nt
	b.L1 = 1.23
	b.L2 = 4.56
	fmt.Println(b.L1, b.L2)
	fmt.Println(f1(b))
	c := nt{L1: 3.2}
	fmt.Println(c)
	fmt.Printf("%v\n", c)
	fmt.Printf("%+v\n", c)
	bytes, err := json.Marshal(c)
	exitOnError(err)
	fmt.Println(string(bytes))
	fmt.Println(b.m1())
}

func exitOnError(err error) {
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
