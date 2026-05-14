from . import base_types
from ._DateAndDateTimeSearch5Choice import DateAndDateTimeSearch5Choice
from ._SettlementTransactionStatusType2 import SettlementTransactionStatusType2

class SettlementInstructionQueryStatus3(base_types._BaseFieldType):

	__slots__ = ["_DtPrd", "_Tp"]
	@property
	def DtPrd(self):
		return self._DtPrd

	@DtPrd.setter
	def DtPrd(self, value):
		self._DtPrd = value if type(value) != base_types.auto else self.make_default("DtPrd")

	@DtPrd.deleter
	def DtPrd(self):
		del self._DtPrd
		self._DtPrd = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtPrd', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=SettlementTransactionStatusType2, min=1, max=1, mutex_group=None, array=False),
	))

