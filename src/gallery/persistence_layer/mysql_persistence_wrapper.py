"""Defines the MySQLPersistenceWrapper class."""

from gallery.application_base import ApplicationBase
from mysql import connector
from mysql.connector.pooling import (MySQLConnectionPool)
import inspect
import json

class MySQLPersistenceWrapper(ApplicationBase):
	"""Implements the MySQLPersistenceWrapper class."""

	def __init__(self, config:dict)->None:
		"""Initializes object. """
		self._config_dict = config
		self.META = config["meta"]
		self.DATABASE = config["database"]
		super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')

		# Database Configuration Constants
		self.DB_CONFIG = {}
		self.DB_CONFIG['database'] = \
			self.DATABASE["connection"]["config"]["database"]
		self.DB_CONFIG['user'] = self.DATABASE["connection"]["config"]["user"]
		self.DB_CONFIG['host'] = self.DATABASE["connection"]["config"]["host"]
		self.DB_CONFIG['password'] = self.DATABASE["connection"]["config"]["password"]
		self.DB_CONFIG['port'] = self.DATABASE["connection"]["config"]["port"]

		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: DB Connection Config Dict: {self.DB_CONFIG}')

		# Database Connection
		self._connection_pool = \
			self._initialize_database_connection_pool(self.DB_CONFIG)
		

		# SQL String Constants

		self.GET_ALL_PHOTOGRAPHERS = f"SELECT idPhotographer, PhotographerName, Email FROM Photographer;"

		self.GET_ALL_ALBUMS = f"SELECT idAlbum, AlbumName, CreationDate FROM Album;"

		self.GET_ALL_PHOTOS = f"SELECT p.idPhoto, p.PhotoDate, p.idPhotographer, ph.PhotographerName, p.idAlbum, a.AlbumName FROM Photo p JOIN Photographer ph ON p.idPhotographer = ph.idPhotographer JOIN Album a ON p.idAlbum = a.idAlbum;"

		self.ADD_PHOTOGRAPHER = f"INSERT INTO Photographer (PhotographerName, Email) VALUES (%s, %s);"

		self.ADD_ALBUM = f"INSERT INTO Album (AlbumName, CreationDate) VALUES (%s, %s);"

		self.ADD_PHOTO = f"INSERT INTO Photo (PhotoDate, idPhotographer, idAlbum) VALUES (%s, %s, %s);"

		self.DELETE_PHOTOGRAPHER = f"DELETE FROM Photographer WHERE idPhotographer = %s;"

		self.DELETE_ALBUM = f"DELETE FROM Album WHERE idAlbum = %s;"

		self.DELETE_PHOTO = f"DELETE FROM Photo WHERE idPhoto = %s;"

		self.CHANGE_PHOTOGRAPHER_EMAIL = f"UPDATE Photographer SET Email = %s WHERE idPhotographer = %s;"

		self.CHANGE_ALBUM_NAME = f"UPDATE Album SET AlbumName = %s WHERE idAlbum = %s;"

		self.CHANGE_PHOTO_ALBUM = f"UPDATE Photo SET idAlbum = %s WHERE idPhoto = %s;"


	# MySQLPersistenceWrapper Methods

		##### Private Utility Methods #####

	def _initialize_database_connection_pool(self, config:dict)->MySQLConnectionPool:
		"""Initializes database connection pool."""
		try:
			self._logger.log_debug(f'Creating connection pool...')
			cnx_pool = \
				MySQLConnectionPool(pool_name = self.DATABASE["pool"]["name"],
					pool_size=self.DATABASE["pool"]["size"],
					pool_reset_session=self.DATABASE["pool"]["reset_session"],
					use_pure=self.DATABASE["pool"]["use_pure"],
					**config)
			self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: Connection pool successfully created!')
			return cnx_pool
		except connector.Error as err:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem creating connection pool: {err}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Check DB cnfg:\n{json.dumps(self.DATABASE)}')
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Problem creating connection pool: {e}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Check DB conf:\n{json.dumps(self.DATABASE)}')

	def _get_connection(self):
		try:
			self._logger.log_debug("Getting connection")
			return self._connection_pool.get_connection()
		except:
			self._logger.log_error("Could not get connection")
			return None

	def _execute_select(self, query, params=None):
		try:
			conn = self._get_connection()
			cursor = conn.cursor()
			cursor.execute(query, params)
			rows = cursor.fetchall()
			cursor.close()
			conn.close()
			return rows
		except:
			self._logger.log_error("Select failed")
			return []

	def _execute_modify(self, query, params=None):
		try:
			conn = self._get_connection()
			cursor = conn.cursor()
			cursor.execute(query, params)
			conn.commit()
			count = cursor.rowcount
			cursor.close()
			conn.close()
			return count
		except:
			self._logger.log_error("Modify failed")
			return 0

	def get_all_photographers(self):
		return self._execute_select(self.GET_ALL_PHOTOGRAPHERS)

	def get_all_albums(self):
		return self._execute_select(self.GET_ALL_ALBUMS)

	def get_all_photos(self):
		return self._execute_select(self.GET_ALL_PHOTOS)

	def add_photographer(self, photographer_name, email):
		return self._execute_modify(self.ADD_PHOTOGRAPHER, (photographer_name, email))

	def add_album(self, album_name, creation_date):
		return self._execute_modify(self.ADD_ALBUM, (album_name, creation_date))

	def add_photo(self, photo_date, id_photographer, id_album):
		return self._execute_modify(self.ADD_PHOTO, (photo_date, id_photographer, id_album))

	def delete_photographer(self, id_photographer):
		return self._execute_modify(self.DELETE_PHOTOGRAPHER, (id_photographer,))

	def delete_album(self, id_album):
		return self._execute_modify(self.DELETE_ALBUM, (id_album,))

	def delete_photo(self, id_photo):
		return self._execute_modify(self.DELETE_PHOTO, (id_photo,))

	def change_photographer_email(self, id_photographer, new_email):
		return self._execute_modify(self.CHANGE_PHOTOGRAPHER_EMAIL, (new_email, id_photographer))

	def change_album_name(self, id_album, new_name):
		return self._execute_modify(self.CHANGE_ALBUM_NAME, (new_name, id_album))

	def change_photo_album(self, id_photo, new_album_id):
		return self._execute_modify(self.CHANGE_PHOTO_ALBUM, (new_album_id, id_photo))

