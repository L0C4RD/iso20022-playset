from . import base_types
from .Status25Choice import Status25Choice
from .Account23 import Account23
from .ISODate import ISODate
from .AcceptedStatusReason1Choice import AcceptedStatusReason1Choice
from .BlockedStatusReason2Choice import BlockedStatusReason2Choice
from .AccountStatus2 import AccountStatus2
from .Max35Text import Max35Text

class AccountManagementStatusAndReason5(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_Sts", "_AcctSts", "_AcctApplId", "_CRSRptgDt", "_ExstgAcctId", "_FATCARptgDt", "_BlckdSts", "_StsRsn"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def AcctSts(self):
		return self._AcctSts

	@AcctSts.setter
	def AcctSts(self, value):
		self._AcctSts = value if type(value) != base_types.auto else self.make_default("AcctSts")

	@AcctSts.deleter
	def AcctSts(self):
		del self._AcctSts
		self._AcctSts = None

	@property
	def AcctApplId(self):
		return self._AcctApplId

	@AcctApplId.setter
	def AcctApplId(self, value):
		self._AcctApplId = value if type(value) != base_types.auto else self.make_default("AcctApplId")

	@AcctApplId.deleter
	def AcctApplId(self):
		del self._AcctApplId
		self._AcctApplId = None

	@property
	def CRSRptgDt(self):
		return self._CRSRptgDt

	@CRSRptgDt.setter
	def CRSRptgDt(self, value):
		self._CRSRptgDt = value if type(value) != base_types.auto else self.make_default("CRSRptgDt")

	@CRSRptgDt.deleter
	def CRSRptgDt(self):
		del self._CRSRptgDt
		self._CRSRptgDt = None

	@property
	def ExstgAcctId(self):
		return self._ExstgAcctId

	@ExstgAcctId.setter
	def ExstgAcctId(self, value):
		self._ExstgAcctId = value if type(value) != base_types.auto else self.make_default("ExstgAcctId")

	@ExstgAcctId.deleter
	def ExstgAcctId(self):
		del self._ExstgAcctId
		self._ExstgAcctId = None

	@property
	def FATCARptgDt(self):
		return self._FATCARptgDt

	@FATCARptgDt.setter
	def FATCARptgDt(self, value):
		self._FATCARptgDt = value if type(value) != base_types.auto else self.make_default("FATCARptgDt")

	@FATCARptgDt.deleter
	def FATCARptgDt(self):
		del self._FATCARptgDt
		self._FATCARptgDt = None

	@property
	def BlckdSts(self):
		return self._BlckdSts

	@BlckdSts.setter
	def BlckdSts(self, value):
		self._BlckdSts = value if type(value) != base_types.auto else self.make_default("BlckdSts")

	@BlckdSts.deleter
	def BlckdSts(self):
		del self._BlckdSts
		self._BlckdSts = None

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != base_types.auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=Status25Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSts', type=AccountStatus2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctApplId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CRSRptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExstgAcctId', type=Account23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FATCARptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckdSts', type=BlockedStatusReason2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=AcceptedStatusReason1Choice, min=0, max=None, mutex_group=None, array=True),
	))

