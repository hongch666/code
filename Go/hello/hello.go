package main

import "fmt"

/*mod文件创建：
1.目录下右键，选择“在集成终端中打开”
2.终端中输入“go mod init 包的标识符”
*/
// ? question
// // no use
// todo something to do
// * normal
// ! warning
func BubbleSort2(arr [6]int) {
	n := len(arr)
	for i := n - 1; i > 0; i-- { // 逆序遍历
		for j := 0; j < i; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
	fmt.Println(arr)
}
func main() {
	var arr [6]int = [6]int{7, 4, 9, 3, 5, 2}
	BubbleSort2(arr)
	fmt.Println("hello world")
	fmt.Println("666")
}
