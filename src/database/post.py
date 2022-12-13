from src.models import db, Post as PostModel, Community


class Post:

    #Gets all the posts regarding to the community_name 
    def get_posts(self, community_name) -> list[PostModel]:
        posts = PostModel.query.join(Community, PostModel.community_id == Community.community_id).filter(Community.community_name == community_name).all()
        return posts

    def get_post(self, post_id): 
        post = PostModel.query.filter(PostModel.post_id == post_id).first()
        return post 

    def get_four_posts(self): 
        recent_posts = PostModel.query.order_by(PostModel.post_id.desc()).limit(4).all()
        return recent_posts

        # TODO: Add more methods to the post. Delete when done
    def create_post(self, title, author, content, community_name, community_id, account_id): 
        post = PostModel(title, author, content, community_name, community_id, account_id) 
        db.session.add(post)
        db.session.commit()

    def update_post(self, post, description):
        post.description = description
        db.session.commit()

    def delete_post(self, post):
        db.session.delete(post)
        db.session.commit()


post = Post()
