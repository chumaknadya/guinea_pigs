# -*- coding: UTF-8 -*-
if __name__ == '__build__':
    raise Exception


def read_stop_words(filename):
    with open(filename, 'r') as myfile:
        data = myfile.read().replace('\n', '')
    return data

def canonize(source,filename):
    stop_symbols = '.,!?:;-\n\r()'
    stop_words = read_stop_words(filename)
    return ([x for x in [y.strip(stop_symbols) for y in source.lower().split()] if x and (x not in stop_words)])


def genshingle(source):
    import binascii
    shingleLen = 10 # длина шингла
    out = []
    for i in range(len(source) - (shingleLen - 1)):
        out.append(binascii.crc32(' '.join([x for x in source[i:i + shingleLen]]).encode('utf-8')))

    return out


def compaire(source1, source2):
    same = 0
    try:
        for i in range(len(source1)):
            if source1[i] in source2:
                same = same + 1
        return float(same * 2) / float(len(source1) + len(source2)) * 100
    except ZeroDivisionError:
        return None





