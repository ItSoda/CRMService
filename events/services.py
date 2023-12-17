from django.shortcuts import get_object_or_404

from events.models import Events, Teams
from users.models import Users
from django.db.models import BooleanField, ExpressionWrapper, F, Value

def get_event(event_id):
    event = get_object_or_404(Events, id=event_id)
    return event


# add participants
def user_update_participation(user_id, event_id):
    user = get_object_or_404(Users, id=user_id)
    event = get_event(event_id=event_id)
    if not event.participian.filter(id=user_id).exists():
        user.participation = user.participation + 1
        user.save()


def event_update_participation(user_id, event_id):
    event = get_event(event_id=event_id)
    event.participian.add(user_id)
    event.save()

    return event


# add wins
def user_update_winner(user_id, event_id):
    user = get_object_or_404(Users, id=user_id)
    event = get_event(event_id=event_id)
    if not event.winners.filter(id=user_id).exists():
        user.wins = user.wins + 1
        user.save()


def event_update_winner(user_id, event_id):
    event = get_event(event_id=event_id)
    event.winners.add(user_id)
    event.save()

    return event


def user_update_create_event(user):
    user.create_event = user.create_event + 1
    user.save()


def fetch_team(user_id):
    try:
        user = Users.objects.get(id=user_id)
        teams = Teams.objects.all()
        for team in teams:
            if user in team.members.all():
                return team
    except Teams.DoesNotExist:
        return None
