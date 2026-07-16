# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptedStatusReason1Choice
from . import Account23
from . import AccountStatus2
from . import BlockedStatusReason2Choice
from . import ISODate
from . import Max35Text
from . import Status25Choice

class AccountManagementStatusAndReason5(base_types._BaseFieldType):

	__slots__ = ["_AcctApplId", "_AcctId", "_AcctSts", "_BlckdSts", "_CRSRptgDt", "_ExstgAcctId", "_FATCARptgDt", "_Sts", "_StsRsn"]
	@property
	def AcctApplId(self):
		return self._AcctApplId

	@AcctApplId.setter
	def AcctApplId(self, value):
		self._AcctApplId = value if value is not None else base_types.UninitialisedField(self, 'AcctApplId', Max35Text, False)

	@AcctApplId.deleter
	def AcctApplId(self):
		del self._AcctApplId
		self._AcctApplId = base_types.UninitialisedField(self, 'AcctApplId', Max35Text, False)

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def AcctSts(self):
		return self._AcctSts

	@AcctSts.setter
	def AcctSts(self, value):
		self._AcctSts = value if value is not None else base_types.UninitialisedField(self, 'AcctSts', AccountStatus2, False)

	@AcctSts.deleter
	def AcctSts(self):
		del self._AcctSts
		self._AcctSts = base_types.UninitialisedField(self, 'AcctSts', AccountStatus2, False)

	@property
	def BlckdSts(self):
		return self._BlckdSts

	@BlckdSts.setter
	def BlckdSts(self, value):
		self._BlckdSts = value if value is not None else base_types.UninitialisedField(self, 'BlckdSts', BlockedStatusReason2Choice, False)

	@BlckdSts.deleter
	def BlckdSts(self):
		del self._BlckdSts
		self._BlckdSts = base_types.UninitialisedField(self, 'BlckdSts', BlockedStatusReason2Choice, False)

	@property
	def CRSRptgDt(self):
		return self._CRSRptgDt

	@CRSRptgDt.setter
	def CRSRptgDt(self, value):
		self._CRSRptgDt = value if value is not None else base_types.UninitialisedField(self, 'CRSRptgDt', ISODate, False)

	@CRSRptgDt.deleter
	def CRSRptgDt(self):
		del self._CRSRptgDt
		self._CRSRptgDt = base_types.UninitialisedField(self, 'CRSRptgDt', ISODate, False)

	@property
	def ExstgAcctId(self):
		return self._ExstgAcctId

	@ExstgAcctId.setter
	def ExstgAcctId(self, value):
		self._ExstgAcctId = value if value is not None else base_types.UninitialisedField(self, 'ExstgAcctId', Account23, True)

	@ExstgAcctId.deleter
	def ExstgAcctId(self):
		del self._ExstgAcctId
		self._ExstgAcctId = base_types.UninitialisedField(self, 'ExstgAcctId', Account23, True)

	@property
	def FATCARptgDt(self):
		return self._FATCARptgDt

	@FATCARptgDt.setter
	def FATCARptgDt(self, value):
		self._FATCARptgDt = value if value is not None else base_types.UninitialisedField(self, 'FATCARptgDt', ISODate, False)

	@FATCARptgDt.deleter
	def FATCARptgDt(self):
		del self._FATCARptgDt
		self._FATCARptgDt = base_types.UninitialisedField(self, 'FATCARptgDt', ISODate, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', Status25Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', Status25Choice, False)

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if value is not None else base_types.UninitialisedField(self, 'StsRsn', AcceptedStatusReason1Choice, True)

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = base_types.UninitialisedField(self, 'StsRsn', AcceptedStatusReason1Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctApplId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSts', type=AccountStatus2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckdSts', type=BlockedStatusReason2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CRSRptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExstgAcctId', type=Account23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FATCARptgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=Status25Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=AcceptedStatusReason1Choice, min=0, max=None, mutex_group=None, array=True),
	))