import os
import time

class Post:
    def __init__(self):
        self.filename = "index.html"
    def main(self):
        title = raw_input("Title: ")
        month, day, year = time.localtime()[1], time.localtime()[2], time.localtime()[0]
        data = "{0} / {1} / {2}".format(month, day, year)
        post = raw_input("Post: ")
        with open(self.filename,'r') as file:
            data = file.read().replace("<div class='posts'>", "<div class='posts'><p><span class='title'><h1>"+title+"</h1></span><span class='data'><h4>"+data+"</h4></span><span class='post'>"+post+"</span></p>")
            with open(self.filename, 'w') as file:
                file.write(data)
        os.system("git add -A")
        os.system("git commit -m 'Post'")
        os.system("git push -u origin gh-pages")

Post().main()

