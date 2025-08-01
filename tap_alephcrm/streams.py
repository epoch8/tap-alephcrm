"""Stream type classes for tap-alephcrm."""

from __future__ import annotations

import typing as t
from pathlib import Path
from datetime import datetime

from singer_sdk import typing as th  # JSON Schema typing helpers
from singer_sdk.pagination import BaseOffsetPaginator

from tap_alephcrm.client import alephcrmStream

from .schemas.StoresStream import schema as schema__StoresStream
from .schemas.OrdersStream import schema as schema__OrdersStream
from .schemas.ProductsStream import schema as schema__ProductsStream


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


    def get_child_context(self, record: dict, context: t.Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "accountId": record["Id"]
        }


class MarketplacesStream(alephcrmStream):
    name = "marketplaces"
    path = "/v2/accounts/{accountId}/marketplaces"
    primary_keys: t.ClassVar[list[str]] = ["accountId", "Id"]
    replication_key = None

    parent_stream_type = AccountsStream
    ignore_parent_replication_keys = True

    schema = th.PropertiesList(
        th.Property("accountId", th.IntegerType),
        th.Property("Id", th.IntegerType),
        th.Property("Name", th.StringType)
    ).to_dict()


class StoresStream(alephcrmStream):
    name = "stores"
    path = "/v2/accounts/{accountId}/stores"
    primary_keys: t.ClassVar[list[str]] = ["accountId", "Id"]
    replication_key = None

    parent_stream_type = AccountsStream
    ignore_parent_replication_keys = True

    schema = schema__StoresStream


class MyPaginator(BaseOffsetPaginator):
    def has_more(self, response):
        data = response.json()
        limit = data.get("Paging", {}).get("Limit", {})
        offset = data.get("Paging", {}).get("Offset", {})
        total = data.get("Paging", {}).get("Total", {})
        return offset + limit < total


class OrdersStream(alephcrmStream):
    name = "orders"
    path = "/v2/orders"
    primary_keys: t.ClassVar[list[str]] = ["accountId", "Id"]
    replication_key = "DateCreated"
    STATE_MSG_FREQUENCY = 100
    is_sorted = True

    parent_stream_type = AccountsStream
    ignore_parent_replication_keys = True

    schema = schema__OrdersStream


    def get_new_paginator(self):
        return MyPaginator(start_value=0, page_size=100)
    

    def get_url_params(self, context, next_page_token):
        params = {
            "accountId": context["accountId"],
            "sort": "dateCreated",
        }

        if (replication_key_value := self.get_starting_replication_key_value(context=context)) is not None:
            replication_key_value = datetime.strptime(replication_key_value, "%Y-%m-%dT%H:%M:%SZ")
            replication_key_value = datetime.strftime(replication_key_value, "%Y-%m-%d %H:%M")
            params["dateCreatedFrom"] = replication_key_value

        # Next page token is an offset
        if next_page_token:
            params["offset"] = next_page_token

        return params


class ProductsStream(alephcrmStream):
    name = "products"
    path = "/v2/products"
    primary_keys: t.ClassVar[list[str]] = ["accountId", "Id"]
    replication_key = None

    parent_stream_type = AccountsStream
    ignore_parent_replication_keys = True

    schema = schema__ProductsStream


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
    

    def post_process(self, row: dict, context: dict | None = None) -> dict | None:
        # Primary key unnested
        row["Id"] = row.get("Identification", {}).get('Id')

        return row
