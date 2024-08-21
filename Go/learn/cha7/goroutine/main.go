package main

import (
	"fmt"
	"time"
)

func main() {
	for i := 0; i < 5; i++ {
		go sleepGopher(i)
	}
	time.Sleep(4 * time.Second)
}

func sleepGopher(id int) {
	time.Sleep(3 * time.Second)
	fmt.Println("...snore...", id)
}
