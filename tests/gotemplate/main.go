package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"text/template"
)

type Message struct {
	Role     string `json:"Role"`
	Content  string `json:"Content"`
	Thinking string `json:"Thinking"`
}

type TestData struct {
	Messages   []Message `json:"Messages"`
	System     string    `json:"System"`
	Tools      []string  `json:"Tools"`
	ToolCalls  []string  `json:"ToolCalls"`
	IsThinkSet bool      `json:"IsThinkSet"`
}

func main() {
	dataFilePath := flag.String("data-file", "", "Path to json file containing test data")
	goFilePath := flag.String("go-template", "", "Path to the go template file under test data")
	flag.Parse()

	if *dataFilePath == "" {
		panic("CLI Option 'data-file' required!")
	}
	if *goFilePath == "" {
		panic("CLI Option 'go-template' required!")
	}

	testData, err := os.ReadFile(*dataFilePath)
	if err != nil {
		panic(fmt.Sprintf("Could not read file '%s': %s", *dataFilePath, err))
	}
	testSet := map[string]TestData{}
	err = json.Unmarshal(testData, &testSet)
	if err != nil {
		panic(fmt.Sprintf("Failed to unmarshal test data: %s", err))
	}

	templateData, err := os.ReadFile(*goFilePath)
	if err != nil {
		panic(fmt.Sprintf("Could not read file '%s': %s", *goFilePath, err))
	}
	templateUnderTest, err := template.New("Test").Parse(string(templateData))
	if err != nil {
		panic(fmt.Sprintf("Could not parse go template file '%s': %s", *goFilePath, err))
	}

	for _, testMessages := range testSet {
		templateUnderTest.Execute(os.Stdout, testMessages)
	}
}
