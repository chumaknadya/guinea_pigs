import numbers
import sys

import src
from src import Duplication
from src import News
from src import file_processor

channels = src.read_channels_from_file("resources/test.xml")
to_check = src.News("МИД Италии выразил протест Франции",
                "http http http http http http http http http http http http http http http http ",
                "http://news.liga.net/news/world/14922757-glava_mid_ispanii_predlozhil_dvoynoy_podkhod_k_otnosheniyam_s_rf.htm")

duplications = []
for c in channels:
    c.load_news()
    for n in c.news:
        duplication_percent = n.percentage_of_duplication(to_check)
        if isinstance(duplication_percent, numbers.Number):
            if duplication_percent > 10:
                duplications.append(Duplication(n, duplication_percent))

duplications.append(Duplication(News("t", "d", "url"), 15))
file_processor.write_results_to_file(duplications)
