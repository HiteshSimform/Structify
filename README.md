# Structify


1. Net Salary


net_salary = basic_salary + allowances - deductions

You already validate this in your serializer.

1. Leave-Based Deduction
When unpaid leaves exist, deduction should be calculated like this:


per_day_salary = basic_salary / total_working_days
unpaid_leaves = total_leaves_taken - paid_leaves
leave_deduction = unpaid_leaves × per_day_salary


net_salary = basic_salary + allowances - deductions - leave_deduction


1. Attendance-Based Working Days
   
If you are tracking working days via attendance or calendar:
working_days = Total weekdays in pay period - weekends - holidays
actual_present_days = working_days - leave_days - absents
Optional prorated salary if joined mid-month or has absents:
prorated_salary = (actual_present_days / working_days) × (basic_salary + allowances)

1. Department Expense
For reporting purposes:

department_total_salary = sum of net_salary for all employees in department
department_avg_salary = department_total_salary / number_of_employees

DepartmentSalarySummarySerializer.

1. Monthly Deduction % (Optional)
Useful for dashboard or analytics:
deduction_percent = (total_deductions / (basic_salary + allowances)) × 100


6. Tax or PF Deductions (Future Feature)
You can extend the deduction calculation:

deductions = leave_deductions + tax + pf + loans