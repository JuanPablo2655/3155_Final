from src.models import db, Community as CommunityModel

class Community: 
    #Gets a community from the community database 
    def get_community(community_name): 
        community = CommunityModel.query.filter_by(community_name=community_name).first()
        return community 

    #Creates a new community
    def create_community(community_name, description): 
        new_community = CommunityModel(community_name=community_name, description=description)
        db.session.add(new_community)
        db.session.commit()

    #Update a community description in the database
    def update_community(community, description): 
        community.description = description
        db.session.commit() 
    
    #Deletes a community from the database 
    def delete_community(community): 
        db.session.delete(community)
        db.session.commit()
        community = Community()
    
