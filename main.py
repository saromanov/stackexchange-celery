from celery.task.sets import TaskSet
from celery import group
from tasks import se_search, se_recent,se_user
import stackexchange

sets = TaskSet(tasks=[se_search.subtask(args=(stackexchange.SeasonedAdvice, "fish",)),
                      se_search.subtask(args=(stackexchange.SeasonedAdvice,"scones",)),
                      se_recent.subtask(args=(stackexchange.UnixampLinux,),),
                      se_user.subtask(args=(stackexchange.StackOverflow, 12345),)
                      ])
result = sets.apply_async()
isready = result.ready()
print(result.join())

