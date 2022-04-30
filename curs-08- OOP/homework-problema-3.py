class ListaCdDvd:

    cd_dvd_list = []

    def __init__(self, title, content):
        self.title = title
        self.content = content
        cd_dvd_list.append(self)

    def __str__(self):
        return f"Title: {self.title} \n\t Content: {self.content}"


album_1 = ListaCdDvd("Titlu 1", "Content 1")
album_2 = ListaCdDvd("Titlu 2", "Content 2")
album_3 = ListaCdDvd("Titlu 3", "Content 3")

for album in cd_dvd_list:
    print(album)

