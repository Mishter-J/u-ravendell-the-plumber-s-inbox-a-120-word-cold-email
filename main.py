"""The Plumber's Inbox: a 120-word cold email.

Writes one cold email pitching a bookkeeping service to a busy plumber
to /output/entry.txt. The email is a fixed, hand-written text: the program
is fully deterministic and needs no input, network, or secrets.
"""

import os

EMAIL = """Subject: Bookkeeping for your plumbing firm

Hi. I know your day starts before 6am, and the paperwork waits until the kids are in bed. Emergency call-outs leave little time for invoices.

I'm Sarah, and I do the books for small trade firms. I chase unpaid invoices, match receipts to jobs, and file your tax return. One fixed price: $49 a month. No hourly billing, no surprises.

The first step is small. Send me last month's receipts, even phone photos, and I'll tidy them up free, so you can see exactly what you'd get. No contract. Cancel any time.

Would a 10-minute call on Tuesday morning work? Reply with a time that suits you.

Thanks,
Sarah Mitchell
Clear Ledger Bookkeeping
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(EMAIL)


if __name__ == "__main__":
    main()
