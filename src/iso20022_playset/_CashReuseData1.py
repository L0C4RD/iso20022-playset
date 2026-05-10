from . import base_types
from ._ReinvestedCashTypeAndAmount1 import ReinvestedCashTypeAndAmount1
from ._PercentageRate import PercentageRate

class CashReuseData1(base_types._BaseFieldType):

	__slots__ = ["_CshRinvstmtRate", "_RinvstdCsh"]
	@property
	def CshRinvstmtRate(self):
		return self._CshRinvstmtRate

	@CshRinvstmtRate.setter
	def CshRinvstmtRate(self, value):
		self._CshRinvstmtRate = value if type(value) != base_types.auto else self.make_default("CshRinvstmtRate")

	@CshRinvstmtRate.deleter
	def CshRinvstmtRate(self):
		del self._CshRinvstmtRate
		self._CshRinvstmtRate = None

	@property
	def RinvstdCsh(self):
		return self._RinvstdCsh

	@RinvstdCsh.setter
	def RinvstdCsh(self, value):
		self._RinvstdCsh = value if type(value) != base_types.auto else self.make_default("RinvstdCsh")

	@RinvstdCsh.deleter
	def RinvstdCsh(self):
		del self._RinvstdCsh
		self._RinvstdCsh = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshRinvstmtRate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstdCsh', type=ReinvestedCashTypeAndAmount1, min=1, max=None, mutex_group=None, array=True),
	))

