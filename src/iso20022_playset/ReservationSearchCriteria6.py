from . import base_types
from .DateTimeSearch2Choice import DateTimeSearch2Choice
from .ReservationType2Choice import ReservationType2Choice
from .AccountIdentification4Choice import AccountIdentification4Choice
from .SystemIdentification2Choice import SystemIdentification2Choice
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8

class ReservationSearchCriteria6(base_types._BaseFieldType):

	__slots__ = ["_DtTm", "_CurRsvatnTp", "_DfltRsvatnTp", "_SysId", "_AcctId", "_AcctOwnr"]
	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

	@property
	def CurRsvatnTp(self):
		return self._CurRsvatnTp

	@CurRsvatnTp.setter
	def CurRsvatnTp(self, value):
		self._CurRsvatnTp = value if type(value) != auto else self.make_default("CurRsvatnTp")

	@CurRsvatnTp.deleter
	def CurRsvatnTp(self):
		del self._CurRsvatnTp
		self._CurRsvatnTp = None

	@property
	def DfltRsvatnTp(self):
		return self._DfltRsvatnTp

	@DfltRsvatnTp.setter
	def DfltRsvatnTp(self, value):
		self._DfltRsvatnTp = value if type(value) != auto else self.make_default("DfltRsvatnTp")

	@DfltRsvatnTp.deleter
	def DfltRsvatnTp(self):
		del self._DfltRsvatnTp
		self._DfltRsvatnTp = None

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if type(value) != auto else self.make_default("SysId")

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtTm', type=DateTimeSearch2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurRsvatnTp', type=ReservationType2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltRsvatnTp', type=ReservationType2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
	))

