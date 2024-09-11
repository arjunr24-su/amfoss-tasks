package main
import (
    "fmt"
    "io/ioutil"
    "strconv"
    "strings"
)
func main() {
    data, _ := ioutil.ReadFile("input.txt")
    n, _ := strconv.Atoi(strings.TrimSpace(string(data)))
    var output strings.Builder
    for i := 0; i < n; i++ {
        output.WriteString(strings.Repeat(" ", n-i-1) + strings.Repeat("*", 2*i+1) + "\n")
    }
    for i := n-2