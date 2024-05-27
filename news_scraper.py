import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os


class NewsScraper:
    def __init__(self, url):
        self.url = url
        self.html_content = None

    def fetch_content(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Check if the request was successful
            self.html_content = response.content
            print(f"Successfully fetched content from {self.url}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching content from {self.url}: {e}")
            return None


class Parser:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
        self.text = ""
        self.image_urls = []

    def parse(self):
        self._extract_text()
        self._extract_images()

    def _extract_text(self):
        paragraphs = self.soup.find_all('p')
        self.text = ' '.join([para.get_text() for para in paragraphs])
        print("Extracted text from the HTML content.")

    def _extract_images(self):
        images = self.soup.find_all('img')
        self.image_urls = [img['src'] for img in images if 'src' in img.attrs]
        print(
            f"Extracted {len(self.image_urls)} image URLs from the HTML content.")


class ImageDownloader:
    def __init__(self, image_urls):
        self.image_urls = image_urls
        self.images = []
        self.assets_folder = 'assets'
        self.image_urls_downloadable = []

        # Create the assets directory if it doesn't exist
        if not os.path.exists(self.assets_folder):
            os.makedirs(self.assets_folder)

        if os.path.exists(self.assets_folder):
            for filename in os.listdir(self.assets_folder):
                file_path = os.path.join(self.assets_folder, filename)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    self._delete_folder_contents(file_path)

    def download_images(self):
        for idx, url in enumerate(self.image_urls):
            try:
                response = requests.get(url)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content))
                self.images.append(image)

                # Save the image to the assets folder
                image_path = os.path.join(
                    self.assets_folder, f'image_{idx + 1}.png')
                image.save(image_path)
                self.image_urls_downloadable.append(url)
                print(f"Downloaded and saved image from {url} as {image_path}")
            except requests.exceptions.RequestException as e:
                print(f"Error downloading image from {url}: {e}")
            except IOError as e:
                print(f"Error processing image from {url}: {e}")


class ScraperApp:
    def __init__(self, url):
        self.url = url
        self.text = ""
        self.images = []
        self.images_downloadable = None

    def run(self):
        scraper = NewsScraper(self.url)
        scraper.fetch_content()

        if scraper.html_content:
            parser = Parser(scraper.html_content)
            parser.parse()
            self.text = parser.text
            print("Text has been stored.")

            downloader = ImageDownloader(parser.image_urls)
            downloader.download_images()
            self.images = downloader.images
            self.images_downloadable = downloader.image_urls_downloadable
            print("Images have been stored.")


# if __name__ == "__main__":
#     # url = "https://www.bbc.com/news/articles/cv22mryvleko"
#     url = "https://www.bbc.com/news/articles/cgllgxlg5dgo"
#     app = ScraperApp(url)
#     app.run()
#     print(app.images_downloadable)
#     print(f"Scraped text: {app.text}")
#     print(f"Number of images downloaded: {len(app.images)}")
