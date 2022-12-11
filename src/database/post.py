from src.models import db, Post as PostModel, Community


class Post:

    # Gets a comment from the community database. Still need to get the community w it.
    def get_post(title, community_id):
        post = PostModel.filter(title=title).filter(community_id=community_id)
        return post

        # TODO: Add more methods to the post. Delete when done
    def create_post(title: str, author: str, content: str, account_id: int, community_id: int):
        post = PostModel(title, author, content,
                        account_id, community_id)
        db.session.add(post)
        db.session.commit()

    def update_post(post, description):
        post.description = description
        db.session.commit()

    def delete_post(post):
        db.session.delete(post)
        db.session.commit()


post = Post()
