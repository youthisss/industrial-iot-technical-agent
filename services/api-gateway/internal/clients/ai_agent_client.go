package clients

type AIAgentClient struct {
	BaseURL string
}

func NewAIAgentClient(baseURL string) AIAgentClient {
	return AIAgentClient{BaseURL: baseURL}
}
