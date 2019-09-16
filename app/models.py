class sources:
    '''
    sources class to define sources Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country



class Articles:
    '''
    Articles class to define articles objects
    '''
    def __init__(self,id,name,author,title,description,url,urloImage,publishedAt,content):
        self.id = id
        self.name = name 
        self.author = author
        self.title = title
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content


    def save_articles(self):
        Articles.all_articles.append(self)


    @classmethod
    def clear_articles(cls):
        Articles.all_articles.clear()

    @classmethod
    def get_articles(cls,id):

        response = []

        for articles in cls.all_articles:
            if articles.id == id:
                response.append(articles)

        return response