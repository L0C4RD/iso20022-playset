from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._Max35Text import Max35Text
from ._PartyIdentification272 import PartyIdentification272
from ._ISODateTime import ISODateTime

class GroupHeader111(base_types._BaseFieldType):

	__slots__ = ["_CdtrAgt", "_CreDtTm", "_InitgPty", "_FwdgAgt", "_DbtrAgt", "_MsgId"]
	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if type(value) != base_types.auto else self.make_default("CdtrAgt")

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if type(value) != base_types.auto else self.make_default("InitgPty")

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = None

	@property
	def FwdgAgt(self):
		return self._FwdgAgt

	@FwdgAgt.setter
	def FwdgAgt(self, value):
		self._FwdgAgt = value if type(value) != base_types.auto else self.make_default("FwdgAgt")

	@FwdgAgt.deleter
	def FwdgAgt(self):
		del self._FwdgAgt
		self._FwdgAgt = None

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if type(value) != base_types.auto else self.make_default("DbtrAgt")

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPty', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FwdgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

