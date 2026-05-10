from . import base_types
import AccountInterest4
import TotalTransactions6
import ISODateTime
import CopyDuplicate1Code
import SequenceRange1Choice
import ReportEntry15
import ReportingSource1Choice
import Pagination1
import Max35Text
import Number
import CashBalance8
import CashAccount43
import DateTimePeriod1
import CashAccount40
import Max500Text

class AccountReport37(base_types._BaseFieldType):

	__slots__ = ["_Intrst", "_Acct", "_RptPgntn", "_CpyDplctInd", "_TxsSummry", "_RptgSrc", "_CreDtTm", "_RptgSeq", "_RltdAcct", "_AddtlRptInf", "_ElctrncSeqNb", "_Id", "_LglSeqNb", "_Bal", "_Ntry", "_FrToDt"]
	@property
	def Intrst(self):
		return self._Intrst

	@Intrst.setter
	def Intrst(self, value):
		self._Intrst = value if type(value) != auto else self.make_default("Intrst")

	@Intrst.deleter
	def Intrst(self):
		del self._Intrst
		self._Intrst = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def RptPgntn(self):
		return self._RptPgntn

	@RptPgntn.setter
	def RptPgntn(self, value):
		self._RptPgntn = value if type(value) != auto else self.make_default("RptPgntn")

	@RptPgntn.deleter
	def RptPgntn(self):
		del self._RptPgntn
		self._RptPgntn = None

	@property
	def CpyDplctInd(self):
		return self._CpyDplctInd

	@CpyDplctInd.setter
	def CpyDplctInd(self, value):
		self._CpyDplctInd = value if type(value) != auto else self.make_default("CpyDplctInd")

	@CpyDplctInd.deleter
	def CpyDplctInd(self):
		del self._CpyDplctInd
		self._CpyDplctInd = None

	@property
	def TxsSummry(self):
		return self._TxsSummry

	@TxsSummry.setter
	def TxsSummry(self, value):
		self._TxsSummry = value if type(value) != auto else self.make_default("TxsSummry")

	@TxsSummry.deleter
	def TxsSummry(self):
		del self._TxsSummry
		self._TxsSummry = None

	@property
	def RptgSrc(self):
		return self._RptgSrc

	@RptgSrc.setter
	def RptgSrc(self, value):
		self._RptgSrc = value if type(value) != auto else self.make_default("RptgSrc")

	@RptgSrc.deleter
	def RptgSrc(self):
		del self._RptgSrc
		self._RptgSrc = None

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
	def RptgSeq(self):
		return self._RptgSeq

	@RptgSeq.setter
	def RptgSeq(self, value):
		self._RptgSeq = value if type(value) != auto else self.make_default("RptgSeq")

	@RptgSeq.deleter
	def RptgSeq(self):
		del self._RptgSeq
		self._RptgSeq = None

	@property
	def RltdAcct(self):
		return self._RltdAcct

	@RltdAcct.setter
	def RltdAcct(self, value):
		self._RltdAcct = value if type(value) != auto else self.make_default("RltdAcct")

	@RltdAcct.deleter
	def RltdAcct(self):
		del self._RltdAcct
		self._RltdAcct = None

	@property
	def AddtlRptInf(self):
		return self._AddtlRptInf

	@AddtlRptInf.setter
	def AddtlRptInf(self, value):
		self._AddtlRptInf = value if type(value) != auto else self.make_default("AddtlRptInf")

	@AddtlRptInf.deleter
	def AddtlRptInf(self):
		del self._AddtlRptInf
		self._AddtlRptInf = None

	@property
	def ElctrncSeqNb(self):
		return self._ElctrncSeqNb

	@ElctrncSeqNb.setter
	def ElctrncSeqNb(self, value):
		self._ElctrncSeqNb = value if type(value) != auto else self.make_default("ElctrncSeqNb")

	@ElctrncSeqNb.deleter
	def ElctrncSeqNb(self):
		del self._ElctrncSeqNb
		self._ElctrncSeqNb = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def LglSeqNb(self):
		return self._LglSeqNb

	@LglSeqNb.setter
	def LglSeqNb(self, value):
		self._LglSeqNb = value if type(value) != auto else self.make_default("LglSeqNb")

	@LglSeqNb.deleter
	def LglSeqNb(self):
		del self._LglSeqNb
		self._LglSeqNb = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def Ntry(self):
		return self._Ntry

	@Ntry.setter
	def Ntry(self, value):
		self._Ntry = value if type(value) != auto else self.make_default("Ntry")

	@Ntry.deleter
	def Ntry(self):
		del self._Ntry
		self._Ntry = None

	@property
	def FrToDt(self):
		return self._FrToDt

	@FrToDt.setter
	def FrToDt(self, value):
		self._FrToDt = value if type(value) != auto else self.make_default("FrToDt")

	@FrToDt.deleter
	def FrToDt(self):
		del self._FrToDt
		self._FrToDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Intrst', type=AccountInterest4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Acct', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyDplctInd', type=CopyDuplicate1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxsSummry', type=TotalTransactions6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgSrc', type=ReportingSource1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgSeq', type=SequenceRange1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRptInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncSeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglSeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=CashBalance8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ntry', type=ReportEntry15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrToDt', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
	))

