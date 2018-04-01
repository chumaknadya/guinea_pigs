import numbers
import sys

import src
from src import Duplication
from src import News
from src import file_processor

channels = src.read_channels_from_file("resources/test.xml")
to_check = src.News("title",
                "Людей собираются эвакуировать из Думы в Идлиб на северо-западе Сирии. Однако точная дата эвакуации не называется'",
                "url")

duplications = []
for c in channels:
    c.load_news()
    for n in c.news:
        duplication_percent = n.percentage_of_duplication(to_check)
        if isinstance(duplication_percent, numbers.Number):
            if duplication_percent > 10:
                duplications.append(Duplication(n, duplication_percent))

file_processor.write_results_to_file(duplications)
