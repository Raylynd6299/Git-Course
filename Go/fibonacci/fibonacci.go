package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	var swap, lim, num1, num2 int
	num1 = 0
	num2 = 1

	file, err := os.Create("fibo.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	//Pedir el numero de fibonacci a obtener
	fmt.Scanf("%d", &lim)

	//generamos el proceso
	for i := 0; i < lim; i++ {
		if i <= 0 {
			//fmt.Printf("%d, ", num1)
			//fmt.Printf("%d, ", num2)
			file.WriteString(strconv.Itoa(num1) + ", ")
			file.WriteString(strconv.Itoa(num2) + ", ")
		}
		swap = num2
		num2 = num1 + num2
		num1 = swap
		file.WriteString(strconv.Itoa(num2) + ", ")
	}
	fmt.Println("\nbye")
}
