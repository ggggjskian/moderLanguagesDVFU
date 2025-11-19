package main

import "fmt"

type DB_connection struct {
	db_user_name string
	db_user_password string
	db_name string
	db_host_name string
	db_port int
}

func calculate_two_numbers(x, y int) int {
	return x + y
}

func main() {
	con1 := DB_connection{"admin", "changeme123","task_db","localhost", 8080}
	fmt.Println(con1)
	fmt.Print(calculate_two_numbers(2, 193))
}
