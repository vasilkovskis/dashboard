# utils.py
def is_admin(session):
    return session.get('user_role') == 'admin'

def is_editor(session):
    return session.get('user_role') == 'editor'

def is_viewer(session):
    return session.get('user_role') == 'viewer'
