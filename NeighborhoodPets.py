#Author: Faith Elledge
#Githubuser: Elledgef
#Data: 10/26/22
#Description: Class that adds a pet to the list, deletes a pet from the list. searches for the owener, gets a
# list of all pet species, saves a json file and loads a json file.

import json

class Neighborhoodpets:
    """ Stores data from pet list, species, and owner name"""

    def __init__(self):
            self._pet_data_list = []

    def save_as_json(self,filename):
        """Saves json file"""
        with open('filename', 'w') as outfile:
            for pets in self._pet_data_list:
                    outfile.write(str(pets) + '\n')

    def read_json(self,filename):
        """Reads json file"""
        with open('filename','r') as infile:
                self._pet_data_list = json.load(infile)['data']

    def add_pet(self, pet_name, species, owner):
        """Adds Pet"""
        self._name = pet_name
        self._species = species
        self._owner = owner

    def delete_pet(self, pet_name):
        """Deletes pet"""
        self._pet_data_list.remove(pet_name)

    def get_owner(self,owner_name):
        """ Finds Owner"""
        self._owner = owner_name

    def get_all_species(self):
        """ Set of all species"""
        for pets in self._pet_data_list:
            self._pet_data_list.append(pets(self._species))
        return (self._species)




