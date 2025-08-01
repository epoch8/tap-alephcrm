from singer_sdk import typing as th  # JSON Schema typing helpers


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
                        th.Property("ExternalId", th.StringType),
                        th.Property("Title", th.StringType),
                        th.Property(
                            "ListingType",
                            th.ObjectType(
                                th.Property("Key", th.IntegerType),
                                th.Property("Value", th.StringType),
                                th.Property("Description", th.StringType)
                            )
                        ),
                        th.Property("PermanentLink", th.StringType)
                    )
                ),
                th.Property("Quantity", th.IntegerType),
                th.Property(
                    "QuantitiesDetails",
                    th.ObjectType(
                        th.Property(
                            "Requested",
                            th.ObjectType(
                                th.Property("Key", th.StringType),
                                th.Property("Value", th.NumberType)
                            )
                        ),
                        th.Property(
                            "Picked",
                            th.ObjectType(
                                th.Property("Key", th.StringType),
                                th.Property("Value", th.NumberType)
                            )
                        ),
                        th.Property(
                            "StockMovements",
                            th.ArrayType(
                                th.ObjectType(
                                    th.Property(
                                        "Account",
                                        th.ObjectType(
                                            th.Property("Id", th.IntegerType),
                                            th.Property("DocType", th.StringType),
                                            th.Property("DocNumber", th.StringType),
                                            th.Property("PickupCode", th.StringType),
                                            th.Property("OwnCode", th.StringType),
                                            th.Property("Name", th.StringType),
                                            th.Property("BusinessName", th.StringType)
                                        )
                                    ),
                                    th.Property("PrevStock", th.IntegerType),
                                    th.Property("PostStock", th.IntegerType),
                                    th.Property("Quantity", th.IntegerType),
                                    th.Property("MinPublicationQuantity", th.IntegerType),
                                    th.Property("MaxPublicationQuantity", th.IntegerType),
                                    th.Property("DateCreated", th.DateTimeType)
                                )
                            )
                        )
                    )
                ),
                th.Property("UnitPrice", th.NumberType),
                th.Property("FullUnitPrice", th.NumberType),
                th.Property("UnitPriceCost", th.NumberType),
                th.Property("CalculatedComponentUnitPrice", th.NumberType),
                th.Property("CalculatedComponentFullUnitPrice", th.NumberType),
                th.Property("SaleFee", th.NumberType),
                th.Property("Notes", th.StringType),
                th.Property(
                    "Status",
                    th.ObjectType(
                        th.Property("Key", th.IntegerType),
                        th.Property("Value", th.StringType)
                    )
                ),
                th.Property(
                    "StatusType",
                    th.ObjectType(
                        th.Property("Key", th.IntegerType),
                        th.Property("Value", th.StringType)
                    )
                ),
                th.Property("IsCancelled", th.BooleanType)
            )
        )
    ),
    th.Property(
        "Payments",
        th.ArrayType(
            th.ObjectType(
                th.Property("ExternalPaymentId", th.StringType),
                th.Property("Amount", th.NumberType),
                th.Property("AmountNoDiscount", th.NumberType),
                th.Property("ShippingAmount", th.NumberType),
                th.Property("ShippingAmountNoDiscount", th.NumberType),
                th.Property("TransactionAmount", th.NumberType),
                th.Property("Total", th.NumberType),
                th.Property("SubTotal", th.NumberType),
                th.Property("Installments", th.IntegerType),
                th.Property("InstallmentAmount", th.NumberType),
                th.Property("Notes", th.StringType),
                th.Property("CurrencySymbol", th.StringType),
                th.Property(
                    "Method",
                    th.ObjectType(
                        th.Property("Key", th.IntegerType),
                        th.Property("Value", th.StringType)
                    )
                ),
                th.Property(
                    "Status",
                    th.ObjectType(
                        th.Property("Key", th.IntegerType),
                        th.Property("Value", th.StringType)
                    )
                ),
                th.Property(
                    "Condition",
                    th.ObjectType(
                        th.Property("Key", th.IntegerType),
                        th.Property("Value", th.StringType)
                    )
                ),
                th.Property(
                    "Discounts",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("Amount", th.NumberType),
                            th.Property("Value", th.NumberType),
                            th.Property("Type", th.StringType),
                            th.Property("Priority", th.StringType),
                            th.Property("Notes", th.StringType),
                            th.Property("Code", th.StringType)
                        )
                    )
                ),
                th.Property(
                    "Taxes",
                    th.ObjectType(
                        th.Property("Amount", th.NumberType),
                        th.Property("CurrencySymbol", th.StringType)
                    )
                ),
                th.Property("AuthorizationCode", th.StringType),
                th.Property("DateCreated", th.DateTimeType),
                th.Property("DateApproved", th.DateTimeType),
                th.Property("LastUpdate", th.DateTimeType)
            )
        )
    ),
    th.Property(
        "Adjustments",
        th.ArrayType(
            th.ObjectType(
                th.Property(
                    "Type",
                    th.ObjectType(
                        th.Property("Key", th.IntegerType),
                        th.Property("Value", th.StringType)
                    )
                ),
                th.Property("Code", th.StringType),
                th.Property("Description", th.StringType),
                th.Property(
                    "Item",
                    th.ObjectType(
                        th.Property("Id", th.IntegerType),
                        th.Property("Brand", th.StringType),
                        th.Property("Sku", th.StringType),
                        th.Property("SellerSku", th.StringType)
                    )
                ),
                th.Property(
                    "Value",
                    th.ObjectType(
                        th.Property(
                            "Type",
                            th.ObjectType(
                                th.Property("Key", th.IntegerType),
                                th.Property("Value", th.StringType)
                            )
                        ),
                        th.Property("Value", th.IntegerType)
                    )
                )
            )
        )
    ),
    th.Property(
        "Shipping",
        th.ObjectType(
            th.Property("ExternalShippingId", th.IntegerType),
            th.Property("Cost", th.NumberType),
            th.Property("ReceiverCost", th.NumberType),
            th.Property("SenderCost", th.NumberType),
            th.Property(
                "Method",
                th.ObjectType(
                    th.Property("Key", th.IntegerType),
                    th.Property("Value", th.StringType)
                )
            ),
            th.Property(
                "Status",
                th.ObjectType(
                    th.Property("Key", th.IntegerType),
                    th.Property("Value", th.StringType)
                )
            ),
            th.Property(
                "LogisticType",
                th.ObjectType(
                    th.Property("Key", th.IntegerType),
                    th.Property("Value", th.StringType)
                )
            ),
            th.Property(
                "CourierInfo",
                th.ObjectType(
                    th.Property("BusinessName", th.StringType),
                    th.Property("DocType", th.StringType),
                    th.Property("DocNumber", th.StringType),
                    th.Property("LegalNumber", th.StringType),
                    th.Property("OwnCode", th.StringType),
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
                            th.Property("AlternativePhone", th.StringType),
                        )
                    )
                )
            ),
            th.Property(
                "ShippingLabels",
                th.ObjectType(
                    th.Property("SubStatus", th.StringType),
                    th.Property("ShippingLabelUrlPdf", th.StringType),
                    th.Property("ShippingLabelUrlZip", th.StringType)
                )
            ),
            th.Property(
                "Pickup",
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
                "ReceiverAddress",
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
            th.Property(
                "Receiver",
                th.ObjectType(
                    th.Property("Name", th.StringType),
                    th.Property("Phone", th.StringType)
                )
            ),
            th.Property("EstimatedDeliveryDate", th.DateTimeType),
            th.Property("DateCreated", th.DateTimeType),
            th.Property("LastUpdated", th.DateTimeType),
            th.Property(
                "PackageInfo",
                th.ObjectType(
                    th.Property("Quantity", th.IntegerType),
                    th.Property("UnitType", th.IntegerType),
                    th.Property(
                        "Dimensions",
                        th.ObjectType(
                            th.Property("Height", th.IntegerType),
                            th.Property("Width", th.IntegerType),
                            th.Property("Depth", th.IntegerType),
                            th.Property("MeasureType", th.IntegerType)
                        )
                    ),
                    th.Property(
                        "Dimensions",
                        th.ObjectType(
                            th.Property("Gross", th.IntegerType),
                            th.Property("Liquid", th.IntegerType),
                            th.Property("MeasureType", th.IntegerType)
                        )
                    )
                )
            )
        )
    ),
    th.Property(
        "Buyer",
        th.ObjectType(
            th.Property("Code", th.IntegerType),
            th.Property("Owncode", th.StringType),
            th.Property("Name", th.StringType),
            th.Property("Phone", th.StringType),
            th.Property("Email", th.StringType),
            th.Property("DocType", th.StringType),
            th.Property("DocNumber", th.StringType),
            th.Property("Nickname", th.StringType),
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
                    th.Property("AlternativePhone", th.StringType),
                )
            ),
            th.Property(
                "BillingInfo",
                th.ObjectType(
                    th.Property("DocType", th.StringType),
                    th.Property("DocNumber", th.StringType),
                    th.Property("TaxPayerType", th.StringType),
                    th.Property("BusinessName", th.StringType),
                    th.Property(
                        "StateRegistration",
                        th.ObjectType(
                            th.Property("DocType", th.StringType),
                            th.Property("DocNumber", th.StringType)
                        )
                    ),
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
                            th.Property("AlternativePhone", th.StringType),
                        )
                    )
                )
            )
        )
    ),
    th.Property(
        "Billing",
        th.ObjectType(
            th.Property("SaleFee", th.NumberType),
            th.Property(
                "Invoice",
                th.ObjectType(
                    th.Property("DanfePdfUrl", th.StringType),
                    th.Property("XmlUrl", th.StringType)
                )
            )
        )
    ),
    th.Property(
        "ActiveClaims",
        th.ArrayType(
            th.ObjectType(
                th.Property("ExternalClaimId", th.IntegerType),
                th.Property("DateCreated", th.DateTimeType)
            )
        )
    ),
    th.Property(
        "Documents",
        th.ArrayType(
            th.ObjectType(
                th.Property("Type", th.IntegerType),
                th.Property("Name", th.StringType),
                th.Property("Extension", th.StringType),
                th.Property("Fullfilename", th.StringType),
                th.Property("Size", th.IntegerType),
                th.Property("DocumentDate", th.DateTimeType),
                th.Property("DateCreated", th.DateTimeType)
            )
        )
    ),
    th.Property("ExternalJson", th.StringType),
    th.Property("Integrated", th.BooleanType),
    th.Property("IntegratedOrderId", th.StringType),
    th.Property("ErpStatus", th.StringType),
    th.Property("Notes", th.StringType),
    th.Property(
        "Status",
        th.ObjectType(
            th.Property("Key", th.IntegerType),
            th.Property("Value", th.StringType)
        )
    ),
    th.Property(
        "StatusType",
        th.ObjectType(
            th.Property("Key", th.IntegerType),
            th.Property("Value", th.StringType)
        )
    ),
    th.Property(
        "MarketPlace",
        th.ObjectType(
            th.Property("Key", th.IntegerType),
            th.Property("Value", th.StringType),
            th.Property("Channel", th.StringType)
        )
    ),
    th.Property("DateCreated", th.DateTimeType),
    th.Property("LastUpdated", th.DateTimeType),
    th.Property("DateClosed", th.DateTimeType),
    th.Property("IsCancelled", th.BooleanType),
    th.Property(
        "Invoice",
        th.ObjectType(
            th.Property("DanfePdfUrl", th.StringType),
            th.Property("XmlUrl", th.StringType)
        )
    )
).to_dict()
