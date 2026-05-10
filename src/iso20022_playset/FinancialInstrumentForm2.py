import base_types
import Appearance3Choice
import FormOfSecurity8Choice

class FinancialInstrumentForm2(base_types._BaseFieldType):

	__slots__ = ["_BookgApprnc", "_LglForm"]
	@property
	def BookgApprnc(self):
		return self._BookgApprnc

	@BookgApprnc.setter
	def BookgApprnc(self, value):
		self._BookgApprnc = value if type(value) != auto else self.make_default("BookgApprnc")

	@BookgApprnc.deleter
	def BookgApprnc(self):
		del self._BookgApprnc
		self._BookgApprnc = None

	@property
	def LglForm(self):
		return self._LglForm

	@LglForm.setter
	def LglForm(self, value):
		self._LglForm = value if type(value) != auto else self.make_default("LglForm")

	@LglForm.deleter
	def LglForm(self):
		del self._LglForm
		self._LglForm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BookgApprnc', type=Appearance3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglForm', type=FormOfSecurity8Choice, min=0, max=1, mutex_group=None, array=False),
	))

