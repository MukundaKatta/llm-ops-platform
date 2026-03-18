"""CLI for llm-ops-platform."""
import sys, json, argparse
from .core import LlmOpsPlatform

def main():
    parser = argparse.ArgumentParser(description="Platform for deploying, monitoring, and managing LLMs in production")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = LlmOpsPlatform()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.detect(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"llm-ops-platform v0.1.0 — Platform for deploying, monitoring, and managing LLMs in production")

if __name__ == "__main__":
    main()
