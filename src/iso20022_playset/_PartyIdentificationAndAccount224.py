from . import base_types
from ._CashAccountIdentification5Choice import CashAccountIdentification5Choice
from ._LEIIdentifier import LEIIdentifier
from ._PartyTextInformation2 import PartyTextInformation2
from ._CashAccountIdentification9Choice import CashAccountIdentification9Choice
from ._PartyIdentification133Choice import PartyIdentification133Choice
from ._AlternatePartyIdentification7 import AlternatePartyIdentification7

class PartyIdentificationAndAccount224(base_types._BaseFieldType):

	__slots__ = ["_TaxAcct", "_CshAcct", "_Id", "_ComssnAcct", "_AddtlInf", "_ChrgsAcct", "_LEI", "_AltrnId"]
	@property
	def TaxAcct(self):
		return self._TaxAcct

	@TaxAcct.setter
	def TaxAcct(self, value):
		self._TaxAcct = value if type(value) != base_types.auto else self.make_default("TaxAcct")

	@TaxAcct.deleter
	def TaxAcct(self):
		del self._TaxAcct
		self._TaxAcct = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

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
	def ComssnAcct(self):
		return self._ComssnAcct

	@ComssnAcct.setter
	def ComssnAcct(self, value):
		self._ComssnAcct = value if type(value) != base_types.auto else self.make_default("ComssnAcct")

	@ComssnAcct.deleter
	def ComssnAcct(self):
		del self._ComssnAcct
		self._ComssnAcct = None

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
	def ChrgsAcct(self):
		return self._ChrgsAcct

	@ChrgsAcct.setter
	def ChrgsAcct(self, value):
		self._ChrgsAcct = value if type(value) != base_types.auto else self.make_default("ChrgsAcct")

	@ChrgsAcct.deleter
	def ChrgsAcct(self):
		del self._ChrgsAcct
		self._ChrgsAcct = None

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification133Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComssnAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification7, min=0, max=1, mutex_group=None, array=False),
	))

