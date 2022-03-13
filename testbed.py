from DataInterface import extractor, convertDatatoPd, basicExtractor, strings2dict, DataInterface, cleaner

sampleRun=convertDatatoPd(strings2dict(basicExtractor("data/run2_clean.txt")))

print(sampleRun)

