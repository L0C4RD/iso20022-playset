# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max1000Text
from . import TradeCounterpartyRelationship1Choice
from . import TradeCounterpartyType1Code

class TradeCounterpartyRelationshipRecord1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_EndRltshPty", "_RltshTp", "_StartRltshPty"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max1000Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max1000Text, False)

	@property
	def EndRltshPty(self):
		return self._EndRltshPty

	@EndRltshPty.setter
	def EndRltshPty(self, value):
		self._EndRltshPty = value if value is not None else base_types.UninitialisedField(self, 'EndRltshPty', TradeCounterpartyType1Code, False)

	@EndRltshPty.deleter
	def EndRltshPty(self):
		del self._EndRltshPty
		self._EndRltshPty = base_types.UninitialisedField(self, 'EndRltshPty', TradeCounterpartyType1Code, False)

	@property
	def RltshTp(self):
		return self._RltshTp

	@RltshTp.setter
	def RltshTp(self, value):
		self._RltshTp = value if value is not None else base_types.UninitialisedField(self, 'RltshTp', TradeCounterpartyRelationship1Choice, False)

	@RltshTp.deleter
	def RltshTp(self):
		del self._RltshTp
		self._RltshTp = base_types.UninitialisedField(self, 'RltshTp', TradeCounterpartyRelationship1Choice, False)

	@property
	def StartRltshPty(self):
		return self._StartRltshPty

	@StartRltshPty.setter
	def StartRltshPty(self, value):
		self._StartRltshPty = value if value is not None else base_types.UninitialisedField(self, 'StartRltshPty', TradeCounterpartyType1Code, False)

	@StartRltshPty.deleter
	def StartRltshPty(self):
		del self._StartRltshPty
		self._StartRltshPty = base_types.UninitialisedField(self, 'StartRltshPty', TradeCounterpartyType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndRltshPty', type=TradeCounterpartyType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltshTp', type=TradeCounterpartyRelationship1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartRltshPty', type=TradeCounterpartyType1Code, min=1, max=1, mutex_group=None, array=False),
	))