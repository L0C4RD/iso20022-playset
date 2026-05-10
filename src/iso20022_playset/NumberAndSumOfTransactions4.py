from . import base_types
import AmountAndDirection35
import DecimalNumber
import Max15NumericText

class NumberAndSumOfTransactions4(base_types._BaseFieldType):

	__slots__ = ["_TtlNetNtry", "_Sum", "_NbOfNtries"]
	@property
	def TtlNetNtry(self):
		return self._TtlNetNtry

	@TtlNetNtry.setter
	def TtlNetNtry(self, value):
		self._TtlNetNtry = value if type(value) != auto else self.make_default("TtlNetNtry")

	@TtlNetNtry.deleter
	def TtlNetNtry(self):
		del self._TtlNetNtry
		self._TtlNetNtry = None

	@property
	def Sum(self):
		return self._Sum

	@Sum.setter
	def Sum(self, value):
		self._Sum = value if type(value) != auto else self.make_default("Sum")

	@Sum.deleter
	def Sum(self):
		del self._Sum
		self._Sum = None

	@property
	def NbOfNtries(self):
		return self._NbOfNtries

	@NbOfNtries.setter
	def NbOfNtries(self, value):
		self._NbOfNtries = value if type(value) != auto else self.make_default("NbOfNtries")

	@NbOfNtries.deleter
	def NbOfNtries(self):
		del self._NbOfNtries
		self._NbOfNtries = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlNetNtry', type=AmountAndDirection35, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfNtries', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
	))

