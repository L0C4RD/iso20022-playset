from . import base_types
from .SecuritiesAccount18 import SecuritiesAccount18
from .PartyIdentification33Choice import PartyIdentification33Choice
from .AlternatePartyIdentification4 import AlternatePartyIdentification4
from .PartyTextInformation1 import PartyTextInformation1

class PartyIdentificationAndAccount31(base_types._BaseFieldType):

	__slots__ = ["_Id", "_AltrnId", "_ClrAcct", "_AddtlInf"]
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
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if type(value) != base_types.auto else self.make_default("AltrnId")

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = None

	@property
	def ClrAcct(self):
		return self._ClrAcct

	@ClrAcct.setter
	def ClrAcct(self, value):
		self._ClrAcct = value if type(value) != base_types.auto else self.make_default("ClrAcct")

	@ClrAcct.deleter
	def ClrAcct(self):
		del self._ClrAcct
		self._ClrAcct = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification33Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAcct', type=SecuritiesAccount18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation1, min=0, max=1, mutex_group=None, array=False),
	))

