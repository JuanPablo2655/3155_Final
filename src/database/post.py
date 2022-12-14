from src.models import db, Post as PostModel, Community


class Post:


    def get_posts(self, community_name) -> list[PostModel]:
        """
        Gets a post by community name from the database.
        """
        posts = PostModel.query.join(Community, PostModel.community_id == Community.community_id).filter(Community.community_name == community_name).all()
        return posts

    def get_post(self, post_id): 
        """
        Gets a specific post by post id from the database.
        """
        post = PostModel.query.filter(PostModel.post_id == post_id).first()
        return post 

    def get_four_posts(self): 
        """
        Gets the four most recent posts from the database.
        """
        recent_posts = PostModel.query.order_by(PostModel.post_id.desc()).limit(4).all()
        return recent_posts

    def create_post(self, title, author, content, community_name, community_id, account_id): 
        """
        Creates a new post to the database.
        """
        post = PostModel(title, author, content, community_name, community_id, account_id) 
        db.session.add(post)
        db.session.commit()

    # TODO: Finish the update_post function
    def update_post(self, post, title, content):
        post.title = title
        post.content = content
        db.session.commit()

    def delete_post(self, post):
        """
        Deletes a post from the database.
        """
        db.session.delete(post)
        db.session.commit()


post = Post()
