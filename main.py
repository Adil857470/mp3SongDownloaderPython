import PyPDF2
import re
from youtubesearchpython import SearchVideos
def Download(name):
    import pafy
    output = name
    search = SearchVideos(output, offset=1, mode="json", max_results=1)
    js = (search.result())
    js = re.search("(?P<url>https?://[^\s]+)", js).group("url")
    js = js.split('"')
    print(js[0])
    url = js[0]
    result = pafy.new(url)
    best_quality_audio = result.getbestaudio()
    best_quality_audio.download()
pdf = open('pdf/Saregama_Carvaan_Songlist_1.0.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
print("Total Number Of pages", pdfReader.numPages)
i = 94
l3 = []
ext = []
full = []
songName = []
while i < pdfReader.numPages:
    pg = pdfReader.getPage(i)
    text = pg.extractText()
    i = i + 1
    clean = re.compile('\n')
    h = re.sub(clean, '', text)
    clean = re.compile('Š')
    h = re.sub(clean, ': ', h)
    clean = re.compile('˜˚')
    h = re.sub(clean, '', h)
    full.append(h)
    r = r"([0-9]+)\."
    for st in h.split(r):
        output = re.sub(r, '\n', st)
        for line in output.split("\n"):
            print(line)
            if len(line) > 20:
                try:
                    Download(line)
                except Exception as e:
                    print(e)
                    pass

