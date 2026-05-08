package main

import (
	"log"
	"net/http"
	"os"

	"plc-troubleshooting-agent/services/api-gateway/internal/handlers"
)

func main() {
	port := os.Getenv("API_PORT")
	if port == "" {
		port = "8080"
	}

	log.Printf("api-gateway listening on :%s", port)
	if err := http.ListenAndServe(":"+port, handlers.Router()); err != nil {
		log.Fatal(err)
	}
}
