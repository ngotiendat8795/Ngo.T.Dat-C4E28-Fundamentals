from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_database()

posts = db["posts"]

new_post = {
    'title':'DATNT - Bâng Khuâng Trời Rộng Nhớ Sông Dài',
    'author': 'Huy Cận',
    'content': "Lơ thơ cồn cỏ gió đìu hiu. Đâu tiếng làng xa vãn chợ chiểu. Nắng xuống trời lên sâu chót vót. Sông dài trời rộng bến cô liêu."
}


posts.insert_one(new_post)
