# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementDataRate2
from . import SettlementDataVolume2

class SettlementTotalData1(base_types._BaseFieldType):

	__slots__ = ["_Faild", "_FaildRate", "_Sttld", "_Ttl"]
	@property
	def Faild(self):
		return self._Faild

	@Faild.setter
	def Faild(self, value):
		self._Faild = value if value is not None else base_types.UninitialisedField(self, 'Faild', SettlementDataVolume2, False)

	@Faild.deleter
	def Faild(self):
		del self._Faild
		self._Faild = base_types.UninitialisedField(self, 'Faild', SettlementDataVolume2, False)

	@property
	def FaildRate(self):
		return self._FaildRate

	@FaildRate.setter
	def FaildRate(self, value):
		self._FaildRate = value if value is not None else base_types.UninitialisedField(self, 'FaildRate', SettlementDataRate2, False)

	@FaildRate.deleter
	def FaildRate(self):
		del self._FaildRate
		self._FaildRate = base_types.UninitialisedField(self, 'FaildRate', SettlementDataRate2, False)

	@property
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if value is not None else base_types.UninitialisedField(self, 'Sttld', SettlementDataVolume2, False)

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = base_types.UninitialisedField(self, 'Sttld', SettlementDataVolume2, False)

	@property
	def Ttl(self):
		return self._Ttl

	@Ttl.setter
	def Ttl(self, value):
		self._Ttl = value if value is not None else base_types.UninitialisedField(self, 'Ttl', SettlementDataVolume2, False)

	@Ttl.deleter
	def Ttl(self):
		del self._Ttl
		self._Ttl = base_types.UninitialisedField(self, 'Ttl', SettlementDataVolume2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Faild', type=SettlementDataVolume2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaildRate', type=SettlementDataRate2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttld', type=SettlementDataVolume2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ttl', type=SettlementDataVolume2, min=1, max=1, mutex_group=None, array=False),
	))