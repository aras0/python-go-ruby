package main

import (
    "log"
    "os/exec"
    "os"
    "fmt"
    "time"
)


func main() {

    start := time.Now()

    cmd := exec.Command("/usr/bin/ruby", "calculations.rb", "5 1 2 + 4 * + 3 -")

    elapsed := time.Since(start)

    log.Printf("Time %s", elapsed)

    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    log.Println(cmd.Run())

}