from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._TrueFalseIndicator import TrueFalseIndicator

class PaymentConditionStatus2(base_types._BaseFieldType):

	__slots__ = ["_GrntedPmt", "_EarlyPmt", "_AccptdAmt"]
	@property
	def GrntedPmt(self):
		return self._GrntedPmt

	@GrntedPmt.setter
	def GrntedPmt(self, value):
		self._GrntedPmt = value if type(value) != base_types.auto else self.make_default("GrntedPmt")

	@GrntedPmt.deleter
	def GrntedPmt(self):
		del self._GrntedPmt
		self._GrntedPmt = None

	@property
	def EarlyPmt(self):
		return self._EarlyPmt

	@EarlyPmt.setter
	def EarlyPmt(self, value):
		self._EarlyPmt = value if type(value) != base_types.auto else self.make_default("EarlyPmt")

	@EarlyPmt.deleter
	def EarlyPmt(self):
		del self._EarlyPmt
		self._EarlyPmt = None

	@property
	def AccptdAmt(self):
		return self._AccptdAmt

	@AccptdAmt.setter
	def AccptdAmt(self, value):
		self._AccptdAmt = value if type(value) != base_types.auto else self.make_default("AccptdAmt")

	@AccptdAmt.deleter
	def AccptdAmt(self):
		del self._AccptdAmt
		self._AccptdAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrntedPmt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyPmt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

