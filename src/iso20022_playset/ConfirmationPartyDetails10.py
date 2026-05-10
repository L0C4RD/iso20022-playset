import base_types
import Max35Text
import SecuritiesAccount35
import PartyTextInformation5
import AlternatePartyIdentification8
import AccountIdentification55Choice
import TradingPartyCapacity3Choice
import PartyIdentification117Choice

class ConfirmationPartyDetails10(base_types._BaseFieldType):

	__slots__ = ["_AltrnId", "_SfkpgAcct", "_PrcgId", "_PtyCpcty", "_CshDtls", "_AddtlInf", "_Id"]
	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if type(value) != auto else self.make_default("AltrnId")

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def PrcgId(self):
		return self._PrcgId

	@PrcgId.setter
	def PrcgId(self, value):
		self._PrcgId = value if type(value) != auto else self.make_default("PrcgId")

	@PrcgId.deleter
	def PrcgId(self):
		del self._PrcgId
		self._PrcgId = None

	@property
	def PtyCpcty(self):
		return self._PtyCpcty

	@PtyCpcty.setter
	def PtyCpcty(self, value):
		self._PtyCpcty = value if type(value) != auto else self.make_default("PtyCpcty")

	@PtyCpcty.deleter
	def PtyCpcty(self):
		del self._PtyCpcty
		self._PtyCpcty = None

	@property
	def CshDtls(self):
		return self._CshDtls

	@CshDtls.setter
	def CshDtls(self, value):
		self._CshDtls = value if type(value) != auto else self.make_default("CshDtls")

	@CshDtls.deleter
	def CshDtls(self):
		del self._CshDtls
		self._CshDtls = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount35, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyCpcty', type=TradingPartyCapacity3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshDtls', type=AccountIdentification55Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification117Choice, min=1, max=1, mutex_group=None, array=False),
	))

