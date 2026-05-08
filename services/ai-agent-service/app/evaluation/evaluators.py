from app.evaluation.metrics import EVALUATION_METRICS


def run_placeholder_evaluation() -> dict[str, float]:
    return {metric: 1.0 for metric in EVALUATION_METRICS}
