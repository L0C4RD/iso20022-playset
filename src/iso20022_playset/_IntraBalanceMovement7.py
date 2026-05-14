# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40
from ._IntraBalanceMovement6 import IntraBalanceMovement6
from ._IntraBalanceStatusAndReason2 import IntraBalanceStatusAndReason2
from ._Max35Text import Max35Text
from ._SystemPartyIdentification8 import SystemPartyIdentification8

class IntraBalanceMovement7(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrTxId", "_AcctSvcrTxId", "_CorpActnEvtId", "_CshAcct", "_CshAcctOwnr", "_CshAcctSvcr", "_MktInfrstrctrTxId", "_MvmntDtls", "_PoolId", "_PrcrTxId", "_StsAndRsn"]
	@property
	def AcctOwnrTxId(self):
		return self._AcctOwnrTxId

	@AcctOwnrTxId.setter
	def AcctOwnrTxId(self, value):
		self._AcctOwnrTxId = value if type(value) != base_types.auto else self.make_default("AcctOwnrTxId")

	@AcctOwnrTxId.deleter
	def AcctOwnrTxId(self):
		del self._AcctOwnrTxId
		self._AcctOwnrTxId = None

	@property
	def AcctSvcrTxId(self):
		return self._AcctSvcrTxId

	@AcctSvcrTxId.setter
	def AcctSvcrTxId(self, value):
		self._AcctSvcrTxId = value if type(value) != base_types.auto else self.make_default("AcctSvcrTxId")

	@AcctSvcrTxId.deleter
	def AcctSvcrTxId(self):
		del self._AcctSvcrTxId
		self._AcctSvcrTxId = None

	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if type(value) != base_types.auto else self.make_default("CorpActnEvtId")

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def CshAcctOwnr(self):
		return self._CshAcctOwnr

	@CshAcctOwnr.setter
	def CshAcctOwnr(self, value):
		self._CshAcctOwnr = value if type(value) != base_types.auto else self.make_default("CshAcctOwnr")

	@CshAcctOwnr.deleter
	def CshAcctOwnr(self):
		del self._CshAcctOwnr
		self._CshAcctOwnr = None

	@property
	def CshAcctSvcr(self):
		return self._CshAcctSvcr

	@CshAcctSvcr.setter
	def CshAcctSvcr(self, value):
		self._CshAcctSvcr = value if type(value) != base_types.auto else self.make_default("CshAcctSvcr")

	@CshAcctSvcr.deleter
	def CshAcctSvcr(self):
		del self._CshAcctSvcr
		self._CshAcctSvcr = None

	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if type(value) != base_types.auto else self.make_default("MktInfrstrctrTxId")

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = None

	@property
	def MvmntDtls(self):
		return self._MvmntDtls

	@MvmntDtls.setter
	def MvmntDtls(self, value):
		self._MvmntDtls = value if type(value) != base_types.auto else self.make_default("MvmntDtls")

	@MvmntDtls.deleter
	def MvmntDtls(self):
		del self._MvmntDtls
		self._MvmntDtls = None

	@property
	def PoolId(self):
		return self._PoolId

	@PoolId.setter
	def PoolId(self, value):
		self._PoolId = value if type(value) != base_types.auto else self.make_default("PoolId")

	@PoolId.deleter
	def PoolId(self):
		del self._PoolId
		self._PoolId = None

	@property
	def PrcrTxId(self):
		return self._PrcrTxId

	@PrcrTxId.setter
	def PrcrTxId(self, value):
		self._PrcrTxId = value if type(value) != base_types.auto else self.make_default("PrcrTxId")

	@PrcrTxId.deleter
	def PrcrTxId(self):
		del self._PrcrTxId
		self._PrcrTxId = None

	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if type(value) != base_types.auto else self.make_default("StsAndRsn")

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrTxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntDtls', type=IntraBalanceMovement6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsAndRsn', type=IntraBalanceStatusAndReason2, min=0, max=1, mutex_group=None, array=False),
	))