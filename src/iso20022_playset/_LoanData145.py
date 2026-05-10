from . import base_types
from ._ISODate import ISODate
from ._TrueFalseIndicator import TrueFalseIndicator
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._Max52Text import Max52Text
from ._ContractTerm7Choice import ContractTerm7Choice
from ._InterestRate27Choice import InterestRate27Choice
from ._SecurityCommodity9 import SecurityCommodity9
from ._MICIdentifier import MICIdentifier
from ._PercentageRate import PercentageRate
from ._CollateralDeliveryMethod1Code import CollateralDeliveryMethod1Code
from ._Cleared16Choice import Cleared16Choice
from ._ISODateTime import ISODateTime
from ._MasterAgreement7 import MasterAgreement7
from ._SpecialCollateral1Code import SpecialCollateral1Code

class LoanData145(base_types._BaseFieldType):

	__slots__ = ["_RbtRate", "_MstrAgrmt", "_ClrSts", "_TermntnDt", "_CollDlvryMtd", "_AsstTp", "_DlvryByVal", "_LndgFee", "_LnVal", "_GnlColl", "_ExctnDtTm", "_TradgVn", "_ValDt", "_Term", "_EvtDt", "_UnqTradIdr"]
	@property
	def AsstTp(self):
		return self._AsstTp

	@AsstTp.setter
	def AsstTp(self, value):
		self._AsstTp = value if type(value) != base_types.auto else self.make_default("AsstTp")

	@AsstTp.deleter
	def AsstTp(self):
		del self._AsstTp
		self._AsstTp = None

	@property
	def ClrSts(self):
		return self._ClrSts

	@ClrSts.setter
	def ClrSts(self, value):
		self._ClrSts = value if type(value) != base_types.auto else self.make_default("ClrSts")

	@ClrSts.deleter
	def ClrSts(self):
		del self._ClrSts
		self._ClrSts = None

	@property
	def CollDlvryMtd(self):
		return self._CollDlvryMtd

	@CollDlvryMtd.setter
	def CollDlvryMtd(self, value):
		self._CollDlvryMtd = value if type(value) != base_types.auto else self.make_default("CollDlvryMtd")

	@CollDlvryMtd.deleter
	def CollDlvryMtd(self):
		del self._CollDlvryMtd
		self._CollDlvryMtd = None

	@property
	def DlvryByVal(self):
		return self._DlvryByVal

	@DlvryByVal.setter
	def DlvryByVal(self, value):
		self._DlvryByVal = value if type(value) != base_types.auto else self.make_default("DlvryByVal")

	@DlvryByVal.deleter
	def DlvryByVal(self):
		del self._DlvryByVal
		self._DlvryByVal = None

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if type(value) != base_types.auto else self.make_default("EvtDt")

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = None

	@property
	def ExctnDtTm(self):
		return self._ExctnDtTm

	@ExctnDtTm.setter
	def ExctnDtTm(self, value):
		self._ExctnDtTm = value if type(value) != base_types.auto else self.make_default("ExctnDtTm")

	@ExctnDtTm.deleter
	def ExctnDtTm(self):
		del self._ExctnDtTm
		self._ExctnDtTm = None

	@property
	def GnlColl(self):
		return self._GnlColl

	@GnlColl.setter
	def GnlColl(self, value):
		self._GnlColl = value if type(value) != base_types.auto else self.make_default("GnlColl")

	@GnlColl.deleter
	def GnlColl(self):
		del self._GnlColl
		self._GnlColl = None

	@property
	def LnVal(self):
		return self._LnVal

	@LnVal.setter
	def LnVal(self, value):
		self._LnVal = value if type(value) != base_types.auto else self.make_default("LnVal")

	@LnVal.deleter
	def LnVal(self):
		del self._LnVal
		self._LnVal = None

	@property
	def LndgFee(self):
		return self._LndgFee

	@LndgFee.setter
	def LndgFee(self, value):
		self._LndgFee = value if type(value) != base_types.auto else self.make_default("LndgFee")

	@LndgFee.deleter
	def LndgFee(self):
		del self._LndgFee
		self._LndgFee = None

	@property
	def MstrAgrmt(self):
		return self._MstrAgrmt

	@MstrAgrmt.setter
	def MstrAgrmt(self, value):
		self._MstrAgrmt = value if type(value) != base_types.auto else self.make_default("MstrAgrmt")

	@MstrAgrmt.deleter
	def MstrAgrmt(self):
		del self._MstrAgrmt
		self._MstrAgrmt = None

	@property
	def RbtRate(self):
		return self._RbtRate

	@RbtRate.setter
	def RbtRate(self, value):
		self._RbtRate = value if type(value) != base_types.auto else self.make_default("RbtRate")

	@RbtRate.deleter
	def RbtRate(self):
		del self._RbtRate
		self._RbtRate = None

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if type(value) != base_types.auto else self.make_default("Term")

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = None

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if type(value) != base_types.auto else self.make_default("TermntnDt")

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = None

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != base_types.auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def UnqTradIdr(self):
		return self._UnqTradIdr

	@UnqTradIdr.setter
	def UnqTradIdr(self, value):
		self._UnqTradIdr = value if type(value) != base_types.auto else self.make_default("UnqTradIdr")

	@UnqTradIdr.deleter
	def UnqTradIdr(self):
		del self._UnqTradIdr
		self._UnqTradIdr = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstTp', type=SecurityCommodity9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSts', type=Cleared16Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollDlvryMtd', type=CollateralDeliveryMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryByVal', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlColl', type=SpecialCollateral1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LnVal', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LndgFee', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmt', type=MasterAgreement7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RbtRate', type=InterestRate27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Term', type=ContractTerm7Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TermntnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTradIdr', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

