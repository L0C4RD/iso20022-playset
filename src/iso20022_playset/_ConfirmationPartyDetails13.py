from . import base_types
from ._AlternatePartyIdentification8 import AlternatePartyIdentification8
from ._Max35Text import Max35Text
from ._PartyIdentification240Choice import PartyIdentification240Choice
from ._PartyTextInformation5 import PartyTextInformation5
from ._YesNoIndicator import YesNoIndicator

class ConfirmationPartyDetails13(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AltrnId", "_Id", "_InvstrPrtcnAssoctnMmbsh", "_PrcgId"]
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
	def InvstrPrtcnAssoctnMmbsh(self):
		return self._InvstrPrtcnAssoctnMmbsh

	@InvstrPrtcnAssoctnMmbsh.setter
	def InvstrPrtcnAssoctnMmbsh(self, value):
		self._InvstrPrtcnAssoctnMmbsh = value if type(value) != base_types.auto else self.make_default("InvstrPrtcnAssoctnMmbsh")

	@InvstrPrtcnAssoctnMmbsh.deleter
	def InvstrPrtcnAssoctnMmbsh(self):
		del self._InvstrPrtcnAssoctnMmbsh
		self._InvstrPrtcnAssoctnMmbsh = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification240Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrPrtcnAssoctnMmbsh', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

