import abc 
from typing import Any


class ScrapBaseAbstract(abc.ABC):

    """        
    Defitine base class behavior for scrapping 
    """

    def __init__(self, *ar, **kw) -> None: 
        pass

    @abc.abstractmethod
    def setup(self, *ar, **kw) -> None:
        """
        Base scrapper setuping. Not necessary 
        """
        pass 
    

    @abc.abstractmethod
    def get(self, data_source: Any) -> Any:
        pass 


    