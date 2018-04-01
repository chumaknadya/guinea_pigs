import sys

import src

channels = src.read_channels_from_file(sys.argv[1])
print(channels)
for c in channels:
    c.load_news()