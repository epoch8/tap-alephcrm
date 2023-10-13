from singer_sdk import typing as th  # JSON Schema typing helpers


schema = th.PropertiesList(
    th.Property("Id", th.IntegerType),
    th.Property("accountId", th.IntegerType),
    th.Property(
        "Identification",
        th.ObjectType(
            th.Property("Id", th.IntegerType),
            th.Property("SKU", th.StringType),
            th.Property("OwnCode", th.StringType),
            th.Property(
                "Brand",
                th.ObjectType(
                    th.Property("Id", th.IntegerType),
                    th.Property("Name", th.StringType)
                )
            ),
            th.Property("Name", th.StringType),
            th.Property(
                "CatalogStatus",
                th.ObjectType(
                    th.Property("Key", th.IntegerType),
                    th.Property("Value", th.StringType)
                )
            ),
            th.Property(
                "ProductType",
                th.ObjectType(
                    th.Property("Id", th.IntegerType),
                    th.Property("Name", th.StringType)
                )
            )
        )
    ),
    th.Property(
        "Stock",
        th.ObjectType(
            th.Property("Quantity", th.IntegerType),
            th.Property("B2BQuantity", th.IntegerType),
            th.Property("Movement", th.IntegerType),
            th.Property("PublishQuantity", th.IntegerType),
            th.Property("MinPublicationQuantity", th.IntegerType),
            th.Property("MaxPublicationQuantity", th.IntegerType),
            th.Property(
                "MeasurableQuantity",
                th.ObjectType(
                    th.Property("Quantity", th.IntegerType),
                    th.Property("Unit", th.StringType)
                )
            ),
            th.Property(
                "Alert",
                th.ObjectType(
                    th.Property("RedQty", th.IntegerType),
                    th.Property("YellowQty", th.IntegerType)
                )
            )
        )
    ),
    th.Property(
        "Price",
        th.ArrayType(
            th.ObjectType(
                th.Property("Price", th.NumberType),
                th.Property("PriceWithTaxes", th.NumberType),
                th.Property("SuggestedRetailPrice", th.NumberType),
                th.Property("SuggestedRetailPriceAutoCalculated", th.BooleanType),
                th.Property("PriceAutoCalculated", th.BooleanType),
                th.Property("FinalPriceWithShippingCost", th.NumberType),
                th.Property("B2BDiscountRate", th.NumberType),
                th.Property("SalesMargin", th.NumberType),
                th.Property(
                    "PriceList",
                    th.ObjectType(
                        th.Property("Id", th.IntegerType),
                        th.Property("Name", th.StringType),
                        th.Property("DiscountRate", th.NumberType),
                    )
                ),
                th.Property("Cost", th.NumberType)
            )
        )
    ),
    th.Property(
        "Kits",
        th.ArrayType(
            th.ObjectType(
                th.Property("Id", th.IntegerType),
                th.Property("SKU", th.StringType),
                th.Property("OwnCode", th.StringType),
                th.Property(
                    "Brand",
                    th.ObjectType(
                        th.Property("Id", th.IntegerType),
                        th.Property("Name", th.StringType)
                    )
                ),
                th.Property("Name", th.StringType),
                th.Property(
                    "CatalogStatus",
                    th.ObjectType(
                        th.Property("Key", th.IntegerType),
                        th.Property("Value", th.StringType)
                    )
                ),
                th.Property(
                    "ProductType",
                    th.ObjectType(
                        th.Property("Id", th.IntegerType),
                        th.Property("Name", th.StringType)
                    )
                )
            )
        )
    ),
    th.Property(
        "KitComponents",
        th.ArrayType(
            th.ObjectType(
                th.Property(
                    "Identification",
                    th.ObjectType(
                        th.Property("Id", th.IntegerType),
                        th.Property("SKU", th.StringType),
                        th.Property("OwnCode", th.StringType),
                        th.Property(
                            "Brand",
                            th.ObjectType(
                                th.Property("Id", th.IntegerType),
                                th.Property("Name", th.StringType)
                            )
                        ),
                        th.Property("Name", th.StringType),
                        th.Property(
                            "CatalogStatus",
                            th.ObjectType(
                                th.Property("Key", th.IntegerType),
                                th.Property("Value", th.StringType)
                            )
                        ),
                        th.Property(
                            "ProductType",
                            th.ObjectType(
                                th.Property("Id", th.IntegerType),
                                th.Property("Name", th.StringType)
                            )
                        )
                    )
                ),
                th.Property(
                    "Price",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("Price", th.NumberType),
                            th.Property("PriceWithTaxes", th.NumberType),
                            th.Property("SuggestedRetailPrice", th.NumberType),
                            th.Property("SuggestedRetailPriceAutoCalculated", th.BooleanType),
                            th.Property("PriceAutoCalculated", th.BooleanType),
                            th.Property("FinalPriceWithShippingCost", th.NumberType),
                            th.Property("B2BDiscountRate", th.NumberType),
                            th.Property("SalesMargin", th.NumberType),
                            th.Property(
                                "PriceList",
                                th.ObjectType(
                                    th.Property("Id", th.IntegerType),
                                    th.Property("Name", th.StringType),
                                    th.Property("DiscountRate", th.NumberType),
                                )
                            ),
                            th.Property("Cost", th.NumberType)
                        )
                    )
                ),
                th.Property(
                    "Stock",
                    th.ObjectType(
                        th.Property("Quantity", th.IntegerType),
                        th.Property("B2BQuantity", th.IntegerType),
                        th.Property("Movement", th.IntegerType),
                        th.Property("PublishQuantity", th.IntegerType),
                        th.Property("MinPublicationQuantity", th.IntegerType),
                        th.Property("MaxPublicationQuantity", th.IntegerType),
                        th.Property(
                            "MeasurableQuantity",
                            th.ObjectType(
                                th.Property("Quantity", th.IntegerType),
                                th.Property("Unit", th.StringType)
                            )
                        ),
                        th.Property(
                            "Alert",
                            th.ObjectType(
                                th.Property("RedQty", th.IntegerType),
                                th.Property("YellowQty", th.IntegerType)
                            )
                        )
                    )
                ),
                th.Property("Quantity", th.IntegerType),
                th.Property("Principal", th.BooleanType)
            )
        )
    ),
    th.Property(
        "Publications",
        th.ArrayType(
            th.ObjectType(
                th.Property(
                    "MarketPlace",
                    th.ObjectType(
                        th.Property("Key", th.IntegerType),
                        th.Property("Value", th.StringType)
                    )
                ),
                th.Property(
                    "Details",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property(
                                "Status",
                                th.ObjectType(
                                    th.Property("Id", th.IntegerType),
                                    th.Property("Name", th.StringType)
                                )
                            ),
                            th.Property("Quantity", th.IntegerType),
                            th.Property("ExternalIds", th.StringType)
                        )
                    )
                )
            )
        )
    )
).to_dict()
