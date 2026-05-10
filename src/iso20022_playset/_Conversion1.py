from . import base_types
from ._AdditionalInformation15 import AdditionalInformation15
from ._FinancialInstrumentIdentification1 import FinancialInstrumentIdentification1

class Conversion1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_TrgtScty"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def TrgtScty(self):
		return self._TrgtScty

	@TrgtScty.setter
	def TrgtScty(self, value):
		self._TrgtScty = value if type(value) != base_types.auto else self.make_default("TrgtScty")

	@TrgtScty.deleter
	def TrgtScty(self):
		del self._TrgtScty
		self._TrgtScty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrgtScty', type=FinancialInstrumentIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

