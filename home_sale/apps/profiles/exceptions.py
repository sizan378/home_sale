from rest_framework.exceptions import APIException



class ProfileNotFound(APIException):
    status_code = 404
    default_detail = "The requested profile doesn't exist"


class NotYourProfile(APIException):
    status = 403
    default_detail = "You can't edit this profile"

    