# -*- coding: utf-8 -*-
# Want to sort objects of the same class,
# but they don't support comparison operations
from operator import attrgetter


class UserName(object):
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return 'UserName({0}~{1}~{2})'.format(self.user_id,
                                              self.first_name,
                                              self.last_name)


class User(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "User({})".format(self.user_id)


users = [User(23), User(3), User(99)]
print users
users = sorted(users, key=lambda u: u.user_id)
print users

# Also can use operator.attrgetter()
n_users = [UserName(2, 'zhang', 'lu'), UserName(1, 'zhao', 'lingpu'),
           UserName(5, 'an', 'quan'), UserName(3, 'ce', 'shi')]
sort_users = sorted(n_users, key=attrgetter('user_id'))
min_user = min(n_users, key=attrgetter('user_id'))
max_user = max(n_users, key=attrgetter('user_id'))
by_name = sorted(n_users,
                 key=attrgetter('last_name', 'first_name'),
                 reverse=True)
print sort_users
print min_user
print max_user
print by_name
