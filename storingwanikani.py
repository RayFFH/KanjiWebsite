import mysql.connector
import json

# Connect to MySQL Server
connection = mysql.connector.connect(
   host = "localhost",
    user = "root",
    passwd = "349dsahoDSI3:",
    database= "testdatabase"
)

# Create a cursor
cursor = connection.cursor()

# Load JSON data
json_data = '''
[
    {
        "kanji": "一",
        "level": 1
    },
    {
        "kanji": "二",
        "level": 1
    },
    {
        "kanji": "九",
        "level": 1
    },
    {
        "kanji": "七",
        "level": 1
    },
    {
        "kanji": "人",
        "level": 1
    },
    {
        "kanji": "入",
        "level": 1
    },
    {
        "kanji": "八",
        "level": 1
    },
    {
        "kanji": "力",
        "level": 1
    },
    {
        "kanji": "十",
        "level": 1
    },
    {
        "kanji": "三",
        "level": 1
    },
    {
        "kanji": "上",
        "level": 1
    },
    {
        "kanji": "下",
        "level": 1
    },
    {
        "kanji": "口",
        "level": 1
    },
    {
        "kanji": "大",
        "level": 1
    },
    {
        "kanji": "女",
        "level": 1
    },
    {
        "kanji": "山",
        "level": 1
    },
    {
        "kanji": "川",
        "level": 1
    },
    {
        "kanji": "工",
        "level": 1
    },
    {
        "kanji": "刀",
        "level": 2
    },
    {
        "kanji": "土",
        "level": 2
    },
    {
        "kanji": "千",
        "level": 2
    },
    {
        "kanji": "夕",
        "level": 2
    },
    {
        "kanji": "子",
        "level": 2
    },
    {
        "kanji": "小",
        "level": 2
    },
    {
        "kanji": "丁",
        "level": 2
    },
    {
        "kanji": "了",
        "level": 2
    },
    {
        "kanji": "又",
        "level": 51
    },
    {
        "kanji": "丸",
        "level": 2
    },
    {
        "kanji": "才",
        "level": 2
    },
    {
        "kanji": "中",
        "level": 2
    },
    {
        "kanji": "五",
        "level": 2
    },
    {
        "kanji": "六",
        "level": 2
    },
    {
        "kanji": "円",
        "level": 2
    },
    {
        "kanji": "天",
        "level": 2
    },
    {
        "kanji": "手",
        "level": 2
    },
    {
        "kanji": "文",
        "level": 2
    },
    {
        "kanji": "日",
        "level": 2
    },
    {
        "kanji": "月",
        "level": 2
    },
    {
        "kanji": "木",
        "level": 2
    },
    {
        "kanji": "水",
        "level": 2
    },
    {
        "kanji": "火",
        "level": 2
    },
    {
        "kanji": "犬",
        "level": 2
    },
    {
        "kanji": "王",
        "level": 2
    },
    {
        "kanji": "出",
        "level": 2
    },
    {
        "kanji": "右",
        "level": 2
    },
    {
        "kanji": "四",
        "level": 2
    },
    {
        "kanji": "左",
        "level": 2
    },
    {
        "kanji": "本",
        "level": 2
    },
    {
        "kanji": "正",
        "level": 2
    },
    {
        "kanji": "玉",
        "level": 2
    },
    {
        "kanji": "田",
        "level": 2
    },
    {
        "kanji": "白",
        "level": 2
    },
    {
        "kanji": "目",
        "level": 2
    },
    {
        "kanji": "石",
        "level": 4
    },
    {
        "kanji": "立",
        "level": 2
    },
    {
        "kanji": "万",
        "level": 3
    },
    {
        "kanji": "久",
        "level": 32
    },
    {
        "kanji": "今",
        "level": 3
    },
    {
        "kanji": "元",
        "level": 3
    },
    {
        "kanji": "公",
        "level": 10
    },
    {
        "kanji": "内",
        "level": 3
    },
    {
        "kanji": "分",
        "level": 3
    },
    {
        "kanji": "切",
        "level": 3
    },
    {
        "kanji": "午",
        "level": 3
    },
    {
        "kanji": "友",
        "level": 3
    },
    {
        "kanji": "太",
        "level": 3
    },
    {
        "kanji": "少",
        "level": 3
    },
    {
        "kanji": "引",
        "level": 3
    },
    {
        "kanji": "心",
        "level": 3
    },
    {
        "kanji": "戸",
        "level": 3
    },
    {
        "kanji": "方",
        "level": 3
    },
    {
        "kanji": "牛",
        "level": 3
    },
    {
        "kanji": "父",
        "level": 3
    },
    {
        "kanji": "毛",
        "level": 3
    },
    {
        "kanji": "止",
        "level": 3
    },
    {
        "kanji": "兄",
        "level": 5
    },
    {
        "kanji": "冬",
        "level": 3
    },
    {
        "kanji": "北",
        "level": 3
    },
    {
        "kanji": "半",
        "level": 3
    },
    {
        "kanji": "古",
        "level": 3
    },
    {
        "kanji": "台",
        "level": 3
    },
    {
        "kanji": "外",
        "level": 3
    },
    {
        "kanji": "市",
        "level": 3
    },
    {
        "kanji": "広",
        "level": 3
    },
    {
        "kanji": "母",
        "level": 3
    },
    {
        "kanji": "用",
        "level": 3
    },
    {
        "kanji": "矢",
        "level": 3
    },
    {
        "kanji": "世",
        "level": 4
    },
    {
        "kanji": "主",
        "level": 4
    },
    {
        "kanji": "他",
        "level": 4
    },
    {
        "kanji": "代",
        "level": 4
    },
    {
        "kanji": "写",
        "level": 4
    },
    {
        "kanji": "去",
        "level": 4
    },
    {
        "kanji": "号",
        "level": 4
    },
    {
        "kanji": "央",
        "level": 4
    },
    {
        "kanji": "平",
        "level": 4
    },
    {
        "kanji": "打",
        "level": 4
    },
    {
        "kanji": "氷",
        "level": 4
    },
    {
        "kanji": "申",
        "level": 4
    },
    {
        "kanji": "皮",
        "level": 5
    },
    {
        "kanji": "皿",
        "level": 4
    },
    {
        "kanji": "礼",
        "level": 4
    },
    {
        "kanji": "休",
        "level": 4
    },
    {
        "kanji": "先",
        "level": 4
    },
    {
        "kanji": "名",
        "level": 4
    },
    {
        "kanji": "字",
        "level": 4
    },
    {
        "kanji": "年",
        "level": 4
    },
    {
        "kanji": "早",
        "level": 4
    },
    {
        "kanji": "気",
        "level": 4
    },
    {
        "kanji": "百",
        "level": 4
    },
    {
        "kanji": "竹",
        "level": 4
    },
    {
        "kanji": "糸",
        "level": 4
    },
    {
        "kanji": "耳",
        "level": 4
    },
    {
        "kanji": "虫",
        "level": 4
    },
    {
        "kanji": "村",
        "level": 4
    },
    {
        "kanji": "男",
        "level": 4
    },
    {
        "kanji": "町",
        "level": 4
    },
    {
        "kanji": "花",
        "level": 4
    },
    {
        "kanji": "見",
        "level": 4
    },
    {
        "kanji": "貝",
        "level": 4
    },
    {
        "kanji": "赤",
        "level": 4
    },
    {
        "kanji": "足",
        "level": 4
    },
    {
        "kanji": "車",
        "level": 4
    },
    {
        "kanji": "不",
        "level": 4
    },
    {
        "kanji": "仕",
        "level": 4
    },
    {
        "kanji": "交",
        "level": 5
    },
    {
        "kanji": "会",
        "level": 5
    },
    {
        "kanji": "光",
        "level": 5
    },
    {
        "kanji": "同",
        "level": 5
    },
    {
        "kanji": "回",
        "level": 5
    },
    {
        "kanji": "多",
        "level": 5
    },
    {
        "kanji": "当",
        "level": 5
    },
    {
        "kanji": "毎",
        "level": 5
    },
    {
        "kanji": "池",
        "level": 8
    },
    {
        "kanji": "米",
        "level": 5
    },
    {
        "kanji": "羽",
        "level": 5
    },
    {
        "kanji": "考",
        "level": 5
    },
    {
        "kanji": "肉",
        "level": 5
    },
    {
        "kanji": "自",
        "level": 5
    },
    {
        "kanji": "色",
        "level": 5
    },
    {
        "kanji": "行",
        "level": 5
    },
    {
        "kanji": "西",
        "level": 5
    },
    {
        "kanji": "何",
        "level": 5
    },
    {
        "kanji": "体",
        "level": 5
    },
    {
        "kanji": "作",
        "level": 5
    },
    {
        "kanji": "図",
        "level": 5
    },
    {
        "kanji": "声",
        "level": 5
    },
    {
        "kanji": "売",
        "level": 9
    },
    {
        "kanji": "弟",
        "level": 5
    },
    {
        "kanji": "形",
        "level": 5
    },
    {
        "kanji": "来",
        "level": 5
    },
    {
        "kanji": "社",
        "level": 5
    },
    {
        "kanji": "角",
        "level": 5
    },
    {
        "kanji": "言",
        "level": 5
    },
    {
        "kanji": "谷",
        "level": 5
    },
    {
        "kanji": "走",
        "level": 5
    },
    {
        "kanji": "近",
        "level": 5
    },
    {
        "kanji": "里",
        "level": 5
    },
    {
        "kanji": "麦",
        "level": 5
    },
    {
        "kanji": "学",
        "level": 5
    },
    {
        "kanji": "林",
        "level": 5
    },
    {
        "kanji": "空",
        "level": 5
    },
    {
        "kanji": "金",
        "level": 5
    },
    {
        "kanji": "雨",
        "level": 5
    },
    {
        "kanji": "青",
        "level": 5
    },
    {
        "kanji": "草",
        "level": 5
    },
    {
        "kanji": "音",
        "level": 5
    },
    {
        "kanji": "化",
        "level": 6
    },
    {
        "kanji": "地",
        "level": 6
    },
    {
        "kanji": "両",
        "level": 6
    },
    {
        "kanji": "全",
        "level": 6
    },
    {
        "kanji": "向",
        "level": 6
    },
    {
        "kanji": "安",
        "level": 6
    },
    {
        "kanji": "州",
        "level": 6
    },
    {
        "kanji": "曲",
        "level": 6
    },
    {
        "kanji": "有",
        "level": 6
    },
    {
        "kanji": "次",
        "level": 6
    },
    {
        "kanji": "死",
        "level": 6
    },
    {
        "kanji": "羊",
        "level": 6
    },
    {
        "kanji": "血",
        "level": 6
    },
    {
        "kanji": "京",
        "level": 6
    },
    {
        "kanji": "国",
        "level": 6
    },
    {
        "kanji": "夜",
        "level": 6
    },
    {
        "kanji": "妹",
        "level": 6
    },
    {
        "kanji": "姉",
        "level": 6
    },
    {
        "kanji": "店",
        "level": 6
    },
    {
        "kanji": "明",
        "level": 6
    },
    {
        "kanji": "東",
        "level": 6
    },
    {
        "kanji": "歩",
        "level": 6
    },
    {
        "kanji": "画",
        "level": 6
    },
    {
        "kanji": "直",
        "level": 6
    },
    {
        "kanji": "知",
        "level": 6
    },
    {
        "kanji": "長",
        "level": 6
    },
    {
        "kanji": "前",
        "level": 6
    },
    {
        "kanji": "南",
        "level": 6
    },
    {
        "kanji": "室",
        "level": 6
    },
    {
        "kanji": "後",
        "level": 6
    },
    {
        "kanji": "思",
        "level": 6
    },
    {
        "kanji": "星",
        "level": 6
    },
    {
        "kanji": "活",
        "level": 6
    },
    {
        "kanji": "海",
        "level": 6
    },
    {
        "kanji": "点",
        "level": 6
    },
    {
        "kanji": "科",
        "level": 6
    },
    {
        "kanji": "茶",
        "level": 6
    },
    {
        "kanji": "食",
        "level": 6
    },
    {
        "kanji": "首",
        "level": 6
    },
    {
        "kanji": "欠",
        "level": 7
    },
    {
        "kanji": "氏",
        "level": 7
    },
    {
        "kanji": "由",
        "level": 7
    },
    {
        "kanji": "札",
        "level": 7
    },
    {
        "kanji": "民",
        "level": 7
    },
    {
        "kanji": "辺",
        "level": 7
    },
    {
        "kanji": "付",
        "level": 7
    },
    {
        "kanji": "以",
        "level": 7
    },
    {
        "kanji": "失",
        "level": 7
    },
    {
        "kanji": "必",
        "level": 7
    },
    {
        "kanji": "未",
        "level": 7
    },
    {
        "kanji": "末",
        "level": 7
    },
    {
        "kanji": "校",
        "level": 7
    },
    {
        "kanji": "夏",
        "level": 7
    },
    {
        "kanji": "家",
        "level": 7
    },
    {
        "kanji": "弱",
        "level": 7
    },
    {
        "kanji": "時",
        "level": 7
    },
    {
        "kanji": "紙",
        "level": 7
    },
    {
        "kanji": "記",
        "level": 7
    },
    {
        "kanji": "通",
        "level": 7
    },
    {
        "kanji": "高",
        "level": 7
    },
    {
        "kanji": "強",
        "level": 7
    },
    {
        "kanji": "教",
        "level": 7
    },
    {
        "kanji": "理",
        "level": 7
    },
    {
        "kanji": "組",
        "level": 7
    },
    {
        "kanji": "船",
        "level": 7
    },
    {
        "kanji": "週",
        "level": 7
    },
    {
        "kanji": "雪",
        "level": 7
    },
    {
        "kanji": "魚",
        "level": 7
    },
    {
        "kanji": "鳥",
        "level": 7
    },
    {
        "kanji": "黄",
        "level": 7
    },
    {
        "kanji": "黒",
        "level": 7
    },
    {
        "kanji": "支",
        "level": 8
    },
    {
        "kanji": "住",
        "level": 8
    },
    {
        "kanji": "助",
        "level": 8
    },
    {
        "kanji": "医",
        "level": 8
    },
    {
        "kanji": "君",
        "level": 8
    },
    {
        "kanji": "対",
        "level": 8
    },
    {
        "kanji": "局",
        "level": 8
    },
    {
        "kanji": "役",
        "level": 8
    },
    {
        "kanji": "投",
        "level": 8
    },
    {
        "kanji": "決",
        "level": 8
    },
    {
        "kanji": "究",
        "level": 8
    },
    {
        "kanji": "身",
        "level": 8
    },
    {
        "kanji": "者",
        "level": 8
    },
    {
        "kanji": "研",
        "level": 8
    },
    {
        "kanji": "馬",
        "level": 8
    },
    {
        "kanji": "森",
        "level": 8
    },
    {
        "kanji": "場",
        "level": 8
    },
    {
        "kanji": "朝",
        "level": 8
    },
    {
        "kanji": "番",
        "level": 8
    },
    {
        "kanji": "答",
        "level": 8
    },
    {
        "kanji": "絵",
        "level": 8
    },
    {
        "kanji": "買",
        "level": 8
    },
    {
        "kanji": "道",
        "level": 8
    },
    {
        "kanji": "間",
        "level": 8
    },
    {
        "kanji": "雲",
        "level": 8
    },
    {
        "kanji": "数",
        "level": 8
    },
    {
        "kanji": "楽",
        "level": 8
    },
    {
        "kanji": "話",
        "level": 8
    },
    {
        "kanji": "電",
        "level": 8
    },
    {
        "kanji": "所",
        "level": 8
    },
    {
        "kanji": "事",
        "level": 9
    },
    {
        "kanji": "使",
        "level": 9
    },
    {
        "kanji": "具",
        "level": 9
    },
    {
        "kanji": "受",
        "level": 9
    },
    {
        "kanji": "和",
        "level": 9
    },
    {
        "kanji": "始",
        "level": 10
    },
    {
        "kanji": "定",
        "level": 9
    },
    {
        "kanji": "実",
        "level": 9
    },
    {
        "kanji": "服",
        "level": 9
    },
    {
        "kanji": "泳",
        "level": 9
    },
    {
        "kanji": "物",
        "level": 9
    },
    {
        "kanji": "苦",
        "level": 9
    },
    {
        "kanji": "表",
        "level": 9
    },
    {
        "kanji": "部",
        "level": 9
    },
    {
        "kanji": "乗",
        "level": 9
    },
    {
        "kanji": "客",
        "level": 9
    },
    {
        "kanji": "屋",
        "level": 9
    },
    {
        "kanji": "度",
        "level": 9
    },
    {
        "kanji": "待",
        "level": 12
    },
    {
        "kanji": "持",
        "level": 9
    },
    {
        "kanji": "界",
        "level": 9
    },
    {
        "kanji": "発",
        "level": 9
    },
    {
        "kanji": "相",
        "level": 9
    },
    {
        "kanji": "県",
        "level": 9
    },
    {
        "kanji": "美",
        "level": 9
    },
    {
        "kanji": "負",
        "level": 9
    },
    {
        "kanji": "送",
        "level": 9
    },
    {
        "kanji": "重",
        "level": 9
    },
    {
        "kanji": "談",
        "level": 9
    },
    {
        "kanji": "要",
        "level": 9
    },
    {
        "kanji": "勝",
        "level": 9
    },
    {
        "kanji": "仮",
        "level": 9
    },
    {
        "kanji": "起",
        "level": 10
    },
    {
        "kanji": "速",
        "level": 10
    },
    {
        "kanji": "配",
        "level": 10
    },
    {
        "kanji": "酒",
        "level": 10
    },
    {
        "kanji": "院",
        "level": 10
    },
    {
        "kanji": "終",
        "level": 10
    },
    {
        "kanji": "習",
        "level": 10
    },
    {
        "kanji": "転",
        "level": 10
    },
    {
        "kanji": "進",
        "level": 10
    },
    {
        "kanji": "落",
        "level": 10
    },
    {
        "kanji": "葉",
        "level": 10
    },
    {
        "kanji": "軽",
        "level": 10
    },
    {
        "kanji": "運",
        "level": 10
    },
    {
        "kanji": "開",
        "level": 10
    },
    {
        "kanji": "集",
        "level": 10
    },
    {
        "kanji": "飲",
        "level": 10
    },
    {
        "kanji": "業",
        "level": 10
    },
    {
        "kanji": "漢",
        "level": 10
    },
    {
        "kanji": "路",
        "level": 10
    },
    {
        "kanji": "農",
        "level": 10
    },
    {
        "kanji": "鉄",
        "level": 10
    },
    {
        "kanji": "歌",
        "level": 10
    },
    {
        "kanji": "算",
        "level": 10
    },
    {
        "kanji": "聞",
        "level": 10
    },
    {
        "kanji": "語",
        "level": 10
    },
    {
        "kanji": "読",
        "level": 10
    },
    {
        "kanji": "鳴",
        "level": 10
    },
    {
        "kanji": "線",
        "level": 10
    },
    {
        "kanji": "横",
        "level": 10
    },
    {
        "kanji": "調",
        "level": 10
    },
    {
        "kanji": "親",
        "level": 10
    },
    {
        "kanji": "頭",
        "level": 10
    },
    {
        "kanji": "顔",
        "level": 10
    },
    {
        "kanji": "病",
        "level": 10
    },
    {
        "kanji": "最",
        "level": 10
    },
    {
        "kanji": "争",
        "level": 11
    },
    {
        "kanji": "仲",
        "level": 11
    },
    {
        "kanji": "伝",
        "level": 11
    },
    {
        "kanji": "共",
        "level": 11
    },
    {
        "kanji": "好",
        "level": 11
    },
    {
        "kanji": "成",
        "level": 11
    },
    {
        "kanji": "老",
        "level": 11
    },
    {
        "kanji": "位",
        "level": 11
    },
    {
        "kanji": "低",
        "level": 11
    },
    {
        "kanji": "初",
        "level": 11
    },
    {
        "kanji": "別",
        "level": 11
    },
    {
        "kanji": "利",
        "level": 11
    },
    {
        "kanji": "努",
        "level": 11
    },
    {
        "kanji": "労",
        "level": 11
    },
    {
        "kanji": "命",
        "level": 11
    },
    {
        "kanji": "岸",
        "level": 11
    },
    {
        "kanji": "放",
        "level": 11
    },
    {
        "kanji": "昔",
        "level": 11
    },
    {
        "kanji": "波",
        "level": 11
    },
    {
        "kanji": "注",
        "level": 11
    },
    {
        "kanji": "育",
        "level": 11
    },
    {
        "kanji": "拾",
        "level": 11
    },
    {
        "kanji": "指",
        "level": 11
    },
    {
        "kanji": "洋",
        "level": 11
    },
    {
        "kanji": "神",
        "level": 11
    },
    {
        "kanji": "秒",
        "level": 11
    },
    {
        "kanji": "級",
        "level": 11
    },
    {
        "kanji": "追",
        "level": 11
    },
    {
        "kanji": "戦",
        "level": 11
    },
    {
        "kanji": "競",
        "level": 11
    },
    {
        "kanji": "良",
        "level": 11
    },
    {
        "kanji": "功",
        "level": 11
    },
    {
        "kanji": "特",
        "level": 11
    },
    {
        "kanji": "便",
        "level": 11
    },
    {
        "kanji": "働",
        "level": 11
    },
    {
        "kanji": "令",
        "level": 11
    },
    {
        "kanji": "意",
        "level": 11
    },
    {
        "kanji": "味",
        "level": 11
    },
    {
        "kanji": "勉",
        "level": 12
    },
    {
        "kanji": "庭",
        "level": 12
    },
    {
        "kanji": "息",
        "level": 12
    },
    {
        "kanji": "旅",
        "level": 12
    },
    {
        "kanji": "根",
        "level": 12
    },
    {
        "kanji": "流",
        "level": 12
    },
    {
        "kanji": "消",
        "level": 12
    },
    {
        "kanji": "倍",
        "level": 12
    },
    {
        "kanji": "員",
        "level": 12
    },
    {
        "kanji": "島",
        "level": 12
    },
    {
        "kanji": "祭",
        "level": 12
    },
    {
        "kanji": "章",
        "level": 12
    },
    {
        "kanji": "第",
        "level": 12
    },
    {
        "kanji": "都",
        "level": 12
    },
    {
        "kanji": "動",
        "level": 12
    },
    {
        "kanji": "商",
        "level": 12
    },
    {
        "kanji": "悪",
        "level": 12
    },
    {
        "kanji": "族",
        "level": 12
    },
    {
        "kanji": "深",
        "level": 12
    },
    {
        "kanji": "球",
        "level": 12
    },
    {
        "kanji": "童",
        "level": 12
    },
    {
        "kanji": "陽",
        "level": 12
    },
    {
        "kanji": "階",
        "level": 12
    },
    {
        "kanji": "寒",
        "level": 12
    },
    {
        "kanji": "悲",
        "level": 17
    },
    {
        "kanji": "暑",
        "level": 12
    },
    {
        "kanji": "期",
        "level": 12
    },
    {
        "kanji": "植",
        "level": 12
    },
    {
        "kanji": "歯",
        "level": 12
    },
    {
        "kanji": "温",
        "level": 12
    },
    {
        "kanji": "港",
        "level": 12
    },
    {
        "kanji": "湯",
        "level": 12
    },
    {
        "kanji": "登",
        "level": 12
    },
    {
        "kanji": "着",
        "level": 12
    },
    {
        "kanji": "短",
        "level": 12
    },
    {
        "kanji": "野",
        "level": 12
    },
    {
        "kanji": "泉",
        "level": 12
    },
    {
        "kanji": "生",
        "level": 3
    },
    {
        "kanji": "亡",
        "level": 6
    },
    {
        "kanji": "合",
        "level": 12
    },
    {
        "kanji": "風",
        "level": 7
    },
    {
        "kanji": "予",
        "level": 9
    },
    {
        "kanji": "反",
        "level": 8
    },
    {
        "kanji": "々",
        "level": 2
    },
    {
        "kanji": "新",
        "level": 9
    },
    {
        "kanji": "返",
        "level": 9
    },
    {
        "kanji": "問",
        "level": 13
    },
    {
        "kanji": "宿",
        "level": 13
    },
    {
        "kanji": "想",
        "level": 13
    },
    {
        "kanji": "感",
        "level": 13
    },
    {
        "kanji": "整",
        "level": 13
    },
    {
        "kanji": "暗",
        "level": 13
    },
    {
        "kanji": "様",
        "level": 13
    },
    {
        "kanji": "橋",
        "level": 13
    },
    {
        "kanji": "福",
        "level": 13
    },
    {
        "kanji": "緑",
        "level": 13
    },
    {
        "kanji": "練",
        "level": 13
    },
    {
        "kanji": "詩",
        "level": 13
    },
    {
        "kanji": "銀",
        "level": 13
    },
    {
        "kanji": "題",
        "level": 13
    },
    {
        "kanji": "館",
        "level": 13
    },
    {
        "kanji": "駅",
        "level": 13
    },
    {
        "kanji": "億",
        "level": 13
    },
    {
        "kanji": "器",
        "level": 13
    },
    {
        "kanji": "士",
        "level": 13
    },
    {
        "kanji": "料",
        "level": 13
    },
    {
        "kanji": "標",
        "level": 13
    },
    {
        "kanji": "殺",
        "level": 13
    },
    {
        "kanji": "然",
        "level": 13
    },
    {
        "kanji": "熱",
        "level": 13
    },
    {
        "kanji": "課",
        "level": 13
    },
    {
        "kanji": "賞",
        "level": 13
    },
    {
        "kanji": "輪",
        "level": 13
    },
    {
        "kanji": "選",
        "level": 13
    },
    {
        "kanji": "鏡",
        "level": 13
    },
    {
        "kanji": "願",
        "level": 13
    },
    {
        "kanji": "養",
        "level": 13
    },
    {
        "kanji": "像",
        "level": 13
    },
    {
        "kanji": "情",
        "level": 13
    },
    {
        "kanji": "謝",
        "level": 13
    },
    {
        "kanji": "映",
        "level": 13
    },
    {
        "kanji": "疑",
        "level": 13
    },
    {
        "kanji": "皆",
        "level": 13
    },
    {
        "kanji": "例",
        "level": 14
    },
    {
        "kanji": "卒",
        "level": 14
    },
    {
        "kanji": "協",
        "level": 14
    },
    {
        "kanji": "参",
        "level": 14
    },
    {
        "kanji": "周",
        "level": 14
    },
    {
        "kanji": "囲",
        "level": 14
    },
    {
        "kanji": "固",
        "level": 14
    },
    {
        "kanji": "季",
        "level": 14
    },
    {
        "kanji": "完",
        "level": 14
    },
    {
        "kanji": "希",
        "level": 14
    },
    {
        "kanji": "念",
        "level": 14
    },
    {
        "kanji": "折",
        "level": 14
    },
    {
        "kanji": "望",
        "level": 14
    },
    {
        "kanji": "材",
        "level": 14
    },
    {
        "kanji": "束",
        "level": 14
    },
    {
        "kanji": "松",
        "level": 14
    },
    {
        "kanji": "残",
        "level": 14
    },
    {
        "kanji": "求",
        "level": 10
    },
    {
        "kanji": "的",
        "level": 14
    },
    {
        "kanji": "約",
        "level": 14
    },
    {
        "kanji": "芸",
        "level": 14
    },
    {
        "kanji": "基",
        "level": 14
    },
    {
        "kanji": "性",
        "level": 14
    },
    {
        "kanji": "技",
        "level": 15
    },
    {
        "kanji": "格",
        "level": 14
    },
    {
        "kanji": "能",
        "level": 14
    },
    {
        "kanji": "術",
        "level": 15
    },
    {
        "kanji": "私",
        "level": 6
    },
    {
        "kanji": "骨",
        "level": 14
    },
    {
        "kanji": "妥",
        "level": 14
    },
    {
        "kanji": "雰",
        "level": 14
    },
    {
        "kanji": "頑",
        "level": 14
    },
    {
        "kanji": "寺",
        "level": 15
    },
    {
        "kanji": "岩",
        "level": 15
    },
    {
        "kanji": "帰",
        "level": 15
    },
    {
        "kanji": "春",
        "level": 15
    },
    {
        "kanji": "昼",
        "level": 15
    },
    {
        "kanji": "晴",
        "level": 15
    },
    {
        "kanji": "秋",
        "level": 15
    },
    {
        "kanji": "計",
        "level": 15
    },
    {
        "kanji": "列",
        "level": 15
    },
    {
        "kanji": "区",
        "level": 15
    },
    {
        "kanji": "坂",
        "level": 15
    },
    {
        "kanji": "式",
        "level": 15
    },
    {
        "kanji": "信",
        "level": 15
    },
    {
        "kanji": "勇",
        "level": 15
    },
    {
        "kanji": "単",
        "level": 15
    },
    {
        "kanji": "司",
        "level": 15
    },
    {
        "kanji": "変",
        "level": 15
    },
    {
        "kanji": "夫",
        "level": 15
    },
    {
        "kanji": "建",
        "level": 15
    },
    {
        "kanji": "昨",
        "level": 15
    },
    {
        "kanji": "毒",
        "level": 15
    },
    {
        "kanji": "法",
        "level": 15
    },
    {
        "kanji": "泣",
        "level": 15
    },
    {
        "kanji": "浅",
        "level": 15
    },
    {
        "kanji": "紀",
        "level": 15
    },
    {
        "kanji": "英",
        "level": 15
    },
    {
        "kanji": "軍",
        "level": 15
    },
    {
        "kanji": "飯",
        "level": 15
    },
    {
        "kanji": "仏",
        "level": 15
    },
    {
        "kanji": "築",
        "level": 15
    },
    {
        "kanji": "晩",
        "level": 15
    },
    {
        "kanji": "猫",
        "level": 15
    },
    {
        "kanji": "園",
        "level": 16
    },
    {
        "kanji": "曜",
        "level": 16
    },
    {
        "kanji": "書",
        "level": 16
    },
    {
        "kanji": "遠",
        "level": 16
    },
    {
        "kanji": "門",
        "level": 16
    },
    {
        "kanji": "係",
        "level": 16
    },
    {
        "kanji": "取",
        "level": 16
    },
    {
        "kanji": "品",
        "level": 16
    },
    {
        "kanji": "守",
        "level": 16
    },
    {
        "kanji": "幸",
        "level": 16
    },
    {
        "kanji": "急",
        "level": 16
    },
    {
        "kanji": "真",
        "level": 16
    },
    {
        "kanji": "箱",
        "level": 16
    },
    {
        "kanji": "荷",
        "level": 16
    },
    {
        "kanji": "面",
        "level": 16
    },
    {
        "kanji": "典",
        "level": 16
    },
    {
        "kanji": "喜",
        "level": 17
    },
    {
        "kanji": "府",
        "level": 16
    },
    {
        "kanji": "治",
        "level": 16
    },
    {
        "kanji": "浴",
        "level": 16
    },
    {
        "kanji": "笑",
        "level": 16
    },
    {
        "kanji": "辞",
        "level": 16
    },
    {
        "kanji": "関",
        "level": 16
    },
    {
        "kanji": "保",
        "level": 9
    },
    {
        "kanji": "弁",
        "level": 16
    },
    {
        "kanji": "政",
        "level": 16
    },
    {
        "kanji": "留",
        "level": 16
    },
    {
        "kanji": "証",
        "level": 16
    },
    {
        "kanji": "険",
        "level": 16
    },
    {
        "kanji": "危",
        "level": 16
    },
    {
        "kanji": "存",
        "level": 16
    },
    {
        "kanji": "専",
        "level": 16
    },
    {
        "kanji": "冒",
        "level": 16
    },
    {
        "kanji": "冗",
        "level": 16
    },
    {
        "kanji": "阪",
        "level": 16
    },
    {
        "kanji": "原",
        "level": 17
    },
    {
        "kanji": "細",
        "level": 17
    },
    {
        "kanji": "薬",
        "level": 17
    },
    {
        "kanji": "鼻",
        "level": 17
    },
    {
        "kanji": "側",
        "level": 17
    },
    {
        "kanji": "兵",
        "level": 17
    },
    {
        "kanji": "堂",
        "level": 17
    },
    {
        "kanji": "塩",
        "level": 17
    },
    {
        "kanji": "席",
        "level": 17
    },
    {
        "kanji": "敗",
        "level": 17
    },
    {
        "kanji": "果",
        "level": 17
    },
    {
        "kanji": "栄",
        "level": 17
    },
    {
        "kanji": "梅",
        "level": 17
    },
    {
        "kanji": "無",
        "level": 17
    },
    {
        "kanji": "結",
        "level": 17
    },
    {
        "kanji": "因",
        "level": 17
    },
    {
        "kanji": "常",
        "level": 17
    },
    {
        "kanji": "識",
        "level": 17
    },
    {
        "kanji": "非",
        "level": 17
    },
    {
        "kanji": "干",
        "level": 17
    },
    {
        "kanji": "是",
        "level": 17
    },
    {
        "kanji": "渉",
        "level": 17
    },
    {
        "kanji": "虚",
        "level": 17
    },
    {
        "kanji": "官",
        "level": 17
    },
    {
        "kanji": "察",
        "level": 17
    },
    {
        "kanji": "底",
        "level": 17
    },
    {
        "kanji": "愛",
        "level": 17
    },
    {
        "kanji": "署",
        "level": 17
    },
    {
        "kanji": "警",
        "level": 17
    },
    {
        "kanji": "恋",
        "level": 17
    },
    {
        "kanji": "覚",
        "level": 17
    },
    {
        "kanji": "説",
        "level": 17
    },
    {
        "kanji": "幻",
        "level": 17
    },
    {
        "kanji": "訓",
        "level": 18
    },
    {
        "kanji": "試",
        "level": 9
    },
    {
        "kanji": "弓",
        "level": 18
    },
    {
        "kanji": "告",
        "level": 18
    },
    {
        "kanji": "種",
        "level": 18
    },
    {
        "kanji": "達",
        "level": 18
    },
    {
        "kanji": "類",
        "level": 18
    },
    {
        "kanji": "報",
        "level": 18
    },
    {
        "kanji": "祈",
        "level": 18
    },
    {
        "kanji": "等",
        "level": 18
    },
    {
        "kanji": "汽",
        "level": 18
    },
    {
        "kanji": "借",
        "level": 18
    },
    {
        "kanji": "焼",
        "level": 18
    },
    {
        "kanji": "座",
        "level": 18
    },
    {
        "kanji": "忘",
        "level": 18
    },
    {
        "kanji": "洗",
        "level": 18
    },
    {
        "kanji": "胸",
        "level": 18
    },
    {
        "kanji": "脳",
        "level": 18
    },
    {
        "kanji": "僧",
        "level": 18
    },
    {
        "kanji": "禅",
        "level": 18
    },
    {
        "kanji": "験",
        "level": 9
    },
    {
        "kanji": "可",
        "level": 18
    },
    {
        "kanji": "許",
        "level": 18
    },
    {
        "kanji": "枚",
        "level": 18
    },
    {
        "kanji": "静",
        "level": 18
    },
    {
        "kanji": "句",
        "level": 18
    },
    {
        "kanji": "禁",
        "level": 18
    },
    {
        "kanji": "喫",
        "level": 18
    },
    {
        "kanji": "煙",
        "level": 18
    },
    {
        "kanji": "加",
        "level": 19
    },
    {
        "kanji": "節",
        "level": 19
    },
    {
        "kanji": "減",
        "level": 19
    },
    {
        "kanji": "順",
        "level": 19
    },
    {
        "kanji": "容",
        "level": 19
    },
    {
        "kanji": "布",
        "level": 19
    },
    {
        "kanji": "易",
        "level": 19
    },
    {
        "kanji": "財",
        "level": 19
    },
    {
        "kanji": "若",
        "level": 19
    },
    {
        "kanji": "詞",
        "level": 19
    },
    {
        "kanji": "昆",
        "level": 19
    },
    {
        "kanji": "閥",
        "level": 19
    },
    {
        "kanji": "歴",
        "level": 19
    },
    {
        "kanji": "舌",
        "level": 19
    },
    {
        "kanji": "冊",
        "level": 19
    },
    {
        "kanji": "宇",
        "level": 19
    },
    {
        "kanji": "宙",
        "level": 19
    },
    {
        "kanji": "忙",
        "level": 19
    },
    {
        "kanji": "履",
        "level": 19
    },
    {
        "kanji": "団",
        "level": 19
    },
    {
        "kanji": "暴",
        "level": 19
    },
    {
        "kanji": "混",
        "level": 19
    },
    {
        "kanji": "乱",
        "level": 19
    },
    {
        "kanji": "徒",
        "level": 19
    },
    {
        "kanji": "得",
        "level": 19
    },
    {
        "kanji": "改",
        "level": 19
    },
    {
        "kanji": "続",
        "level": 19
    },
    {
        "kanji": "連",
        "level": 19
    },
    {
        "kanji": "善",
        "level": 19
    },
    {
        "kanji": "困",
        "level": 20
    },
    {
        "kanji": "絡",
        "level": 19
    },
    {
        "kanji": "比",
        "level": 19
    },
    {
        "kanji": "災",
        "level": 20
    },
    {
        "kanji": "機",
        "level": 20
    },
    {
        "kanji": "率",
        "level": 20
    },
    {
        "kanji": "飛",
        "level": 20
    },
    {
        "kanji": "害",
        "level": 20
    },
    {
        "kanji": "余",
        "level": 20
    },
    {
        "kanji": "難",
        "level": 20
    },
    {
        "kanji": "妨",
        "level": 20
    },
    {
        "kanji": "被",
        "level": 20
    },
    {
        "kanji": "裕",
        "level": 20
    },
    {
        "kanji": "震",
        "level": 20
    },
    {
        "kanji": "尻",
        "level": 20
    },
    {
        "kanji": "尾",
        "level": 20
    },
    {
        "kanji": "械",
        "level": 20
    },
    {
        "kanji": "確",
        "level": 20
    },
    {
        "kanji": "嫌",
        "level": 20
    },
    {
        "kanji": "個",
        "level": 20
    },
    {
        "kanji": "圧",
        "level": 20
    },
    {
        "kanji": "在",
        "level": 20
    },
    {
        "kanji": "夢",
        "level": 20
    },
    {
        "kanji": "産",
        "level": 20
    },
    {
        "kanji": "倒",
        "level": 20
    },
    {
        "kanji": "臭",
        "level": 20
    },
    {
        "kanji": "厚",
        "level": 20
    },
    {
        "kanji": "妻",
        "level": 20
    },
    {
        "kanji": "議",
        "level": 20
    },
    {
        "kanji": "犯",
        "level": 20
    },
    {
        "kanji": "罪",
        "level": 20
    },
    {
        "kanji": "防",
        "level": 20
    },
    {
        "kanji": "穴",
        "level": 20
    },
    {
        "kanji": "論",
        "level": 20
    },
    {
        "kanji": "経",
        "level": 20
    },
    {
        "kanji": "笛",
        "level": 19
    },
    {
        "kanji": "史",
        "level": 19
    },
    {
        "kanji": "敵",
        "level": 21
    },
    {
        "kanji": "済",
        "level": 21
    },
    {
        "kanji": "委",
        "level": 21
    },
    {
        "kanji": "挙",
        "level": 21
    },
    {
        "kanji": "判",
        "level": 21
    },
    {
        "kanji": "制",
        "level": 21
    },
    {
        "kanji": "務",
        "level": 21
    },
    {
        "kanji": "査",
        "level": 21
    },
    {
        "kanji": "総",
        "level": 21
    },
    {
        "kanji": "設",
        "level": 21
    },
    {
        "kanji": "資",
        "level": 21
    },
    {
        "kanji": "権",
        "level": 21
    },
    {
        "kanji": "件",
        "level": 21
    },
    {
        "kanji": "派",
        "level": 21
    },
    {
        "kanji": "岡",
        "level": 21
    },
    {
        "kanji": "素",
        "level": 21
    },
    {
        "kanji": "断",
        "level": 21
    },
    {
        "kanji": "評",
        "level": 21
    },
    {
        "kanji": "批",
        "level": 21
    },
    {
        "kanji": "任",
        "level": 21
    },
    {
        "kanji": "検",
        "level": 21
    },
    {
        "kanji": "審",
        "level": 21
    },
    {
        "kanji": "条",
        "level": 21
    },
    {
        "kanji": "責",
        "level": 21
    },
    {
        "kanji": "省",
        "level": 21
    },
    {
        "kanji": "増",
        "level": 21
    },
    {
        "kanji": "税",
        "level": 21
    },
    {
        "kanji": "解",
        "level": 21
    },
    {
        "kanji": "際",
        "level": 21
    },
    {
        "kanji": "認",
        "level": 21
    },
    {
        "kanji": "企",
        "level": 21
    },
    {
        "kanji": "義",
        "level": 21
    },
    {
        "kanji": "罰",
        "level": 22
    },
    {
        "kanji": "誕",
        "level": 22
    },
    {
        "kanji": "脱",
        "level": 22
    },
    {
        "kanji": "過",
        "level": 22
    },
    {
        "kanji": "坊",
        "level": 22
    },
    {
        "kanji": "寝",
        "level": 22
    },
    {
        "kanji": "宮",
        "level": 22
    },
    {
        "kanji": "各",
        "level": 22
    },
    {
        "kanji": "案",
        "level": 22
    },
    {
        "kanji": "置",
        "level": 22
    },
    {
        "kanji": "費",
        "level": 22
    },
    {
        "kanji": "価",
        "level": 22
    },
    {
        "kanji": "勢",
        "level": 22
    },
    {
        "kanji": "営",
        "level": 22
    },
    {
        "kanji": "示",
        "level": 22
    },
    {
        "kanji": "統",
        "level": 22
    },
    {
        "kanji": "領",
        "level": 22
    },
    {
        "kanji": "策",
        "level": 22
    },
    {
        "kanji": "藤",
        "level": 22
    },
    {
        "kanji": "副",
        "level": 22
    },
    {
        "kanji": "観",
        "level": 22
    },
    {
        "kanji": "値",
        "level": 22
    },
    {
        "kanji": "吸",
        "level": 22
    },
    {
        "kanji": "域",
        "level": 22
    },
    {
        "kanji": "姿",
        "level": 22
    },
    {
        "kanji": "応",
        "level": 22
    },
    {
        "kanji": "提",
        "level": 22
    },
    {
        "kanji": "援",
        "level": 22
    },
    {
        "kanji": "状",
        "level": 22
    },
    {
        "kanji": "態",
        "level": 22
    },
    {
        "kanji": "賀",
        "level": 22
    },
    {
        "kanji": "収",
        "level": 23
    },
    {
        "kanji": "停",
        "level": 23
    },
    {
        "kanji": "革",
        "level": 23
    },
    {
        "kanji": "職",
        "level": 23
    },
    {
        "kanji": "鬼",
        "level": 23
    },
    {
        "kanji": "規",
        "level": 23
    },
    {
        "kanji": "護",
        "level": 23
    },
    {
        "kanji": "割",
        "level": 23
    },
    {
        "kanji": "裁",
        "level": 23
    },
    {
        "kanji": "崎",
        "level": 23
    },
    {
        "kanji": "演",
        "level": 23
    },
    {
        "kanji": "律",
        "level": 23
    },
    {
        "kanji": "師",
        "level": 23
    },
    {
        "kanji": "看",
        "level": 23
    },
    {
        "kanji": "準",
        "level": 23
    },
    {
        "kanji": "則",
        "level": 23
    },
    {
        "kanji": "備",
        "level": 23
    },
    {
        "kanji": "導",
        "level": 23
    },
    {
        "kanji": "幹",
        "level": 23
    },
    {
        "kanji": "張",
        "level": 23
    },
    {
        "kanji": "優",
        "level": 23
    },
    {
        "kanji": "宅",
        "level": 23
    },
    {
        "kanji": "沢",
        "level": 23
    },
    {
        "kanji": "贅",
        "level": 23
    },
    {
        "kanji": "施",
        "level": 23
    },
    {
        "kanji": "現",
        "level": 23
    },
    {
        "kanji": "乳",
        "level": 23
    },
    {
        "kanji": "呼",
        "level": 23
    },
    {
        "kanji": "城",
        "level": 23
    },
    {
        "kanji": "俳",
        "level": 23
    },
    {
        "kanji": "秀",
        "level": 23
    },
    {
        "kanji": "担",
        "level": 24
    },
    {
        "kanji": "額",
        "level": 24
    },
    {
        "kanji": "製",
        "level": 24
    },
    {
        "kanji": "違",
        "level": 24
    },
    {
        "kanji": "輸",
        "level": 24
    },
    {
        "kanji": "燃",
        "level": 24
    },
    {
        "kanji": "祝",
        "level": 24
    },
    {
        "kanji": "届",
        "level": 24
    },
    {
        "kanji": "狭",
        "level": 24
    },
    {
        "kanji": "肩",
        "level": 24
    },
    {
        "kanji": "腕",
        "level": 24
    },
    {
        "kanji": "腰",
        "level": 24
    },
    {
        "kanji": "触",
        "level": 24
    },
    {
        "kanji": "載",
        "level": 24
    },
    {
        "kanji": "層",
        "level": 24
    },
    {
        "kanji": "型",
        "level": 24
    },
    {
        "kanji": "庁",
        "level": 24
    },
    {
        "kanji": "視",
        "level": 24
    },
    {
        "kanji": "差",
        "level": 24
    },
    {
        "kanji": "管",
        "level": 24
    },
    {
        "kanji": "象",
        "level": 24
    },
    {
        "kanji": "量",
        "level": 24
    },
    {
        "kanji": "境",
        "level": 24
    },
    {
        "kanji": "環",
        "level": 24
    },
    {
        "kanji": "武",
        "level": 24
    },
    {
        "kanji": "質",
        "level": 24
    },
    {
        "kanji": "述",
        "level": 24
    },
    {
        "kanji": "供",
        "level": 24
    },
    {
        "kanji": "展",
        "level": 24
    },
    {
        "kanji": "販",
        "level": 24
    },
    {
        "kanji": "株",
        "level": 24
    },
    {
        "kanji": "限",
        "level": 25
    },
    {
        "kanji": "与",
        "level": 25
    },
    {
        "kanji": "含",
        "level": 25
    },
    {
        "kanji": "影",
        "level": 25
    },
    {
        "kanji": "況",
        "level": 25
    },
    {
        "kanji": "渡",
        "level": 25
    },
    {
        "kanji": "響",
        "level": 25
    },
    {
        "kanji": "票",
        "level": 25
    },
    {
        "kanji": "景",
        "level": 25
    },
    {
        "kanji": "抜",
        "level": 25
    },
    {
        "kanji": "訴",
        "level": 25
    },
    {
        "kanji": "訟",
        "level": 25
    },
    {
        "kanji": "逮",
        "level": 25
    },
    {
        "kanji": "補",
        "level": 25
    },
    {
        "kanji": "候",
        "level": 25
    },
    {
        "kanji": "構",
        "level": 25
    },
    {
        "kanji": "模",
        "level": 25
    },
    {
        "kanji": "捕",
        "level": 25
    },
    {
        "kanji": "鮮",
        "level": 25
    },
    {
        "kanji": "効",
        "level": 25
    },
    {
        "kanji": "属",
        "level": 25
    },
    {
        "kanji": "慣",
        "level": 25
    },
    {
        "kanji": "豊",
        "level": 25
    },
    {
        "kanji": "満",
        "level": 25
    },
    {
        "kanji": "肥",
        "level": 25
    },
    {
        "kanji": "巻",
        "level": 25
    },
    {
        "kanji": "捜",
        "level": 25
    },
    {
        "kanji": "絞",
        "level": 25
    },
    {
        "kanji": "輩",
        "level": 25
    },
    {
        "kanji": "隠",
        "level": 25
    },
    {
        "kanji": "掛",
        "level": 25
    },
    {
        "kanji": "替",
        "level": 25
    },
    {
        "kanji": "居",
        "level": 25
    },
    {
        "kanji": "造",
        "level": 26
    },
    {
        "kanji": "授",
        "level": 26
    },
    {
        "kanji": "印",
        "level": 26
    },
    {
        "kanji": "創",
        "level": 26
    },
    {
        "kanji": "復",
        "level": 26
    },
    {
        "kanji": "往",
        "level": 26
    },
    {
        "kanji": "較",
        "level": 26
    },
    {
        "kanji": "筆",
        "level": 26
    },
    {
        "kanji": "鉛",
        "level": 26
    },
    {
        "kanji": "貯",
        "level": 26
    },
    {
        "kanji": "故",
        "level": 26
    },
    {
        "kanji": "障",
        "level": 26
    },
    {
        "kanji": "従",
        "level": 26
    },
    {
        "kanji": "我",
        "level": 26
    },
    {
        "kanji": "激",
        "level": 26
    },
    {
        "kanji": "刺",
        "level": 26
    },
    {
        "kanji": "励",
        "level": 26
    },
    {
        "kanji": "討",
        "level": 26
    },
    {
        "kanji": "郵",
        "level": 26
    },
    {
        "kanji": "針",
        "level": 26
    },
    {
        "kanji": "徴",
        "level": 26
    },
    {
        "kanji": "怪",
        "level": 26
    },
    {
        "kanji": "獣",
        "level": 26
    },
    {
        "kanji": "突",
        "level": 26
    },
    {
        "kanji": "菓",
        "level": 26
    },
    {
        "kanji": "河",
        "level": 26
    },
    {
        "kanji": "振",
        "level": 26
    },
    {
        "kanji": "汗",
        "level": 26
    },
    {
        "kanji": "豚",
        "level": 26
    },
    {
        "kanji": "再",
        "level": 26
    },
    {
        "kanji": "接",
        "level": 26
    },
    {
        "kanji": "独",
        "level": 26
    },
    {
        "kanji": "占",
        "level": 26
    },
    {
        "kanji": "招",
        "level": 27
    },
    {
        "kanji": "段",
        "level": 27
    },
    {
        "kanji": "胃",
        "level": 27
    },
    {
        "kanji": "腹",
        "level": 27
    },
    {
        "kanji": "痛",
        "level": 27
    },
    {
        "kanji": "退",
        "level": 27
    },
    {
        "kanji": "屈",
        "level": 27
    },
    {
        "kanji": "悩",
        "level": 27
    },
    {
        "kanji": "暇",
        "level": 27
    },
    {
        "kanji": "織",
        "level": 27
    },
    {
        "kanji": "貸",
        "level": 27
    },
    {
        "kanji": "迷",
        "level": 27
    },
    {
        "kanji": "惑",
        "level": 27
    },
    {
        "kanji": "誘",
        "level": 27
    },
    {
        "kanji": "就",
        "level": 27
    },
    {
        "kanji": "訪",
        "level": 27
    },
    {
        "kanji": "怒",
        "level": 27
    },
    {
        "kanji": "昇",
        "level": 27
    },
    {
        "kanji": "眠",
        "level": 27
    },
    {
        "kanji": "睡",
        "level": 27
    },
    {
        "kanji": "症",
        "level": 27
    },
    {
        "kanji": "締",
        "level": 27
    },
    {
        "kanji": "迫",
        "level": 27
    },
    {
        "kanji": "靴",
        "level": 27
    },
    {
        "kanji": "濃",
        "level": 27
    },
    {
        "kanji": "端",
        "level": 27
    },
    {
        "kanji": "極",
        "level": 27
    },
    {
        "kanji": "途",
        "level": 27
    },
    {
        "kanji": "健",
        "level": 27
    },
    {
        "kanji": "康",
        "level": 27
    },
    {
        "kanji": "郎",
        "level": 27
    },
    {
        "kanji": "給",
        "level": 27
    },
    {
        "kanji": "逆",
        "level": 28
    },
    {
        "kanji": "巨",
        "level": 28
    },
    {
        "kanji": "庫",
        "level": 28
    },
    {
        "kanji": "児",
        "level": 28
    },
    {
        "kanji": "冷",
        "level": 28
    },
    {
        "kanji": "凍",
        "level": 28
    },
    {
        "kanji": "幼",
        "level": 28
    },
    {
        "kanji": "稚",
        "level": 28
    },
    {
        "kanji": "処",
        "level": 28
    },
    {
        "kanji": "博",
        "level": 28
    },
    {
        "kanji": "清",
        "level": 28
    },
    {
        "kanji": "潔",
        "level": 28
    },
    {
        "kanji": "録",
        "level": 28
    },
    {
        "kanji": "隊",
        "level": 28
    },
    {
        "kanji": "修",
        "level": 28
    },
    {
        "kanji": "券",
        "level": 28
    },
    {
        "kanji": "婦",
        "level": 28
    },
    {
        "kanji": "奇",
        "level": 28
    },
    {
        "kanji": "妙",
        "level": 28
    },
    {
        "kanji": "麗",
        "level": 28
    },
    {
        "kanji": "微",
        "level": 28
    },
    {
        "kanji": "益",
        "level": 28
    },
    {
        "kanji": "移",
        "level": 28
    },
    {
        "kanji": "程",
        "level": 28
    },
    {
        "kanji": "精",
        "level": 28
    },
    {
        "kanji": "絶",
        "level": 28
    },
    {
        "kanji": "並",
        "level": 28
    },
    {
        "kanji": "憲",
        "level": 28
    },
    {
        "kanji": "衆",
        "level": 28
    },
    {
        "kanji": "傘",
        "level": 28
    },
    {
        "kanji": "浜",
        "level": 28
    },
    {
        "kanji": "撃",
        "level": 28
    },
    {
        "kanji": "攻",
        "level": 28
    },
    {
        "kanji": "監",
        "level": 29
    },
    {
        "kanji": "杯",
        "level": 29
    },
    {
        "kanji": "乾",
        "level": 29
    },
    {
        "kanji": "催",
        "level": 29
    },
    {
        "kanji": "促",
        "level": 29
    },
    {
        "kanji": "欧",
        "level": 29
    },
    {
        "kanji": "江",
        "level": 29
    },
    {
        "kanji": "請",
        "level": 29
    },
    {
        "kanji": "雄",
        "level": 29
    },
    {
        "kanji": "韓",
        "level": 29
    },
    {
        "kanji": "壊",
        "level": 29
    },
    {
        "kanji": "診",
        "level": 29
    },
    {
        "kanji": "閣",
        "level": 29
    },
    {
        "kanji": "僚",
        "level": 29
    },
    {
        "kanji": "積",
        "level": 29
    },
    {
        "kanji": "督",
        "level": 29
    },
    {
        "kanji": "臣",
        "level": 29
    },
    {
        "kanji": "略",
        "level": 29
    },
    {
        "kanji": "航",
        "level": 29
    },
    {
        "kanji": "寄",
        "level": 29
    },
    {
        "kanji": "板",
        "level": 29
    },
    {
        "kanji": "街",
        "level": 29
    },
    {
        "kanji": "宗",
        "level": 29
    },
    {
        "kanji": "緊",
        "level": 29
    },
    {
        "kanji": "娘",
        "level": 29
    },
    {
        "kanji": "宴",
        "level": 29
    },
    {
        "kanji": "怖",
        "level": 29
    },
    {
        "kanji": "恐",
        "level": 29
    },
    {
        "kanji": "添",
        "level": 29
    },
    {
        "kanji": "猛",
        "level": 29
    },
    {
        "kanji": "烈",
        "level": 29
    },
    {
        "kanji": "索",
        "level": 29
    },
    {
        "kanji": "詰",
        "level": 29
    },
    {
        "kanji": "詳",
        "level": 17
    },
    {
        "kanji": "魅",
        "level": 30
    },
    {
        "kanji": "渇",
        "level": 30
    },
    {
        "kanji": "系",
        "level": 30
    },
    {
        "kanji": "婚",
        "level": 30
    },
    {
        "kanji": "遊",
        "level": 30
    },
    {
        "kanji": "旗",
        "level": 30
    },
    {
        "kanji": "照",
        "level": 30
    },
    {
        "kanji": "快",
        "level": 30
    },
    {
        "kanji": "版",
        "level": 30
    },
    {
        "kanji": "貧",
        "level": 30
    },
    {
        "kanji": "乏",
        "level": 30
    },
    {
        "kanji": "適",
        "level": 30
    },
    {
        "kanji": "預",
        "level": 30
    },
    {
        "kanji": "延",
        "level": 30
    },
    {
        "kanji": "翌",
        "level": 30
    },
    {
        "kanji": "覧",
        "level": 30
    },
    {
        "kanji": "懐",
        "level": 30
    },
    {
        "kanji": "押",
        "level": 30
    },
    {
        "kanji": "更",
        "level": 30
    },
    {
        "kanji": "枕",
        "level": 30
    },
    {
        "kanji": "浮",
        "level": 30
    },
    {
        "kanji": "漏",
        "level": 30
    },
    {
        "kanji": "符",
        "level": 30
    },
    {
        "kanji": "購",
        "level": 30
    },
    {
        "kanji": "越",
        "level": 30
    },
    {
        "kanji": "飾",
        "level": 30
    },
    {
        "kanji": "騒",
        "level": 30
    },
    {
        "kanji": "背",
        "level": 30
    },
    {
        "kanji": "撮",
        "level": 30
    },
    {
        "kanji": "盗",
        "level": 30
    },
    {
        "kanji": "離",
        "level": 31
    },
    {
        "kanji": "融",
        "level": 31
    },
    {
        "kanji": "編",
        "level": 31
    },
    {
        "kanji": "華",
        "level": 31
    },
    {
        "kanji": "既",
        "level": 31
    },
    {
        "kanji": "普",
        "level": 31
    },
    {
        "kanji": "豪",
        "level": 31
    },
    {
        "kanji": "鑑",
        "level": 31
    },
    {
        "kanji": "除",
        "level": 31
    },
    {
        "kanji": "尋",
        "level": 31
    },
    {
        "kanji": "幾",
        "level": 31
    },
    {
        "kanji": "廊",
        "level": 31
    },
    {
        "kanji": "掃",
        "level": 31
    },
    {
        "kanji": "泥",
        "level": 31
    },
    {
        "kanji": "棒",
        "level": 31
    },
    {
        "kanji": "驚",
        "level": 31
    },
    {
        "kanji": "嘆",
        "level": 31
    },
    {
        "kanji": "倉",
        "level": 31
    },
    {
        "kanji": "孫",
        "level": 31
    },
    {
        "kanji": "巣",
        "level": 31
    },
    {
        "kanji": "帯",
        "level": 31
    },
    {
        "kanji": "径",
        "level": 31
    },
    {
        "kanji": "救",
        "level": 31
    },
    {
        "kanji": "散",
        "level": 31
    },
    {
        "kanji": "粉",
        "level": 31
    },
    {
        "kanji": "脈",
        "level": 31
    },
    {
        "kanji": "菜",
        "level": 31
    },
    {
        "kanji": "貨",
        "level": 31
    },
    {
        "kanji": "陸",
        "level": 31
    },
    {
        "kanji": "似",
        "level": 31
    },
    {
        "kanji": "均",
        "level": 31
    },
    {
        "kanji": "墓",
        "level": 31
    },
    {
        "kanji": "富",
        "level": 31
    },
    {
        "kanji": "徳",
        "level": 31
    },
    {
        "kanji": "探",
        "level": 31
    },
    {
        "kanji": "偵",
        "level": 31
    },
    {
        "kanji": "綺",
        "level": 28
    },
    {
        "kanji": "序",
        "level": 32
    },
    {
        "kanji": "迎",
        "level": 32
    },
    {
        "kanji": "志",
        "level": 32
    },
    {
        "kanji": "恩",
        "level": 32
    },
    {
        "kanji": "採",
        "level": 32
    },
    {
        "kanji": "桜",
        "level": 32
    },
    {
        "kanji": "永",
        "level": 32
    },
    {
        "kanji": "液",
        "level": 32
    },
    {
        "kanji": "眼",
        "level": 32
    },
    {
        "kanji": "祖",
        "level": 32
    },
    {
        "kanji": "績",
        "level": 32
    },
    {
        "kanji": "興",
        "level": 32
    },
    {
        "kanji": "衛",
        "level": 32
    },
    {
        "kanji": "複",
        "level": 32
    },
    {
        "kanji": "雑",
        "level": 32
    },
    {
        "kanji": "賛",
        "level": 32
    },
    {
        "kanji": "酸",
        "level": 32
    },
    {
        "kanji": "銭",
        "level": 32
    },
    {
        "kanji": "飼",
        "level": 32
    },
    {
        "kanji": "傷",
        "level": 32
    },
    {
        "kanji": "党",
        "level": 32
    },
    {
        "kanji": "卵",
        "level": 32
    },
    {
        "kanji": "厳",
        "level": 32
    },
    {
        "kanji": "捨",
        "level": 32
    },
    {
        "kanji": "込",
        "level": 32
    },
    {
        "kanji": "密",
        "level": 32
    },
    {
        "kanji": "汚",
        "level": 32
    },
    {
        "kanji": "欲",
        "level": 32
    },
    {
        "kanji": "暖",
        "level": 32
    },
    {
        "kanji": "机",
        "level": 32
    },
    {
        "kanji": "秘",
        "level": 32
    },
    {
        "kanji": "訳",
        "level": 32
    },
    {
        "kanji": "染",
        "level": 32
    },
    {
        "kanji": "簡",
        "level": 33
    },
    {
        "kanji": "閉",
        "level": 33
    },
    {
        "kanji": "誌",
        "level": 33
    },
    {
        "kanji": "窓",
        "level": 33
    },
    {
        "kanji": "否",
        "level": 33
    },
    {
        "kanji": "筋",
        "level": 33
    },
    {
        "kanji": "垂",
        "level": 33
    },
    {
        "kanji": "宝",
        "level": 4
    },
    {
        "kanji": "宣",
        "level": 33
    },
    {
        "kanji": "尊",
        "level": 33
    },
    {
        "kanji": "忠",
        "level": 33
    },
    {
        "kanji": "拡",
        "level": 33
    },
    {
        "kanji": "操",
        "level": 33
    },
    {
        "kanji": "敬",
        "level": 33
    },
    {
        "kanji": "暮",
        "level": 33
    },
    {
        "kanji": "灰",
        "level": 33
    },
    {
        "kanji": "熟",
        "level": 33
    },
    {
        "kanji": "異",
        "level": 33
    },
    {
        "kanji": "皇",
        "level": 33
    },
    {
        "kanji": "盛",
        "level": 33
    },
    {
        "kanji": "砂",
        "level": 33
    },
    {
        "kanji": "漠",
        "level": 33
    },
    {
        "kanji": "糖",
        "level": 33
    },
    {
        "kanji": "納",
        "level": 33
    },
    {
        "kanji": "肺",
        "level": 33
    },
    {
        "kanji": "著",
        "level": 33
    },
    {
        "kanji": "蒸",
        "level": 33
    },
    {
        "kanji": "蔵",
        "level": 33
    },
    {
        "kanji": "装",
        "level": 33
    },
    {
        "kanji": "裏",
        "level": 33
    },
    {
        "kanji": "諸",
        "level": 33
    },
    {
        "kanji": "賃",
        "level": 33
    },
    {
        "kanji": "誤",
        "level": 34
    },
    {
        "kanji": "臓",
        "level": 34
    },
    {
        "kanji": "貴",
        "level": 34
    },
    {
        "kanji": "降",
        "level": 34
    },
    {
        "kanji": "丼",
        "level": 34
    },
    {
        "kanji": "吐",
        "level": 34
    },
    {
        "kanji": "奴",
        "level": 34
    },
    {
        "kanji": "隷",
        "level": 34
    },
    {
        "kanji": "芋",
        "level": 34
    },
    {
        "kanji": "縮",
        "level": 34
    },
    {
        "kanji": "純",
        "level": 34
    },
    {
        "kanji": "縦",
        "level": 34
    },
    {
        "kanji": "粋",
        "level": 34
    },
    {
        "kanji": "聖",
        "level": 34
    },
    {
        "kanji": "磁",
        "level": 34
    },
    {
        "kanji": "紅",
        "level": 34
    },
    {
        "kanji": "射",
        "level": 34
    },
    {
        "kanji": "幕",
        "level": 34
    },
    {
        "kanji": "拝",
        "level": 34
    },
    {
        "kanji": "薦",
        "level": 34
    },
    {
        "kanji": "推",
        "level": 34
    },
    {
        "kanji": "揮",
        "level": 34
    },
    {
        "kanji": "沿",
        "level": 34
    },
    {
        "kanji": "源",
        "level": 34
    },
    {
        "kanji": "劇",
        "level": 17
    },
    {
        "kanji": "勤",
        "level": 34
    },
    {
        "kanji": "歓",
        "level": 34
    },
    {
        "kanji": "承",
        "level": 34
    },
    {
        "kanji": "損",
        "level": 34
    },
    {
        "kanji": "枝",
        "level": 34
    },
    {
        "kanji": "爪",
        "level": 34
    },
    {
        "kanji": "豆",
        "level": 34
    },
    {
        "kanji": "刻",
        "level": 34
    },
    {
        "kanji": "腐",
        "level": 34
    },
    {
        "kanji": "遅",
        "level": 35
    },
    {
        "kanji": "彫",
        "level": 35
    },
    {
        "kanji": "測",
        "level": 35
    },
    {
        "kanji": "破",
        "level": 35
    },
    {
        "kanji": "舎",
        "level": 35
    },
    {
        "kanji": "講",
        "level": 35
    },
    {
        "kanji": "滞",
        "level": 35
    },
    {
        "kanji": "紹",
        "level": 35
    },
    {
        "kanji": "介",
        "level": 35
    },
    {
        "kanji": "己",
        "level": 35
    },
    {
        "kanji": "厄",
        "level": 35
    },
    {
        "kanji": "亀",
        "level": 35
    },
    {
        "kanji": "互",
        "level": 35
    },
    {
        "kanji": "剣",
        "level": 35
    },
    {
        "kanji": "寿",
        "level": 35
    },
    {
        "kanji": "彼",
        "level": 35
    },
    {
        "kanji": "恥",
        "level": 35
    },
    {
        "kanji": "杉",
        "level": 35
    },
    {
        "kanji": "汁",
        "level": 35
    },
    {
        "kanji": "噌",
        "level": 35
    },
    {
        "kanji": "炎",
        "level": 35
    },
    {
        "kanji": "為",
        "level": 35
    },
    {
        "kanji": "熊",
        "level": 35
    },
    {
        "kanji": "獄",
        "level": 35
    },
    {
        "kanji": "酔",
        "level": 35
    },
    {
        "kanji": "酢",
        "level": 35
    },
    {
        "kanji": "鍋",
        "level": 35
    },
    {
        "kanji": "湖",
        "level": 35
    },
    {
        "kanji": "銅",
        "level": 35
    },
    {
        "kanji": "払",
        "level": 15
    },
    {
        "kanji": "油",
        "level": 35
    },
    {
        "kanji": "醤",
        "level": 35
    },
    {
        "kanji": "旧",
        "level": 36
    },
    {
        "kanji": "姓",
        "level": 36
    },
    {
        "kanji": "貿",
        "level": 36
    },
    {
        "kanji": "将",
        "level": 36
    },
    {
        "kanji": "盟",
        "level": 36
    },
    {
        "kanji": "遺",
        "level": 36
    },
    {
        "kanji": "伸",
        "level": 36
    },
    {
        "kanji": "債",
        "level": 36
    },
    {
        "kanji": "及",
        "level": 36
    },
    {
        "kanji": "奈",
        "level": 36
    },
    {
        "kanji": "幅",
        "level": 36
    },
    {
        "kanji": "廃",
        "level": 36
    },
    {
        "kanji": "甘",
        "level": 36
    },
    {
        "kanji": "換",
        "level": 36
    },
    {
        "kanji": "摘",
        "level": 36
    },
    {
        "kanji": "核",
        "level": 36
    },
    {
        "kanji": "沖",
        "level": 36
    },
    {
        "kanji": "縄",
        "level": 36
    },
    {
        "kanji": "津",
        "level": 36
    },
    {
        "kanji": "献",
        "level": 36
    },
    {
        "kanji": "療",
        "level": 36
    },
    {
        "kanji": "継",
        "level": 36
    },
    {
        "kanji": "維",
        "level": 36
    },
    {
        "kanji": "舞",
        "level": 36
    },
    {
        "kanji": "伎",
        "level": 36
    },
    {
        "kanji": "踏",
        "level": 36
    },
    {
        "kanji": "般",
        "level": 36
    },
    {
        "kanji": "頼",
        "level": 36
    },
    {
        "kanji": "依",
        "level": 36
    },
    {
        "kanji": "鹿",
        "level": 36
    },
    {
        "kanji": "諾",
        "level": 36
    },
    {
        "kanji": "牙",
        "level": 36
    },
    {
        "kanji": "跳",
        "level": 37
    },
    {
        "kanji": "昭",
        "level": 37
    },
    {
        "kanji": "漁",
        "level": 37
    },
    {
        "kanji": "償",
        "level": 37
    },
    {
        "kanji": "刑",
        "level": 37
    },
    {
        "kanji": "募",
        "level": 37
    },
    {
        "kanji": "執",
        "level": 37
    },
    {
        "kanji": "塁",
        "level": 37
    },
    {
        "kanji": "崩",
        "level": 37
    },
    {
        "kanji": "患",
        "level": 37
    },
    {
        "kanji": "戻",
        "level": 37
    },
    {
        "kanji": "抗",
        "level": 37
    },
    {
        "kanji": "抵",
        "level": 37
    },
    {
        "kanji": "旬",
        "level": 37
    },
    {
        "kanji": "湾",
        "level": 37
    },
    {
        "kanji": "爆",
        "level": 37
    },
    {
        "kanji": "弾",
        "level": 37
    },
    {
        "kanji": "聴",
        "level": 37
    },
    {
        "kanji": "跡",
        "level": 37
    },
    {
        "kanji": "遣",
        "level": 37
    },
    {
        "kanji": "闘",
        "level": 37
    },
    {
        "kanji": "陣",
        "level": 37
    },
    {
        "kanji": "香",
        "level": 37
    },
    {
        "kanji": "兆",
        "level": 37
    },
    {
        "kanji": "臨",
        "level": 37
    },
    {
        "kanji": "削",
        "level": 37
    },
    {
        "kanji": "契",
        "level": 37
    },
    {
        "kanji": "恵",
        "level": 37
    },
    {
        "kanji": "抱",
        "level": 37
    },
    {
        "kanji": "掲",
        "level": 37
    },
    {
        "kanji": "狙",
        "level": 37
    },
    {
        "kanji": "葬",
        "level": 37
    },
    {
        "kanji": "需",
        "level": 38
    },
    {
        "kanji": "齢",
        "level": 38
    },
    {
        "kanji": "宜",
        "level": 38
    },
    {
        "kanji": "繰",
        "level": 38
    },
    {
        "kanji": "避",
        "level": 38
    },
    {
        "kanji": "妊",
        "level": 38
    },
    {
        "kanji": "娠",
        "level": 38
    },
    {
        "kanji": "致",
        "level": 38
    },
    {
        "kanji": "刊",
        "level": 38
    },
    {
        "kanji": "奏",
        "level": 38
    },
    {
        "kanji": "伴",
        "level": 38
    },
    {
        "kanji": "併",
        "level": 38
    },
    {
        "kanji": "傾",
        "level": 38
    },
    {
        "kanji": "却",
        "level": 38
    },
    {
        "kanji": "奥",
        "level": 38
    },
    {
        "kanji": "慮",
        "level": 38
    },
    {
        "kanji": "懸",
        "level": 38
    },
    {
        "kanji": "房",
        "level": 38
    },
    {
        "kanji": "扱",
        "level": 38
    },
    {
        "kanji": "抑",
        "level": 38
    },
    {
        "kanji": "択",
        "level": 38
    },
    {
        "kanji": "描",
        "level": 38
    },
    {
        "kanji": "盤",
        "level": 38
    },
    {
        "kanji": "称",
        "level": 38
    },
    {
        "kanji": "緒",
        "level": 38
    },
    {
        "kanji": "緩",
        "level": 38
    },
    {
        "kanji": "託",
        "level": 38
    },
    {
        "kanji": "賄",
        "level": 38
    },
    {
        "kanji": "賂",
        "level": 38
    },
    {
        "kanji": "贈",
        "level": 38
    },
    {
        "kanji": "逃",
        "level": 38
    },
    {
        "kanji": "還",
        "level": 38
    },
    {
        "kanji": "超",
        "level": 36
    },
    {
        "kanji": "邦",
        "level": 39
    },
    {
        "kanji": "鈴",
        "level": 39
    },
    {
        "kanji": "阜",
        "level": 39
    },
    {
        "kanji": "岐",
        "level": 39
    },
    {
        "kanji": "隆",
        "level": 39
    },
    {
        "kanji": "雇",
        "level": 39
    },
    {
        "kanji": "控",
        "level": 39
    },
    {
        "kanji": "壁",
        "level": 39
    },
    {
        "kanji": "棋",
        "level": 39
    },
    {
        "kanji": "渋",
        "level": 39
    },
    {
        "kanji": "片",
        "level": 39
    },
    {
        "kanji": "群",
        "level": 39
    },
    {
        "kanji": "仙",
        "level": 39
    },
    {
        "kanji": "充",
        "level": 39
    },
    {
        "kanji": "免",
        "level": 39
    },
    {
        "kanji": "勧",
        "level": 39
    },
    {
        "kanji": "圏",
        "level": 39
    },
    {
        "kanji": "埋",
        "level": 39
    },
    {
        "kanji": "埼",
        "level": 39
    },
    {
        "kanji": "奪",
        "level": 39
    },
    {
        "kanji": "御",
        "level": 39
    },
    {
        "kanji": "慎",
        "level": 39
    },
    {
        "kanji": "拒",
        "level": 39
    },
    {
        "kanji": "枠",
        "level": 39
    },
    {
        "kanji": "甲",
        "level": 39
    },
    {
        "kanji": "斐",
        "level": 39
    },
    {
        "kanji": "祉",
        "level": 39
    },
    {
        "kanji": "稲",
        "level": 39
    },
    {
        "kanji": "譲",
        "level": 39
    },
    {
        "kanji": "謙",
        "level": 39
    },
    {
        "kanji": "躍",
        "level": 39
    },
    {
        "kanji": "銃",
        "level": 39
    },
    {
        "kanji": "項",
        "level": 39
    },
    {
        "kanji": "鋼",
        "level": 39
    },
    {
        "kanji": "顧",
        "level": 40
    },
    {
        "kanji": "駐",
        "level": 40
    },
    {
        "kanji": "駆",
        "level": 40
    },
    {
        "kanji": "柱",
        "level": 40
    },
    {
        "kanji": "唱",
        "level": 40
    },
    {
        "kanji": "孝",
        "level": 40
    },
    {
        "kanji": "俊",
        "level": 40
    },
    {
        "kanji": "兼",
        "level": 40
    },
    {
        "kanji": "剤",
        "level": 40
    },
    {
        "kanji": "吹",
        "level": 40
    },
    {
        "kanji": "堀",
        "level": 40
    },
    {
        "kanji": "巡",
        "level": 40
    },
    {
        "kanji": "戒",
        "level": 40
    },
    {
        "kanji": "排",
        "level": 40
    },
    {
        "kanji": "携",
        "level": 40
    },
    {
        "kanji": "敏",
        "level": 40
    },
    {
        "kanji": "鋭",
        "level": 40
    },
    {
        "kanji": "敷",
        "level": 40
    },
    {
        "kanji": "殿",
        "level": 40
    },
    {
        "kanji": "犠",
        "level": 40
    },
    {
        "kanji": "獲",
        "level": 40
    },
    {
        "kanji": "茂",
        "level": 40
    },
    {
        "kanji": "繁",
        "level": 40
    },
    {
        "kanji": "頻",
        "level": 40
    },
    {
        "kanji": "殖",
        "level": 40
    },
    {
        "kanji": "薄",
        "level": 40
    },
    {
        "kanji": "衝",
        "level": 40
    },
    {
        "kanji": "誉",
        "level": 40
    },
    {
        "kanji": "褒",
        "level": 40
    },
    {
        "kanji": "透",
        "level": 40
    },
    {
        "kanji": "隣",
        "level": 40
    },
    {
        "kanji": "雅",
        "level": 40
    },
    {
        "kanji": "遜",
        "level": 41
    },
    {
        "kanji": "伺",
        "level": 41
    },
    {
        "kanji": "徹",
        "level": 41
    },
    {
        "kanji": "瀬",
        "level": 41
    },
    {
        "kanji": "撤",
        "level": 41
    },
    {
        "kanji": "措",
        "level": 41
    },
    {
        "kanji": "拠",
        "level": 41
    },
    {
        "kanji": "儀",
        "level": 41
    },
    {
        "kanji": "樹",
        "level": 41
    },
    {
        "kanji": "棄",
        "level": 41
    },
    {
        "kanji": "虎",
        "level": 41
    },
    {
        "kanji": "蛍",
        "level": 41
    },
    {
        "kanji": "蜂",
        "level": 41
    },
    {
        "kanji": "酎",
        "level": 41
    },
    {
        "kanji": "蜜",
        "level": 41
    },
    {
        "kanji": "墟",
        "level": 41
    },
    {
        "kanji": "艦",
        "level": 41
    },
    {
        "kanji": "潜",
        "level": 41
    },
    {
        "kanji": "拳",
        "level": 41
    },
    {
        "kanji": "炭",
        "level": 41
    },
    {
        "kanji": "畑",
        "level": 41
    },
    {
        "kanji": "包",
        "level": 41
    },
    {
        "kanji": "衣",
        "level": 41
    },
    {
        "kanji": "仁",
        "level": 41
    },
    {
        "kanji": "鉱",
        "level": 41
    },
    {
        "kanji": "至",
        "level": 41
    },
    {
        "kanji": "誠",
        "level": 41
    },
    {
        "kanji": "郷",
        "level": 41
    },
    {
        "kanji": "侵",
        "level": 41
    },
    {
        "kanji": "偽",
        "level": 41
    },
    {
        "kanji": "克",
        "level": 42
    },
    {
        "kanji": "到",
        "level": 42
    },
    {
        "kanji": "双",
        "level": 42
    },
    {
        "kanji": "哲",
        "level": 42
    },
    {
        "kanji": "喪",
        "level": 42
    },
    {
        "kanji": "堅",
        "level": 42
    },
    {
        "kanji": "床",
        "level": 42
    },
    {
        "kanji": "括",
        "level": 42
    },
    {
        "kanji": "弧",
        "level": 42
    },
    {
        "kanji": "挑",
        "level": 42
    },
    {
        "kanji": "掘",
        "level": 42
    },
    {
        "kanji": "揚",
        "level": 42
    },
    {
        "kanji": "握",
        "level": 42
    },
    {
        "kanji": "揺",
        "level": 42
    },
    {
        "kanji": "斎",
        "level": 42
    },
    {
        "kanji": "暫",
        "level": 42
    },
    {
        "kanji": "析",
        "level": 42
    },
    {
        "kanji": "枢",
        "level": 42
    },
    {
        "kanji": "軸",
        "level": 42
    },
    {
        "kanji": "柄",
        "level": 42
    },
    {
        "kanji": "泊",
        "level": 42
    },
    {
        "kanji": "滑",
        "level": 42
    },
    {
        "kanji": "潟",
        "level": 42
    },
    {
        "kanji": "焦",
        "level": 42
    },
    {
        "kanji": "範",
        "level": 42
    },
    {
        "kanji": "紛",
        "level": 42
    },
    {
        "kanji": "糾",
        "level": 42
    },
    {
        "kanji": "綱",
        "level": 42
    },
    {
        "kanji": "網",
        "level": 42
    },
    {
        "kanji": "肝",
        "level": 42
    },
    {
        "kanji": "芝",
        "level": 42
    },
    {
        "kanji": "荒",
        "level": 42
    },
    {
        "kanji": "袋",
        "level": 42
    },
    {
        "kanji": "誰",
        "level": 43
    },
    {
        "kanji": "珍",
        "level": 43
    },
    {
        "kanji": "裂",
        "level": 43
    },
    {
        "kanji": "襲",
        "level": 43
    },
    {
        "kanji": "貢",
        "level": 43
    },
    {
        "kanji": "趣",
        "level": 43
    },
    {
        "kanji": "距",
        "level": 43
    },
    {
        "kanji": "籍",
        "level": 43
    },
    {
        "kanji": "露",
        "level": 43
    },
    {
        "kanji": "牧",
        "level": 43
    },
    {
        "kanji": "刷",
        "level": 43
    },
    {
        "kanji": "朗",
        "level": 43
    },
    {
        "kanji": "潮",
        "level": 43
    },
    {
        "kanji": "即",
        "level": 43
    },
    {
        "kanji": "垣",
        "level": 43
    },
    {
        "kanji": "威",
        "level": 43
    },
    {
        "kanji": "封",
        "level": 43
    },
    {
        "kanji": "筒",
        "level": 43
    },
    {
        "kanji": "岳",
        "level": 45
    },
    {
        "kanji": "慰",
        "level": 43
    },
    {
        "kanji": "懇",
        "level": 43
    },
    {
        "kanji": "懲",
        "level": 43
    },
    {
        "kanji": "摩",
        "level": 43
    },
    {
        "kanji": "擦",
        "level": 43
    },
    {
        "kanji": "撲",
        "level": 43
    },
    {
        "kanji": "斉",
        "level": 43
    },
    {
        "kanji": "旨",
        "level": 43
    },
    {
        "kanji": "柔",
        "level": 43
    },
    {
        "kanji": "沈",
        "level": 43
    },
    {
        "kanji": "沼",
        "level": 43
    },
    {
        "kanji": "泰",
        "level": 43
    },
    {
        "kanji": "滅",
        "level": 43
    },
    {
        "kanji": "滋",
        "level": 43
    },
    {
        "kanji": "炉",
        "level": 43
    },
    {
        "kanji": "琴",
        "level": 43
    },
    {
        "kanji": "寸",
        "level": 44
    },
    {
        "kanji": "竜",
        "level": 44
    },
    {
        "kanji": "縁",
        "level": 44
    },
    {
        "kanji": "翼",
        "level": 44
    },
    {
        "kanji": "吉",
        "level": 44
    },
    {
        "kanji": "刃",
        "level": 44
    },
    {
        "kanji": "忍",
        "level": 44
    },
    {
        "kanji": "桃",
        "level": 44
    },
    {
        "kanji": "辛",
        "level": 44
    },
    {
        "kanji": "謎",
        "level": 44
    },
    {
        "kanji": "侍",
        "level": 44
    },
    {
        "kanji": "俺",
        "level": 44
    },
    {
        "kanji": "叱",
        "level": 44
    },
    {
        "kanji": "娯",
        "level": 44
    },
    {
        "kanji": "斗",
        "level": 44
    },
    {
        "kanji": "朱",
        "level": 44
    },
    {
        "kanji": "丘",
        "level": 44
    },
    {
        "kanji": "梨",
        "level": 44
    },
    {
        "kanji": "僕",
        "level": 12
    },
    {
        "kanji": "匹",
        "level": 15
    },
    {
        "kanji": "叫",
        "level": 44
    },
    {
        "kanji": "釣",
        "level": 44
    },
    {
        "kanji": "髪",
        "level": 44
    },
    {
        "kanji": "嵐",
        "level": 44
    },
    {
        "kanji": "笠",
        "level": 44
    },
    {
        "kanji": "涙",
        "level": 44
    },
    {
        "kanji": "缶",
        "level": 44
    },
    {
        "kanji": "姫",
        "level": 44
    },
    {
        "kanji": "棚",
        "level": 44
    },
    {
        "kanji": "粒",
        "level": 44
    },
    {
        "kanji": "砲",
        "level": 44
    },
    {
        "kanji": "雷",
        "level": 44
    },
    {
        "kanji": "芽",
        "level": 44
    },
    {
        "kanji": "塔",
        "level": 44
    },
    {
        "kanji": "澄",
        "level": 45
    },
    {
        "kanji": "矛",
        "level": 45
    },
    {
        "kanji": "肌",
        "level": 45
    },
    {
        "kanji": "舟",
        "level": 45
    },
    {
        "kanji": "鐘",
        "level": 45
    },
    {
        "kanji": "凶",
        "level": 45
    },
    {
        "kanji": "塊",
        "level": 45
    },
    {
        "kanji": "狩",
        "level": 45
    },
    {
        "kanji": "頃",
        "level": 45
    },
    {
        "kanji": "魂",
        "level": 45
    },
    {
        "kanji": "脚",
        "level": 45
    },
    {
        "kanji": "也",
        "level": 45
    },
    {
        "kanji": "井",
        "level": 45
    },
    {
        "kanji": "呪",
        "level": 45
    },
    {
        "kanji": "嬢",
        "level": 45
    },
    {
        "kanji": "暦",
        "level": 45
    },
    {
        "kanji": "曇",
        "level": 45
    },
    {
        "kanji": "眺",
        "level": 45
    },
    {
        "kanji": "裸",
        "level": 45
    },
    {
        "kanji": "賭",
        "level": 45
    },
    {
        "kanji": "疲",
        "level": 45
    },
    {
        "kanji": "塾",
        "level": 45
    },
    {
        "kanji": "卓",
        "level": 45
    },
    {
        "kanji": "磨",
        "level": 45
    },
    {
        "kanji": "菌",
        "level": 45
    },
    {
        "kanji": "陰",
        "level": 45
    },
    {
        "kanji": "霊",
        "level": 45
    },
    {
        "kanji": "湿",
        "level": 45
    },
    {
        "kanji": "硬",
        "level": 45
    },
    {
        "kanji": "稼",
        "level": 45
    },
    {
        "kanji": "嫁",
        "level": 45
    },
    {
        "kanji": "溝",
        "level": 45
    },
    {
        "kanji": "滝",
        "level": 45
    },
    {
        "kanji": "狂",
        "level": 45
    },
    {
        "kanji": "翔",
        "level": 45
    },
    {
        "kanji": "墨",
        "level": 46
    },
    {
        "kanji": "鳩",
        "level": 46
    },
    {
        "kanji": "穏",
        "level": 46
    },
    {
        "kanji": "鈍",
        "level": 46
    },
    {
        "kanji": "魔",
        "level": 46
    },
    {
        "kanji": "寮",
        "level": 46
    },
    {
        "kanji": "盆",
        "level": 46
    },
    {
        "kanji": "棟",
        "level": 46
    },
    {
        "kanji": "吾",
        "level": 46
    },
    {
        "kanji": "斬",
        "level": 46
    },
    {
        "kanji": "寧",
        "level": 46
    },
    {
        "kanji": "椅",
        "level": 46
    },
    {
        "kanji": "歳",
        "level": 46
    },
    {
        "kanji": "涼",
        "level": 46
    },
    {
        "kanji": "猿",
        "level": 46
    },
    {
        "kanji": "瞳",
        "level": 46
    },
    {
        "kanji": "鍵",
        "level": 46
    },
    {
        "kanji": "零",
        "level": 46
    },
    {
        "kanji": "碁",
        "level": 46
    },
    {
        "kanji": "租",
        "level": 46
    },
    {
        "kanji": "幽",
        "level": 46
    },
    {
        "kanji": "泡",
        "level": 46
    },
    {
        "kanji": "癖",
        "level": 46
    },
    {
        "kanji": "鍛",
        "level": 46
    },
    {
        "kanji": "錬",
        "level": 46
    },
    {
        "kanji": "穂",
        "level": 46
    },
    {
        "kanji": "帝",
        "level": 46
    },
    {
        "kanji": "瞬",
        "level": 46
    },
    {
        "kanji": "菊",
        "level": 46
    },
    {
        "kanji": "誇",
        "level": 46
    },
    {
        "kanji": "庄",
        "level": 46
    },
    {
        "kanji": "阻",
        "level": 46
    },
    {
        "kanji": "黙",
        "level": 46
    },
    {
        "kanji": "俵",
        "level": 46
    },
    {
        "kanji": "綿",
        "level": 46
    },
    {
        "kanji": "架",
        "level": 46
    },
    {
        "kanji": "砕",
        "level": 47
    },
    {
        "kanji": "粘",
        "level": 47
    },
    {
        "kanji": "粧",
        "level": 47
    },
    {
        "kanji": "欺",
        "level": 47
    },
    {
        "kanji": "詐",
        "level": 47
    },
    {
        "kanji": "霧",
        "level": 47
    },
    {
        "kanji": "柳",
        "level": 47
    },
    {
        "kanji": "伊",
        "level": 47
    },
    {
        "kanji": "佐",
        "level": 47
    },
    {
        "kanji": "尺",
        "level": 47
    },
    {
        "kanji": "哀",
        "level": 47
    },
    {
        "kanji": "唇",
        "level": 47
    },
    {
        "kanji": "塀",
        "level": 47
    },
    {
        "kanji": "墜",
        "level": 47
    },
    {
        "kanji": "如",
        "level": 47
    },
    {
        "kanji": "婆",
        "level": 47
    },
    {
        "kanji": "崖",
        "level": 47
    },
    {
        "kanji": "帽",
        "level": 47
    },
    {
        "kanji": "幣",
        "level": 47
    },
    {
        "kanji": "恨",
        "level": 47
    },
    {
        "kanji": "憎",
        "level": 47
    },
    {
        "kanji": "憩",
        "level": 47
    },
    {
        "kanji": "扇",
        "level": 47
    },
    {
        "kanji": "扉",
        "level": 47
    },
    {
        "kanji": "挿",
        "level": 47
    },
    {
        "kanji": "掌",
        "level": 47
    },
    {
        "kanji": "滴",
        "level": 47
    },
    {
        "kanji": "炊",
        "level": 47
    },
    {
        "kanji": "爽",
        "level": 47
    },
    {
        "kanji": "畳",
        "level": 47
    },
    {
        "kanji": "瞭",
        "level": 47
    },
    {
        "kanji": "箸",
        "level": 47
    },
    {
        "kanji": "胴",
        "level": 47
    },
    {
        "kanji": "芯",
        "level": 47
    },
    {
        "kanji": "虹",
        "level": 47
    },
    {
        "kanji": "帳",
        "level": 48
    },
    {
        "kanji": "蚊",
        "level": 48
    },
    {
        "kanji": "蛇",
        "level": 48
    },
    {
        "kanji": "貼",
        "level": 48
    },
    {
        "kanji": "辱",
        "level": 48
    },
    {
        "kanji": "鉢",
        "level": 48
    },
    {
        "kanji": "闇",
        "level": 48
    },
    {
        "kanji": "隙",
        "level": 48
    },
    {
        "kanji": "霜",
        "level": 48
    },
    {
        "kanji": "飢",
        "level": 48
    },
    {
        "kanji": "餓",
        "level": 48
    },
    {
        "kanji": "畜",
        "level": 48
    },
    {
        "kanji": "迅",
        "level": 48
    },
    {
        "kanji": "騎",
        "level": 48
    },
    {
        "kanji": "蓄",
        "level": 48
    },
    {
        "kanji": "尽",
        "level": 48
    },
    {
        "kanji": "彩",
        "level": 48
    },
    {
        "kanji": "憶",
        "level": 48
    },
    {
        "kanji": "溶",
        "level": 48
    },
    {
        "kanji": "耐",
        "level": 48
    },
    {
        "kanji": "踊",
        "level": 48
    },
    {
        "kanji": "賢",
        "level": 48
    },
    {
        "kanji": "輝",
        "level": 48
    },
    {
        "kanji": "脅",
        "level": 48
    },
    {
        "kanji": "麻",
        "level": 48
    },
    {
        "kanji": "灯",
        "level": 48
    },
    {
        "kanji": "咲",
        "level": 48
    },
    {
        "kanji": "培",
        "level": 48
    },
    {
        "kanji": "悔",
        "level": 48
    },
    {
        "kanji": "脇",
        "level": 48
    },
    {
        "kanji": "遂",
        "level": 48
    },
    {
        "kanji": "班",
        "level": 48
    },
    {
        "kanji": "塗",
        "level": 48
    },
    {
        "kanji": "斜",
        "level": 48
    },
    {
        "kanji": "殴",
        "level": 48
    },
    {
        "kanji": "盾",
        "level": 48
    },
    {
        "kanji": "穫",
        "level": 48
    },
    {
        "kanji": "巾",
        "level": 47
    },
    {
        "kanji": "駒",
        "level": 49
    },
    {
        "kanji": "紫",
        "level": 49
    },
    {
        "kanji": "抽",
        "level": 49
    },
    {
        "kanji": "誓",
        "level": 49
    },
    {
        "kanji": "悟",
        "level": 49
    },
    {
        "kanji": "拓",
        "level": 49
    },
    {
        "kanji": "拘",
        "level": 49
    },
    {
        "kanji": "礎",
        "level": 49
    },
    {
        "kanji": "鶴",
        "level": 49
    },
    {
        "kanji": "刈",
        "level": 49
    },
    {
        "kanji": "剛",
        "level": 49
    },
    {
        "kanji": "唯",
        "level": 49
    },
    {
        "kanji": "壇",
        "level": 49
    },
    {
        "kanji": "尼",
        "level": 49
    },
    {
        "kanji": "概",
        "level": 49
    },
    {
        "kanji": "浸",
        "level": 49
    },
    {
        "kanji": "淡",
        "level": 49
    },
    {
        "kanji": "煮",
        "level": 49
    },
    {
        "kanji": "覆",
        "level": 49
    },
    {
        "kanji": "謀",
        "level": 49
    },
    {
        "kanji": "陶",
        "level": 49
    },
    {
        "kanji": "隔",
        "level": 49
    },
    {
        "kanji": "征",
        "level": 49
    },
    {
        "kanji": "陛",
        "level": 49
    },
    {
        "kanji": "俗",
        "level": 49
    },
    {
        "kanji": "桑",
        "level": 49
    },
    {
        "kanji": "潤",
        "level": 49
    },
    {
        "kanji": "珠",
        "level": 49
    },
    {
        "kanji": "衰",
        "level": 49
    },
    {
        "kanji": "奨",
        "level": 49
    },
    {
        "kanji": "劣",
        "level": 49
    },
    {
        "kanji": "勘",
        "level": 49
    },
    {
        "kanji": "妃",
        "level": 49
    },
    {
        "kanji": "丈",
        "level": 15
    },
    {
        "kanji": "峰",
        "level": 50
    },
    {
        "kanji": "巧",
        "level": 50
    },
    {
        "kanji": "邪",
        "level": 50
    },
    {
        "kanji": "駄",
        "level": 50
    },
    {
        "kanji": "唐",
        "level": 50
    },
    {
        "kanji": "廷",
        "level": 50
    },
    {
        "kanji": "鬱",
        "level": 50
    },
    {
        "kanji": "鰐",
        "level": 50
    },
    {
        "kanji": "蟹",
        "level": 50
    },
    {
        "kanji": "簿",
        "level": 50
    },
    {
        "kanji": "彰",
        "level": 50
    },
    {
        "kanji": "漫",
        "level": 50
    },
    {
        "kanji": "訂",
        "level": 50
    },
    {
        "kanji": "諮",
        "level": 50
    },
    {
        "kanji": "銘",
        "level": 50
    },
    {
        "kanji": "堰",
        "level": 50
    },
    {
        "kanji": "堤",
        "level": 50
    },
    {
        "kanji": "漂",
        "level": 50
    },
    {
        "kanji": "翻",
        "level": 50
    },
    {
        "kanji": "軌",
        "level": 50
    },
    {
        "kanji": "后",
        "level": 50
    },
    {
        "kanji": "奮",
        "level": 50
    },
    {
        "kanji": "亭",
        "level": 50
    },
    {
        "kanji": "仰",
        "level": 50
    },
    {
        "kanji": "伯",
        "level": 50
    },
    {
        "kanji": "偶",
        "level": 50
    },
    {
        "kanji": "淀",
        "level": 50
    },
    {
        "kanji": "墳",
        "level": 50
    },
    {
        "kanji": "壮",
        "level": 50
    },
    {
        "kanji": "把",
        "level": 50
    },
    {
        "kanji": "搬",
        "level": 50
    },
    {
        "kanji": "晶",
        "level": 50
    },
    {
        "kanji": "洞",
        "level": 50
    },
    {
        "kanji": "涯",
        "level": 50
    },
    {
        "kanji": "疫",
        "level": 50
    },
    {
        "kanji": "孔",
        "level": 46
    },
    {
        "kanji": "偉",
        "level": 51
    },
    {
        "kanji": "頂",
        "level": 51
    },
    {
        "kanji": "召",
        "level": 51
    },
    {
        "kanji": "挟",
        "level": 51
    },
    {
        "kanji": "枯",
        "level": 51
    },
    {
        "kanji": "沸",
        "level": 51
    },
    {
        "kanji": "濯",
        "level": 51
    },
    {
        "kanji": "燥",
        "level": 51
    },
    {
        "kanji": "瓶",
        "level": 51
    },
    {
        "kanji": "耕",
        "level": 51
    },
    {
        "kanji": "肯",
        "level": 51
    },
    {
        "kanji": "脂",
        "level": 51
    },
    {
        "kanji": "膚",
        "level": 51
    },
    {
        "kanji": "軒",
        "level": 51
    },
    {
        "kanji": "軟",
        "level": 51
    },
    {
        "kanji": "郊",
        "level": 51
    },
    {
        "kanji": "隅",
        "level": 51
    },
    {
        "kanji": "隻",
        "level": 51
    },
    {
        "kanji": "邸",
        "level": 51
    },
    {
        "kanji": "郡",
        "level": 51
    },
    {
        "kanji": "釈",
        "level": 51
    },
    {
        "kanji": "肪",
        "level": 51
    },
    {
        "kanji": "喚",
        "level": 51
    },
    {
        "kanji": "媛",
        "level": 51
    },
    {
        "kanji": "貞",
        "level": 51
    },
    {
        "kanji": "玄",
        "level": 51
    },
    {
        "kanji": "苗",
        "level": 51
    },
    {
        "kanji": "渦",
        "level": 51
    },
    {
        "kanji": "慈",
        "level": 51
    },
    {
        "kanji": "襟",
        "level": 51
    },
    {
        "kanji": "蓮",
        "level": 51
    },
    {
        "kanji": "亮",
        "level": 51
    },
    {
        "kanji": "聡",
        "level": 51
    },
    {
        "kanji": "浦",
        "level": 51
    },
    {
        "kanji": "塚",
        "level": 51
    },
    {
        "kanji": "陥",
        "level": 52
    },
    {
        "kanji": "貫",
        "level": 52
    },
    {
        "kanji": "覇",
        "level": 52
    },
    {
        "kanji": "呂",
        "level": 52
    },
    {
        "kanji": "茨",
        "level": 52
    },
    {
        "kanji": "擁",
        "level": 52
    },
    {
        "kanji": "孤",
        "level": 52
    },
    {
        "kanji": "賠",
        "level": 52
    },
    {
        "kanji": "鎖",
        "level": 52
    },
    {
        "kanji": "噴",
        "level": 52
    },
    {
        "kanji": "祥",
        "level": 52
    },
    {
        "kanji": "牲",
        "level": 52
    },
    {
        "kanji": "秩",
        "level": 52
    },
    {
        "kanji": "唆",
        "level": 52
    },
    {
        "kanji": "膨",
        "level": 52
    },
    {
        "kanji": "芳",
        "level": 52
    },
    {
        "kanji": "恒",
        "level": 52
    },
    {
        "kanji": "倫",
        "level": 52
    },
    {
        "kanji": "陳",
        "level": 52
    },
    {
        "kanji": "須",
        "level": 52
    },
    {
        "kanji": "偏",
        "level": 52
    },
    {
        "kanji": "遇",
        "level": 52
    },
    {
        "kanji": "糧",
        "level": 52
    },
    {
        "kanji": "殊",
        "level": 52
    },
    {
        "kanji": "慢",
        "level": 52
    },
    {
        "kanji": "没",
        "level": 52
    },
    {
        "kanji": "怠",
        "level": 52
    },
    {
        "kanji": "遭",
        "level": 52
    },
    {
        "kanji": "惰",
        "level": 52
    },
    {
        "kanji": "猟",
        "level": 52
    },
    {
        "kanji": "乃",
        "level": 52
    },
    {
        "kanji": "綾",
        "level": 52
    },
    {
        "kanji": "颯",
        "level": 52
    },
    {
        "kanji": "隼",
        "level": 52
    },
    {
        "kanji": "輔",
        "level": 52
    },
    {
        "kanji": "寛",
        "level": 53
    },
    {
        "kanji": "胞",
        "level": 53
    },
    {
        "kanji": "浄",
        "level": 53
    },
    {
        "kanji": "随",
        "level": 53
    },
    {
        "kanji": "稿",
        "level": 53
    },
    {
        "kanji": "丹",
        "level": 53
    },
    {
        "kanji": "壌",
        "level": 53
    },
    {
        "kanji": "舗",
        "level": 53
    },
    {
        "kanji": "騰",
        "level": 53
    },
    {
        "kanji": "緯",
        "level": 53
    },
    {
        "kanji": "艇",
        "level": 53
    },
    {
        "kanji": "披",
        "level": 53
    },
    {
        "kanji": "錦",
        "level": 53
    },
    {
        "kanji": "准",
        "level": 53
    },
    {
        "kanji": "剰",
        "level": 53
    },
    {
        "kanji": "繊",
        "level": 53
    },
    {
        "kanji": "諭",
        "level": 53
    },
    {
        "kanji": "惨",
        "level": 53
    },
    {
        "kanji": "虐",
        "level": 53
    },
    {
        "kanji": "据",
        "level": 53
    },
    {
        "kanji": "徐",
        "level": 53
    },
    {
        "kanji": "搭",
        "level": 53
    },
    {
        "kanji": "蒙",
        "level": 53
    },
    {
        "kanji": "鯉",
        "level": 53
    },
    {
        "kanji": "戴",
        "level": 53
    },
    {
        "kanji": "緋",
        "level": 53
    },
    {
        "kanji": "曙",
        "level": 53
    },
    {
        "kanji": "胡",
        "level": 53
    },
    {
        "kanji": "瓜",
        "level": 53
    },
    {
        "kanji": "帥",
        "level": 53
    },
    {
        "kanji": "啓",
        "level": 53
    },
    {
        "kanji": "葵",
        "level": 53
    },
    {
        "kanji": "駿",
        "level": 53
    },
    {
        "kanji": "諒",
        "level": 53
    },
    {
        "kanji": "莉",
        "level": 53
    },
    {
        "kanji": "鯨",
        "level": 54
    },
    {
        "kanji": "荘",
        "level": 54
    },
    {
        "kanji": "栽",
        "level": 54
    },
    {
        "kanji": "拐",
        "level": 54
    },
    {
        "kanji": "冠",
        "level": 54
    },
    {
        "kanji": "勲",
        "level": 54
    },
    {
        "kanji": "酬",
        "level": 54
    },
    {
        "kanji": "紋",
        "level": 54
    },
    {
        "kanji": "卸",
        "level": 54
    },
    {
        "kanji": "欄",
        "level": 54
    },
    {
        "kanji": "逸",
        "level": 54
    },
    {
        "kanji": "尚",
        "level": 54
    },
    {
        "kanji": "顕",
        "level": 54
    },
    {
        "kanji": "粛",
        "level": 54
    },
    {
        "kanji": "愚",
        "level": 54
    },
    {
        "kanji": "庶",
        "level": 54
    },
    {
        "kanji": "践",
        "level": 54
    },
    {
        "kanji": "呈",
        "level": 54
    },
    {
        "kanji": "疎",
        "level": 54
    },
    {
        "kanji": "疾",
        "level": 54
    },
    {
        "kanji": "謡",
        "level": 54
    },
    {
        "kanji": "鎌",
        "level": 54
    },
    {
        "kanji": "酷",
        "level": 54
    },
    {
        "kanji": "叙",
        "level": 54
    },
    {
        "kanji": "且",
        "level": 54
    },
    {
        "kanji": "痴",
        "level": 54
    },
    {
        "kanji": "呆",
        "level": 54
    },
    {
        "kanji": "哺",
        "level": 54
    },
    {
        "kanji": "傲",
        "level": 54
    },
    {
        "kanji": "茎",
        "level": 54
    },
    {
        "kanji": "阿",
        "level": 54
    },
    {
        "kanji": "悠",
        "level": 54
    },
    {
        "kanji": "杏",
        "level": 54
    },
    {
        "kanji": "茜",
        "level": 54
    },
    {
        "kanji": "栞",
        "level": 54
    },
    {
        "kanji": "伏",
        "level": 55
    },
    {
        "kanji": "鎮",
        "level": 55
    },
    {
        "kanji": "奉",
        "level": 55
    },
    {
        "kanji": "憂",
        "level": 55
    },
    {
        "kanji": "朴",
        "level": 55
    },
    {
        "kanji": "栃",
        "level": 55
    },
    {
        "kanji": "惜",
        "level": 55
    },
    {
        "kanji": "佳",
        "level": 55
    },
    {
        "kanji": "悼",
        "level": 55
    },
    {
        "kanji": "該",
        "level": 55
    },
    {
        "kanji": "赴",
        "level": 55
    },
    {
        "kanji": "髄",
        "level": 55
    },
    {
        "kanji": "傍",
        "level": 55
    },
    {
        "kanji": "累",
        "level": 55
    },
    {
        "kanji": "癒",
        "level": 55
    },
    {
        "kanji": "郭",
        "level": 55
    },
    {
        "kanji": "尿",
        "level": 55
    },
    {
        "kanji": "賓",
        "level": 55
    },
    {
        "kanji": "虜",
        "level": 55
    },
    {
        "kanji": "憾",
        "level": 55
    },
    {
        "kanji": "弥",
        "level": 55
    },
    {
        "kanji": "粗",
        "level": 55
    },
    {
        "kanji": "循",
        "level": 55
    },
    {
        "kanji": "凝",
        "level": 55
    },
    {
        "kanji": "脊",
        "level": 55
    },
    {
        "kanji": "昌",
        "level": 55
    },
    {
        "kanji": "旦",
        "level": 55
    },
    {
        "kanji": "愉",
        "level": 55
    },
    {
        "kanji": "抹",
        "level": 55
    },
    {
        "kanji": "栓",
        "level": 55
    },
    {
        "kanji": "之",
        "level": 55
    },
    {
        "kanji": "龍",
        "level": 55
    },
    {
        "kanji": "遼",
        "level": 55
    },
    {
        "kanji": "瑛",
        "level": 55
    },
    {
        "kanji": "那",
        "level": 55
    },
    {
        "kanji": "拍",
        "level": 56
    },
    {
        "kanji": "猶",
        "level": 56
    },
    {
        "kanji": "宰",
        "level": 56
    },
    {
        "kanji": "寂",
        "level": 56
    },
    {
        "kanji": "縫",
        "level": 56
    },
    {
        "kanji": "呉",
        "level": 56
    },
    {
        "kanji": "凡",
        "level": 56
    },
    {
        "kanji": "恭",
        "level": 56
    },
    {
        "kanji": "錯",
        "level": 56
    },
    {
        "kanji": "穀",
        "level": 56
    },
    {
        "kanji": "陵",
        "level": 56
    },
    {
        "kanji": "弊",
        "level": 56
    },
    {
        "kanji": "舶",
        "level": 56
    },
    {
        "kanji": "窮",
        "level": 56
    },
    {
        "kanji": "悦",
        "level": 56
    },
    {
        "kanji": "縛",
        "level": 56
    },
    {
        "kanji": "轄",
        "level": 56
    },
    {
        "kanji": "弦",
        "level": 56
    },
    {
        "kanji": "窒",
        "level": 56
    },
    {
        "kanji": "洪",
        "level": 56
    },
    {
        "kanji": "摂",
        "level": 56
    },
    {
        "kanji": "飽",
        "level": 56
    },
    {
        "kanji": "紳",
        "level": 56
    },
    {
        "kanji": "庸",
        "level": 56
    },
    {
        "kanji": "靖",
        "level": 56
    },
    {
        "kanji": "嘉",
        "level": 56
    },
    {
        "kanji": "搾",
        "level": 56
    },
    {
        "kanji": "蝶",
        "level": 56
    },
    {
        "kanji": "碑",
        "level": 56
    },
    {
        "kanji": "尉",
        "level": 56
    },
    {
        "kanji": "凛",
        "level": 56
    },
    {
        "kanji": "匠",
        "level": 56
    },
    {
        "kanji": "遥",
        "level": 56
    },
    {
        "kanji": "智",
        "level": 56
    },
    {
        "kanji": "柴",
        "level": 56
    },
    {
        "kanji": "賊",
        "level": 57
    },
    {
        "kanji": "鼓",
        "level": 57
    },
    {
        "kanji": "旋",
        "level": 57
    },
    {
        "kanji": "腸",
        "level": 57
    },
    {
        "kanji": "槽",
        "level": 57
    },
    {
        "kanji": "伐",
        "level": 57
    },
    {
        "kanji": "漬",
        "level": 57
    },
    {
        "kanji": "坪",
        "level": 57
    },
    {
        "kanji": "紺",
        "level": 57
    },
    {
        "kanji": "羅",
        "level": 57
    },
    {
        "kanji": "峡",
        "level": 57
    },
    {
        "kanji": "俸",
        "level": 57
    },
    {
        "kanji": "醸",
        "level": 57
    },
    {
        "kanji": "弔",
        "level": 57
    },
    {
        "kanji": "乙",
        "level": 57
    },
    {
        "kanji": "遍",
        "level": 57
    },
    {
        "kanji": "衡",
        "level": 57
    },
    {
        "kanji": "款",
        "level": 60
    },
    {
        "kanji": "閲",
        "level": 57
    },
    {
        "kanji": "喝",
        "level": 57
    },
    {
        "kanji": "敢",
        "level": 57
    },
    {
        "kanji": "膜",
        "level": 57
    },
    {
        "kanji": "盲",
        "level": 57
    },
    {
        "kanji": "胎",
        "level": 57
    },
    {
        "kanji": "酵",
        "level": 57
    },
    {
        "kanji": "堕",
        "level": 57
    },
    {
        "kanji": "遮",
        "level": 57
    },
    {
        "kanji": "烏",
        "level": 57
    },
    {
        "kanji": "凸",
        "level": 57
    },
    {
        "kanji": "凹",
        "level": 57
    },
    {
        "kanji": "楓",
        "level": 57
    },
    {
        "kanji": "哉",
        "level": 57
    },
    {
        "kanji": "蒼",
        "level": 57
    },
    {
        "kanji": "瑠",
        "level": 58
    },
    {
        "kanji": "萌",
        "level": 57
    },
    {
        "kanji": "硫",
        "level": 58
    },
    {
        "kanji": "赦",
        "level": 58
    },
    {
        "kanji": "窃",
        "level": 58
    },
    {
        "kanji": "慨",
        "level": 58
    },
    {
        "kanji": "扶",
        "level": 58
    },
    {
        "kanji": "戯",
        "level": 58
    },
    {
        "kanji": "忌",
        "level": 59
    },
    {
        "kanji": "濁",
        "level": 58
    },
    {
        "kanji": "奔",
        "level": 58
    },
    {
        "kanji": "肖",
        "level": 58
    },
    {
        "kanji": "朽",
        "level": 58
    },
    {
        "kanji": "殻",
        "level": 58
    },
    {
        "kanji": "享",
        "level": 58
    },
    {
        "kanji": "藩",
        "level": 58
    },
    {
        "kanji": "媒",
        "level": 58
    },
    {
        "kanji": "鶏",
        "level": 58
    },
    {
        "kanji": "嘱",
        "level": 58
    },
    {
        "kanji": "迭",
        "level": 58
    },
    {
        "kanji": "椎",
        "level": 58
    },
    {
        "kanji": "絹",
        "level": 58
    },
    {
        "kanji": "陪",
        "level": 58
    },
    {
        "kanji": "剖",
        "level": 58
    },
    {
        "kanji": "譜",
        "level": 58
    },
    {
        "kanji": "淑",
        "level": 58
    },
    {
        "kanji": "帆",
        "level": 58
    },
    {
        "kanji": "憤",
        "level": 58
    },
    {
        "kanji": "酌",
        "level": 58
    },
    {
        "kanji": "暁",
        "level": 58
    },
    {
        "kanji": "傑",
        "level": 58
    },
    {
        "kanji": "錠",
        "level": 58
    },
    {
        "kanji": "凌",
        "level": 58
    },
    {
        "kanji": "瑞",
        "level": 58
    },
    {
        "kanji": "菅",
        "level": 58
    },
    {
        "kanji": "漣",
        "level": 60
    },
    {
        "kanji": "璃",
        "level": 58
    },
    {
        "kanji": "遷",
        "level": 59
    },
    {
        "kanji": "拙",
        "level": 59
    },
    {
        "kanji": "峠",
        "level": 59
    },
    {
        "kanji": "篤",
        "level": 59
    },
    {
        "kanji": "叔",
        "level": 59
    },
    {
        "kanji": "雌",
        "level": 59
    },
    {
        "kanji": "堪",
        "level": 59
    },
    {
        "kanji": "吟",
        "level": 59
    },
    {
        "kanji": "甚",
        "level": 59
    },
    {
        "kanji": "崇",
        "level": 59
    },
    {
        "kanji": "漆",
        "level": 59
    },
    {
        "kanji": "岬",
        "level": 59
    },
    {
        "kanji": "紡",
        "level": 59
    },
    {
        "kanji": "礁",
        "level": 59
    },
    {
        "kanji": "屯",
        "level": 59
    },
    {
        "kanji": "姻",
        "level": 59
    },
    {
        "kanji": "擬",
        "level": 59
    },
    {
        "kanji": "睦",
        "level": 59
    },
    {
        "kanji": "閑",
        "level": 59
    },
    {
        "kanji": "曹",
        "level": 59
    },
    {
        "kanji": "詠",
        "level": 59
    },
    {
        "kanji": "卑",
        "level": 59
    },
    {
        "kanji": "侮",
        "level": 59
    },
    {
        "kanji": "鋳",
        "level": 59
    },
    {
        "kanji": "蔑",
        "level": 59
    },
    {
        "kanji": "胆",
        "level": 59
    },
    {
        "kanji": "浪",
        "level": 59
    },
    {
        "kanji": "禍",
        "level": 59
    },
    {
        "kanji": "酪",
        "level": 59
    },
    {
        "kanji": "憧",
        "level": 59
    },
    {
        "kanji": "慶",
        "level": 59
    },
    {
        "kanji": "亜",
        "level": 59
    },
    {
        "kanji": "汰",
        "level": 59
    },
    {
        "kanji": "梓",
        "level": 59
    },
    {
        "kanji": "沙",
        "level": 59
    },
    {
        "kanji": "逝",
        "level": 60
    },
    {
        "kanji": "匿",
        "level": 60
    },
    {
        "kanji": "寡",
        "level": 60
    },
    {
        "kanji": "痢",
        "level": 60
    },
    {
        "kanji": "坑",
        "level": 60
    },
    {
        "kanji": "藍",
        "level": 60
    },
    {
        "kanji": "畔",
        "level": 60
    },
    {
        "kanji": "唄",
        "level": 60
    },
    {
        "kanji": "拷",
        "level": 60
    },
    {
        "kanji": "渓",
        "level": 60
    },
    {
        "kanji": "廉",
        "level": 60
    },
    {
        "kanji": "謹",
        "level": 60
    },
    {
        "kanji": "湧",
        "level": 60
    },
    {
        "kanji": "醜",
        "level": 60
    },
    {
        "kanji": "升",
        "level": 60
    },
    {
        "kanji": "殉",
        "level": 60
    },
    {
        "kanji": "煩",
        "level": 60
    },
    {
        "kanji": "劾",
        "level": 60
    },
    {
        "kanji": "桟",
        "level": 60
    },
    {
        "kanji": "婿",
        "level": 60
    },
    {
        "kanji": "慕",
        "level": 60
    },
    {
        "kanji": "罷",
        "level": 60
    },
    {
        "kanji": "矯",
        "level": 60
    },
    {
        "kanji": "某",
        "level": 60
    },
    {
        "kanji": "囚",
        "level": 39
    },
    {
        "kanji": "泌",
        "level": 60
    },
    {
        "kanji": "漸",
        "level": 60
    },
    {
        "kanji": "藻",
        "level": 60
    },
    {
        "kanji": "妄",
        "level": 60
    },
    {
        "kanji": "蛮",
        "level": 60
    },
    {
        "kanji": "倹",
        "level": 60
    },
    {
        "kanji": "狐",
        "level": 60
    },
    {
        "kanji": "匂",
        "level": 30
    },
    {
        "kanji": "嬉",
        "level": 40
    },
    {
        "kanji": "嘘",
        "level": 41
    },
    {
        "kanji": "串",
        "level": 37
    },
    {
        "kanji": "喉",
        "level": 18
    },
    {
        "kanji": "叩",
        "level": 18
    },
    {
        "kanji": "飴",
        "level": 18
    },
    {
        "kanji": "噂",
        "level": 33
    },
    {
        "kanji": "諦",
        "level": 22
    },
    {
        "kanji": "捉",
        "level": 25
    },
    {
        "kanji": "膝",
        "level": 38
    },
    {
        "kanji": "眉",
        "level": 37
    },
    {
        "kanji": "濡",
        "level": 30
    },
    {
        "kanji": "痩",
        "level": 34
    },
    {
        "kanji": "羨",
        "level": 21
    },
    {
        "kanji": "慌",
        "level": 49
    },
    {
        "kanji": "挨",
        "level": 44
    },
    {
        "kanji": "拶",
        "level": 44
    },
    {
        "kanji": "斤",
        "level": 5
    },
    {
        "kanji": "袖",
        "level": 22
    },
    {
        "kanji": "凄",
        "level": 41
    },
    {
        "kanji": "妖",
        "level": 40
    },
    {
        "kanji": "喋",
        "level": 35
    },
    {
        "kanji": "鮭",
        "level": 36
    },
    {
        "kanji": "宛",
        "level": 39
    },
    {
        "kanji": "蹴",
        "level": 49
    },
    {
        "kanji": "喧",
        "level": 41
    },
    {
        "kanji": "嘩",
        "level": 41
    },
    {
        "kanji": "麺",
        "level": 40
    },
    {
        "kanji": "苺",
        "level": 14
    },
    {
        "kanji": "股",
        "level": 33
    },
    {
        "kanji": "柵",
        "level": 30
    },
    {
        "kanji": "噛",
        "level": 38
    },
    {
        "kanji": "狼",
        "level": 14
    },
    {
        "kanji": "咳",
        "level": 34
    },
    {
        "kanji": "拉",
        "level": 40
    },
    {
        "kanji": "苛",
        "level": 18
    },
    {
        "kanji": "煎",
        "level": 47
    },
    {
        "kanji": "戚",
        "level": 35
    },
    {
        "kanji": "餅",
        "level": 42
    },
    {
        "kanji": "屁",
        "level": 33
    },
    {
        "kanji": "璧",
        "level": 38
    },
    {
        "kanji": "痒",
        "level": 23
    },
    {
        "kanji": "冥",
        "level": 60
    },
    {
        "kanji": "莫",
        "level": 25
    },
    {
        "kanji": "頁",
        "level": 10
    },
    {
        "kanji": "勿",
        "level": 55
    }
]
'''

data = json.loads(json_data)

# Insert data into the table
for entry in data:
    cursor.execute("INSERT INTO kanji_data (kanji, level) VALUES (%s, %s)", (entry["kanji"], entry["level"]))

# Commit changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()