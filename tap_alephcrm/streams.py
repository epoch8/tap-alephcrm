"""Stream type classes for tap-alephcrm."""

from __future__ import annotations

import typing as t
from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers
from singer_sdk.pagination import BaseOffsetPaginator

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


class MyPaginator(BaseOffsetPaginator):
    def has_more(self, response):
        data = response.json()
        limit = data.get("Paging", {}).get("Limit", {})
        offset = data.get("Paging", {}).get("Offset", {})
        total = data.get("Paging", {}).get("Total", {})
        return offset + limit < total


class OrdersStream(AccountsStream):
    name = "orders"
    path = "/v2/orders"
    primary_keys: t.ClassVar[list[str]] = ["Id"]
    replication_key = None

    parent_stream_type = AccountsStream
    ignore_parent_replication_keys = True

    schema = th.PropertiesList(
        th.Property("accountId", th.IntegerType),
        th.Property("Id", th.IntegerType),
        th.Property("ExternalOrderId", th.StringType),
        th.Property("PackId", th.StringType),
        th.Property("SourcePackId", th.StringType),
        th.Property("IsCompletePackOrder", th.BooleanType),
        th.Property(
            "SellerAccount",
            th.ObjectType(
                th.Property("Id", th.IntegerType),
                th.Property("OwnCode", th.StringType),
                th.Property("Name", th.StringType),
                th.Property("BusinessName", th.StringType)
            )
        ),
        th.Property(
            "Items",
            th.ArrayType(
                th.ObjectType(
                    th.Property("Id", th.IntegerType),
                    th.Property(
                        "Type",
                        th.ObjectType(
                            th.Property("Key", th.IntegerType),
                            th.Property("Value", th.StringType)
                        )
                    ),
                    th.Property("ParentItemId", th.IntegerType),
                    th.Property(
                        "Product",
                        th.ObjectType(
                            th.Property("Id", th.IntegerType),
                            th.Property("Sku", th.StringType),
                            th.Property("Brand", th.StringType),
                            th.Property("SellerSku", th.StringType),
                            th.Property("EAN", th.StringType),
                            th.Property(
                                "Attributes",
                                th.ObjectType(
                                    th.Property(
                                        "NetWeight",
                                        th.ObjectType(
                                            th.Property("Key", th.StringType),
                                            th.Property("Value", th.IntegerType)
                                        )
                                    ),
                                    th.Property(
                                        "SalesTags",
                                        th.ObjectType(
                                            th.Property("Text", th.StringType),
                                            th.Property(
                                                "Items",
                                                th.ArrayType(th.StringType)
                                            ),
                                            th.Property("Delimiter", th.StringType)
                                        )
                                    )
                                )
                            ),
                            th.Property("Title", th.StringType),
                            th.Property("IntegrationCode", th.StringType),
                            th.Property(
                                "Category",
                                th.ObjectType(
                                    th.Property("Key", th.StringType),
                                    th.Property("Key", th.StringType)
                                )
                            )
                        )
                    ),
                    th.Property(
                        "ProductListing",
                        th.ObjectType(
                            th.Property("Reference", th.StringType),
                            th.Property("Id", th.IntegerType),
                            th.Property()
                        )
                    )
                )
            )
        )
    ).to_dict()

    def get_new_paginator(self):
        return MyPaginator(start_value=0, page_size=100)

    def get_url_params(self, context, next_page_token):
        params = {
            "accountId": context["accountId"]
        }

        # Next page token is an offset
        if next_page_token:
            params["offset"] = next_page_token

        return params
