import news_scraper
import script_writer
import video_maker


class NewsByteCreator:
    def __init__(self, article_link):
        self.news = None
        self.script = None
        self.headlines = None
        self.image_urls = None
        self.article_link = article_link

    def create_byte(self):
        scrapper = news_scraper.ScraperApp(self.article_link)
        scrapper.run()

        self.news = scrapper.text
        self.image_urls = scrapper.images_downloadable

        writer = script_writer.ScriptWriter(self.news)
        self.headlines = writer.write_headlines()
        self.script = writer.script

        print(self.headlines)

        creator = video_maker.VideoAggregator()
        response = creator.generate_video(self.image_urls, self.headlines)

        return response


# theCreator = NewsByteCreator("https://www.bbc.com/news/articles/cgllgxlg5dgo")
theCreator = NewsByteCreator(
    "https://www.bbc.com/sport/tennis/articles/c722ez0r3pzo")
print(theCreator.create_byte())
