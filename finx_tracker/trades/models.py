from django.db import models

# from finx_tracker.portfolios.models import Grouping


class Trade(models.Model):
    class Meta:
        managed = True
        db_table = "trades_trade"

    account_id = models.TextField(blank=True, null=True)
    acct_alias = models.FloatField(blank=True, null=True)
    model = models.FloatField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    fx_rate_to_base = models.BigIntegerField(blank=True, null=True)
    asset_category = models.TextField(blank=True, null=True)
    symbol = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    conid = models.BigIntegerField(blank=True, null=True)
    security_id = models.TextField(blank=True, null=True)
    security_id_type = models.TextField(blank=True, null=True)
    cusip = models.TextField(blank=True, null=True)
    isin = models.TextField(blank=True, null=True)
    listing_exchange = models.TextField(blank=True, null=True)
    underlying_conid = models.FloatField(blank=True, null=True)
    underlying_symbol = models.TextField(blank=True, null=True)
    underlying_security_id = models.TextField(blank=True, null=True)
    underlying_listing_exchange = models.TextField(blank=True, null=True)
    issuer = models.FloatField(blank=True, null=True)
    multiplier = models.BigIntegerField(blank=True, null=True)
    strike = models.FloatField(blank=True, null=True)
    expiry = models.TextField(blank=True, null=True)
    trade_id = models.BigIntegerField(
        blank=True, null=True, unique=True
    )  # unique so we get a 1:1 join in GroupingTrade
    put_call = models.TextField(blank=True, null=True)
    report_date = models.DateField(blank=True, null=True)
    principal_adjust_factor = models.FloatField(blank=True, null=True)
    date_time = models.TextField(blank=True, null=True)
    trade_date = models.TextField(blank=True, null=True)
    settle_date_target = models.TextField(blank=True, null=True)
    transaction_type = models.TextField(blank=True, null=True)
    exchange = models.TextField(blank=True, null=True)
    quantity = models.BigIntegerField(blank=True, null=True)
    trade_price = models.FloatField(blank=True, null=True)
    trade_money = models.FloatField(blank=True, null=True)
    proceeds = models.FloatField(blank=True, null=True)
    taxes = models.BigIntegerField(blank=True, null=True)
    ib_commission = models.FloatField(blank=True, null=True)
    ib_commission_currency = models.TextField(blank=True, null=True)
    net_cash = models.FloatField(blank=True, null=True)
    close_price = models.FloatField(blank=True, null=True)
    open_close_indicator = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    fifo_pnl_realized = models.FloatField(blank=True, null=True)
    fx_pnl = models.BigIntegerField(blank=True, null=True)
    mtm_pnl = models.FloatField(blank=True, null=True)
    orig_trade_price = models.BigIntegerField(blank=True, null=True)
    orig_trade_date = models.FloatField(blank=True, null=True)
    orig_trade_id = models.FloatField(blank=True, null=True)
    orig_order_id = models.BigIntegerField(blank=True, null=True)
    clearing_firm_id = models.FloatField(blank=True, null=True)
    transaction_id = models.BigIntegerField(blank=True, null=True)
    buy_sell = models.TextField(blank=True, null=True)
    ib_order_id = models.BigIntegerField(blank=True, null=True)
    ib_exec_id = models.TextField(blank=True, null=True)
    brokerage_order_id = models.TextField(blank=True, null=True)
    order_reference = models.FloatField(blank=True, null=True)
    volatility_order_link = models.FloatField(blank=True, null=True)
    exch_order_id = models.FloatField(blank=True, null=True)
    ext_exec_id = models.TextField(blank=True, null=True)
    order_time = models.TextField(blank=True, null=True)
    open_date_time = models.DateTimeField(blank=True, null=True)
    holding_period_date_time = models.DateTimeField(blank=True, null=True)
    when_realized = models.FloatField(blank=True, null=True)
    when_reopened = models.FloatField(blank=True, null=True)
    level_of_detail = models.TextField(blank=True, null=True)
    change_in_price = models.BigIntegerField(blank=True, null=True)
    change_in_quantity = models.BigIntegerField(blank=True, null=True)
    order_type = models.TextField(blank=True, null=True)
    trader_id = models.FloatField(blank=True, null=True)
    is_api_order = models.TextField(blank=True, null=True)
    accrued_int = models.BigIntegerField(blank=True, null=True)

    groupings = models.ManyToManyField(to="portfolios.Grouping", through="portfolios.GroupingTrade")
