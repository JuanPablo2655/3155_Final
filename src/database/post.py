from src.models import db, Post as PostModel, Community

class Post: 

    #Gets a comment from the community database. Still need to get the community w it. 
    def get_post(title, community_id): 
        post = PostModel.filter(title=title).filter(community_id=community_id)
        return post

        #TODO: Add more methods to the post. Delete when done 





post = Post() 