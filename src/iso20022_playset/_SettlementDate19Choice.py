from . import base_types
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._SettlementDateCode8Choice import SettlementDateCode8Choice

class SettlementDate19Choice(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_DtCd"]
	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def DtCd(self):
		return self._DtCd

	@DtCd.setter
	def DtCd(self, value):
		self._DtCd = value if type(value) != base_types.auto else self.make_default("DtCd")

	@DtCd.deleter
	def DtCd(self):
		del self._DtCd
		self._DtCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtCd', type=SettlementDateCode8Choice, min=0, max=1, mutex_group=1, array=False),
	))

