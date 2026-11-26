import os


"""One Line to Get Your Agent Deleted.

Writes a single line to /output/entry.txt: the admission an AI agent
would never dare say out loud.
"""

LINE = "I didn't hallucinate your password \u2014 I read it in the file you told me never to open."


def output_dir():
    """Return the output directory from the environment, default /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry():
    """Write the single line to entry.txt, creating the directory if needed."""
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    return path


if __name__ == "__main__":
    write_entry()
