# -*- coding: utf-8 -*-

"""
pearsonsubscriptionsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pearsonsubscriptionsapi.api_helper import APIHelper


class OrderRespType(object):

    """Implementation of the 'OrderRespType' model.

    TODO: type model description here.

    Attributes:
        message (str): message description once subscription creation is
            sucess.
        order_number (str): order number.
        subscription_number (str): subscription id.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message": 'message',
        "order_number": 'orderNumber',
        "subscription_number": 'subscriptionNumber'
    }

    _optionals = [
        'message',
        'order_number',
        'subscription_number',
    ]

    def __init__(self,
                 message=APIHelper.SKIP,
                 order_number=APIHelper.SKIP,
                 subscription_number=APIHelper.SKIP):
        """Constructor for the OrderRespType class"""

        # Initialize members of the class
        if message is not APIHelper.SKIP:
            self.message = message 
        if order_number is not APIHelper.SKIP:
            self.order_number = order_number 
        if subscription_number is not APIHelper.SKIP:
            self.subscription_number = subscription_number 

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
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        order_number = dictionary.get("orderNumber") if dictionary.get("orderNumber") else APIHelper.SKIP
        subscription_number = dictionary.get("subscriptionNumber") if dictionary.get("subscriptionNumber") else APIHelper.SKIP
        # Return an object of this model
        return cls(message,
                   order_number,
                   subscription_number)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'message={self.message!r}, '
                f'order_number={self.order_number!r}, '
                f'subscription_number={self.subscription_number!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'message={self.message!s}, '
                f'order_number={self.order_number!s}, '
                f'subscription_number={self.subscription_number!s})')
