# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification55Choice
from . import AlternatePartyIdentification8
from . import Max35Text
from . import PartyIdentification240Choice
from . import PartyTextInformation5
from . import SecuritiesAccount35
from . import TradingPartyCapacity3Choice

class ConfirmationPartyDetails14(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AltrnId", "_CshDtls", "_Id", "_PrcgId", "_PtyCpcty", "_SfkpgAcct"]
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
	def CshDtls(self):
		return self._CshDtls

	@CshDtls.setter
	def CshDtls(self, value):
		self._CshDtls = value if value is not None else base_types.UninitialisedField(self, 'CshDtls', AccountIdentification55Choice, False)

	@CshDtls.deleter
	def CshDtls(self):
		del self._CshDtls
		self._CshDtls = base_types.UninitialisedField(self, 'CshDtls', AccountIdentification55Choice, False)

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
	def PtyCpcty(self):
		return self._PtyCpcty

	@PtyCpcty.setter
	def PtyCpcty(self, value):
		self._PtyCpcty = value if value is not None else base_types.UninitialisedField(self, 'PtyCpcty', TradingPartyCapacity3Choice, False)

	@PtyCpcty.deleter
	def PtyCpcty(self):
		del self._PtyCpcty
		self._PtyCpcty = base_types.UninitialisedField(self, 'PtyCpcty', TradingPartyCapacity3Choice, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount35, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount35, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshDtls', type=AccountIdentification55Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification240Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyCpcty', type=TradingPartyCapacity3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount35, min=0, max=1, mutex_group=None, array=False),
	))