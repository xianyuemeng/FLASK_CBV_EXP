# -*- coding: utf-8 -*-


class ErrorNo:
    SUCCESS                         = (0, '')
    INTERNAL_SERVER_ERROR           = (1, u'服务端异常')
    NO_LOGIN                        = (2, u'未登录')
    USERNAME_PASSWORD_MISMATCH      = (3, u'用户名或密码不正确')
    INVALID_ARGUMENT                = (4, u'无效参数')
    INVALID_JSON                    = (5, u'无效Json')
    INVALID_OPERATION               = (6, u'无效操作')
    REPEATED_OPERATION              = (7, u'重复操作')
    OBJECT_NOT_EXIST                = (8, u'目标不存在')
    OBJECT_READONLY                 = (9, u'目标只读')
    OBJECT_CREATE_FAIL              = (10, u'目标创建失败')
    USER_NOT_EXIST                  = (11, u'用户不存在')
    NO_PERMISSION                   = (12, u'权限不足')
    INVALID_SMS                     = (13, u'无效验证码')
    INFO_NOT_MATCH                  = (14, u'信息不匹配')
    MISTRUST_DEVICE                 = (15, u'不信任的设备')
    PAYPASS_MISMATCH                = (16, u'支付密码不匹配')
    WALLET_NOT_ENOUGH               = (17, u'余额不足')
    PROCESSING                      = (18, u'处理中')
    PAY_FAILED                      = (19, u'支付失败')
    UNKNOWN                         = (999, u'未知错误')

    @staticmethod
    def get_description(v):
        if ErrorNo.has_value(v):
            return v[1]
        else:
            return ErrorNo.UNKNOWN[1]

    @staticmethod
    def get_error_no(v):
        if ErrorNo.has_value(v):
            return v[0]
        else:
            return ErrorNo.UNKNOWN[0]

    @staticmethod
    def has_value(v):
        return v in ErrorNo.__dict__.values()
