package main

import (
	"context"
	"log"
	"net/http"

	"plc-troubleshooting-agent/services/api-gateway/internal/clients"
	"plc-troubleshooting-agent/services/api-gateway/internal/config"
	"plc-troubleshooting-agent/services/api-gateway/internal/db"
	"plc-troubleshooting-agent/services/api-gateway/internal/handlers"
	"plc-troubleshooting-agent/services/api-gateway/internal/repository"
)

func main() {
	cfg := config.Load()

	ctx := context.Background()

	database, err := db.Connect(ctx, cfg.DatabaseURL)
	if err != nil {
		log.Fatalf("database connection failed: %v", err)
	}
	defer database.Close()

	machineRepo := repository.NewMachineRepository(database)
	incidentRepo := repository.NewIncidentRepository(database)
	AgentRunRepo := repository.NewAgentRunRepository(database)
	aiClient := clients.NewAIClient(cfg.AIAgentServiceURL)

	router := handlers.Router(handlers.Dependencies{
		MachineRepo:  machineRepo,
		IncidentRepo: incidentRepo,
		AgentRunRepo: AgentRunRepo,
		AIClient:     aiClient,
	})

	log.Printf("api-gateway listening on :%s", cfg.APIPort)

	if err := http.ListenAndServe(":"+cfg.APIPort, router); err != nil {
		log.Fatal(err)
	}
}
