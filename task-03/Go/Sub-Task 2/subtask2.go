package main
import (
    "io/ioutil"
)
func main() {
    data, _ := ioutil.ReadFile("input.txt")
    ioutil.WriteFile("output.txt", data, 0644)
}
