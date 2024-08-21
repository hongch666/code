package main

import "fmt"

type talker interface {
	talk() string
}

type t1 struct{}

func (t t1) talk() string {
	return "sb"
}

func shout(t talker) {
	fmt.Println(t.talk())
}

func main() {
	a := t1{}
	fmt.Println(a.talk())
	shout(a)
}
