import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
	"""Тесты для класса AnonymousSurvey"""
	def setUp(self):
		"""Создание опроса и набора ответов для всех тестовых методов."""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']

	def test_store_single_response(self):
		"""Проверяет, что один ответ сохранен правильно."""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""Проверяет, что три ответа были сохранены правильно."""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)
unittest.main()
