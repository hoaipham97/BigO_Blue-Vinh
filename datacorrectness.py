from airflow import DAG
from momo.dpairflow.etl.etl_dag_config import EtlDagConfig
from momo.dpairflow.generate_dag.dp_dag_builder import DpDagBuilder

from momo.dpairflow.operators.dp_metric_formula_operator import DpMetricFormulaOperator

DAG_NAME = 'data_correctness_metric_row_count_python_interface'

dag = DAG(
    dag_id=DAG_NAME,
    default_args=EtlDagConfig.get_default_args(),
    schedule_interval=None,
    catchup=False,
    max_active_runs=1,
    concurrency=20,
    user_defined_macros=DpDagBuilder().get_macros(),
    description=""
)


def add_data_correctness_formula(
    target_dataset,
    target_table_name,
    metric_name,
    formula
):
  DpMetricFormulaOperator(project_id='project-5400504384186300846',
                          dataset='DATA_CORRECTNESS_METRIC_CALCULATOR'
                          ).add_metric(dag=dag,
                                       target_project_id='project-5400504384186300846',
                                       target_dataset=target_dataset,
                                       target_table_name=target_table_name,
                                       metric_name=metric_name,
                                       formula=formula
                                       )

# SQL of Fomular need exactly like below template,
#   - First column
#       should always be `PARSE_DATE("%y%m%d", _TABLE_SUFFIX) AS SHARDING`
#
#   - Second column
#       is name your metric have to `CAST to STRING` and be named as `KEY`
#
#   - Third column
#       have to `CAST to NUMERIC` and named as `VALUE`
#
#
#   Example:
#
#     SELECT
#       PARSE_DATE("%y%m%d", _TABLE_SUFFIX) AS SHARDING,
#       CAST("ROW_COUNT" AS STRING) AS KEY,
#       CAST(COUNT(1) AS NUMERIC) AS VALUE
#     FROM
#       `project-5400504384186300846.UMARKETADM.TRANS_20*`
#     GROUP BY
#       _TABLE_SUFFIX

# YOUR METRIC HERE  |  |  |  |  |
#                   V  V  V  V  V

def add_ROW_COUNT_metric_for_table(target_dataset, target_table_name):
  add_data_correctness_formula(
      target_dataset=target_dataset,
      target_table_name=target_table_name,
      metric_name='ROW_COUNT',
      formula=f"""
SELECT
    PARSE_DATE("%y%m%d", _TABLE_SUFFIX) AS SHARDING,
    CAST("ROW_COUNT" AS STRING) AS KEY,
    CAST(COUNT(1) AS NUMERIC) AS VALUE
FROM
    `project-5400504384186300846.{target_dataset}.{target_table_name}_20*`
GROUP BY
    _TABLE_SUFFIX
    """
  )

add_ROW_COUNT_metric_for_table("BITEAM_EXP", "PAID_USER_TRANS")
add_ROW_COUNT_metric_for_table("BITEAM_EXP", "MONTHLY_ACTIVEUSER_EVENT")
add_ROW_COUNT_metric_for_table("BITEAM_EXP", "CONVERTED_USER_RETENTION")
add_ROW_COUNT_metric_for_table("BITEAM_EXP", "USER_INFO")

add_ROW_COUNT_metric_for_table("BITEAM_EXP", "DAILY_ACTIVEUSER_TRANS")

