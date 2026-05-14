# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max1000Text import Max1000Text
from ._TradeCounterpartyRelationship1Choice import TradeCounterpartyRelationship1Choice
from ._TradeCounterpartyType1Code import TradeCounterpartyType1Code

class TradeCounterpartyRelationshipRecord1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_EndRltshPty", "_RltshTp", "_StartRltshPty"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def EndRltshPty(self):
		return self._EndRltshPty

	@EndRltshPty.setter
	def EndRltshPty(self, value):
		self._EndRltshPty = value if type(value) != base_types.auto else self.make_default("EndRltshPty")

	@EndRltshPty.deleter
	def EndRltshPty(self):
		del self._EndRltshPty
		self._EndRltshPty = None

	@property
	def RltshTp(self):
		return self._RltshTp

	@RltshTp.setter
	def RltshTp(self, value):
		self._RltshTp = value if type(value) != base_types.auto else self.make_default("RltshTp")

	@RltshTp.deleter
	def RltshTp(self):
		del self._RltshTp
		self._RltshTp = None

	@property
	def StartRltshPty(self):
		return self._StartRltshPty

	@StartRltshPty.setter
	def StartRltshPty(self, value):
		self._StartRltshPty = value if type(value) != base_types.auto else self.make_default("StartRltshPty")

	@StartRltshPty.deleter
	def StartRltshPty(self):
		del self._StartRltshPty
		self._StartRltshPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndRltshPty', type=TradeCounterpartyType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltshTp', type=TradeCounterpartyRelationship1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartRltshPty', type=TradeCounterpartyType1Code, min=1, max=1, mutex_group=None, array=False),
	))