from src.models import db, Comment as CommentModel


class Comment:

    # Gets a comment from the community database
    def get_comment(self, comment_id):
        comment = CommentModel.query.filter_by(comment_id=comment_id).first()
        return comment

    def create_comment(self, title: str, author: str, content: str, date_posted: str, votes: str, post_id: int, account_id: int):
        comment = CommentModel(title, author, content,
                               date_posted, votes, post_id, account_id)
        db.session.add(comment)
        db.session.commit()

    def update_comment(self, comment, content):
        comment.content = content
        db.session.commit()

    def delete_comment(self, comment):
        db.session.delete(comment)
        db.session.commit()


comment = Comment()
