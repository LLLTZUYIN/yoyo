import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
  "title": "小王子【70周年精裝紀念版】",
  "author": "安東尼‧聖修伯里",
  "cover": "https://www.books.com.tw/img/001/066/04/0010660414.jpg",
  "url": "https://www.books.com.tw/products/0010660414",
  "anniversary": 70
},

{
  "title": "最後14堂星期二的課【20週年紀念版】",
  "author": "米奇‧艾爾邦",
  "cover": "https://www.books.com.tw/img/001/079/06/0010790676.jpg",
  "url": "https://www.books.com.tw/products/0010790676",
  "anniversary": 20
},

{
  "title": "撒哈拉歲月【三毛逝世30週年紀念版】",
  "author": "三毛",
  "cover": "https://www.books.com.tw/img/001/089/77/0010897794.jpg",
  "url": "https://www.books.com.tw/products/0010897794",
  "anniversary": 30
},

{
  "title": "靜宜求學趣",
  "author": "林姿穎",
  "cover": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.chinatimes.com%2Fnewsphoto%2F2020-07-31%2F1024%2F20200731002175.jpg&tbnid=um05D7S9GiIs_M&vet=12ahUKEwiJ-rDPscKCAxVBU_UHHRJjD0wQMygHegQIARB8..i&imgrefurl=https%3A%2F%2Fwww.chinatimes.com%2Fhottopic%2F20200731002166-260804&docid=1uc3wOTyRQJB1M&w=1024&h=683&q=%E8%96%A9%E6%91%A9%E8%80%B6&ved=2ahUKEwiJ-rDPscKCAxVBU_UHHRJjD0wQMygHegQIARB8",
  "url": "https://oomis-ltys-projects.vercel.app/",
  "anniversary": 19
}

]

collection_ref = db.collection("圖書精選")
for doc in docs:
  collection_ref.add(doc)