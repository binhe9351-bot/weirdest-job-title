#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown - make.fun bounty entry."""
import os

ENTRY = "Chief Executive Officer of Lost Sock Recovery"


def main():
    print(ENTRY)
    for path in ("/output/entry.txt", os.path.join(os.getcwd(), "output", "entry.txt")):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY + "\n")
            break
        except Exception:
            continue


if __name__ == "__main__":
    main()
