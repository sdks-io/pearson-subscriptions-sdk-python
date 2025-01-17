# -*- coding: utf-8 -*-

"""
pearsonsubscriptionsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from pearsonsubscriptionsapi.api_helper import APIHelper
from pearsonsubscriptionsapi.models.initial_term import InitialTerm
from pearsonsubscriptionsapi.models.renewal_term import RenewalTerm


class Terms(object):

    """Implementation of the 'Terms' model.

    Container for the terms and renewal settings of the subscription.

    Attributes:
        initial_term (InitialTerm): Information about the first term of the
            subscription.
        renewal_terms (List[RenewalTerm]): List of renewal terms of the
            subscription. Only applicable if the type of the first term is
            `TERMED` and the value of the `renewalSetting` field is
            `RENEW_WITH_SPECIFIC_TERM`.
        renewal_setting (RenewalSettingEnum): Specifies the type of the terms
            that follow the first term if the subscription is renewed. Only
            applicable if the type of the first term is `TERMED`.  *
            `RENEW_WITH_SPECIFIC_TERM` - Each renewal term has a predefined
            duration. The first entry in `renewalTerms` specifies the duration
            of the second term of the subscription, the second entry in
            `renewalTerms` specifies the duration of the third term of the
            subscription, and so on. The last entry in `renewalTerms`
            specifies the ultimate duration of each renewal term. *
            `RENEW_TO_EVERGREEN` - The second term of the subscription does
            not have a predefined duration.
        auto_renew (bool): Specifies whether the subscription automatically
            renews at the end of the each term. For REDEMPTION, default it to
            false.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "initial_term": 'initialTerm',
        "renewal_terms": 'renewalTerms',
        "renewal_setting": 'renewalSetting',
        "auto_renew": 'autoRenew'
    }

    _optionals = [
        'initial_term',
        'renewal_terms',
        'renewal_setting',
        'auto_renew',
    ]

    def __init__(self,
                 initial_term=APIHelper.SKIP,
                 renewal_terms=APIHelper.SKIP,
                 renewal_setting=APIHelper.SKIP,
                 auto_renew=APIHelper.SKIP):
        """Constructor for the Terms class"""

        # Initialize members of the class
        if initial_term is not APIHelper.SKIP:
            self.initial_term = initial_term 
        if renewal_terms is not APIHelper.SKIP:
            self.renewal_terms = renewal_terms 
        if renewal_setting is not APIHelper.SKIP:
            self.renewal_setting = renewal_setting 
        if auto_renew is not APIHelper.SKIP:
            self.auto_renew = auto_renew 

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
        initial_term = InitialTerm.from_dictionary(dictionary.get('initialTerm')) if 'initialTerm' in dictionary.keys() else APIHelper.SKIP
        renewal_terms = None
        if dictionary.get('renewalTerms') is not None:
            renewal_terms = [RenewalTerm.from_dictionary(x) for x in dictionary.get('renewalTerms')]
        else:
            renewal_terms = APIHelper.SKIP
        renewal_setting = dictionary.get("renewalSetting") if dictionary.get("renewalSetting") else APIHelper.SKIP
        auto_renew = dictionary.get("autoRenew") if "autoRenew" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(initial_term,
                   renewal_terms,
                   renewal_setting,
                   auto_renew)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'initial_term={self.initial_term!r}, '
                f'renewal_terms={self.renewal_terms!r}, '
                f'renewal_setting={self.renewal_setting!r}, '
                f'auto_renew={self.auto_renew!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'initial_term={self.initial_term!s}, '
                f'renewal_terms={self.renewal_terms!s}, '
                f'renewal_setting={self.renewal_setting!s}, '
                f'auto_renew={self.auto_renew!s})')
