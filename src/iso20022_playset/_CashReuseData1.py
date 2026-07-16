# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate
from . import ReinvestedCashTypeAndAmount1

class CashReuseData1(base_types._BaseFieldType):

	__slots__ = ["_CshRinvstmtRate", "_RinvstdCsh"]
	@property
	def CshRinvstmtRate(self):
		return self._CshRinvstmtRate

	@CshRinvstmtRate.setter
	def CshRinvstmtRate(self, value):
		self._CshRinvstmtRate = value if value is not None else base_types.UninitialisedField(self, 'CshRinvstmtRate', PercentageRate, False)

	@CshRinvstmtRate.deleter
	def CshRinvstmtRate(self):
		del self._CshRinvstmtRate
		self._CshRinvstmtRate = base_types.UninitialisedField(self, 'CshRinvstmtRate', PercentageRate, False)

	@property
	def RinvstdCsh(self):
		return self._RinvstdCsh

	@RinvstdCsh.setter
	def RinvstdCsh(self, value):
		self._RinvstdCsh = value if value is not None else base_types.UninitialisedField(self, 'RinvstdCsh', ReinvestedCashTypeAndAmount1, True)

	@RinvstdCsh.deleter
	def RinvstdCsh(self):
		del self._RinvstdCsh
		self._RinvstdCsh = base_types.UninitialisedField(self, 'RinvstdCsh', ReinvestedCashTypeAndAmount1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshRinvstmtRate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstdCsh', type=ReinvestedCashTypeAndAmount1, min=1, max=None, mutex_group=None, array=True),
	))