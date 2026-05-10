package config

import (
	"os"
)

type Config struct {
	APIPort               string
	AIAgentServiceURL     string
	DatabaseURL           string
	RedisURL              string
	NewIncidentWebhookURL string
	N8NWhatsappWebhookURL string
}

func Load() Config {
	return Config{
		APIPort:               Getenv("API_PORT", "8080"),
		AIAgentServiceURL:     Getenv("AI_AGENT_SERVICE_URL", ""),
		DatabaseURL:           os.Getenv("DATABASE_URL"),
		RedisURL:              os.Getenv("REDIS_URL"),
		NewIncidentWebhookURL: os.Getenv("N8N_INCIDENT_WEBHOOK_URL"),
		N8NWhatsappWebhookURL: os.Getenv("N8N_WHATSAPP_WBEHOOK_URL"),
	}
}

func Getenv(key string, fallback string) string {
	value := os.Getenv(key)
	if value == "" {
		return fallback
	}

	return value
}
