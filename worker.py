__author__ = 'Felipe Parpinelli'

import sched
import time
import coderep
import history
from providers import github_resources
from providers import stackoverflow_resouces

s = sched.scheduler(time.time, time.sleep)


def update_values(sc):
    print "worker..."
    github_resources.update_stars()
    stackoverflow_resouces.update_tags()
    coderep.update_rep()

    history.set_history()

    # 43200 seconds == 12 hours
    sc.enter(43200, 1, update_values, (sc,))


def run():
    s.enter(1, 1, update_values, (s,))
    s.run()


def run_worker(environ, start_response):
    data = "Booting worker ...\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    run()
    return iter([data])

