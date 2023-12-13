from model import Todo

#most of the code here is in mongodb
# this is the mongodb driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.TodoList
collection = database.todo


#fectches one title from function in the models and main 
async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(title, desc):
    await collection.update_one({"title":title},{"$set":{
        "description":desc}})
    #set a document to find the title with new title and return it
    document = await collection.find_one({"title":title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True