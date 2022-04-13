from core.schema import signal_mutation_module_validate
from django.db.models import Q
from django.core.exceptions import PermissionDenied
import graphene_django_optimizer as gql_optimizer
from .apps import BankingDetailsConfig
from django.utils.translation import gettext as _
from core.schema import OrderedDjangoFilterConnectionField

# # We do need all queries and mutations in the namespace here.
from .gql_queries import *  # lgtm [py/polluting-import]
from .gql_mutations import *  # lgtm [py/polluting-import]

class Query(graphene.ObjectType):
    InsureeBankingDetails = OrderedDjangoFilterConnectionField(
        InsureeBankDetailsGQLType,
        show_history=graphene.Boolean(),
        client_mutation_id=graphene.String(),
        orderBy=graphene.List(of_type=graphene.String),
    )

    HFBankingDetails = OrderedDjangoFilterConnectionField(
        HealthFacilityBankDetailsGQLType,
        show_history=graphene.Boolean(),
        client_mutation_id=graphene.String(),
        orderBy=graphene.List(of_type=graphene.String),
    )

def resolve_bankingdetails(self, info, **kwargs):
        """
        Extra steps to perform when insuree banking details is queried
        """
        # Check if user has permission
        if not info.context.user.has_perms(BankingDetailsConfig.gql_query_insureebankdetails_perms):
            raise PermissionDenied(_("unauthorized"))
        filters = []
        
        # Used to specify if user want to see all records including invalid records as history
        show_history = kwargs.get('show_history', False)
        if not show_history:
            filters += filter_validity(**kwargs)

        client_mutation_id = kwargs.get("client_mutation_id", None)
        if client_mutation_id:
            filters.append(Q(mutations__mutation__client_mutation_id=client_mutation_id))

        return gql_optimizer.query(InsureeBankDetails.objects.filter(*filters).all(), info)
