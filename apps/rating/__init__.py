from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from apps.people.models import Teacher

from models import Rating, GlobalRating


def _update_global_rating(rating):
    """ Update teacher global rating

        Args:
            rating (Rating):  Rating object.

        Raises:
            Teacher.DoesNotExist

    """

    global_rating, created = GlobalRating.objects.get_or_create(teacher=rating.teacher)

    global_rating.total_evil_value += rating.evil_value
    global_rating.total_easier_value += rating.easier_value
    global_rating.total_vague_value += rating.vague_value
    global_rating.total_brainy_value += rating.brainy_value

    global_rating.calculate_raking()
    global_rating.save()


@transaction.atomic
def make_rate(teacher_id, **values):
    """ Perform the teacher rate

        Args:
            teacher_id (int):  Teacher id.
            user_id (int):  User id.

        Kwargs:
            values (list):  Values of rating of evil, easier, vague and brainy kinds.

        Raises:
            ObjectDoesNotExist

    """
    try:
        rating = Rating(teacher=Teacher.objects.get(pk=teacher_id),
                        evil_value=values['evil_value'], easier_value=values['easier_value'],
                        vague_value=values['vague_value'], brainy_value=values['brainy_value'])
        rating.save()

        _update_global_rating(rating)

    except (Teacher.DoesNotExist, User.DoesNotExist) as e:
        raise ObjectDoesNotExist(e.message)


