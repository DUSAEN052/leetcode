"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        weight = 0
        sub = []
        for employee in employees:
            if employee.id == id:
                weight += employee.importance
                sub.extend(employee.subordinates)
        while sub:
            empid = sub.pop(0)
            for employee in employees:
                if empid == employee.id:
                    weight += employee.importance
                    sub.extend(employee.subordinates)
        return weight
        