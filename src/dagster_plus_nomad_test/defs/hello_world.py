"""Hello-world assets for the Nomad agent smoke test.

Three tiny assets in a chain so we can confirm:
1. The Dagster+ control plane registers the code location through the
   ``testing-nomad`` agent queue (= the new Nomad agent picks it up).
2. The agent successfully launches a Nomad batch job for a run.
3. Run worker → code-server → run worker round-trip works end-to-end.
"""

import dagster as dg


@dg.asset
def greeting() -> str:
    return "hello"


@dg.asset
def subject() -> str:
    return "nomad"


@dg.asset
def message(greeting: str, subject: str) -> str:
    out = f"{greeting}, {subject}!"
    print(out)
    return out
