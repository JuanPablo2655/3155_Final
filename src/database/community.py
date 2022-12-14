from src.models import db, Community as CommunityModel


class Community:

    # Gets all communities
    def get_all_communities(self) -> list[CommunityModel]:
        communities: list[CommunityModel] = CommunityModel.query.all()
        return communities

    # Gets a community from the community database
    def get_community(self, slug: str):
        get_comm = CommunityModel.query.filter_by(
            slug=slug).first()
        return get_comm

    def check_community(self, slug):
        community_object = CommunityModel.query.filter_by(
            slug=slug).first()
        return community_object

    # Creates a new community
    def create_community(self, slug: str, community_title: str, description: str, account_id: int):
        new_community = CommunityModel(
            slug, community_title, description, account_id)
        db.session.add(new_community)
        db.session.commit()

    # Update a community description in the database
    def update_community(self, community, description: str):
        community.description = description
        db.session.commit()

    # Deletes a community from the database
    def delete_community(self, community):
        db.session.delete(community)
        db.session.commit()


community = Community()