add_ROW_COUNT_metric_for_table("ASTERISKCDRDB", "CDR")
add_ROW_COUNT_metric_for_table("CALL_CENTER", "AGENT")
add_ROW_COUNT_metric_for_table("CALL_CENTER", "ASTERISKCDRDB")
add_ROW_COUNT_metric_for_table("CALL_CENTER", "AUDIT")
add_ROW_COUNT_metric_for_table("CALL_CENTER", "CALL_ENTRY")
add_ROW_COUNT_metric_for_table("CASHBACK", "CASHBACK_BADGES_CATEGORY")
add_ROW_COUNT_metric_for_table("CASHBACK", "CASHBACK_BADGES")
add_ROW_COUNT_metric_for_table("CASHBACK", "CASHBACK_FEED_HISTORY")
add_ROW_COUNT_metric_for_table("CASHBACK", "CASHBACK_MISSION_HISTORY")
add_ROW_COUNT_metric_for_table("CASHBACK", "CASHBACK_MISSION")
add_ROW_COUNT_metric_for_table("CONNECTOR_ADM", "PROXY_TRANS_ACCOUNT_NEW")
add_ROW_COUNT_metric_for_table("CONNECTOR_ADM", "PROXY_TRANS_CHECK_INFO_NEW")
add_ROW_COUNT_metric_for_table("CONNECTOR_ADM", "PROXY_TRANS_DATA_NEW")
add_ROW_COUNT_metric_for_table("CONNECTOR", "BANK_ACCOUNT")
add_ROW_COUNT_metric_for_table("CONNECTOR", "BANK_CARD_INFO")
add_ROW_COUNT_metric_for_table("CONNECTOR", "BANK_CARD_TRANSACTION")
add_ROW_COUNT_metric_for_table("CONNECTOR", "BANK_CUSTOMER")
add_ROW_COUNT_metric_for_table("CONNECTOR", "BANK_TRANSACTION_MOMO")
add_ROW_COUNT_metric_for_table("CONNECTOR", "BANK_TRANSACTION")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GOOGLE_AUTHENTICATION")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GOOGLE_REMITTANCE_DETAIL")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GOOGLE_REMITTANCE")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GOOGLE_TRANS_ASSOCIATE")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GOOGLE_TRANS")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GW_C2C_TRANS")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GW_CASH_TRANSACTION")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GW_IDENTIFY_IMAGE")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GW_IDENTIFY_TRANS")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GW_LOAN_INFO_HISTORY")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GW_LOAN_INFO")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GW_PARTNER_TRANSACTION")
add_ROW_COUNT_metric_for_table("CONNECTOR", "GW_TRANS_INFO")
add_ROW_COUNT_metric_for_table("CONNECTOR", "INTEGRATE_LINK_TRANSACTION")
add_ROW_COUNT_metric_for_table("CONNECTOR", "INTEGRATE_LINK")
add_ROW_COUNT_metric_for_table("CONNECTOR", "KYB_INFO")
add_ROW_COUNT_metric_for_table("CONNECTOR", "M_SERVICE_TRANS_DATA")
add_ROW_COUNT_metric_for_table("CONNECTOR", "M_SERVICE_TRANS")
add_ROW_COUNT_metric_for_table("CONNECTOR", "MBI_TRACKING")
add_ROW_COUNT_metric_for_table("CONNECTOR", "MIS_MLSTORE_EXPORT_DETAIL")
add_ROW_COUNT_metric_for_table("CONNECTOR", "MIS_MLSTORE_EXPORT")
add_ROW_COUNT_metric_for_table("CONNECTOR", "MIS_MLSTORE_IMPORT")
add_ROW_COUNT_metric_for_table("CONNECTOR", "OCR_TRANSACTION")
add_ROW_COUNT_metric_for_table("CONNECTOR", "PAYMENT_TRANSACTION")
add_ROW_COUNT_metric_for_table("CONNECTOR", "PROFILE")
add_ROW_COUNT_metric_for_table("CONNECTOR", "PROXY_TRANS_ACCOUNT")
add_ROW_COUNT_metric_for_table("CONNECTOR", "PROXY_TRANS_BILL_INFO_NEW")
add_ROW_COUNT_metric_for_table("CONNECTOR", "PROXY_TRANS_BILL_INFO")
add_ROW_COUNT_metric_for_table("CONNECTOR", "PROXY_TRANS_CHECK_INFO_NEW")
add_ROW_COUNT_metric_for_table("CONNECTOR", "PROXY_TRANS_DATA")
add_ROW_COUNT_metric_for_table("CONNECTOR", "PROXY_TRANS_NEW")
add_ROW_COUNT_metric_for_table("CONNECTOR", "PROXY_TRANS")
add_ROW_COUNT_metric_for_table("CONNECTOR", "SACOMBANK_VISADIRECT")
add_ROW_COUNT_metric_for_table("CONNECTOR", "SCB_DATA")
add_ROW_COUNT_metric_for_table("CONNECTOR", "SHOPPING_TRANS_DATA")
add_ROW_COUNT_metric_for_table("CONNECTOR", "SHOPPING_TRANSACTION")
add_ROW_COUNT_metric_for_table("CONNECTOR", "VISA_TRANSACTION")
add_ROW_COUNT_metric_for_table("CONNECTOR", "VISACARD_INFO")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_DEAL_MARKET_CATEGORY")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_DEAL_MARKET_GIFT")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_DEAL_MARKET_HISTORY")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_DEAL_MARKET_MERCHANT_STORE")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_DEAL_MARKET")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_GET_DEAL_MARKET_CATEGORY")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_GET_DEAL_MARKET")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_GROUP_AGENT_WARNING_CONFIG")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_GROUP_AGENT_WARNING_DETAIL")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_INBOX_EMAIL_CSKH")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_LOG_DATABASE")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_MASTER_DATA_VER2")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_MASTER_DATA")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_MASTER_GROUP")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_MOMO_WALLET_HIGH_RISK")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_PER_TEAM")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_REQUEST_DEAL_CASHBACK_AGENT")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_REQUEST_DEAL_CASHBACK_APPROVAL")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_REQUEST_DEAL_CASHBACK_HISTORY")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_REQUEST_DEAL_CASHBACK_PROCESS")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_REQUEST_DEAL_CASHBACK_RULE_VALUE")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_REQUEST_DEAL_CASHBACK_SERVICE")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_REQUEST_DEAL_CASHBACK")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_REQUEST_LOCK_ACCOUNT")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_REQUEST_RESET_PASSWORD")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_SURVEY_OFFLINE_PAYMENT_DETAIL")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_SURVEY_OFFLINE_PAYMENT")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_TEAM_PROCESS_TICKET")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_TICKET_COMMENT")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_TICKET_RATING")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_TICKET_RISK")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_TICKET_TRANSACTION_RISK")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_TICKET")
add_ROW_COUNT_metric_for_table("CRM_ADMIN", "CRM_WARNING_SYSTEM_ERROR")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MIS_ACCOUNT_IDENTITY_APPROVAL")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MIS_ACCOUNT_IDENTITY")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MIS_CITY")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MIS_DISTRICT")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MIS_PROFILE_BASE")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MIS_PROFILE_PROPERTY")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MIS_PROFILE_RECORD")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MIS_PROFILE")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MIS_SUSPENND_AMOUNT_AGENT")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MIS_USER")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MIS_WARD")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MS_ALL_TRANS_PAID")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "MS_ALL_TRANS_UNPAID")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "posm_attachment")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "POSM_BRAND")
add_ROW_COUNT_metric_for_table("MIS_ADMIN", "POSM_SHOP")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "DELIVERY_MESSAGE")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "OPS_INCIDENTS")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "PARTNER_RESULT_TOTAL")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "SMS_REPORT")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_ACCIDENT_TICKETS")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_AGENT_SERVICE_MONITOR_PROD")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_ASSET_ALERT_TICKET_MAP")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_ASSET_CATEGORIES")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_ASSET_ITEMS")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_ASSET_MAP")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_ASSET_SUBCATEGORIES")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_ASSET_SUPPORT_REQUEST_MAP")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_INCIDENTS")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_REQUEST_SUPPORT")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_SQI_AGENT_SERVICE_PROD")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_SQI_AGENT_TRANS_30_DAYS")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_SQI_MAPCODE")
add_ROW_COUNT_metric_for_table("OPERATOR_PROD", "VH_TRANS_RAW_DAILY")
add_ROW_COUNT_metric_for_table("PROMOTION", "CASHBACK_USER_INFO")
add_ROW_COUNT_metric_for_table("PROMOTION", "CASHBACK_USER_WALK_BY_DATE")
add_ROW_COUNT_metric_for_table("PROMOTION", "promotion_access_trade_pub")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_ACTIONS")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_AUTO_SEND_NOTIFICATION_HISTORY")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_AUTO_SEND_XBANNER_HISTORY")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_BANK_INFO_USER")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_CHALLENGE_MISSION")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_CHALLENGE_RECEIVER")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_CHALLENGE_WHITELIST_BY_DATE")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_CHALLENGE")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_CODE_GENERATE_HISTORY")
add_ROW_COUNT_metric_for_table("PROMOTION", "promotion_code_generate")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_CODE_LIST")
add_ROW_COUNT_metric_for_table("PROMOTION", "promotion_code")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_DEAL_PACKAGE_DETAIL")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_GIFT_USER_COUNTER")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_MESSAGE_QUEUE_TRACKING")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_NOTI_REMIND_CHALLENGE")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_SERVICE_CONFIG_BY_PROMOTION")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_SERVICE_CONFIG")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_SERVICE_DETAILS")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_SERVICE_MAPPING_GIFT")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_SERVICE_USER_CHOOSE")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_SERVICES")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_STATUS_USER_CHALLENGE_MISSION")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_STATUS_USER_CHALLENGE")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_USER_GROUP_UPDATE")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_USER_LIST_PACKAGE")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_USER_LIST")
add_ROW_COUNT_metric_for_table("PROMOTION", "promotion_user_ranking_result")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_USER_REFERRAL_CASHBACK_TOTAL")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_USER_REGISTER_REFERRAL_PARTNER")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_USER_TOTAL_DISCOUNT")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTION_VOUCHER")
add_ROW_COUNT_metric_for_table("PROMOTION", "PROMOTIONS")
add_ROW_COUNT_metric_for_table("PROMOTION", "USER_REGISTER_BANK_INFO")
add_ROW_COUNT_metric_for_table("PROMOTION", "USER_REGISTER_REFERRAL_PARTNER_HISTORY")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_CATEGORY")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_CUSTOMER_ADDRESS")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_CUSTOMER")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_MESSAGE_TEMPLATE")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_ORDER_DETAIL")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_ORDER_HISTORY")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_ORDER")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_PRODUCT_AMOUNT")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_PRODUCT_DETAIL")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_PRODUCT_MERCHANT_MAP")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_PRODUCT_SKU")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_PRODUCT")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "ECOM_WARNING")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "M4B_ACTIVITY_LOG")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "M4B_CONTACT_POINT")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "M4B_D_SERVICE")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "M4B_DEFINITION")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "M4B_MERCHANT_APP_HISTORY")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "M4B_MERCHANT_CATEGORY")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "M4B_MERCHANT_CONTRACT")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "M4B_MERCHANT_FEE_INFO")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "M4B_MERCHANT_RATING")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "M4B_PLACE")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "MOMO_BUSINESS_ROLE")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "MOMO_BUSSINESS_M_BANK_INFO")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "MOMO_BUSSINESS_MERCHANT_INFO")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "OAUTH2_OAUTH_ACCESS_TOKENS")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "OAUTH2_OAUTH_AUTH_CODES")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "OAUTH2_SSO_CLIENT")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "PAYMENT_PARTNER")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "PAYMENT_TRANSACTION")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "PRO_GET_APPROVED_HISTORY")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_CUSTOMER")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_ERROR_CODE")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_HISTORY_ORDER")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_ORDER_DETAIL")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_ORDER")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_PARTNER_FEE")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_PAYMENT_ACCOUNT")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_PAYMENT_PARTNER")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_PAYMENT_TRANSACTION_DETAIL")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_PAYMENT_TRANSACTION")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_PRODUCT")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_REFUND_TRANSACTION")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_USER_ACCESS_TOKEN_HISTORY")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "SDK_USER_ACCESS_TOKEN")
add_ROW_COUNT_metric_for_table("SDK_ADMIN", "V_M4B_MERCHANT_INFO_FULL")
add_ROW_COUNT_metric_for_table("SERIOUS", "TICKET_INFO")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "AI_KYC_TRACKING")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "APP_FEEDBACK")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "BILL_AVAILABLE")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "BILL_CACHE")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "BILL")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "BLOCK_TRANHIS_USER")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "BLOCK_TRANS_HIS")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "CASH_BACK_HIS")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "CATEGORY_CASHBACK")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "CONFIG_HIS")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "FEEDBACK_RATING_NPS")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "FEEDBACK_TRANS")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "FILM_MOMO")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "FRAUD_BLACKLIST")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "FRAUD_OTP_HISTORY")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "FRAUD_PREVENTION_HISTORY")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "GATEWAY_TRANSACTION")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "GIFT_SNAPSHOT")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "GIFT_TYPE")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "GIFT")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "GLOBAL_CONFIG")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "LOAN_INFO")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "LOAN_REQUEST_HIS")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "LOANHIS")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "POINT_HIS")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "PROD_MAP_CODE")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "SCHEDULE_NOTI")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "SCHEDULED_PAY_HIS")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "SCHEDULED_PAY")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "SERVICE_CASHBACK")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "SERVICE")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "STORE_COMMENT")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "SYNC_TRANS_HISTORY")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "TRANHIS_SERVICE")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "TRANHIS")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "TRANREPORT")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "UPDATE_PHONE_INFO")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "USER_LOCATION")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "USER_M2NBANK")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "USER_PAYMENT_SERVICE_MAINTENANCE")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "VOUCHER_HISTORY")
add_ROW_COUNT_metric_for_table("SOAP_ADMIN", "VOUCHER_USED")
add_ROW_COUNT_metric_for_table("UMARKETADM", "ACCOUNT")
add_ROW_COUNT_metric_for_table("UMARKETADM", "AGENT_BODY")
add_ROW_COUNT_metric_for_table("UMARKETADM", "AGENT_DATA")
add_ROW_COUNT_metric_for_table("UMARKETADM", "AGENT_GROUP_MAP")
add_ROW_COUNT_metric_for_table("UMARKETADM", "AGENT_GROUP")
add_ROW_COUNT_metric_for_table("UMARKETADM", "AGENT_REF")
add_ROW_COUNT_metric_for_table("UMARKETADM", "CAP_DETAILS")
add_ROW_COUNT_metric_for_table("UMARKETADM", "CAP_SET")
add_ROW_COUNT_metric_for_table("UMARKETADM", "CAP_TRACK")
add_ROW_COUNT_metric_for_table("UMARKETADM", "MS_ALL_TRANS_PAID_V3")
add_ROW_COUNT_metric_for_table("UMARKETADM", "MS_ALL_TRANS_UNPAID_V3")
add_ROW_COUNT_metric_for_table("UMARKETADM", "TRANS_DATA")
add_ROW_COUNT_metric_for_table("UMARKETADM", "TRANS_PARTY")
add_ROW_COUNT_metric_for_table("UMARKETADM", "TRANS")
