# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SettlementDataRate2 import SettlementDataRate2
from ._SettlementDataVolume2 import SettlementDataVolume2

class SettlementTotalData1(base_types._BaseFieldType):

	__slots__ = ["_Faild", "_FaildRate", "_Sttld", "_Ttl"]
	@property
	def Faild(self):
		return self._Faild

	@Faild.setter
	def Faild(self, value):
		self._Faild = value if type(value) != base_types.auto else self.make_default("Faild")

	@Faild.deleter
	def Faild(self):
		del self._Faild
		self._Faild = None

	@property
	def FaildRate(self):
		return self._FaildRate

	@FaildRate.setter
	def FaildRate(self, value):
		self._FaildRate = value if type(value) != base_types.auto else self.make_default("FaildRate")

	@FaildRate.deleter
	def FaildRate(self):
		del self._FaildRate
		self._FaildRate = None

	@property
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if type(value) != base_types.auto else self.make_default("Sttld")

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = None

	@property
	def Ttl(self):
		return self._Ttl

	@Ttl.setter
	def Ttl(self, value):
		self._Ttl = value if type(value) != base_types.auto else self.make_default("Ttl")

	@Ttl.deleter
	def Ttl(self):
		del self._Ttl
		self._Ttl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Faild', type=SettlementDataVolume2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaildRate', type=SettlementDataRate2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttld', type=SettlementDataVolume2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ttl', type=SettlementDataVolume2, min=1, max=1, mutex_group=None, array=False),
	))