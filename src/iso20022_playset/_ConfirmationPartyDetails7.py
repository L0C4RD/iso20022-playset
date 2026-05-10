from . import base_types
from ._AlternatePartyIdentification8 import AlternatePartyIdentification8
from ._InvestorCapacity4Choice import InvestorCapacity4Choice
from ._Max35Text import Max35Text
from ._PartyIdentification117Choice import PartyIdentification117Choice
from ._PartyTextInformation5 import PartyTextInformation5
from ._TradingPartyCapacity4Choice import TradingPartyCapacity4Choice

class ConfirmationPartyDetails7(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AltrnId", "_Id", "_InvstrCpcty", "_PrcgId", "_TradgPtyCpcty"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if type(value) != base_types.auto else self.make_default("AltrnId")

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def InvstrCpcty(self):
		return self._InvstrCpcty

	@InvstrCpcty.setter
	def InvstrCpcty(self, value):
		self._InvstrCpcty = value if type(value) != base_types.auto else self.make_default("InvstrCpcty")

	@InvstrCpcty.deleter
	def InvstrCpcty(self):
		del self._InvstrCpcty
		self._InvstrCpcty = None

	@property
	def PrcgId(self):
		return self._PrcgId

	@PrcgId.setter
	def PrcgId(self, value):
		self._PrcgId = value if type(value) != base_types.auto else self.make_default("PrcgId")

	@PrcgId.deleter
	def PrcgId(self):
		del self._PrcgId
		self._PrcgId = None

	@property
	def TradgPtyCpcty(self):
		return self._TradgPtyCpcty

	@TradgPtyCpcty.setter
	def TradgPtyCpcty(self, value):
		self._TradgPtyCpcty = value if type(value) != base_types.auto else self.make_default("TradgPtyCpcty")

	@TradgPtyCpcty.deleter
	def TradgPtyCpcty(self):
		del self._TradgPtyCpcty
		self._TradgPtyCpcty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification117Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrCpcty', type=InvestorCapacity4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPtyCpcty', type=TradingPartyCapacity4Choice, min=0, max=1, mutex_group=None, array=False),
	))

