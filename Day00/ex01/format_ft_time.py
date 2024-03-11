from time import time, gmtime, strftime

current_time = gmtime()

total_sec = time()

print(f'Seconds since January 1, 1970: {total_sec} or {total_sec:.2} in \
        scientific notation')

print(strftime('%b %d %Y', current_time))
