from celery.task.sets import TaskSet
from tasks import se_search, se_recent
import stackexchange

sets = TaskSet(tasks=[se_search.subtask(args=(stackexchange.SeasonedAdvice, "fish",)),
                      se_search.subtask(args=(stackexchange.SeasonedAdvice,"scones",)),
                      se_recent.subtask(args=(stackexchange.UnixampLinux,))
                      ])
result = sets.apply_async()
isready = result.ready()
print(result.join())

