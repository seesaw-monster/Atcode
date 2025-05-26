package main

import (
  "fmt"
)

func main(){
  var N int
  fmt.Scan(&N)
  var P  = make([]int, N)
  for i:=0;i<N;i++{
    fmt.Scan(&P[i])
  }

  var rank = make([]int, N)
  var index = make([]int, N)
  for i, _ := range(index){
    index[i] = i
  }

  r:=1
  k:=0
  all_count:=0
  var max_num int
  for r<=N {
    max_num = 0
    for _, p := range(P){
      if p>max_num {
        max_num=p
        k=1
      } else if p==max_num {
        k++
      }
    }

    all_count+=k
    Q := make([]int, N-all_count)
    tmp := make([]int, N-all_count)
    c := 0
    for i, p := range(P){
      if p==max_num{
        rank[index[i]]=r
      } else {
        Q[c]=p
        tmp[c]=index[i]
        c++
      }
    }
    r+=k
    P = Q
    index = tmp
  }

  for _, r := range(rank){
    fmt.Println(r)
  }
}
