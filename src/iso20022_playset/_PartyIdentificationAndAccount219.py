# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlternatePartyIdentification8
from . import ClearingSide1Code
from . import Max35Text
from . import PartyIdentification240Choice
from . import PartyTextInformation1
from . import SecuritiesAccount20

class PartyIdentificationAndAccount219(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AltrnId", "_ClrAcct", "_Id", "_PrcgId", "_Sd"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', PartyTextInformation1, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', PartyTextInformation1, False)

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
	def ClrAcct(self):
		return self._ClrAcct

	@ClrAcct.setter
	def ClrAcct(self, value):
		self._ClrAcct = value if value is not None else base_types.UninitialisedField(self, 'ClrAcct', SecuritiesAccount20, False)

	@ClrAcct.deleter
	def ClrAcct(self):
		del self._ClrAcct
		self._ClrAcct = base_types.UninitialisedField(self, 'ClrAcct', SecuritiesAccount20, False)

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
	def Sd(self):
		return self._Sd

	@Sd.setter
	def Sd(self, value):
		self._Sd = value if value is not None else base_types.UninitialisedField(self, 'Sd', ClearingSide1Code, False)

	@Sd.deleter
	def Sd(self):
		del self._Sd
		self._Sd = base_types.UninitialisedField(self, 'Sd', ClearingSide1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAcct', type=SecuritiesAccount20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification240Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sd', type=ClearingSide1Code, min=0, max=1, mutex_group=None, array=False),
	))