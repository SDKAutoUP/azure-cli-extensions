# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class AlertOperations(object):
    """AlertOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~cost_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        scope,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.AlertsResult"
        """Lists the alerts for scope defined.

        :param scope: The scope associated with alerts operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AlertsResult, or the result of cls(response)
        :rtype: ~cost_management_client.models.AlertsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AlertsResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01"

        # Construct URL
        url = self.list.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AlertsResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/alerts'}  # type: ignore

    def get(
        self,
        scope,  # type: str
        alert_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Alert"
        """Gets the alert for the scope by alert ID.

        :param scope: The scope associated with alerts operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners.
        :type scope: str
        :param alert_id: Alert ID.
        :type alert_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Alert, or the result of cls(response)
        :rtype: ~cost_management_client.models.Alert
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Alert"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'alertId': self._serialize.url("alert_id", alert_id, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Alert', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/alerts/{alertId}'}  # type: ignore

    def dismiss(
        self,
        scope,  # type: str
        alert_id,  # type: str
        definition=None,  # type: Optional["models.AlertPropertiesDefinition"]
        description=None,  # type: Optional[str]
        source=None,  # type: Optional[Union[str, "models.AlertSource"]]
        cost_entity_id=None,  # type: Optional[str]
        status=None,  # type: Optional[Union[str, "models.AlertStatus"]]
        creation_time=None,  # type: Optional[str]
        close_time=None,  # type: Optional[str]
        modification_time=None,  # type: Optional[str]
        status_modification_user_name=None,  # type: Optional[str]
        status_modification_time=None,  # type: Optional[str]
        time_grain_type=None,  # type: Optional[Union[str, "models.AlertTimeGrainType"]]
        period_start_date=None,  # type: Optional[str]
        triggered_by=None,  # type: Optional[str]
        resource_group_filter=None,  # type: Optional[List[object]]
        resource_filter=None,  # type: Optional[List[object]]
        meter_filter=None,  # type: Optional[List[object]]
        tag_filter=None,  # type: Optional[object]
        threshold=None,  # type: Optional[float]
        operator=None,  # type: Optional[Union[str, "models.AlertOperator"]]
        amount=None,  # type: Optional[float]
        unit=None,  # type: Optional[str]
        current_spend=None,  # type: Optional[float]
        contact_emails=None,  # type: Optional[List[str]]
        contact_groups=None,  # type: Optional[List[str]]
        contact_roles=None,  # type: Optional[List[str]]
        overriding_alert=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Alert"
        """Dismisses the specified alert.

        :param scope: The scope associated with alerts operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners.
        :type scope: str
        :param alert_id: Alert ID.
        :type alert_id: str
        :param definition: defines the type of alert.
        :type definition: ~cost_management_client.models.AlertPropertiesDefinition
        :param description: Alert description.
        :type description: str
        :param source: Source of alert.
        :type source: str or ~cost_management_client.models.AlertSource
        :param cost_entity_id: related budget.
        :type cost_entity_id: str
        :param status: alert status.
        :type status: str or ~cost_management_client.models.AlertStatus
        :param creation_time: dateTime in which alert was created.
        :type creation_time: str
        :param close_time: dateTime in which alert was closed.
        :type close_time: str
        :param modification_time: dateTime in which alert was last modified.
        :type modification_time: str
        :param status_modification_user_name:
        :type status_modification_user_name: str
        :param status_modification_time: dateTime in which the alert status was last modified.
        :type status_modification_time: str
        :param time_grain_type: Type of timegrain cadence.
        :type time_grain_type: str or ~cost_management_client.models.AlertTimeGrainType
        :param period_start_date: datetime of periodStartDate.
        :type period_start_date: str
        :param triggered_by: notificationId that triggered this alert.
        :type triggered_by: str
        :param resource_group_filter: array of resourceGroups to filter by.
        :type resource_group_filter: list[object]
        :param resource_filter: array of resources to filter by.
        :type resource_filter: list[object]
        :param meter_filter: array of meters to filter by.
        :type meter_filter: list[object]
        :param tag_filter: tags to filter by.
        :type tag_filter: object
        :param threshold: notification threshold percentage as a decimal which activated this alert.
        :type threshold: float
        :param operator: operator used to compare currentSpend with amount.
        :type operator: str or ~cost_management_client.models.AlertOperator
        :param amount: budget threshold amount.
        :type amount: float
        :param unit: unit of currency being used.
        :type unit: str
        :param current_spend: current spend.
        :type current_spend: float
        :param contact_emails: list of emails to contact.
        :type contact_emails: list[str]
        :param contact_groups: list of action groups to broadcast to.
        :type contact_groups: list[str]
        :param contact_roles: list of contact roles.
        :type contact_roles: list[str]
        :param overriding_alert: overriding alert.
        :type overriding_alert: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Alert, or the result of cls(response)
        :rtype: ~cost_management_client.models.Alert
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Alert"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _parameters = models.DismissAlertPayload(definition=definition, description=description, source=source, cost_entity_id=cost_entity_id, status=status, creation_time=creation_time, close_time=close_time, modification_time=modification_time, status_modification_user_name=status_modification_user_name, status_modification_time=status_modification_time, time_grain_type=time_grain_type, period_start_date=period_start_date, triggered_by=triggered_by, resource_group_filter=resource_group_filter, resource_filter=resource_filter, meter_filter=meter_filter, tag_filter=tag_filter, threshold=threshold, operator=operator, amount=amount, unit=unit, current_spend=current_spend, contact_emails=contact_emails, contact_groups=contact_groups, contact_roles=contact_roles, overriding_alert=overriding_alert)
        api_version = "2020-06-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.dismiss.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'alertId': self._serialize.url("alert_id", alert_id, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_parameters, 'DismissAlertPayload')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Alert', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    dismiss.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/alerts/{alertId}'}  # type: ignore

    def list_external(
        self,
        external_cloud_provider_type,  # type: Union[str, "models.ExternalCloudProviderType"]
        external_cloud_provider_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.AlertsResult"
        """Lists the Alerts for external cloud provider type defined.

        :param external_cloud_provider_type: The external cloud provider type associated with
         dimension/query operations. This includes 'externalSubscriptions' for linked account and
         'externalBillingAccounts' for consolidated account.
        :type external_cloud_provider_type: str or ~cost_management_client.models.ExternalCloudProviderType
        :param external_cloud_provider_id: This can be '{externalSubscriptionId}' for linked account or
         '{externalBillingAccountId}' for consolidated account used with dimension/query operations.
        :type external_cloud_provider_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AlertsResult, or the result of cls(response)
        :rtype: ~cost_management_client.models.AlertsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AlertsResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01"

        # Construct URL
        url = self.list_external.metadata['url']  # type: ignore
        path_format_arguments = {
            'externalCloudProviderType': self._serialize.url("external_cloud_provider_type", external_cloud_provider_type, 'str'),
            'externalCloudProviderId': self._serialize.url("external_cloud_provider_id", external_cloud_provider_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AlertsResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_external.metadata = {'url': '/providers/Microsoft.CostManagement/{externalCloudProviderType}/{externalCloudProviderId}/alerts'}  # type: ignore
