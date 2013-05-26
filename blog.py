import os

class Post:
    def __init__(self):
        self.filename = "index.html"
    def main(self):
        post = raw_input("Post: ")
        with open(self.filename,'r') as file:
            data = file.read().replace("<div class='posts'>", "<div class='posts'><p>"+post+"</p>")
            with open(self.filename, 'w') as file:
                file.write(data)
        os.system("git add -A")
        os.system("git commit -m 'Post'")
        os.system("git push -u origin gh-pages")

Post().main()

