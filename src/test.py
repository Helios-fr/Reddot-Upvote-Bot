import colorama

post_ids = None
comment = False

if post_ids == None: post_ids = input(colorama.Fore.MAGENTA + "Post ID's (separated by ', '): ").strip()
post_ids = post_ids.split(', ')
new = []
for post_id in post_ids:
    if comment == False:
        if post_id.startswith('t3_'): post_id = post_id[3:]
        post_id = 't3_' + post_id
        new.append(post_id)
    else:
        if post_id.startswith('t1_'): post_id = post_id[3:]
        post_id = 't1_' + post_id
        new.append(post_id)
post_ids = new

print(post_ids)

