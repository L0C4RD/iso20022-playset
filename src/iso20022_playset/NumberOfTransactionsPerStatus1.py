from . import base_types
from .TransactionIndividualStatus1Code import TransactionIndividualStatus1Code
from .DecimalNumber import DecimalNumber
from .Max15NumericText import Max15NumericText

class NumberOfTransactionsPerStatus1(base_types._BaseFieldType):

	__slots__ = ["_DtldNbOfTxs", "_DtldCtrlSum", "_DtldSts"]
	@property
	def DtldNbOfTxs(self):
		return self._DtldNbOfTxs

	@DtldNbOfTxs.setter
	def DtldNbOfTxs(self, value):
		self._DtldNbOfTxs = value if type(value) != base_types.auto else self.make_default("DtldNbOfTxs")

	@DtldNbOfTxs.deleter
	def DtldNbOfTxs(self):
		del self._DtldNbOfTxs
		self._DtldNbOfTxs = None

	@property
	def DtldCtrlSum(self):
		return self._DtldCtrlSum

	@DtldCtrlSum.setter
	def DtldCtrlSum(self, value):
		self._DtldCtrlSum = value if type(value) != base_types.auto else self.make_default("DtldCtrlSum")

	@DtldCtrlSum.deleter
	def DtldCtrlSum(self):
		del self._DtldCtrlSum
		self._DtldCtrlSum = None

	@property
	def DtldSts(self):
		return self._DtldSts

	@DtldSts.setter
	def DtldSts(self, value):
		self._DtldSts = value if type(value) != base_types.auto else self.make_default("DtldSts")

	@DtldSts.deleter
	def DtldSts(self):
		del self._DtldSts
		self._DtldSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldNbOfTxs', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldCtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldSts', type=TransactionIndividualStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))

