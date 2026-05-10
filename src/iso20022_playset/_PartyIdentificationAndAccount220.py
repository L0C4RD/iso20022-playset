from . import base_types
from .Max35Text import Max35Text
from .PartyTextInformation1 import PartyTextInformation1
from .PartyIdentification240Choice import PartyIdentification240Choice
from .AlternatePartyIdentification8 import AlternatePartyIdentification8
from .CountryCode import CountryCode
from .CashAccountIdentification5Choice import CashAccountIdentification5Choice

class PartyIdentificationAndAccount220(base_types._BaseFieldType):

	__slots__ = ["_CshAcct", "_SfkpgAcct", "_Id", "_CtryOfRes", "_PrcgId", "_AddtlInf", "_AltrnId"]
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
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

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
	def CtryOfRes(self):
		return self._CtryOfRes

	@CtryOfRes.setter
	def CtryOfRes(self, value):
		self._CtryOfRes = value if type(value) != base_types.auto else self.make_default("CtryOfRes")

	@CtryOfRes.deleter
	def CtryOfRes(self):
		del self._CtryOfRes
		self._CtryOfRes = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification240Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfRes', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification8, min=0, max=1, mutex_group=None, array=False),
	))

