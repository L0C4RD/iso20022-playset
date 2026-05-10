from . import base_types
from ._Max15NumericText import Max15NumericText
from ._DecimalNumber import DecimalNumber

class ControlData1(base_types._BaseFieldType):

	__slots__ = ["_NbOfTxs", "_CtrlSum"]
	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if type(value) != base_types.auto else self.make_default("CtrlSum")

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = None

	@property
	def NbOfTxs(self):
		return self._NbOfTxs

	@NbOfTxs.setter
	def NbOfTxs(self, value):
		self._NbOfTxs = value if type(value) != base_types.auto else self.make_default("NbOfTxs")

	@NbOfTxs.deleter
	def NbOfTxs(self):
		del self._NbOfTxs
		self._NbOfTxs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfTxs', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))

