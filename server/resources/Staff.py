from flask_restful import Resource
from models import StaffList as StaffListTable


class Staff(Resource):
    path = "/staff_list"

    @classmethod
    def get(cls):
        staff = StaffListTable.get_all()

        if staff:
            return {"staff": [s.json() for s in staff]}, 200
        else:
            return {"staff": "No staff found"}, 404