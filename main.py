import sys

import src
from src import Duplication
from src import fileProcessor

channels = src.read_channels_from_file("resources/test.xml")
to_check = src.News("МИД Италии выразил протест Франции",
                " Министерство выразило протест в связи с инцидентом, в ходе которого французская пограничная полиция ворвалась",
                "http://news.liga.net/news/world/14922757-glava_mid_ispanii_predlozhil_dvoynoy_podkhod_k_otnosheniyam_s_rf.htm")

duplications = []
for c in channels:
    c.load_news()
    for n in c.news:
        duplication_percent = n.percentage_of_duplication(to_check)
        if duplication_percent > 10:
            duplications.append(Duplication(n, duplication_percent))

fileProcessor.write_results_to_file(duplications)
