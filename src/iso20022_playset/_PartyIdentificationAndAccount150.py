# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlternatePartyIdentification8
from . import CashAccountIdentification5Choice
from . import CountryCode
from . import Max35Text
from . import PartyIdentification117Choice
from . import PartyTextInformation1

class PartyIdentificationAndAccount150(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AltrnId", "_CshAcct", "_CtryOfRes", "_Id", "_PrcgId", "_SfkpgAcct"]
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
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification5Choice, False)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification5Choice, False)

	@property
	def CtryOfRes(self):
		return self._CtryOfRes

	@CtryOfRes.setter
	def CtryOfRes(self, value):
		self._CtryOfRes = value if value is not None else base_types.UninitialisedField(self, 'CtryOfRes', CountryCode, False)

	@CtryOfRes.deleter
	def CtryOfRes(self):
		del self._CtryOfRes
		self._CtryOfRes = base_types.UninitialisedField(self, 'CtryOfRes', CountryCode, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification117Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification117Choice, False)

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
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', Max35Text, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfRes', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification117Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))