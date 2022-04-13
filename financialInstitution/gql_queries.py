import graphene
from graphene_django import DjangoObjectType
from core import prefix_filterset, filter_validity, ExtendedConnection
from .models import *


class InsureeBankDetailsGQLType(DjangoObjectType):
    
    class Meta:
        model = InsureeBankDetails
        filter_fields = {
            "id": ["exact"],
            "uuid": ["exact"],
            "financial_service_provider": ["exact"],
            "insuree_account_number": ["exact"],
            "insuree_account_name": ["exact"]
        }
        interfaces = (graphene.relay.Node,)
        connection_class = ExtendedConnection

class HealthFacilityBankDetailsGQLType(DjangoObjectType):
    
    class Meta:
        model = HealthFacilityBankDetails
        filter_fields = {
            "id": ["exact"],
            "uuid": ["exact"],
            "financial_service_provider": ["exact"],
            "insuree_account_number": ["exact"],
            "health_facility_account_name": ["exact"]
        }
        interfaces = (graphene.relay.Node,)
        connection_class = ExtendedConnection
