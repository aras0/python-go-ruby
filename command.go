package main

import "C"
import (
    //"bytes"
    "os/exec"
    "log"
    "time"
    "fmt"
    //"strings"
    "bufio"
    "os"
)

//export run
func run()  {

    var slice []string

    f, err := os.OpenFile("logfile", os.O_RDWR | os.O_CREATE | os.O_APPEND, 0666)
    if err != nil {
        log.Fatalf("error opening file: %v", err)
    }
    defer f.Close()

    log.SetOutput(f)

    // open a file
    if file, err := os.Open("in.txt"); err == nil {
    // make sure it gets closed
    defer file.Close()

    f, err := os.Create("out.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    // create a new scanner and read the file line by line
    scanner := bufio.NewScanner(file)
    scanner.Split(bufio.ScanLines) 

    i := 0
    for scanner.Scan() {
        line := scanner.Text()
    
        log.Println("Read line:", line)

        if(i != 0) {
            startTime := time.Now()
            out, err := exec.Command("/usr/bin/ruby", "calculations.rb", line).Output()

            if err != nil {
                log.Fatal(err)
            }
            elapsed := time.Since(startTime)
        
            log.Println("Out %s, %s\n", out[:len(out)-1], elapsed)

            //fmt.Printf("%s, %s\n", out[:len(out)-1], elapsed)
            //return make([]int, array)
            b := out[:len(out)-1]
            buff := string(b)
            f.WriteString(buff)
            f.WriteString(", ")
            f.WriteString(elapsed.String())
            f.WriteString("\n")

            slice = append(slice, buff, elapsed.String())
            //fmt.Printf("%s\n", slice)

        }
        i++
    }

    // check for errors
    if err = scanner.Err(); err != nil {
      log.Fatal(err)
    }

  } else {
    log.Fatal(err)
  }

    //s := append(out[:len(out)-1], elapsed)
    //results := make([]string, 0)
    //results = append(out[:len(out)-1], string(elapsed))
    fmt.Printf("%s\n", slice)

    //return strings.Join(slice, ", ")
    //return slice
}

func main() {
    run()
}
