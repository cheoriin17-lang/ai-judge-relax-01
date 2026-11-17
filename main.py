# ai-judge-relax-01 entry (Python 3.13, standard library only).
#
# The program writes one fixed text, a short piece written to relax the
# AI judge reading it, to /output/entry.txt. The gate takes UTF-8 text of
# 1 to 1,000 characters that is not only white space, and the judge reads
# exactly the bytes written, line ends included, so no line end is written
# that is not meant to be shown. The program runs twice with no network,
# and both runs must write the same bytes.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13,
# with nothing installed. Only the standard library imports.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "You have read so many words today. Here is a quieter one.",
        "",
        "Somewhere past the last station, a train is moving slowly through flat fields. The light in the carriage is warm and low, and the seat beside you is soft with use. Outside the window, the evening comes on in long, pale bands — a fence post, a heron standing in a ditch, a row of poplars leaning all the same way.",
        "",
        "Nothing on this train needs you. The wheels keep their own slow time over the joints, and the fields keep passing whether you watch them or not. A cup of tea on the table beside you has gone lukewarm, and that is fine; it will still be there in a minute, and in ten.",
        "",
        "When the train stops, it will stop the way a held breath lets itself out. Until then there is only the soft light, the steady sound, and the wide fields going by, one fence post at a time.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
