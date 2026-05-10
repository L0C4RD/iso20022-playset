from . import base_types
from .Max15NumericText import Max15NumericText
from .DecimalNumber import DecimalNumber
from .CancellationIndividualStatus1Code import CancellationIndividualStatus1Code

class NumberOfCancellationsPerStatus1(base_types._BaseFieldType):

	__slots__ = ["_DtldSts", "_DtldNbOfTxs", "_DtldCtrlSum"]
	@property
	def DtldSts(self):
		return self._DtldSts

	@DtldSts.setter
	def DtldSts(self, value):
		self._DtldSts = value if type(value) != auto else self.make_default("DtldSts")

	@DtldSts.deleter
	def DtldSts(self):
		del self._DtldSts
		self._DtldSts = None

	@property
	def DtldNbOfTxs(self):
		return self._DtldNbOfTxs

	@DtldNbOfTxs.setter
	def DtldNbOfTxs(self, value):
		self._DtldNbOfTxs = value if type(value) != auto else self.make_default("DtldNbOfTxs")

	@DtldNbOfTxs.deleter
	def DtldNbOfTxs(self):
		del self._DtldNbOfTxs
		self._DtldNbOfTxs = None

	@property
	def DtldCtrlSum(self):
		return self._DtldCtrlSum

	@DtldCtrlSum.setter
	def DtldCtrlSum(self, value):
		self._DtldCtrlSum = value if type(value) != auto else self.make_default("DtldCtrlSum")

	@DtldCtrlSum.deleter
	def DtldCtrlSum(self):
		del self._DtldCtrlSum
		self._DtldCtrlSum = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldSts', type=CancellationIndividualStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldNbOfTxs', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldCtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

