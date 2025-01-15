# -*- coding: utf-8 -*-

"""
pearsonsubscriptionsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pearsonsubscriptionsapi.api_helper import APIHelper
from pearsonsubscriptionsapi.models.subscribe_to_rate_plans_charge_override import SubscribeToRatePlansChargeOverride


class SubscribeToRatePlan(object):

    """Implementation of the 'SubscribeToRatePlan' model.

    TODO: type model description here.

    Attributes:
        product_rate_plan_id (str): This is unique Product Rate Plan id which
            signifies the subscription
            type,entitlementLevel,maxEntitlements,numEntitlements etc.
        subscribe_to_rate_plans_charge_overrides
            (List[SubscribeToRatePlansChargeOverride]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_rate_plan_id": 'productRatePlanId',
        "subscribe_to_rate_plans_charge_overrides": 'subscribeToRatePlansChargeOverrides'
    }

    _optionals = [
        'product_rate_plan_id',
        'subscribe_to_rate_plans_charge_overrides',
    ]

    def __init__(self,
                 product_rate_plan_id=APIHelper.SKIP,
                 subscribe_to_rate_plans_charge_overrides=APIHelper.SKIP):
        """Constructor for the SubscribeToRatePlan class"""

        # Initialize members of the class
        if product_rate_plan_id is not APIHelper.SKIP:
            self.product_rate_plan_id = product_rate_plan_id 
        if subscribe_to_rate_plans_charge_overrides is not APIHelper.SKIP:
            self.subscribe_to_rate_plans_charge_overrides = subscribe_to_rate_plans_charge_overrides 

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
        subscribe_to_rate_plans_charge_overrides = None
        if dictionary.get('subscribeToRatePlansChargeOverrides') is not None:
            subscribe_to_rate_plans_charge_overrides = [SubscribeToRatePlansChargeOverride.from_dictionary(x) for x in dictionary.get('subscribeToRatePlansChargeOverrides')]
        else:
            subscribe_to_rate_plans_charge_overrides = APIHelper.SKIP
        # Return an object of this model
        return cls(product_rate_plan_id,
                   subscribe_to_rate_plans_charge_overrides)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'product_rate_plan_id={self.product_rate_plan_id!r}, '
                f'subscribe_to_rate_plans_charge_overrides={self.subscribe_to_rate_plans_charge_overrides!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'product_rate_plan_id={self.product_rate_plan_id!s}, '
                f'subscribe_to_rate_plans_charge_overrides={self.subscribe_to_rate_plans_charge_overrides!s})')