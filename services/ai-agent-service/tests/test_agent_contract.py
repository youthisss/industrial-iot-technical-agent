from app.agents.graph import MaintenanceGraph


def test_langgraph_node_contract_is_fixed() -> None:
    assert MaintenanceGraph.nodes == (
        "input_parser",
        "vision_analyzer",
        "document_retriever",
        "first_recommendation_generator",
        "safety_checker",
        "history_lookup_requester",
        "second_recommendation_generator",
        "response_formatter",
        "evaluation_logger",
    )
