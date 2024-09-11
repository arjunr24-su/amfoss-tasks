package main
import (
    "fmt"
    "strings"
)
func main() {
    var n int
    fmt.Print("Enter a number: ")
    fmt.Scan(&n)
    for i := 0; i < n; i++ {
        fmt.Println(strings.Repeat(" ", n-i-1) + strings.Repeat("*", 2*i+1))
    }
    for i := n-2; i >= 0; i-- {
        fmt.Println(strings.Repeat(" ", n-i-1) + strings.Repeat("*", 2*i+1))
    }
}