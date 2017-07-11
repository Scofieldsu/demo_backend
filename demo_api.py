# encoding: utf-8

from flaskapi.api import api_add,api_class
from apidata import api_data


@api_add
def login(name, pwd):
    """
    :description 登录接口
    :param name: str
    :param pwd: str
    :return: 登录信息
    """
    result = {"msg": "login success", "code": 200}
    return result


@api_add
def logout(name):
    """
    :description 退出接口
    :param name: str
    :return: 退出信息success or error
    """
    return "logout success"


@api_class
class UserApi(object):

    @api_data
    def login_test(self,name, pwd):
        """
        :description test登录接口
        :param name: str
        :param pwd: str
        :return: test登录信息
        """
        result = {"msg": "login success", "code": 200}
        return result

    @api_data
    def logout_test(self,name):
        """
        :description test退出接口
        :param name: str
        :return: test退出信息success or error
        """
        return "logout success"