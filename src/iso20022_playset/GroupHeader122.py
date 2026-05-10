import base_types
import Max35Text
import ISODateTime
import PartyIdentification272
import CopyDuplicate1Code
import Authorisation1Choice
import BranchAndFinancialInstitutionIdentification8

class GroupHeader122(base_types._BaseFieldType):

	__slots__ = ["_MsgRcpt", "_MsgId", "_CreDtTm", "_FwdgAgt", "_Authstn", "_InitgPty", "_CpyInd"]
	@property
	def MsgRcpt(self):
		return self._MsgRcpt

	@MsgRcpt.setter
	def MsgRcpt(self, value):
		self._MsgRcpt = value if type(value) != auto else self.make_default("MsgRcpt")

	@MsgRcpt.deleter
	def MsgRcpt(self):
		del self._MsgRcpt
		self._MsgRcpt = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def FwdgAgt(self):
		return self._FwdgAgt

	@FwdgAgt.setter
	def FwdgAgt(self, value):
		self._FwdgAgt = value if type(value) != auto else self.make_default("FwdgAgt")

	@FwdgAgt.deleter
	def FwdgAgt(self):
		del self._FwdgAgt
		self._FwdgAgt = None

	@property
	def Authstn(self):
		return self._Authstn

	@Authstn.setter
	def Authstn(self, value):
		self._Authstn = value if type(value) != auto else self.make_default("Authstn")

	@Authstn.deleter
	def Authstn(self):
		del self._Authstn
		self._Authstn = None

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if type(value) != auto else self.make_default("InitgPty")

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = None

	@property
	def CpyInd(self):
		return self._CpyInd

	@CpyInd.setter
	def CpyInd(self, value):
		self._CpyInd = value if type(value) != auto else self.make_default("CpyInd")

	@CpyInd.deleter
	def CpyInd(self):
		del self._CpyInd
		self._CpyInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgRcpt', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FwdgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Authstn', type=Authorisation1Choice, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='InitgPty', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyInd', type=CopyDuplicate1Code, min=0, max=1, mutex_group=None, array=False),
	))

