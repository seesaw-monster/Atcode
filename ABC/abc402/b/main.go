package main

import (
	"bufio"
	"fmt"
  "os"
  "strings"
)

func main(){
  var q int
  fmt.Scanln(&q)

  scanner := bufio.NewScanner(os.Stdin)
  queue := []string{}

  for i:=0; i<q; i++{
    scanner.Scan()
    line := scanner.Text()
    inputs := strings.Fields(line)

    if inputs[0]=="1"{
      queue = append(queue, inputs[1])
    } else {
      fmt.Println(queue[0])
      queue = queue[1:]
    }
  }
}
