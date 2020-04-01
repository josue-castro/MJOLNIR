import os
import unittest
import json
from main import app
from tests.newUserData import newUser

class TestUserRoutes(unittest.TestCase):
  # executed prior to each test
  def setUp(self):
      app.config['DEBUG'] = True
      self.data = newUser
      self.client = app.test_client()

  ######################################
  #-------- Resetting Password --------#
  ######################################

  def test_reset_password(self):
    response = self.client.patch('/users/48/reset', data=json.dumps({'password' : 'newPaswordlololol'}), content_type='application/json',  follow_redirects=True)
    self.assertEqual(response.status_code, 201)
    self.assertEqual(response.json['User']['email'], self.data['email'])
    self.assertEqual(response.json['User']['full_name'], self.data['full_name'])
    self.assertEqual(response.json['User']['id'], 48)
    self.assertEqual(response.json['User']['is_active'], False)
    self.assertEqual(response.json['User']['is_invalid'], False)
    self.assertEqual(response.json['User']['username'], self.data['username'])