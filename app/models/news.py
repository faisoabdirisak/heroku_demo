class News:

    def __init__(self,title,description,url,urlToImage,publishedAt,content):
        self.title = title
        self.description= description
        self.url=url
        self.urlToImage='https://mysteriousuniverse.org/wp-content/uploads/2020/08/breaking-1.jpg'+urlToImage
        self.publishedAt=publishedAt
        self.content=content
