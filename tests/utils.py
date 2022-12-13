from src.models import Community, Post, Comment, db

def refresh_db():
    Comment.query.delete()
    Post.query.delete()
    Community.query.delete()
    db.session.commit()
    
def create_community(name = 'Fortnite', description = 'Super awesome epic game I love Fortnite!')-> Community:
    test_community = Community(community_name = name, description = description)
    db.session.add(test_community)
    db.session.commit()
    return test_community