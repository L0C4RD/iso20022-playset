from . import base_types
from ._TrueFalseIndicator import TrueFalseIndicator
from ._ISODate import ISODate
from ._SettlementInstruction15 import SettlementInstruction15
from ._DecimalNumber import DecimalNumber
from ._BatchBookingIndicator import BatchBookingIndicator
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Authorisation1Choice import Authorisation1Choice
from ._Max35Text import Max35Text
from ._Max15NumericText import Max15NumericText
from ._ISODateTime import ISODateTime

class GroupHeader127(base_types._BaseFieldType):

	__slots__ = ["_NbOfTxs", "_IntrBkSttlmDt", "_MsgId", "_CtrlSum", "_GrpRvsl", "_InstgAgt", "_Authstn", "_TtlRvsdIntrBkSttlmAmt", "_SttlmInf", "_InstdAgt", "_CreDtTm", "_BtchBookg"]
	@property
	def Authstn(self):
		return self._Authstn

	@Authstn.setter
	def Authstn(self, value):
		self._Authstn = value if type(value) != base_types.auto else self.make_default("Authstn")

	@Authstn.deleter
	def Authstn(self):
		del self._Authstn
		self._Authstn = None

	@property
	def BtchBookg(self):
		return self._BtchBookg

	@BtchBookg.setter
	def BtchBookg(self, value):
		self._BtchBookg = value if type(value) != base_types.auto else self.make_default("BtchBookg")

	@BtchBookg.deleter
	def BtchBookg(self):
		del self._BtchBookg
		self._BtchBookg = None

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
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if type(value) != base_types.auto else self.make_default("CtrlSum")

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = None

	@property
	def GrpRvsl(self):
		return self._GrpRvsl

	@GrpRvsl.setter
	def GrpRvsl(self, value):
		self._GrpRvsl = value if type(value) != base_types.auto else self.make_default("GrpRvsl")

	@GrpRvsl.deleter
	def GrpRvsl(self):
		del self._GrpRvsl
		self._GrpRvsl = None

	@property
	def InstdAgt(self):
		return self._InstdAgt

	@InstdAgt.setter
	def InstdAgt(self, value):
		self._InstdAgt = value if type(value) != base_types.auto else self.make_default("InstdAgt")

	@InstdAgt.deleter
	def InstdAgt(self):
		del self._InstdAgt
		self._InstdAgt = None

	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if type(value) != base_types.auto else self.make_default("InstgAgt")

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = None

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmDt")

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = None

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
	def NbOfTxs(self):
		return self._NbOfTxs

	@NbOfTxs.setter
	def NbOfTxs(self, value):
		self._NbOfTxs = value if type(value) != base_types.auto else self.make_default("NbOfTxs")

	@NbOfTxs.deleter
	def NbOfTxs(self):
		del self._NbOfTxs
		self._NbOfTxs = None

	@property
	def SttlmInf(self):
		return self._SttlmInf

	@SttlmInf.setter
	def SttlmInf(self, value):
		self._SttlmInf = value if type(value) != base_types.auto else self.make_default("SttlmInf")

	@SttlmInf.deleter
	def SttlmInf(self):
		del self._SttlmInf
		self._SttlmInf = None

	@property
	def TtlRvsdIntrBkSttlmAmt(self):
		return self._TtlRvsdIntrBkSttlmAmt

	@TtlRvsdIntrBkSttlmAmt.setter
	def TtlRvsdIntrBkSttlmAmt(self, value):
		self._TtlRvsdIntrBkSttlmAmt = value if type(value) != base_types.auto else self.make_default("TtlRvsdIntrBkSttlmAmt")

	@TtlRvsdIntrBkSttlmAmt.deleter
	def TtlRvsdIntrBkSttlmAmt(self):
		del self._TtlRvsdIntrBkSttlmAmt
		self._TtlRvsdIntrBkSttlmAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Authstn', type=Authorisation1Choice, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='BtchBookg', type=BatchBookingIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrpRvsl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfTxs', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInf', type=SettlementInstruction15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlRvsdIntrBkSttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

