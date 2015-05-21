from celery import Celery
import stackexchange

app = Celery('se')
app.config_from_object('celeryconfig')

@app.task(serilizer='json')
def se_search(site,query):
    try:
       cse = stackexchange.Site(site, None)
       return [value.title for value in cse.search(intitle=query[0])]
    except:
        return

@app.task(serializer='json')
def se_recent(site):
    try:
       cse = stackexchange.Site(site, None)
       questions = cse.recent_questions(pagesize=20, filter='_b')
       return [value.title for value in questions]
    except:
        return


@app.task(serializer='json')
def se_user(site, idvalue):
    try:
        cse = stackexchange.Site(site, None)
        user = cse.user(idbalue)
        return {'result': user}
    except:
        return

