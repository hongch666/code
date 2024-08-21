package main

import (
	"fmt"
	"math/rand"
)

type mover interface {
	move() string
}

type eater interface {
	eat() string
}

type Stringer interface {
	name() string
}

type animal struct {
	na     string
	action string
	food   string
}

func (a animal) name() string {
	return a.na
}

func (a animal) eat() string {
	return a.food
}

func (a animal) move() string {
	return a.action
}

func main() {
	fmt.Println(123)
	var animals []animal = []animal{
		animal{na: "dog", action: "running", food: "meat"},
		animal{na: "cat", action: "walking", food: "fish"},
		animal{na: "bird", action: "flying", food: "air"},
	}
	for i := 0; i <= 71; i++ {
		hour := i % 24
		var day int = i/24 + 1
		if (hour >= 0 && hour < 6) || (hour >= 18 && hour <= 23) {
			fmt.Printf("第%v天第%v小时,所有动物都在睡觉\n", day, hour)
		} else {
			a := rand.Intn(3)
			b := rand.Intn(2)
			if b == 0 {
				fmt.Printf("第%v天第%v小时,%v正在通过%v移动\n", day, hour, animals[a].name(), animals[a].move())
			} else {
				fmt.Printf("第%v天第%v小时,%v正在吃%v\n", day, hour, animals[a].name(), animals[a].eat())
			}
		}
	}
}
