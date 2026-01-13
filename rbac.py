def check_role(u,r):
    if u['role']!=r: raise Exception('Denied')
