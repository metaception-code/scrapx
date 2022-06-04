from scrapx.base import ScrapBaseAbstract


class TelegramScrapper(ScrapBaseAbstract):

    def __init__(self, filter: dict = None) -> None:
        self._filter = filter 

    def setup(self):
        
        # put here your setup function. may be login, or anything else
        pass 


    def get(self, data_source: dict) -> dict:
        """
        Should returns data due to the base filter function 
        """

        # Put here your SCRAPPY logic. 
        pass

    def _filter(self) -> None:
        pass 


     