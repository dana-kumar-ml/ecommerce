from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LeavePage(BasePage):
    def go_to_assign_leave(self):
        self.click(By.ID, "menu_leave_viewLeaveModule")
        self.click(By.ID, "menu_leave_assignLeave")
        self.find(By.ID, "assignleave_txtEmployee_empName")

    def assign_leave(self, employee_name, leave_type, from_date, to_date, comment):
        self.type(By.ID, "assignleave_txtEmployee_empName", employee_name)
        self.type(By.ID, "assignleave_txtLeaveType", leave_type)
        self.type(By.ID, "assignleave_txtFromDate", from_date)
        self.type(By.ID, "assignleave_txtToDate", to_date)
        self.type(By.ID, "assignleave_txtComment", comment)
        self.click(By.ID, "assignBtn")

    def check_insufficient_balance_popup(self):
        return self.is_visible(By.XPATH, "//div[contains(text(), 'Insufficient')]")

    def go_to_list_leave(self):
        self.click(By.ID, "menu_leave_viewLeaveModule")
        self.click(By.ID, "menu_leave_viewLeaveList")
        self.find(By.ID, "leaveList_txtEmployee_empName")

    def search_user(self, employee_name):
        self.type(By.ID, "leaveList_txtEmployee_empName", employee_name)
        self.click(By.ID, "btnSearch")

    def get_table_entry_count(self):
        rows = self.driver.find_elements(By.XPATH, "//table[@id='resultTable']/tbody/tr")
        return len(rows)
