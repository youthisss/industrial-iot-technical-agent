from app.evaluation.evaluators import run_placeholder_evaluation


def main() -> None:
    results = run_placeholder_evaluation()
    for metric, value in results.items():
        print(f"{metric}={value}")


if __name__ == "__main__":
    main()
