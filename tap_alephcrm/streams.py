"""Stream type classes for tap-alephcrm."""

from __future__ import annotations

import typing as t
from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_alephcrm.client import alephcrmStream


class AccountsStream(alephcrmStream):
    name = "accounts"
    path = "/v2/accounts"
    primary_keys: t.ClassVar[list[str]] = ["Id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("Id", th.IntegerType),
        th.Property("DocType", th.StringType),
        th.Property("DocNumber", th.StringType),
        th.Property("Name", th.StringType),
        th.Property("BusinessName", th.StringType)
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "accountId": record["Id"]
        }


class MarketplacesStream(AccountsStream):
    name = "marketplaces"
    path = "/v2/accounts/{accountId}/marketplaces"
    primary_keys: t.ClassVar[list[str]] = ["Id"]
    replication_key = None

    parent_stream_type = AccountsStream
    ignore_parent_replication_keys = True

    schema = th.PropertiesList(
        th.Property("accountId", th.IntegerType),
        th.Property("Id", th.IntegerType),
        th.Property("Name", th.StringType)
    ).to_dict()


class StoresStream(AccountsStream):
    name = "stores"
    path = "/v2/accounts/{accountId}/stores"
    primary_keys: t.ClassVar[list[str]] = ["Id"]
    replication_key = None

    parent_stream_type = AccountsStream
    ignore_parent_replication_keys = True

    schema = th.PropertiesList(
        th.Property("accountId", th.IntegerType),
        th.Property("Id", th.IntegerType),
        th.Property("IntegrationCode", th.StringType),
        th.Property(
            "ExternalStoreId",
            th.ArrayType(
                th.ObjectType(
                    th.Property("ExternalId", th.StringType),
                    th.Property("Name", th.StringType),
                    th.Property("MarketPlaceId", th.IntegerType)
                )
            )
        ),
        th.Property("IsPrincipal", th.BooleanType),
        th.Property("OpenHours", th.StringType),
        th.Property("AvailabilityTimeInHours", th.IntegerType),
        th.Property("AdditionalTimeInHours", th.IntegerType),
        th.Property("AllowPickUpStore", th.BooleanType),
        th.Property("AllowShipments", th.BooleanType),
        th.Property(
            "AccountPickup",
            th.ObjectType(
                th.Property("Id", th.IntegerType),
                th.Property("Name", th.StringType),
                th.Property("BusinessName", th.StringType),
                th.Property("ExternalPickupId", th.IntegerType),
                th.Property("IntegrationCode", th.StringType),
                th.Property("SellerAccountId", th.IntegerType)
            )
        ),
        th.Property(
            "LogisticTagsExclude",
            th.ArrayType(
                th.StringType
            )
        ),
        th.Property("Zone", th.StringType),
        th.Property(
            "Address",
            th.ObjectType(
                th.Property("CountryId", th.StringType),
                th.Property("StateCode", th.StringType),
                th.Property("State", th.StringType),
                th.Property("City", th.StringType),
                th.Property("Neighborhood", th.StringType),
                th.Property("StreetName", th.StringType),
                th.Property("StreetNumber", th.StringType),
                th.Property("ZipCode", th.StringType),
                th.Property("Notes", th.StringType),
                th.Property("Description", th.StringType),
                th.Property("Phone", th.StringType),
                th.Property("AlternativePhone", th.StringType)
            )
        ),
        th.Property("DateCreated", th.DateTimeType),
        th.Property("Name", th.StringType),
        th.Property("BusinessName", th.StringType)
    ).to_dict()
