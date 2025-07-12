# 基础配置
PLATFORM = "xhs"
KEYWORDS = "python"
LOGIN_TYPE = "qrcode"  # qrcode or phone or cookie
COOKIES = ""
# 具体值参见media_platform.xxx.field下的枚举值，暂时只支持小红书
SORT_TYPE = "popularity_descending"
# 具体值参见media_platform.xxx.field下的枚举值，暂时只支持抖音
PUBLISH_TIME_TYPE = 0
CRAWLER_TYPE = "search"  # 爬取类型，search(关键词搜索) | detail(帖子详情)| creator(创作者主页数据)
# 建议使用search模式，因为detail模式依赖预设的笔记ID，可能会因为笔记被删除或设为私密而失败

# 是否开启 IP 代理
ENABLE_IP_PROXY = False

# 代理IP池数量
IP_PROXY_POOL_COUNT = 2

# 代理IP提供商名称
IP_PROXY_PROVIDER_NAME = "kuaidaili"

# 设置为True不会打开浏览器（无头浏览器）
# 设置False会打开一个浏览器
# 小红书如果一直扫码登录不通过，打开浏览器手动过一下滑动验证码
# 抖音如果一直提示失败，打开浏览器看下是否扫码登录之后出现了手机号验证，如果出现了手动过一下再试。
HEADLESS = False

# 是否保存登录状态
SAVE_LOGIN_STATE = True

# 数据保存类型选项配置,支持三种类型：csv、db、json
SAVE_DATA_OPTION = "json"  # csv or db or json

# 用户浏览器缓存的浏览器文件配置
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# 爬取开始页数 默认从第一页开始
START_PAGE = 1

# 爬取视频/帖子的数量控制 - 减少数量以降低被检测风险
CRAWLER_MAX_NOTES_COUNT = 5

# 并发爬虫数量控制 - 降低并发数以避免触发反爬虫
MAX_CONCURRENCY_NUM = 1

# 是否开启爬图片模式, 默认不开启爬图片
ENABLE_GET_IMAGES = False

# 是否开启爬评论模式, 默认不开启爬评论
ENABLE_GET_COMMENTS = False

# 是否开启爬二级评论模式, 默认不开启爬二级评论, 目前仅支持 xhs, bilibili
# 老版本项目使用了 db, 则需参考 schema/tables.sql line 287 增加表字段
ENABLE_GET_SUB_COMMENTS = False

# 指定小红书需要爬虫的笔记ID列表
# 注意：这些ID需要是公开可访问的笔记，建议从小红书网页版复制最新的笔记ID
# 笔记ID可以从小红书笔记URL中获取，格式如：https://www.xiaohongshu.com/explore/[笔记ID]
XHS_SPECIFIED_ID_LIST = [
    # 请替换为有效的笔记ID，可以通过以下方式获取：
    # 1. 打开小红书网页版
    # 2. 找到想要爬取的公开笔记
    # 3. 从URL中复制笔记ID（explore/后面的字符串）
    # 示例（请替换为实际有效的ID）：
    # "65f1234567890abcdef12345",  # 替换为实际的笔记ID
    # "65f1234567890abcdef12346",  # 替换为实际的笔记ID
    # "65f1234567890abcdef12347",  # 替换为实际的笔记ID
]

# 指定抖音需要爬取的ID列表
DY_SPECIFIED_ID_LIST = [
    "7280854932641664319",
    "7202432992642387233"
    # ........................
]

# 指定快手平台需要爬取的ID列表
KS_SPECIFIED_ID_LIST = [
    "3xf8enb8dbj6uig",
    "3x6zz972bchmvqe"
]

# 指定B站平台需要爬取的视频bvid列表
BILI_SPECIFIED_ID_LIST = [
    "BV1d54y1g7db",
    "BV1Sz4y1U77N",
    "BV14Q4y1n7jz",
    # ........................
]

# 指定微博平台需要爬取的帖子列表
WEIBO_SPECIFIED_ID_LIST = [
    "4982041758140155",
    # ........................
]

# 指定小红书创作者ID列表
XHS_CREATOR_ID_LIST = [
    "63e36c9a000000002703502b",
    # ........................
]

# 指定Dy创作者ID列表(sec_id)
DY_CREATOR_ID_LIST = [
    "MS4wLjABAAAATJPY7LAlaa5X-c8uNdWkvz0jUGgpw4eeXIwu_8BhvqE",
    # ........................
]

# 指定bili创作者ID列表(sec_id)
BILI_CREATOR_ID_LIST = [
    "20813884",
    # ........................
]

# 指定快手创作者ID列表
KS_CREATOR_ID_LIST = [
    "3x4sm73aye7jq7i",
    # ........................
]


#词云相关
#是否开启生成评论词云图
ENABLE_GET_WORDCLOUD = False
# 自定义词语及其分组
#添加规则：xx:yy 其中xx为自定义添加的词组，yy为将xx该词组分到的组名。
CUSTOM_WORDS = {
    '零几': '年份',  # 将“零几”识别为一个整体
    '高频词': '专业术语'  # 示例自定义词
}

#停用(禁用)词文件路径
STOP_WORDS_FILE = "./docs/hit_stopwords.txt"

#中文字体文件路径
FONT_PATH= "./docs/STZHONGS.TTF"
