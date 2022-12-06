from admin_module import Admin

anakin_skyworker = Admin('Anakin', 'Skyworker')
anakin_skyworker.privilegies.privilegies = ['can add post', 'can edit post', 'can delete post', 'can be a Dart Wader']

anakin_skyworker.create_user()
anakin_skyworker.privilegies.show_privilegies()