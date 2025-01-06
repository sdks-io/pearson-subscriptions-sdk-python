# -*- coding: utf-8 -*-

"""
pplussubscriptionpapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pplussubscriptionpapi.api_helper import APIHelper


class RemoveProduct(object):

    """Implementation of the 'removeProduct' model.

    Remove product details from the subscription plan

    Attributes:
        product_rate_plan_id (str): Internal identifier of the product rate
            plan that the rate plan is based on.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_rate_plan_id": 'productRatePlanId'
    }

    _optionals = [
        'product_rate_plan_id',
    ]

    def __init__(self,
                 product_rate_plan_id=APIHelper.SKIP):
        """Constructor for the RemoveProduct class"""

        # Initialize members of the class
        if product_rate_plan_id is not APIHelper.SKIP:
            self.product_rate_plan_id = product_rate_plan_id 

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
        product_rate_plan_id = dictionary.get("productRatePlanId") if dictionary.get("productRatePlanId") else APIHelper.SKIP
        # Return an object of this model
        return cls(product_rate_plan_id)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'product_rate_plan_id={self.product_rate_plan_id!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'product_rate_plan_id={self.product_rate_plan_id!s})')