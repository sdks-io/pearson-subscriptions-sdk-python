# -*- coding: utf-8 -*-

"""
pearsonsubscriptionsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pearsonsubscriptionsapi.api_helper import APIHelper


class OrderError(object):

    """Implementation of the 'OrderError' model.

    TODO: type model description here.

    Attributes:
        code (str): Error codes.
        message (str): Error message.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "message": 'message'
    }

    _optionals = [
        'code',
        'message',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 message=APIHelper.SKIP):
        """Constructor for the OrderError class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
        if message is not APIHelper.SKIP:
            self.message = message 

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
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   message)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'code={self.code!r}, '
                f'message={self.message!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'code={self.code!s}, '
                f'message={self.message!s})')
