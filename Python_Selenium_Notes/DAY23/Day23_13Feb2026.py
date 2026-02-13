#! Threading i/o  --> input output bound 

'''

Now we're entering real Python intern-level topic — Threading for I/O-bound tasks 💪

Let's break it properly.

🧠 What is I/O-Bound?

I/O-bound means:

The program spends most time waiting, not computing.

Examples:

🌐 Downloading from URLs

📂 Reading files

🗄 Database queries

📨 API calls

CPU is mostly idle while waiting for response.

🚀 Why Threading Helps in I/O-Bound

Imagine:

You download 4 URLs.

Without threading:

Download 1 → wait
Download 2 → wait
Download 3 → wait
Download 4 → wait


With threading:

Start all downloads together
While one waits → another runs

Much faster.

'''