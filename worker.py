__author__ = 'Felipe Parpinelli'

import sched
import time

s = sched.scheduler(time.time, time.sleep)


def update_gh_stars(sc):
    print "worker..."

    # do your stuff
    sc.enter(60, 1, update_gh_stars, (sc,))


def run():
    s.enter(1, 1, update_gh_stars, (s,))
    s.run()


def run_worker(environ, start_response):
    data = "Booting worker ...\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    run()
    return iter([data])

