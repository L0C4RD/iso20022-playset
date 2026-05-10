from . import base_types
from ._LEIIdentifier import LEIIdentifier
from ._PartyIdentification120Choice import PartyIdentification120Choice
from ._PartyTextInformation1 import PartyTextInformation1
from ._Max35Text import Max35Text
from ._AlternatePartyIdentification7 import AlternatePartyIdentification7

class PartyIdentificationAndAccount165(base_types._BaseFieldType):

	__slots__ = ["_Id", "_AddtlInf", "_PrcgId", "_LEI", "_AltrnId"]
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
		base_types.FieldEntry(name='Id', type=PartyIdentification120Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification7, min=0, max=1, mutex_group=None, array=False),
	))

