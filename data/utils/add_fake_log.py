"""Adds fake entries to the action log."""

import header
import debate.models as m
from action_log.models import ActionLog
from motions.models import Motion
from draws.models import Debate
from feedback.models import AdjudicatorFeedback

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import argparse
parser = argparse.ArgumentParser(description=__doc__)
parser.parse_args()

AL = ActionLog

def log(*args, **kwargs):
    action = ActionLog(*args, **kwargs)
    try:
        action.full_clean()
    except ValidationError, e:
        print str(e)
        return
    action.save()

def get_user(username):
    return User.objects.get(username=username)

def get_debate(id):
    return Debate.objects.get(id=id)

def get_adjudicator_feedback(id):
    return AdjudicatorFeedback.objects.get(id=id)

def get_motion(id):
    return Motion.objects.get(id=id)

#log(type=AL.ACTION_TYPE_BALLOT_CHECKIN, user=get_user('czlee1'))
#log(type=AL.ACTION_TYPE_BALLOT_CHECKIN, user=get_user('czlee1'), debate=get_debate(145))
#log(type=AL.ACTION_TYPE_DRAW_CONFIRM, user=get_user('czlee1'), debate=get_debate(145))
#log(type=AL.ACTION_TYPE_FEEDBACK_SUBMIT, user=get_user('czlee1'), debate=get_debate(145))
log(type=AL.ACTION_TYPE_FEEDBACK_SUBMIT, user=get_user('notsuper'), adjudicator_feedback=get_adjudicator_feedback(100))
log(type=AL.ACTION_TYPE_FEEDBACK_SAVE, user=get_user('notsuper'), adjudicator_feedback=get_adjudicator_feedback(138))
log(type=AL.ACTION_TYPE_MOTION_EDIT, user=get_user('ravi'), motion=get_motion(43))

for al in ActionLog.objects.all():
    print repr(al)