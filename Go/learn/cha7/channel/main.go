package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	c := make(chan int)
	for i := 0; i < 5; i++ {
		go sleepGopher(i, c)
	}
	timeout := time.After(2 * time.Second)
	for i := 0; i < 5; i++ {
		select {
		case gopherID := <-c:
			fmt.Println(gopherID)
		case <-timeout:
			fmt.Println("no patience")
			return
		}
	}
}

func sleepGopher(id int, c chan int) {
	time.Sleep(time.Duration(rand.Intn(4000)) * time.Millisecond)
	c <- id
}
