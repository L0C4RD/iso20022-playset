# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlternatePartyIdentification9
from . import CashAccountIdentification6Choice
from . import LEIIdentifier
from . import PartyIdentification147Choice
from . import PartyTextInformation4

class PartyIdentificationAndAccount178(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AltrnId", "_ChrgsAcct", "_ComssnAcct", "_CshAcct", "_Id", "_LEI", "_TaxAcct"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', PartyTextInformation4, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', PartyTextInformation4, False)

	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if value is not None else base_types.UninitialisedField(self, 'AltrnId', AlternatePartyIdentification9, False)

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = base_types.UninitialisedField(self, 'AltrnId', AlternatePartyIdentification9, False)

	@property
	def ChrgsAcct(self):
		return self._ChrgsAcct

	@ChrgsAcct.setter
	def ChrgsAcct(self, value):
		self._ChrgsAcct = value if value is not None else base_types.UninitialisedField(self, 'ChrgsAcct', CashAccountIdentification6Choice, False)

	@ChrgsAcct.deleter
	def ChrgsAcct(self):
		del self._ChrgsAcct
		self._ChrgsAcct = base_types.UninitialisedField(self, 'ChrgsAcct', CashAccountIdentification6Choice, False)

	@property
	def ComssnAcct(self):
		return self._ComssnAcct

	@ComssnAcct.setter
	def ComssnAcct(self, value):
		self._ComssnAcct = value if value is not None else base_types.UninitialisedField(self, 'ComssnAcct', CashAccountIdentification6Choice, False)

	@ComssnAcct.deleter
	def ComssnAcct(self):
		del self._ComssnAcct
		self._ComssnAcct = base_types.UninitialisedField(self, 'ComssnAcct', CashAccountIdentification6Choice, False)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification6Choice, False)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification6Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification147Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification147Choice, False)

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if value is not None else base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@property
	def TaxAcct(self):
		return self._TaxAcct

	@TaxAcct.setter
	def TaxAcct(self, value):
		self._TaxAcct = value if value is not None else base_types.UninitialisedField(self, 'TaxAcct', CashAccountIdentification6Choice, False)

	@TaxAcct.deleter
	def TaxAcct(self):
		del self._TaxAcct
		self._TaxAcct = base_types.UninitialisedField(self, 'TaxAcct', CashAccountIdentification6Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcct', type=CashAccountIdentification6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComssnAcct', type=CashAccountIdentification6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification147Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxAcct', type=CashAccountIdentification6Choice, min=0, max=1, mutex_group=None, array=False),
	))