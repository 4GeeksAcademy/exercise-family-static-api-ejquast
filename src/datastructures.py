
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if "id" not in member:
            member.update(
                id=self._generateId()
            )
        self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        for position, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(position)
                return None
        return None

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == int(id):
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

class FamilyMember:
    def __init__(self, data):
        self.first_name = data.get("first_name")
        self.last_name = data["last_name"]
        self.age = data.get("age", 0)
        self.lucky_numbers = data.get("lucky_numbers")

