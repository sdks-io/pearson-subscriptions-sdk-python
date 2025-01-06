# -*- coding: utf-8 -*-

"""
pplussubscriptionpapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pplussubscriptionpapi.api_helper import APIHelper


class UpdateSubscriptionProcessingOptions(object):

    """Implementation of the 'updateSubscriptionProcessingOptions' model.

    Invoice or Payment.

    Attributes:
        run_billing (bool): Indicates if the current request needs to generate
            an invoice. The invoice will be generated against all
            subscriptions included in this order.
        collect_payment (bool): Indicates if the current request needs to
            collect payments. This value can not be 'true' when 'runBilling'
            flag is 'false'.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "run_billing": 'runBilling',
        "collect_payment": 'collectPayment'
    }

    _optionals = [
        'run_billing',
        'collect_payment',
    ]

    def __init__(self,
                 run_billing=APIHelper.SKIP,
                 collect_payment=APIHelper.SKIP):
        """Constructor for the UpdateSubscriptionProcessingOptions class"""

        # Initialize members of the class
        if run_billing is not APIHelper.SKIP:
            self.run_billing = run_billing 
        if collect_payment is not APIHelper.SKIP:
            self.collect_payment = collect_payment 

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
        run_billing = dictionary.get("runBilling") if "runBilling" in dictionary.keys() else APIHelper.SKIP
        collect_payment = dictionary.get("collectPayment") if "collectPayment" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(run_billing,
                   collect_payment)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'run_billing={self.run_billing!r}, '
                f'collect_payment={self.collect_payment!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'run_billing={self.run_billing!s}, '
                f'collect_payment={self.collect_payment!s})')
