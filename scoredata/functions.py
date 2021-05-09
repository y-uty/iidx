from .models import VersionList


def GetVersionNo(in_ver_name):
    ver_record = VersionList.objects.get(ver_name=in_ver_name)
    return ver_record.ver_no
