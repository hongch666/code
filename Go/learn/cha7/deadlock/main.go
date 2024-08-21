package main

func main() {
	c := make(chan int)
	go func() {
		c <- 2
	}()
	<-c
}
