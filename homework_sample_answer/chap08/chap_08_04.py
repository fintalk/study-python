# import bookmark 
# b = bookmark.Bookmark("タイトル", "http://path.to/site")

# class Blogmark(bookmark.Bookmark):
#     def __init__(self, title, url, genre):
#         super().__init__(title, url)
#         self.genre = genre


from bookmark import Bookmark
b = Bookmark("タイトル", "http://path.to/site")

class Blogmark(Bookmark):
    def __init__(self, title, url, genre):
        super().__init__(title, url)
        self.genre = genre


print(b.title)
print(b.url)

blog = Blogmark("パイソン", "www.python.org", "python")
print(blog.genre)
    