# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Authorisation1Choice
from . import BranchAndFinancialInstitutionIdentification8
from . import CopyDuplicate1Code
from . import ISODateTime
from . import Max35Text
from . import PartyIdentification272

class GroupHeader122(base_types._BaseFieldType):

	__slots__ = ["_Authstn", "_CpyInd", "_CreDtTm", "_FwdgAgt", "_InitgPty", "_MsgId", "_MsgRcpt"]
	@property
	def Authstn(self):
		return self._Authstn

	@Authstn.setter
	def Authstn(self, value):
		self._Authstn = value if value is not None else base_types.UninitialisedField(self, 'Authstn', Authorisation1Choice, True)

	@Authstn.deleter
	def Authstn(self):
		del self._Authstn
		self._Authstn = base_types.UninitialisedField(self, 'Authstn', Authorisation1Choice, True)

	@property
	def CpyInd(self):
		return self._CpyInd

	@CpyInd.setter
	def CpyInd(self, value):
		self._CpyInd = value if value is not None else base_types.UninitialisedField(self, 'CpyInd', CopyDuplicate1Code, False)

	@CpyInd.deleter
	def CpyInd(self):
		del self._CpyInd
		self._CpyInd = base_types.UninitialisedField(self, 'CpyInd', CopyDuplicate1Code, False)

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def FwdgAgt(self):
		return self._FwdgAgt

	@FwdgAgt.setter
	def FwdgAgt(self, value):
		self._FwdgAgt = value if value is not None else base_types.UninitialisedField(self, 'FwdgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@FwdgAgt.deleter
	def FwdgAgt(self):
		del self._FwdgAgt
		self._FwdgAgt = base_types.UninitialisedField(self, 'FwdgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if value is not None else base_types.UninitialisedField(self, 'InitgPty', PartyIdentification272, False)

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = base_types.UninitialisedField(self, 'InitgPty', PartyIdentification272, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@property
	def MsgRcpt(self):
		return self._MsgRcpt

	@MsgRcpt.setter
	def MsgRcpt(self, value):
		self._MsgRcpt = value if value is not None else base_types.UninitialisedField(self, 'MsgRcpt', PartyIdentification272, False)

	@MsgRcpt.deleter
	def MsgRcpt(self):
		del self._MsgRcpt
		self._MsgRcpt = base_types.UninitialisedField(self, 'MsgRcpt', PartyIdentification272, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Authstn', type=Authorisation1Choice, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='CpyInd', type=CopyDuplicate1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FwdgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPty', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRcpt', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
	))