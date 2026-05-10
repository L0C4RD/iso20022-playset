from . import base_types
from .SequenceRange1Choice import SequenceRange1Choice
from .ReportingPeriod5 import ReportingPeriod5
from .Party50Choice import Party50Choice
from .Max35Text import Max35Text
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .TransactionType2 import TransactionType2
from .BalanceType13 import BalanceType13
from .CashAccount40 import CashAccount40

class ReportingRequest7(base_types._BaseFieldType):

	__slots__ = ["_ReqdBalTp", "_RptgSeq", "_Acct", "_ReqdMsgNmId", "_Id", "_RptgPrd", "_ReqdTxTp", "_AcctSvcr", "_AcctOwnr"]
	@property
	def ReqdBalTp(self):
		return self._ReqdBalTp

	@ReqdBalTp.setter
	def ReqdBalTp(self, value):
		self._ReqdBalTp = value if type(value) != base_types.auto else self.make_default("ReqdBalTp")

	@ReqdBalTp.deleter
	def ReqdBalTp(self):
		del self._ReqdBalTp
		self._ReqdBalTp = None

	@property
	def RptgSeq(self):
		return self._RptgSeq

	@RptgSeq.setter
	def RptgSeq(self, value):
		self._RptgSeq = value if type(value) != base_types.auto else self.make_default("RptgSeq")

	@RptgSeq.deleter
	def RptgSeq(self):
		del self._RptgSeq
		self._RptgSeq = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def ReqdMsgNmId(self):
		return self._ReqdMsgNmId

	@ReqdMsgNmId.setter
	def ReqdMsgNmId(self, value):
		self._ReqdMsgNmId = value if type(value) != base_types.auto else self.make_default("ReqdMsgNmId")

	@ReqdMsgNmId.deleter
	def ReqdMsgNmId(self):
		del self._ReqdMsgNmId
		self._ReqdMsgNmId = None

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
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if type(value) != base_types.auto else self.make_default("RptgPrd")

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = None

	@property
	def ReqdTxTp(self):
		return self._ReqdTxTp

	@ReqdTxTp.setter
	def ReqdTxTp(self, value):
		self._ReqdTxTp = value if type(value) != base_types.auto else self.make_default("ReqdTxTp")

	@ReqdTxTp.deleter
	def ReqdTxTp(self):
		del self._ReqdTxTp
		self._ReqdTxTp = None

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqdBalTp', type=BalanceType13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptgSeq', type=SequenceRange1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdMsgNmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=ReportingPeriod5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdTxTp', type=TransactionType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
	))

