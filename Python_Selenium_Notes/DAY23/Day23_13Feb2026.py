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


#! Multi processing (Cpu bound tasks)

'''Multiprocessing (CPU-Bound Tasks)

This is where threading fails and multiprocessing wins 💪

🚀 What is CPU-Bound?

CPU-bound tasks are tasks where:

Heavy calculations

Mathematical operations

Data processing

Encryption

Image processing

Machine learning training

The CPU is constantly working.

Example:

for i in range(10_000_000):
    x = i * i


That is CPU heavy.

⚠️ Why Threading Fails for CPU Tasks?

Because of something called:

🔒 GIL (Global Interpreter Lock)

In Python:

Only ONE thread executes Python bytecode at a time.

Even if you create 10 threads,

Only one runs at a time for CPU-heavy tasks.

So threading does NOT improve CPU-bound performance.

💪 Why Multiprocessing Works

Multiprocessing:

✔ Creates separate processes
✔ Each process has its own Python interpreter
✔ Each process has its own GIL
✔ Can use multiple CPU cores

That means real parallel execution.
'''