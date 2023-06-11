from youtube_transcript_api import YouTubeTranscriptApi

outls = []

tx = YouTubeTranscriptApi.get_transcript('--j9oAm21Io', languages=['ru'])
for i in tx:
        #outtxt = (i['text'])
        #outls.append(outtxt)

        #with open("op.txt", "a") as opf:
           # opf.write(outtxt + "\n")

    print(i)