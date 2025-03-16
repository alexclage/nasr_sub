from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
import logging
import requests, zipfile, io
import os


class NASR_base:

    def __init__(self):


        self.url = os.environ["NASR_URL"]
        self.logger = logging.getLogger(__name__)

        try:
            self.request = requests.get(str(self.url))
            self.soup = BeautifulSoup(self.request.content, features="html.parser")
        except Exception as f:
            self.logger.error(f"Error in retrieving page and making soup\n{f}")

        self.logger.info(f"Successfully retrieved NASR page")

    @property
    def current_date(self) -> datetime.date:
        if not hasattr(self, "current_init_url"):
            self.get_init_urls()
        str_date = self.current_init_url.split("/")[-1]
        return datetime.strptime(str_date, "%Y-%m-%d").date()
    
    @property
    def future_date(self) -> datetime.date:
        if not hasattr(self, "future_init_url"):
            self.get_init_urls()
        str_date = self.future_init_url.split("/")[-1]
        return datetime.strptime(str_date, "%Y-%m-%d").date()
   
    def get_init_urls(self):

        content = self.soup.find("article", attrs={"id":"content"})
        list_items = content.find_all("li")
        self.future_init_url = self.url + list_items[0].a["href"].split("/")[-1]
        self.current_init_url = self.url + list_items[1].a["href"].split("/")[-1]

    def get_zip_url(self, url):

        request = requests.get(url)
        soup = BeautifulSoup(request.content, features="html.parser")
        for links in soup.find_all("a"):
            if links.text == "Data in CSV format":
                link = links["href"]

        if len(link) >= 1:
            return link
        else:
            raise Exception(f"No zip file found searching for 'Data in CSV format at url: '{url}'")
        
    def download_zip(self, url, path):
        r = requests.get(url)
        if r.ok:
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(path)
        else:
            raise Exception(f"Download failed\nStatus Code:\n{r.status_code}\nReason:\n{r.reason}")

    def get_current_zip(self):

        if not hasattr(self, "current_init_url"):
            self.get_init_urls()

        self.current_zip_url = self.get_zip_url(self.current_init_url)

    def get_future_zip(self):
        if not hasattr(self, "future_init_url"):
            self.get_init_urls()
        
        self.future_zip_url = self.get_zip_url(self.future_init_url)

    def download_current_zip(self, path=""):

        # path arg must be in "\\path\\" format
        
        if not hasattr(self, "current_zip_url"):
            self.get_current_zip()

        if path == "":

            save_path = os.environ["ZIP_LOC"]
            self.download_zip(self.current_zip_url, save_path)

        else:

            self.download_zip(self.current_zip_url, path)

        self.logger.info(f"Successfully retrieved Current Zip file")

    def download_future_zip(self, path=""):

        # path arg must be in "\\path\\" format
        
        if not hasattr(self, "future_zip_url"):
            self.get_future_zip()

        if path == "":

            save_path = os.environ["ZIP_LOC"]
            self.download_zip(self.future_zip_url, save_path)

        else:

            self.download_zip(self.future_zip_url, path)

        self.logger.info(f"Successfully retrieved Future Zip file")
        
if __name__ == "__main__":
    NASR = NASR_base()
    NASR.download_current_zip()
