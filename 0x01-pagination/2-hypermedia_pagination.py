#!/usr/bin/env python3
""" Task 1: Simple pagination """
import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initializes an instance of server class """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Finds indexes to paginate and returns the corresponding pages """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        all_of_data = self.dataset()
        Page_list = []

        """ Check to see if # of entries is larger than dataset """
        the_range = (page * page_size)
        if the_range > len(all_of_data):
            """ Return empty list if yes """
            return Page_list

        """ Between start and end idx create new page and append to list """
        both_indexes = index_range(page, page_size)
        for i in range(both_indexes[0], both_indexes[1]):
            new_page = all_of_data[i]
            Page_list.append(new_page)
        return Page_list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Return a dict containing the key/value pairs as listed """
        hp_dict = {}
        all_of_data = self.dataset()
        data_size = len(all_of_data)
        the_range = (page * page_size)
        total_page = (data_size + 1) / page_size
        if the_range > data_size:
            hp_dict['page_size'] = 0
            hp_dict['page'] = page
            hp_dict['data'] = []
            hp_dict['next_page'] = None
            hp_dict['prev_page'] = (page - 1)
            hp_dict['total_pages'] = (total_page + 1)

        else:
            hp_dict['page_size'] = page_size
            hp_dict['page'] = page
            hp_dict['data'] = self.get_page(page, page_size)
            hp_dict['next_page'] = (page + 1)
            if hp_dict['page'] == 1:
                hp_dict['prev_page'] = None
            else:
                hp_dict['prev_page'] = (page - 1)
            hp_dict['total_pages'] = total_page
        return hp_dict
