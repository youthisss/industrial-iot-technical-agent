package services

type TroubleshootingRequest struct {
	RequestID string `json:"request_id"`
	MachineID string `json:"machine_id"`
	PLCType   string `json:"plc_type"`
	ErrorCode string `json:"error_code"`
	Message   string `json:"message"`
	ImageURL  string `json:"image_url,omitempty"`
}
