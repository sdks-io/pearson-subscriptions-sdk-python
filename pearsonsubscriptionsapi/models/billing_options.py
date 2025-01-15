# -*- coding: utf-8 -*-

"""
pearsonsubscriptionsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from pearsonsubscriptionsapi.api_helper import APIHelper


class BillingOptions(object):

    """Implementation of the 'BillingOptions' model.

    TODO: type model description here.

    Attributes:
        document_date (date): TODO: type description here.
        target_date (date): For REDEMPTION, it is end of term date

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "document_date": 'documentDate',
        "target_date": 'targetDate'
    }

    _optionals = [
        'document_date',
        'target_date',
    ]

    def __init__(self,
                 document_date=APIHelper.SKIP,
                 target_date=APIHelper.SKIP):
        """Constructor for the BillingOptions class"""

        # Initialize members of the class
        if document_date is not APIHelper.SKIP:
            self.document_date = document_date 
        if target_date is not APIHelper.SKIP:
            self.target_date = target_date 

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
        document_date = dateutil.parser.parse(dictionary.get('documentDate')).date() if dictionary.get('documentDate') else APIHelper.SKIP
        target_date = dateutil.parser.parse(dictionary.get('targetDate')).date() if dictionary.get('targetDate') else APIHelper.SKIP
        # Return an object of this model
        return cls(document_date,
                   target_date)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'document_date={self.document_date!r}, '
                f'target_date={self.target_date!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'document_date={self.document_date!s}, '
                f'target_date={self.target_date!s})')