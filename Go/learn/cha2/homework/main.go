package main

import "fmt"

func main() {
	key := "GOLANG"
	secret := "CSOITEUIWUIZNSROCNKFD"
	re := ""
	for i, v := range secret {
		num := key[i%len(key)] - 'A'
		re += string('A' + (v-'A'+rune(26)-rune(num))%26)
	}
	fmt.Println(re)

	re1 := "WEDIGYOULUVTHEGOPHERS"
	secret1 := ""
	for i, v := range re1 {
		num := key[i%len(key)] - 'A'
		secret1 += string('A' + (v-'A'+rune(num))%26)
	}
	fmt.Println(secret1)
}
