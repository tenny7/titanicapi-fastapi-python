
from   pymongo         import MongoClient
# from dotenv import load_dotenv, find_dotenv
''' 
Connect to Mongo DB using Mongo Client
'''


# load_dotenv(find_dotenv())
# {os.getenv('usr_password')}
mongo_conn_string = f"mongodb+srv://tennyson:tennyson1@cluster0.hzc91.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&uuidRepresentation=standard"
client = MongoClient(mongo_conn_string)
database = client['titanicdb']
