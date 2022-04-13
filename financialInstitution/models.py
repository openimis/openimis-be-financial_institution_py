from django.db import models
from insuree.models import *
from location.models import *

# Create your models here.

class InsureeBankDetails(core_models.VersionedModel):
    id = models.AutoField(
        db_column='SchemeID', primary_key=True)
        
    uuid = models.CharField(db_column='InsureeBankDetailsUUID',
                            max_length=36, default=uuid.uuid4, unique=True)
    insuree = models.ForeignKey(Insuree, on_delete=models.CASCADE)
    financial_service_provider = models.CharField(db_column='FinancialServiceProvider', max_length=255)
    insuree_account_number = models.CharField(db_column='InsureeAccountNumber', max_length=255)
    insuree_account_name = models.CharField(db_column='InsureeAccountName', max_length=255)

    class Meta:
        managed = True
        db_table = 'tblInsureeBankDetails'

class HealthFacilityBankDetails(core_models.VersionedModel):
    id = models.AutoField(
        db_column='SchemeID', primary_key=True)
        
    uuid = models.CharField(db_column='HealthFacilityBankDetailsUUID',
                            max_length=36, default=uuid.uuid4, unique=True)
    health_facility = models.ForeignKey(HealthFacility, on_delete=models.CASCADE)
    financial_service_provider = models.CharField(db_column='FinancialServiceProvider', max_length=255)
    insuree_account_number = models.CharField(db_column='HealthFacilityAccountNumber', max_length=255)
    health_facility_account_name = models.CharField(db_column='HealthFacilityAccountName', max_length=255)

    class Meta:
        managed = True
        db_table = 'tblHealthFacilityBankDetails'

class InsureeBankDetailsMutation(core_models.UUIDModel, core_models.ObjectMutation):
    insuree_bank_details = models.ForeignKey(InsureeBankDetails, models.DO_NOTHING,
                              related_name='mutations')
    mutation = models.ForeignKey(
        core_models.MutationLog, models.DO_NOTHING, related_name='insureeBankDetails')

    class Meta:
        managed = True
        db_table = "insuree_BankDetailsMutation"

class HealthFacilityBankDetailsMutation(core_models.UUIDModel, core_models.ObjectMutation):
    health_facility_bank_details = models.ForeignKey(HealthFacilityBankDetails, models.DO_NOTHING,
                              related_name='mutations')
    mutation = models.ForeignKey(
        core_models.MutationLog, models.DO_NOTHING, related_name='healthFacilityBankDetails')

    class Meta:
        managed = True
        db_table = "health_facility_FamilyMutation"
