# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlternatePartyIdentification8
from . import InvestorCapacity4Choice
from . import Max35Text
from . import PartyIdentification240Choice
from . import PartyTextInformation5
from . import TradingPartyCapacity4Choice

class ConfirmationPartyDetails12(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AltrnId", "_Id", "_InvstrCpcty", "_PrcgId", "_TradgPtyCpcty"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', PartyTextInformation5, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', PartyTextInformation5, False)

	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if value is not None else base_types.UninitialisedField(self, 'AltrnId', AlternatePartyIdentification8, False)

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = base_types.UninitialisedField(self, 'AltrnId', AlternatePartyIdentification8, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification240Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification240Choice, False)

	@property
	def InvstrCpcty(self):
		return self._InvstrCpcty

	@InvstrCpcty.setter
	def InvstrCpcty(self, value):
		self._InvstrCpcty = value if value is not None else base_types.UninitialisedField(self, 'InvstrCpcty', InvestorCapacity4Choice, False)

	@InvstrCpcty.deleter
	def InvstrCpcty(self):
		del self._InvstrCpcty
		self._InvstrCpcty = base_types.UninitialisedField(self, 'InvstrCpcty', InvestorCapacity4Choice, False)

	@property
	def PrcgId(self):
		return self._PrcgId

	@PrcgId.setter
	def PrcgId(self, value):
		self._PrcgId = value if value is not None else base_types.UninitialisedField(self, 'PrcgId', Max35Text, False)

	@PrcgId.deleter
	def PrcgId(self):
		del self._PrcgId
		self._PrcgId = base_types.UninitialisedField(self, 'PrcgId', Max35Text, False)

	@property
	def TradgPtyCpcty(self):
		return self._TradgPtyCpcty

	@TradgPtyCpcty.setter
	def TradgPtyCpcty(self, value):
		self._TradgPtyCpcty = value if value is not None else base_types.UninitialisedField(self, 'TradgPtyCpcty', TradingPartyCapacity4Choice, False)

	@TradgPtyCpcty.deleter
	def TradgPtyCpcty(self):
		del self._TradgPtyCpcty
		self._TradgPtyCpcty = base_types.UninitialisedField(self, 'TradgPtyCpcty', TradingPartyCapacity4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification240Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrCpcty', type=InvestorCapacity4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPtyCpcty', type=TradingPartyCapacity4Choice, min=0, max=1, mutex_group=None, array=False),
	))