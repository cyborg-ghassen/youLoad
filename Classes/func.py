from pytube import YouTube, Playlist


class Functions:
    def video(self, link, res, output):
        v = YouTube(link)
        print("Downloading {}".format(v.title))
        stream = v.streams.filter(resolution=res, mime_type="video/mp4")[0]
        print(stream)
        stream.download(output_path=output)
        print("Download completed")

    def playlist(self, link, output):
        p = Playlist(link)
        print("Downloading {}".format(p.title))
        for i in p.videos:
            print("{} - Downloading {}".format(i, i.title))
            stream = i.streams.get_highest_resolution()
            print(stream)
            stream.download(output_path=output + p.title)
        print("Download completed")

    def audio(self, link, res, output):
        a = YouTube(link)
        print("Downloading {}".format(a.title))
        a.streams.filter(type="audio", resolution=res).get_audio_only().download(output_path=output, filename=a.title + '.mp3')
        print("Download completed")
