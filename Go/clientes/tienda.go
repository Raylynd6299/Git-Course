package main

import (
	"fmt"
	"strconv"
)

//Operacion -> Es la interfaz de lo que se podra hacer con los objetos
type Operacion interface {
	ChecarStock() int
	Vender() int
	ChecarPrecio() float32
	ChecarGarantia() int
}

//Objeto -> Esta definicion del todos los objetos
type Objeto struct {
	Nombre string
	Costo  float32
}

//Tecnologia -> Es el objeto con caracteristicas de tecnologia
type Tecnologia struct {
	Objeto
	Garantia int
	Stock    int
}

//ElectroDomesticos -> es un objeto electrodomestico
type ElectroDomesticos struct {
	Objeto
	Garantia int
	Stock    int
}

//Cliente -> Define todos los clientes de la operacion
type Cliente struct {
	Nombre string
	Edad   int
	Email  string
	Total  int
}

//GetInfoCli -> Nos da la info del cliente
func (cli *Cliente) GetInfoCli() (string, int) {
	return "Nombre: " + cli.Nombre + ", Edad: " + strconv.Itoa(cli.Edad) + ", Email: " + cli.Email, cli.Total
}

//Operaciones de los Tipos de objeto

//ChecarStock -> Checar stock de tecnologia
func (tech *Tecnologia) ChecarStock() int {
	return tech.Stock
}

//ChecarPrecio -> nos da el precio del objeto
func (tech *Tecnologia) ChecarPrecio() float32 {
	return tech.Costo
}

//Vender -> Funcion para vender Tecnologia
func (tech *Tecnologia) Vender() int {
	return tech.Stock - 1
}

//ChecarGarantia -> Checamos que tenga garantia
func (tech *Tecnologia) ChecarGarantia() int {
	return tech.Garantia
}

//ChecarStock -> Checar stock de tecnologia
func (elec *ElectroDomesticos) ChecarStock() int {
	return elec.Stock
}

//ChecarPrecio -> nos da el precio del objeto
func (elec *ElectroDomesticos) ChecarPrecio() float32 {
	return elec.Costo
}

//Vender -> Funcion para vender Tecnologia
func (elec *ElectroDomesticos) Vender() int {
	return elec.Stock - 1
}

//ChecarGarantia -> Checamos que tenga garantia
func (elec *ElectroDomesticos) ChecarGarantia() int {
	return elec.Garantia
}
func main() {
	var TiraDeClientes []Cliente
	for {
		var nombre, email string
		var edad, op int

		fmt.Println("Ingrese el Nombre del Cliente")
		fmt.Scanf("%v", &nombre)
		fmt.Println("Ingrese el Email del Cliente")
		fmt.Scanf("%v", &email)
		fmt.Println("Ingrese el Edad del Cliente")
		fmt.Scanf("%v", &edad)

		TiraDeClientes = append(TiraDeClientes, Cliente{Nombre: nombre, Email: email, Edad: edad})

		fmt.Println("1:siguiente cliente, 2: Fin")
		fmt.Scanf("%v", &op)
		if op == 2 {
			break
		}
	}

	var TiraDeTech []Tecnologia
	var TiraDeElec []ElectroDomesticos
	for {
		var tip, op int
		var nombre string
		var costo float32

		fmt.Println("1: Tecnologia, 2: ElectroDomestico")
		fmt.Scanf("%v", &tip)
		fmt.Println("Ingrese el Nombre del Cliente")
		fmt.Scanf("%v", &nombre)
		fmt.Println("Ingrese el Costo del Cliente")
		fmt.Scanf("%v", &costo)

		if tip == 1 {
			var stock int
			var garantia int

			fmt.Println("Ingrese el Stock del Cliente")
			fmt.Scanf("%v", &stock)
			fmt.Println("Ingrese el Garanti del Cliente")
			fmt.Scanf("%v", &garantia)

			TiraDeTech = append(TiraDeTech, Tecnologia{Objeto{nombre, costo}, stock, garantia})
		} else if tip == 2 {
			var stock int
			var garantia int

			fmt.Println("Ingrese el Stock del Cliente")
			fmt.Scanf("%v", &stock)
			fmt.Println("Ingrese el Garanti del Cliente")
			fmt.Scanf("%v", &garantia)
			TiraDeElec = append(TiraDeElec, ElectroDomesticos{Objeto{nombre, costo}, stock, garantia})
		}
		fmt.Println("1:siguiente objeto, 2: Fin")
		fmt.Scanf("%v", &op)
		if op == 2 {
			break
		}
	}

	for _, cli := range TiraDeClientes {
		fmt.Println(cli.GetInfoCli())
	}

}
