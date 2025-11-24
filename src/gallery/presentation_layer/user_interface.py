"""Implements the applicatin user interface."""

from gallery.application_base import ApplicationBase
from gallery.service_layer.app_services import AppServices
from prettytable import PrettyTable
import inspect
import json

class UserInterface(ApplicationBase):
    """UserInterface Class Definition."""
    def __init__(self, config:dict)->None:
        """Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
        self.DB = AppServices(config)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')

    def start(self):
        """Start main user interface."""
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: User interface started!')
        running = True

        while running:
            print("\n===== Gallery Menu =====")
            print("1. List photographers")
            print("2. List albums")
            print("3. List photos")
            print("4. Add photographer")
            print("5. Add album")
            print("6. Add photo")
            print("7. Change photographer email")
            print("8. Change album name")
            print("9. Change photo album")
            print("10. Delete photographer")
            print("11. Delete album")
            print("12. Delete photo")
            print("Q. Quit")

            choice = input("Enter choice: ")

            if choice == "1":
                # List photographers
                rows = self.DB.get_all_photographers()
                table = PrettyTable(["ID", "Name", "Email"])
                for row in rows:
                    table.add_row([row[0], row[1], row[2]])
                print(table)

            elif choice == "2":
                # List albums
                rows = self.DB.get_all_albums()
                table = PrettyTable(["ID", "Album Name", "Creation Date"])
                for row in rows:
                    table.add_row([row[0], row[1], row[2]])
                print(table)

            elif choice == "3":
                # List photos
                rows = self.DB.get_all_photos()
                table = PrettyTable(["Photo ID", "Photo Date", "Photographer ID",
                                     "Photographer Name", "Album ID", "Album Name"])
                for row in rows:
                    table.add_row([row[0], row[1], row[2], row[3], row[4], row[5]])
                print(table)

            elif choice == "4":
                # Add photographer
                print("\nAdd Photographer")
                name = input("Photographer name: ")
                email = input("Email: ")
                result = self.DB.add_photographer(name, email)
                if result > 0:
                    print("Photographer added")
                else:
                    print("Error adding photographer")

            elif choice == "5":
                # Add album
                print("\nAdd Album")
                name = input("Album name: ")
                creation_date = input("Creation date (YYYY-MM-DD): ")
                result = self.DB.add_album(name, creation_date)
                if result > 0:
                    print("Album added")
                else:
                    print("Error adding album")

            elif choice == "6":
                # Add photo
                print("\nAdd Photo")
                photo_date = input("Photo date (YYYY-MM-DD): ")
                photographer_id = int(input("Photographer ID: "))
                album_id = int(input("Album ID: "))
                result = self.DB.add_photo(photo_date, photographer_id, album_id)
                if result > 0:
                    print("Photo added")
                else:
                    print("Error adding photo")

            elif choice == "7":
                # Change photographer email
                print("\nChange Photographer Email")
                photographer_id = int(input("Photographer ID: "))
                new_email = input("New email: ")
                result = self.DB.change_photographer_email(photographer_id, new_email)
                if result > 0:
                    print("Email updated")
                else:
                    print("No changes made")

            elif choice == "8":
                # Change album name
                print("\nChange Album Name")
                album_id = int(input("Album ID: "))
                new_name = input("New album name: ")
                result = self.DB.change_album_name(album_id, new_name)
                if result > 0:
                    print("Album updated")
                else:
                    print("No changes made")

            elif choice == "9":
                # Change photo album
                print("\nChange Photo Album")
                photo_id = int(input("Photo ID: "))
                new_album_id = int(input("New Album ID: "))
                result = self.DB.change_photo_album(photo_id, new_album_id)
                if result > 0:
                    print("Photo updated")
                else:
                    print("No changes made")

            elif choice == "10":
                # Delete photographer
                print("\nDelete Photographer")
                photographer_id = int(input("Photographer ID: "))
                result = self.DB.delete_photographer(photographer_id)
                if result > 0:
                    print("Photographer deleted")
                else:
                    print("No rows deleted")

            elif choice == "11":
                # Delete album
                print("\nDelete Album")
                album_id = int(input("Album ID: "))
                result = self.DB.delete_album(album_id)
                if result > 0:
                    print("Album deleted")
                else:
                    print("No rows deleted")

            elif choice == "12":
                # Delete photo
                print("\nDelete Photo")
                photo_id = int(input("Photo ID: "))
                result = self.DB.delete_photo(photo_id)
                if result > 0:
                    print("Photo deleted")
                else:
                    print("No rows deleted")

            elif choice == "Q" or choice == "q":
                print("Goodbye")
                running = False

            else:
                print("Invalid choice")
