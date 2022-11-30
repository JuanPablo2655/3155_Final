from src.models import db, Post as PostModel 

class Post: 

    #Gets a comment from the community database. Still need to get the community w it. 
    def get_post(title, community): 
        comment = PostModel.query.filter_by(title=title).first()
        return comment

        #TODO: Add more methods to the post. Delete when done 





post = Post() 