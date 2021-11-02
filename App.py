runtime = 'development'

if runtime == 'development':
    # Run Development files
    from development.classes.Start import start
    start()
elif runtime == 'production':
    # Run Production files
    from production.classes.Start import start
    start()
else:
    pass


# Testing with F241.06.15-2960X
# telnet://F241-06-15-COMM:2029
# https://autopods.cisco.com/pod/790
