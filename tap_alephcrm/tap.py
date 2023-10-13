"""alephcrm tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_alephcrm import streams


class Tapalephcrm(Tap):
    """alephcrm tap class."""

    name = "tap-alephcrm"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_url",
            th.StringType,
            default="https://api.alephcrm.com",
            description="The url for the API service",
        ),
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        )
    ).to_dict()

    def discover_streams(self) -> list[streams.alephcrmStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.AccountsStream(self),
            streams.MarketplacesStream(self),
            streams.StoresStream(self),
            streams.OrdersStream(self),
            streams.ProductsStream(self)
        ]


if __name__ == "__main__":
    Tapalephcrm.cli()
