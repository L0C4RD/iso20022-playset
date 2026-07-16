# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceType13
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import Max35Text
from . import Party50Choice
from . import ReportingPeriod5
from . import SequenceRange1Choice
from . import TransactionType2

class ReportingRequest7(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_AcctOwnr", "_AcctSvcr", "_Id", "_ReqdBalTp", "_ReqdMsgNmId", "_ReqdTxTp", "_RptgPrd", "_RptgSeq"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', Party50Choice, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', Party50Choice, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', BranchAndFinancialInstitutionIdentification8, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def ReqdBalTp(self):
		return self._ReqdBalTp

	@ReqdBalTp.setter
	def ReqdBalTp(self, value):
		self._ReqdBalTp = value if value is not None else base_types.UninitialisedField(self, 'ReqdBalTp', BalanceType13, True)

	@ReqdBalTp.deleter
	def ReqdBalTp(self):
		del self._ReqdBalTp
		self._ReqdBalTp = base_types.UninitialisedField(self, 'ReqdBalTp', BalanceType13, True)

	@property
	def ReqdMsgNmId(self):
		return self._ReqdMsgNmId

	@ReqdMsgNmId.setter
	def ReqdMsgNmId(self, value):
		self._ReqdMsgNmId = value if value is not None else base_types.UninitialisedField(self, 'ReqdMsgNmId', Max35Text, False)

	@ReqdMsgNmId.deleter
	def ReqdMsgNmId(self):
		del self._ReqdMsgNmId
		self._ReqdMsgNmId = base_types.UninitialisedField(self, 'ReqdMsgNmId', Max35Text, False)

	@property
	def ReqdTxTp(self):
		return self._ReqdTxTp

	@ReqdTxTp.setter
	def ReqdTxTp(self, value):
		self._ReqdTxTp = value if value is not None else base_types.UninitialisedField(self, 'ReqdTxTp', TransactionType2, False)

	@ReqdTxTp.deleter
	def ReqdTxTp(self):
		del self._ReqdTxTp
		self._ReqdTxTp = base_types.UninitialisedField(self, 'ReqdTxTp', TransactionType2, False)

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if value is not None else base_types.UninitialisedField(self, 'RptgPrd', ReportingPeriod5, False)

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = base_types.UninitialisedField(self, 'RptgPrd', ReportingPeriod5, False)

	@property
	def RptgSeq(self):
		return self._RptgSeq

	@RptgSeq.setter
	def RptgSeq(self, value):
		self._RptgSeq = value if value is not None else base_types.UninitialisedField(self, 'RptgSeq', SequenceRange1Choice, False)

	@RptgSeq.deleter
	def RptgSeq(self):
		del self._RptgSeq
		self._RptgSeq = base_types.UninitialisedField(self, 'RptgSeq', SequenceRange1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdBalTp', type=BalanceType13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqdMsgNmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdTxTp', type=TransactionType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=ReportingPeriod5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgSeq', type=SequenceRange1Choice, min=0, max=1, mutex_group=None, array=False),
	))