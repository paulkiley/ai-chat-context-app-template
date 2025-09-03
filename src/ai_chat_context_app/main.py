from __future__ import annotations

import sys
import argparse
from typing import Optional

from chat_history_manager.main import save_chat_history, retrieve_chat_history


def cmd_save(args: argparse.Namespace) -> int:
    content = sys.stdin.read() if not args.file else open(args.file, "r", encoding="utf-8").read()
    if not content:
        print("No content on stdin; pass --file or pipe text", file=sys.stderr)
        return 2
    path = save_chat_history(
        full_conversation=content,
        project_name=args.project,
        topic=args.topic,
        summary=args.summary,
        session_id=args.session,
        dry_run=bool(args.dry_run),
    )
    print(path)
    return 0


def cmd_retrieve(args: argparse.Namespace) -> int:
    chunks = retrieve_chat_history(
        project_name=args.project,
        topic=args.topic,
        session_id=args.session,
        limit_chunks=args.limit,
    )
    for i, chunk in enumerate(chunks, 1):
        if i > 1:
            print("\n" + ("-" * 40) + "\n")
        print(chunk, end="")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="aiapp",
        description="Example app using AI Chat Context Keeper",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("save")
    s.add_argument("--project", required=True)
    s.add_argument("--topic", required=True)
    s.add_argument("--summary")
    s.add_argument("--session")
    s.add_argument("--file")
    s.add_argument("--dry-run", action="store_true")
    s.set_defaults(func=cmd_save)

    r = sub.add_parser("retrieve")
    r.add_argument("--project")
    r.add_argument("--topic")
    r.add_argument("--session")
    r.add_argument("--limit", type=int, default=1)
    r.set_defaults(func=cmd_retrieve)

    return p


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

