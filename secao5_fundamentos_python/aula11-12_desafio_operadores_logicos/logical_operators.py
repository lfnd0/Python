work_tuesday = True
work_wednesday = True

TV_50 = work_tuesday and work_wednesday
TV_32 = work_tuesday != work_wednesday
icecream = work_tuesday or work_wednesday
more_health = not icecream

print('TV 50 = {}, TV 32 = {}, Icecream = {}, Healthy = {}'.format(
    TV_50, TV_32, icecream, more_health))
