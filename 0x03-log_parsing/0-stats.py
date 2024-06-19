#!/usr/bin/python3
"""This script parses a log and outputs its metrics"""


import sys
import signal
import re


class LogProcessor:
    """A class to process log entries and compute statistics."""

    def __init__(self):
        self.total_size = 0
        self.status_code_counts = {}
        self.line_count = 0
        self.valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
        self.log_pattern = re.compile(
            r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

    def print_stats(self):
        """Print the statistics."""
        print(f"File size: {self.total_size}")
        for code in sorted(self.status_code_counts):
            print(f"{code}: {self.status_code_counts[code]}")

    def process_line(self, line):
        """Process a single line of log entry."""
        self.line_count += 1
        match = self.log_pattern.match(line.strip())
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            self.total_size += file_size
            if status_code in self.valid_status_codes:
                if status_code not in self.status_code_counts:
                    self.status_code_counts[status_code] = 1
                else:
                    self.status_code_counts[status_code] += 1

    def signal_handler(self, sig, frame):
        """Handle the signal and print stats."""
        self.print_stats()
        sys.exit(0)


def main():
    processor = LogProcessor()

    # Attach signal handler to SIGINT (Ctrl + C)
    signal.signal(signal.SIGINT, processor.signal_handler)

    # Read lines from stdin
    try:
        for line in sys.stdin:
            processor.process_line(line)
            if processor.line_count % 10 == 0:
                processor.print_stats()
    except KeyboardInterrupt:
        processor.print_stats()
        sys.exit(0)

    # Print final stats after all lines are processed
    processor.print_stats()


if __name__ == "__main__":
    main()
