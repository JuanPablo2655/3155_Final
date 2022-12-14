from src.models import Community, Post, Comment, Account, db


def refresh_db():
    Comment.query.delete()
    Post.query.delete()
    Community.query.delete()
    db.session.commit()


def create_community(name='Fortnite', description='Super awesome epic game I love Fortnite!') -> Community:
    test_community = Community(community_name=name, description=description)
    db.session.add(test_community)
    db.session.commit()
    return test_community

def create_user(user_name='xxflash', full_name='Barry Allen', gaming_password = 'Flash01', email = 'bAllen@gmail.com') -> Account:
    test_user = Account(user_name=user_name, full_name=full_name, gaming_password = gaming_password, email = email)
    db.session.add(test_user)
    db.session.commit()
    return test_user

def create_post(title = 'Fortnite C4', author = 'xxflash', content = 'I love this season', community_name = 'Fortnite', community_id:int =1, account_id:int = 1) -> Post:
    test_post = Post(title = title, author = author, content = content, community_name = community_name, community_id= community_id, account_id = account_id)
    db.session.add(test_post)
    db.session.commit()
    return test_post
