# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FundIdentification6
from . import OptionParty1Code
from . import OptionParty3Code
from . import PartyIdentification265
from . import PartyIdentificationAndAccount119

class TradePartyIdentification10(base_types._BaseFieldType):

	__slots__ = ["_BuyrOrSellrInd", "_FndInf", "_InitrInd", "_SubmitgPty", "_TradPtyId"]
	@property
	def BuyrOrSellrInd(self):
		return self._BuyrOrSellrInd

	@BuyrOrSellrInd.setter
	def BuyrOrSellrInd(self, value):
		self._BuyrOrSellrInd = value if value is not None else base_types.UninitialisedField(self, 'BuyrOrSellrInd', OptionParty1Code, False)

	@BuyrOrSellrInd.deleter
	def BuyrOrSellrInd(self):
		del self._BuyrOrSellrInd
		self._BuyrOrSellrInd = base_types.UninitialisedField(self, 'BuyrOrSellrInd', OptionParty1Code, False)

	@property
	def FndInf(self):
		return self._FndInf

	@FndInf.setter
	def FndInf(self, value):
		self._FndInf = value if value is not None else base_types.UninitialisedField(self, 'FndInf', FundIdentification6, False)

	@FndInf.deleter
	def FndInf(self):
		del self._FndInf
		self._FndInf = base_types.UninitialisedField(self, 'FndInf', FundIdentification6, False)

	@property
	def InitrInd(self):
		return self._InitrInd

	@InitrInd.setter
	def InitrInd(self, value):
		self._InitrInd = value if value is not None else base_types.UninitialisedField(self, 'InitrInd', OptionParty3Code, False)

	@InitrInd.deleter
	def InitrInd(self):
		del self._InitrInd
		self._InitrInd = base_types.UninitialisedField(self, 'InitrInd', OptionParty3Code, False)

	@property
	def SubmitgPty(self):
		return self._SubmitgPty

	@SubmitgPty.setter
	def SubmitgPty(self, value):
		self._SubmitgPty = value if value is not None else base_types.UninitialisedField(self, 'SubmitgPty', PartyIdentificationAndAccount119, False)

	@SubmitgPty.deleter
	def SubmitgPty(self):
		del self._SubmitgPty
		self._SubmitgPty = base_types.UninitialisedField(self, 'SubmitgPty', PartyIdentificationAndAccount119, False)

	@property
	def TradPtyId(self):
		return self._TradPtyId

	@TradPtyId.setter
	def TradPtyId(self, value):
		self._TradPtyId = value if value is not None else base_types.UninitialisedField(self, 'TradPtyId', PartyIdentification265, False)

	@TradPtyId.deleter
	def TradPtyId(self):
		del self._TradPtyId
		self._TradPtyId = base_types.UninitialisedField(self, 'TradPtyId', PartyIdentification265, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyrOrSellrInd', type=OptionParty1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndInf', type=FundIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitrInd', type=OptionParty3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitgPty', type=PartyIdentificationAndAccount119, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradPtyId', type=PartyIdentification265, min=1, max=1, mutex_group=None, array=False),
	))