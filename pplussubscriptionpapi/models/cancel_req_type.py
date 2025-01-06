# -*- coding: utf-8 -*-

"""
pplussubscriptionpapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CancelReqType(object):

    """Implementation of the 'CancelReqType' model.

    TODO: type model description here.

    Attributes:
        subscription_id (str): Subscription id
        subscription_source (SubscriptionSourceEnum): Internal or external
        cancel_reason (str): Reason for subscription cancel
        cancel_date (str): cancellation date

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_id": 'subscriptionId',
        "subscription_source": 'subscriptionSource',
        "cancel_reason": 'cancelReason',
        "cancel_date": 'cancelDate'
    }

    def __init__(self,
                 subscription_id=None,
                 subscription_source=None,
                 cancel_reason=None,
                 cancel_date=None):
        """Constructor for the CancelReqType class"""

        # Initialize members of the class
        self.subscription_id = subscription_id 
        self.subscription_source = subscription_source 
        self.cancel_reason = cancel_reason 
        self.cancel_date = cancel_date 

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
        subscription_id = dictionary.get("subscriptionId") if dictionary.get("subscriptionId") else None
        subscription_source = dictionary.get("subscriptionSource") if dictionary.get("subscriptionSource") else None
        cancel_reason = dictionary.get("cancelReason") if dictionary.get("cancelReason") else None
        cancel_date = dictionary.get("cancelDate") if dictionary.get("cancelDate") else None
        # Return an object of this model
        return cls(subscription_id,
                   subscription_source,
                   cancel_reason,
                   cancel_date)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'subscription_id={self.subscription_id!r}, '
                f'subscription_source={self.subscription_source!r}, '
                f'cancel_reason={self.cancel_reason!r}, '
                f'cancel_date={self.cancel_date!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'subscription_id={self.subscription_id!s}, '
                f'subscription_source={self.subscription_source!s}, '
                f'cancel_reason={self.cancel_reason!s}, '
                f'cancel_date={self.cancel_date!s})')