# app/models/admin.py
class Admin:
  def __init__(self, admin_id, first_name, last_name, email, phone_number, position, permissions, username, password, role):
      self.admin_id = admin_id
      self.first_name = first_name
      self.last_name = last_name
      self.email = email
      self.phone_number = phone_number
      self.position = position
      self.permissions = permissions
      self.username = username
      self.password = password
      self.role = role

  def to_dict(self):
      return self.__dict__
