from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40
from ._ISODateTime import ISODateTime
from ._Max35Text import Max35Text
from ._TotalCharges7 import TotalCharges7

class GroupHeader126(base_types._BaseFieldType):

	__slots__ = ["_ChrgsAcct", "_ChrgsAcctOwnr", "_ChrgsRqstr", "_CreDtTm", "_MsgId", "_TtlChrgs"]
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
	def ChrgsAcctOwnr(self):
		return self._ChrgsAcctOwnr

	@ChrgsAcctOwnr.setter
	def ChrgsAcctOwnr(self, value):
		self._ChrgsAcctOwnr = value if type(value) != base_types.auto else self.make_default("ChrgsAcctOwnr")

	@ChrgsAcctOwnr.deleter
	def ChrgsAcctOwnr(self):
		del self._ChrgsAcctOwnr
		self._ChrgsAcctOwnr = None

	@property
	def ChrgsRqstr(self):
		return self._ChrgsRqstr

	@ChrgsRqstr.setter
	def ChrgsRqstr(self, value):
		self._ChrgsRqstr = value if type(value) != base_types.auto else self.make_default("ChrgsRqstr")

	@ChrgsRqstr.deleter
	def ChrgsRqstr(self):
		del self._ChrgsRqstr
		self._ChrgsRqstr = None

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
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def TtlChrgs(self):
		return self._TtlChrgs

	@TtlChrgs.setter
	def TtlChrgs(self, value):
		self._TtlChrgs = value if type(value) != base_types.auto else self.make_default("TtlChrgs")

	@TtlChrgs.deleter
	def TtlChrgs(self):
		del self._TtlChrgs
		self._TtlChrgs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgsAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctOwnr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsRqstr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlChrgs', type=TotalCharges7, min=0, max=1, mutex_group=None, array=False),
	))

