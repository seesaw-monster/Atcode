package main

import (
	"fmt"
	"unicode"
)

func main(){
  var S string
  fmt.Scanln(&S)

  return_s := ""
  for _, s := range S {
    if unicode.IsUpper(s) {
      return_s=return_s+string(s)
    }
  }

  fmt.Println(return_s)
}
