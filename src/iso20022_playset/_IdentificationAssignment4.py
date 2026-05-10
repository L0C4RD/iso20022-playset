from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._Party50Choice import Party50Choice
from ._Max35Text import Max35Text
from ._ISODateTime import ISODateTime

class IdentificationAssignment4(base_types._BaseFieldType):

	__slots__ = ["_Assgnr", "_Assgne", "_CreDtTm", "_Cretr", "_FrstAgt", "_MsgId"]
	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if type(value) != base_types.auto else self.make_default("Assgnr")

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = None

	@property
	def Assgne(self):
		return self._Assgne

	@Assgne.setter
	def Assgne(self, value):
		self._Assgne = value if type(value) != base_types.auto else self.make_default("Assgne")

	@Assgne.deleter
	def Assgne(self):
		del self._Assgne
		self._Assgne = None

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
	def Cretr(self):
		return self._Cretr

	@Cretr.setter
	def Cretr(self, value):
		self._Cretr = value if type(value) != base_types.auto else self.make_default("Cretr")

	@Cretr.deleter
	def Cretr(self):
		del self._Cretr
		self._Cretr = None

	@property
	def FrstAgt(self):
		return self._FrstAgt

	@FrstAgt.setter
	def FrstAgt(self, value):
		self._FrstAgt = value if type(value) != base_types.auto else self.make_default("FrstAgt")

	@FrstAgt.deleter
	def FrstAgt(self):
		del self._FrstAgt
		self._FrstAgt = None

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
		base_types.FieldEntry(name='Assgnr', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgne', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cretr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

