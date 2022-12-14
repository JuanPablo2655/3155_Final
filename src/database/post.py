from src.models import db, Post as PostModel, Community


class Post:

    # Gets all the posts regarding to the slug
    def get_posts(self, slug) -> list[PostModel]:
        posts = PostModel.query.join(Community, PostModel.community_id == Community.community_id).filter(
            Community.slug == slug).all()
        return posts

    def get_post(self, post_id):
        post = PostModel.query.filter(PostModel.post_id == post_id).first()
        return post

    def check_post(self, title):
        post = PostModel.query.filter(PostModel.title == title).first()
        return post
        
    def get_four_posts(self):
        recent_posts = PostModel.query.order_by(
            PostModel.post_id.desc()).limit(4).all()
        return recent_posts

        # TODO: Add more methods to the post. Delete when done
    def create_post(self, title, author, content, community_slug, community_name, community_id, account_id):
        post = PostModel(title, author, content,
                         community_slug, community_name, community_id, account_id)
        db.session.add(post)
        db.session.commit()

    def update_post(self, post, title, content):
        post.title = title
        post.content = content
        db.session.commit()

    def delete_post(self, post):
        db.session.delete(post)
        db.session.commit()


post = Post()
