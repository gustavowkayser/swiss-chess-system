from app.classes import Rating

class RatingDTO:
    def __init__(self):
        pass

    @staticmethod
    def to_dict(rating: Rating) -> dict:
        return {
            'rating_classico': rating.rating_classico,
            'rating_rapido': rating.rating_rapido,
            'rating_blitz': rating.rating_blitz
        }