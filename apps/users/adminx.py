import xadmin
from users.models import UserProfile,EmailVerifyRecord,Banner
from xadmin import views
# Register your models here.

# xadmin中这里继承object，不再是继承admin
class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_dispaly = ['code','email','seng_type','send_time']
    # 搜索的字段，不要添加时间搜索
    search_fileds = ['code','email','send_type']
    # 过滤
    list_filter = ['code','email','send_type','send_time']


class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fileds = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']
# 创建xadmin的基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# 全局修改，固定写法
class GlobalSettings(object):
    '''
    设置网站标题和页脚
    '''

    site_title = '在线教育平台'  # 修改title
    site_footer = 'Powered By 1906C - 2020'  # 修改footer
    menu_style = 'accordion'  # 设置菜单折叠 # 收起菜单

class UserProfileAdmin(object):
    list_display = ['username','gender','mobile','address']   # 显示的列
    search_filter = ['username','gender','mobile','address']  # 搜索的字段
    list_filter = ['username','gender','mobile','address']  # 过滤
    model_icon = 'fa fa-user'  # 内置了Font Awesome图标  http://www.fontawesome.com.cn/
    style_fields = {"address": "ueditor"}  # 显示富文本的字段
    ordering = ['date_joined']  # 排序
    readonly_fields = ['nick_name']  # 只读字段，不能编辑
    exclude = ['date_joined']   # 不显示的字段
    list_editable = ['mobile']  # 给表格添加信息，可编辑字段
    refresh_times = [3,5]    # 自动刷新时间设置为3秒或5秒


#  将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)
# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.unregister(UserProfile)
# 将后台管理器与models进行关联注册。
xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
