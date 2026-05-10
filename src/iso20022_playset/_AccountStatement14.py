from . import base_types
from ._AccountInterest4 import AccountInterest4
from ._CashAccount40 import CashAccount40
from ._CashAccount43 import CashAccount43
from ._CashBalance8 import CashBalance8
from ._CopyDuplicate1Code import CopyDuplicate1Code
from ._DateTimePeriod1 import DateTimePeriod1
from ._ISODateTime import ISODateTime
from ._Max35Text import Max35Text
from ._Max500Text import Max500Text
from ._Number import Number
from ._Pagination1 import Pagination1
from ._ReportEntry15 import ReportEntry15
from ._ReportingSource1Choice import ReportingSource1Choice
from ._SequenceRange1Choice import SequenceRange1Choice
from ._TotalTransactions6 import TotalTransactions6

class AccountStatement14(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_AddtlStmtInf", "_Bal", "_CpyDplctInd", "_CreDtTm", "_ElctrncSeqNb", "_FrToDt", "_Id", "_Intrst", "_LglSeqNb", "_Ntry", "_RltdAcct", "_RptgSeq", "_RptgSrc", "_StmtPgntn", "_TxsSummry"]
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
	def AddtlStmtInf(self):
		return self._AddtlStmtInf

	@AddtlStmtInf.setter
	def AddtlStmtInf(self, value):
		self._AddtlStmtInf = value if type(value) != base_types.auto else self.make_default("AddtlStmtInf")

	@AddtlStmtInf.deleter
	def AddtlStmtInf(self):
		del self._AddtlStmtInf
		self._AddtlStmtInf = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != base_types.auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def CpyDplctInd(self):
		return self._CpyDplctInd

	@CpyDplctInd.setter
	def CpyDplctInd(self, value):
		self._CpyDplctInd = value if type(value) != base_types.auto else self.make_default("CpyDplctInd")

	@CpyDplctInd.deleter
	def CpyDplctInd(self):
		del self._CpyDplctInd
		self._CpyDplctInd = None

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
	def ElctrncSeqNb(self):
		return self._ElctrncSeqNb

	@ElctrncSeqNb.setter
	def ElctrncSeqNb(self, value):
		self._ElctrncSeqNb = value if type(value) != base_types.auto else self.make_default("ElctrncSeqNb")

	@ElctrncSeqNb.deleter
	def ElctrncSeqNb(self):
		del self._ElctrncSeqNb
		self._ElctrncSeqNb = None

	@property
	def FrToDt(self):
		return self._FrToDt

	@FrToDt.setter
	def FrToDt(self, value):
		self._FrToDt = value if type(value) != base_types.auto else self.make_default("FrToDt")

	@FrToDt.deleter
	def FrToDt(self):
		del self._FrToDt
		self._FrToDt = None

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
	def Intrst(self):
		return self._Intrst

	@Intrst.setter
	def Intrst(self, value):
		self._Intrst = value if type(value) != base_types.auto else self.make_default("Intrst")

	@Intrst.deleter
	def Intrst(self):
		del self._Intrst
		self._Intrst = None

	@property
	def LglSeqNb(self):
		return self._LglSeqNb

	@LglSeqNb.setter
	def LglSeqNb(self, value):
		self._LglSeqNb = value if type(value) != base_types.auto else self.make_default("LglSeqNb")

	@LglSeqNb.deleter
	def LglSeqNb(self):
		del self._LglSeqNb
		self._LglSeqNb = None

	@property
	def Ntry(self):
		return self._Ntry

	@Ntry.setter
	def Ntry(self, value):
		self._Ntry = value if type(value) != base_types.auto else self.make_default("Ntry")

	@Ntry.deleter
	def Ntry(self):
		del self._Ntry
		self._Ntry = None

	@property
	def RltdAcct(self):
		return self._RltdAcct

	@RltdAcct.setter
	def RltdAcct(self, value):
		self._RltdAcct = value if type(value) != base_types.auto else self.make_default("RltdAcct")

	@RltdAcct.deleter
	def RltdAcct(self):
		del self._RltdAcct
		self._RltdAcct = None

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
	def RptgSrc(self):
		return self._RptgSrc

	@RptgSrc.setter
	def RptgSrc(self, value):
		self._RptgSrc = value if type(value) != base_types.auto else self.make_default("RptgSrc")

	@RptgSrc.deleter
	def RptgSrc(self):
		del self._RptgSrc
		self._RptgSrc = None

	@property
	def StmtPgntn(self):
		return self._StmtPgntn

	@StmtPgntn.setter
	def StmtPgntn(self, value):
		self._StmtPgntn = value if type(value) != base_types.auto else self.make_default("StmtPgntn")

	@StmtPgntn.deleter
	def StmtPgntn(self):
		del self._StmtPgntn
		self._StmtPgntn = None

	@property
	def TxsSummry(self):
		return self._TxsSummry

	@TxsSummry.setter
	def TxsSummry(self, value):
		self._TxsSummry = value if type(value) != base_types.auto else self.make_default("TxsSummry")

	@TxsSummry.deleter
	def TxsSummry(self):
		del self._TxsSummry
		self._TxsSummry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlStmtInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=CashBalance8, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CpyDplctInd', type=CopyDuplicate1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncSeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrToDt', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrst', type=AccountInterest4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LglSeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntry', type=ReportEntry15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgSeq', type=SequenceRange1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgSrc', type=ReportingSource1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxsSummry', type=TotalTransactions6, min=0, max=1, mutex_group=None, array=False),
	))

