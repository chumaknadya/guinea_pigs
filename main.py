import sys

import src
from src import Duplication

channels = src.read_channels_from_file("test.xml")
to_check = src.News("МИД Италии выразил протест Франции",
                " Министерство выразило протест в связи с инцидентом, в ходе которого французская пограничная полиция ворвалась",
                "http://news.liga.net/news/world/14922757-glava_mid_ispanii_predlozhil_dvoynoy_podkhod_k_otnosheniyam_s_rf.htm")

print(channels)
duplications = []
for c in channels:
    c.load_news()
    for n in c.news:
        duplication_percent = n.percentage_of_duplication(to_check)
        print(n, "\n", duplication_percent, "\n\n")
        if duplication_percent > 10:
            duplications.append(Duplication(n, duplication_percent))

print(duplications)
