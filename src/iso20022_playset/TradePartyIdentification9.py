from . import base_types
from .PartyIdentification78 import PartyIdentification78
from .FundIdentification6 import FundIdentification6
from .PartyIdentificationAndAccount119 import PartyIdentificationAndAccount119
from .OptionParty3Code import OptionParty3Code
from .OptionParty1Code import OptionParty1Code

class TradePartyIdentification9(base_types._BaseFieldType):

	__slots__ = ["_SubmitgPty", "_TradPtyId", "_InitrInd", "_BuyrOrSellrInd", "_FndInf"]
	@property
	def SubmitgPty(self):
		return self._SubmitgPty

	@SubmitgPty.setter
	def SubmitgPty(self, value):
		self._SubmitgPty = value if type(value) != base_types.auto else self.make_default("SubmitgPty")

	@SubmitgPty.deleter
	def SubmitgPty(self):
		del self._SubmitgPty
		self._SubmitgPty = None

	@property
	def TradPtyId(self):
		return self._TradPtyId

	@TradPtyId.setter
	def TradPtyId(self, value):
		self._TradPtyId = value if type(value) != base_types.auto else self.make_default("TradPtyId")

	@TradPtyId.deleter
	def TradPtyId(self):
		del self._TradPtyId
		self._TradPtyId = None

	@property
	def InitrInd(self):
		return self._InitrInd

	@InitrInd.setter
	def InitrInd(self, value):
		self._InitrInd = value if type(value) != base_types.auto else self.make_default("InitrInd")

	@InitrInd.deleter
	def InitrInd(self):
		del self._InitrInd
		self._InitrInd = None

	@property
	def BuyrOrSellrInd(self):
		return self._BuyrOrSellrInd

	@BuyrOrSellrInd.setter
	def BuyrOrSellrInd(self, value):
		self._BuyrOrSellrInd = value if type(value) != base_types.auto else self.make_default("BuyrOrSellrInd")

	@BuyrOrSellrInd.deleter
	def BuyrOrSellrInd(self):
		del self._BuyrOrSellrInd
		self._BuyrOrSellrInd = None

	@property
	def FndInf(self):
		return self._FndInf

	@FndInf.setter
	def FndInf(self, value):
		self._FndInf = value if type(value) != base_types.auto else self.make_default("FndInf")

	@FndInf.deleter
	def FndInf(self):
		del self._FndInf
		self._FndInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubmitgPty', type=PartyIdentificationAndAccount119, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradPtyId', type=PartyIdentification78, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitrInd', type=OptionParty3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrOrSellrInd', type=OptionParty1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndInf', type=FundIdentification6, min=0, max=1, mutex_group=None, array=False),
	))

