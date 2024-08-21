package main

import "fmt"

type t struct {
	a int
	b string
}

func change(t1 *t) {
	t1.a += 1
}

func (t1 *t) change() {
	t1.a += 1
}

func main() {
	a := 42
	p := &a
	fmt.Println(p)
	t1 := &t{a: 2, b: "666"}
	t1.a = 3
	fmt.Printf("%+v\n", t1)
	arr := &[3]int{1, 2, 3}
	fmt.Println(arr[1])
	fmt.Println(arr[1:])
	change(t1)
	t1.change()
	fmt.Printf("%+v\n", t1)
	fmt.Println(&t1.a)
}
