# AI Agent Design

The AI service keeps a fixed LangGraph-style flow:

1. `input_parser`
2. `vision_analyzer`
3. `document_retriever`
4. `first_recommendation_generator`
5. `safety_checker`
6. `history_lookup_requester`
7. `second_recommendation_generator`
8. `response_formatter`
9. `evaluation_logger`

The retriever interface supports only Pinecone and pgvector adapters.
