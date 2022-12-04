from src.models import db, Comment as CommentModel 

class Comment: 

    #Gets a comment from the community database 
    def get_comment(comment_id): 
        comment = CommentModel.query.filter_by(comment_id=comment_id).first()
        return comment
    
    def create_comment(author, date_posted, content, post_id, account_id): 
        comment = CommentModel(author=author, date_posted=date_posted, content=content, post_id=post_id, account_id=account_id)
        db.session.add(comment)
        db.session.commit()

    def update_comment(comment, content):
        comment.content = content 
        db.session.commit() 

    def delete_comment(comment): 
        db.session.delete(comment) 
        db.session.commit()


comment = Comment() 

