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
        filtered_list = [string for string in self.headlines if string != ""]
        self.headlines = filtered_list
        self.script = writer.script

        print(self.headlines)

        creator = video_maker.VideoAggregator()
        response = creator.generate_video(self.image_urls, self.headlines)

        return response


# theCreator = NewsByteCreator("https://www.bbc.com/news/articles/cgllgxlg5dgo")
theCreator = NewsByteCreator(
    "https://www.bbc.com/future/article/20240522-the-drought-that-forced-a-himalayan-village-in-nepal-to-relocate")
# theCreator = NewsByteCreator(
#     "https://www.bbc.com/travel/article/20240513-ben-franklin-the-us-founding-father-who-travelled-the-globe")
# theCreator = NewsByteCreator(
#     "https://www.bbc.com/news/world-asia-india-67657873")
# theCreator = NewsByteCreator(
#     "https://www.bbc.com/travel/article/20240218-why-indias-wildly-remote-islands-are-trending")
# theCreator = NewsByteCreator(
#     "https://www.bbc.com/news/world-asia-india-68872429")
# theCreator = NewsByteCreator(
#     "https://www.bbc.com/sport/tennis/articles/c722ez0r3pzo")
print(theCreator.create_byte())
