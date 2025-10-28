""" if you wanrt to modify tuple converet it into list"""


t=('python','java','flutter')
print(t)

sub_list=list(t)

sub_list.append('da-ds')

t=tuple(sub_list)

print(t)