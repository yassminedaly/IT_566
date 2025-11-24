"""Implements AppServices Class."""

from gallery.application_base import ApplicationBase
from gallery.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
import inspect

class AppServices(ApplicationBase):
    """AppServices Class Definition."""
    def __init__(self, config:dict)->None:
        """Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
        self.DB = MySQLPersistenceWrapper(config)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')

    def get_all_photographers(self):
        return self.DB.get_all_photographers()

    def get_all_albums(self):
        return self.DB.get_all_albums()

    def get_all_photos(self):
        return self.DB.get_all_photos()

    def add_photographer(self, photographer_name, email):
        return self.DB.add_photographer(photographer_name, email)

    def add_album(self, album_name, creation_date):
        return self.DB.add_album(album_name, creation_date)

    def add_photo(self, photo_date, id_photographer, id_album):
        return self.DB.add_photo(photo_date, id_photographer, id_album)

    def delete_photographer(self, id_photographer):
        return self.DB.delete_photographer(id_photographer)

    def delete_album(self, id_album):
        return self.DB.delete_album(id_album)

    def delete_photo(self, id_photo):
        return self.DB.delete_photo(id_photo)

    def change_photographer_email(self, id_photographer, new_email):
        return self.DB.change_photographer_email(id_photographer, new_email)

    def change_album_name(self, id_album, new_name):
        return self.DB.change_album_name(id_album, new_name)

    def change_photo_album(self, id_photo, new_album_id):
        return self.DB.change_photo_album(id_photo, new_album_id)
