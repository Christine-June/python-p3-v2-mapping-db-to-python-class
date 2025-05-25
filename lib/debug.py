# lib/testing/debug.py
#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department

import ipdb

def reset_database():
    Department.drop_table()
    Department.create_table()

    # Create test departments
    Department.create("Payroll", "Building A, 5th Floor")
    Department.create("Human Resources", "Building C, East Wing")
    Department.create("Accounting", "Building B, 1st Floor")

def test_methods():
    # Test get_all()
    print("All departments:")
    for dept in Department.get_all():
        print(dept)
    
    # Test find_by_id()
    print("\nFind by ID (2):")
    print(Department.find_by_id(2))
    
    # Test find_by_name()
    print("\nFind by name ('Accounting'):")
    print(Department.find_by_name("Accounting"))
    
    # Test delete()
    hr = Department.find_by_name("Human Resources")
    print("\nBefore delete:", Department.get_all())
    hr.delete()
    print("After delete:", Department.get_all())

if __name__ == '__main__':
    reset_database()
    test_methods()
    ipdb.set_trace()