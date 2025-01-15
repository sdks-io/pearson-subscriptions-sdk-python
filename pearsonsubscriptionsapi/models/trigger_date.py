# -*- coding: utf-8 -*-

"""
pearsonsubscriptionsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pearsonsubscriptionsapi.api_helper import APIHelper


class TriggerDate(object):

    """Implementation of the 'TriggerDate' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        trigger_date (str): Date in YYYY-MM-DD format.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "trigger_date": 'triggerDate'
    }

    _optionals = [
        'name',
        'trigger_date',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 trigger_date=APIHelper.SKIP):
        """Constructor for the TriggerDate class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if trigger_date is not APIHelper.SKIP:
            self.trigger_date = trigger_date 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        trigger_date = dictionary.get("triggerDate") if dictionary.get("triggerDate") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   trigger_date)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'trigger_date={self.trigger_date!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'trigger_date={self.trigger_date!s})')