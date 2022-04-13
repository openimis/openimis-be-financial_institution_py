from django.apps import AppConfig

MODULE_NAME = "banking_details"

DEFAULT_CFG = {
    "gql_query_insureebankdetails_perms": ["180001"],
    "gql_query_insureebankdetail_perms": ["180001"],
    "gql_mutation_create_insureebankdetail_perms": ["180002"],
    "gql_mutation_update_insureebankdetail_perms": ["180003"],
    "gql_mutation_delete_insureebankdetail_perms": ["18004"],
    "gql_query_HFacilitybankdetail_perms": ["180005"],
    "gql_mutation_create_HFacilitybankdetail_perms": ["180006"],
    "gql_mutation_update_HFacilitybankdetail_perms": ["180007"],
    "gql_mutation_delete_HFacilitybankdetail_perms": ["18008"],
}

class BankingDetailsConfig(AppConfig):
    name = 'banking_details'

    gql_query_insureebankdetails_perms = []
    gql_query_insureebankdetail_perms = []
    gql_mutation_create_insureebankdetail_perms = []
    gql_mutation_update_insureebankdetail_perms = []
    gql_mutation_delete_insureebankdetail_perms = []
    gql_query_HFacilitybankdetail_perms = []
    gql_mutation_create_HFacilitybankdetail_perms = []
    gql_mutation_update_HFacilitybankdetail_perms = []
    gql_mutation_delete_HFacilitybankdetail_perms = []

    def _configure_permissions(self, cfg):
        BankingDetailsConfig.gql_query_insureebankdetails_perms = cfg["gql_query_insureebankdetails_perms"]
        BankingDetailsConfig.gql_query_insureebankdetail_perms = cfg["gql_query_insureebankdetail_perms"]
        BankingDetailsConfig.gql_mutation_create_insureebankdetail_perms = cfg["gql_mutation_create_insureebankdetail_perms"]
        BankingDetailsConfig.gql_mutation_update_insureebankdetail_perms = cfg["gql_mutation_update_insureebankdetail_perms"]
        BankingDetailsConfig.gql_mutation_delete_insureebankdetail_perms = cfg["gql_mutation_delete_insureebankdetail_perms"]
        BankingDetailsConfig.gql_query_HFacilitybankdetail_perms = cfg["gql_query_HFacilitybankdetail_perms"]
        BankingDetailsConfig.gql_mutation_create_HFacilitybankdetail_perms = cfg["gql_mutation_create_HFacilitybankdetail_perms"]
        BankingDetailsConfig.gql_mutation_update_HFacilitybankdetail_perms = cfg["gql_mutation_update_HFacilitybankdetail_perms"]
        BankingDetailsConfig.gql_mutation_delete_HFacilitybankdetail_perms = cfg["gql_mutation_delete_HFacilitybankdetail_perms"]

    def ready(self):
        from core.models import ModuleConfiguration
        cfg = ModuleConfiguration.get_or_default(MODULE_NAME, DEFAULT_CFG)
        self._configure_permissions(cfg)
