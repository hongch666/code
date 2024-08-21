package main

import "fmt"

func coutlist(list []string) {
	for _, i := range list {
		println(i)
	}
}

func t(s1 string, arrs ...string) []string {
	newslice := make([]string, len(arrs))

	for i := range arrs {
		newslice[i] = s1 + arrs[i]
	}
	return newslice
}

func main() {
	b := [...]string{"nb", "sb", "hello", "go", "code", "666"}
	slice1 := b[:2]
	slice2 := b[2:]
	slice3 := b[:]
	fmt.Println(slice1)
	fmt.Println(slice2)
	fmt.Println(slice3)
	s := "hello world"
	sl := s[1:3]
	println(sl)
	sli := []string{"nb", "sb", "hello", "go", "code", "666"}
	fmt.Println(sli)
	coutlist(sli)
	sli = append(sli, "2333")
	fmt.Println(sli)
	fmt.Println(len(sli), cap(sli))
	sli2 := b[:4:4]
	fmt.Println(len(sli2), cap(sli2))
	sli2 = append(sli2, "123")
	fmt.Println(sli2)
	fmt.Println(len(sli2), cap(sli2))
	sli3 := make([]string, 0, 10)
	fmt.Println(sli3)
	fmt.Println(len(sli3), cap(sli3))
	sli3 = append(sli3, "nb")
	fmt.Println(sli3)
	fmt.Println(len(sli3), cap(sli3))
	fmt.Println(t("nb", "123", "sb"))
	fmt.Println(t("sb", sli2...))
}
