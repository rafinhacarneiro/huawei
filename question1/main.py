from SiteClient import Orders
from SpreadsheetBuilder.Builder import Builder

site = Orders("automationtest@automationtest.com", "%#zJR&wCDEVs5DJa")
spreadsheet = Builder()

orders = site.get_orders_list()
filepath = spreadsheet.save_as_xlsx(orders)

print(filepath)
