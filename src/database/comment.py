from src.models import db, Comment as CommentModel, Post


class Comment:

    # Gets a comment from the post 
    def get_all_comment_from_post(self, post_id) -> list[CommentModel]: 
        all_comments = CommentModel.query.join(Post, CommentModel.post_id == Post.post_id).filter(Post.post_id == post_id).all()
        return all_comments 

    #Get a single comment from the database
    def get_comment(self, comment_id):
        comment = CommentModel.query.filter_by(comment_id=comment_id).first()
        return comment
    
    def create_new_comment(self, author, content, post_id, account_id): 
        new_comment = CommentModel(author, content, post_id, account_id)
        db.session.add(new_comment)
        db.session.commit()



    def update_comment(self, comment, content):
        comment.content = content
        db.session.commit()

    def delete_comment(self, comment):
        db.session.delete(comment)
        db.session.commit()


comment = Comment()
