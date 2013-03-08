import multiprocessing
import os


PORT = os.getenv("PORT", 8000)

bind = "0.0.0.0:{port}".format(port=PORT)
workers = multiprocessing.cpu_count() * 2 + 1
