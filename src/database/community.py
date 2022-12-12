from src.models import db, Community as CommunityModel


class Community:

    #Gets all communities
    def get_all_communities(self) -> list[CommunityModel]:
        communities: list[CommunityModel] = CommunityModel.query.all()
        return communities

    # Gets a community from the community database
    def get_community(self, community_name: str):
        get_comm = CommunityModel.query.filter_by(
        community_name=community_name).first()
        return get_comm

    def check_community(self, community_name):
        community_object = CommunityModel.query.filter_by(community_name=community_name).first()
        return community_object

    # Creates a new community
    def create_community(self, community_title: str, description: str):
        new_community = CommunityModel(community_title, description)
        db.session.add(new_community)
        db.session.commit()

    # Update a community description in the database
    def update_community(self, community: str, description: str):
        community.description = description
        db.session.commit()

    # Deletes a community from the database
    def delete_community(self, community):
        db.session.delete(community)
        db.session.commit()


community = Community()
