import base_types
import CollateralDeliveryMethod1Code
import PrincipalAmount3
import Max52Text
import Max20PositiveNumber
import Cleared16Choice
import ISODate
import InterestRate27Choice
import ISODateTime
import SpecialCollateral1Code
import TrueFalseIndicator
import ContractTerm7Choice
import MasterAgreement7
import MICIdentifier

class LoanData135(base_types._BaseFieldType):

	__slots__ = ["_UnqTradIdr", "_TermntnDt", "_MstrAgrmt", "_MinNtcePrd", "_EarlstCallBckDt", "_Term", "_DlvryByVal", "_ValDt", "_CollDlvryMtd", "_ClrSts", "_ExctnDtTm", "_TradgVn", "_IntrstRate", "_EvtDt", "_GnlColl", "_PrncplAmt"]
	@property
	def UnqTradIdr(self):
		return self._UnqTradIdr

	@UnqTradIdr.setter
	def UnqTradIdr(self, value):
		self._UnqTradIdr = value if type(value) != auto else self.make_default("UnqTradIdr")

	@UnqTradIdr.deleter
	def UnqTradIdr(self):
		del self._UnqTradIdr
		self._UnqTradIdr = None

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if type(value) != auto else self.make_default("TermntnDt")

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = None

	@property
	def MstrAgrmt(self):
		return self._MstrAgrmt

	@MstrAgrmt.setter
	def MstrAgrmt(self, value):
		self._MstrAgrmt = value if type(value) != auto else self.make_default("MstrAgrmt")

	@MstrAgrmt.deleter
	def MstrAgrmt(self):
		del self._MstrAgrmt
		self._MstrAgrmt = None

	@property
	def MinNtcePrd(self):
		return self._MinNtcePrd

	@MinNtcePrd.setter
	def MinNtcePrd(self, value):
		self._MinNtcePrd = value if type(value) != auto else self.make_default("MinNtcePrd")

	@MinNtcePrd.deleter
	def MinNtcePrd(self):
		del self._MinNtcePrd
		self._MinNtcePrd = None

	@property
	def EarlstCallBckDt(self):
		return self._EarlstCallBckDt

	@EarlstCallBckDt.setter
	def EarlstCallBckDt(self, value):
		self._EarlstCallBckDt = value if type(value) != auto else self.make_default("EarlstCallBckDt")

	@EarlstCallBckDt.deleter
	def EarlstCallBckDt(self):
		del self._EarlstCallBckDt
		self._EarlstCallBckDt = None

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if type(value) != auto else self.make_default("Term")

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = None

	@property
	def DlvryByVal(self):
		return self._DlvryByVal

	@DlvryByVal.setter
	def DlvryByVal(self, value):
		self._DlvryByVal = value if type(value) != auto else self.make_default("DlvryByVal")

	@DlvryByVal.deleter
	def DlvryByVal(self):
		del self._DlvryByVal
		self._DlvryByVal = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def CollDlvryMtd(self):
		return self._CollDlvryMtd

	@CollDlvryMtd.setter
	def CollDlvryMtd(self, value):
		self._CollDlvryMtd = value if type(value) != auto else self.make_default("CollDlvryMtd")

	@CollDlvryMtd.deleter
	def CollDlvryMtd(self):
		del self._CollDlvryMtd
		self._CollDlvryMtd = None

	@property
	def ClrSts(self):
		return self._ClrSts

	@ClrSts.setter
	def ClrSts(self, value):
		self._ClrSts = value if type(value) != auto else self.make_default("ClrSts")

	@ClrSts.deleter
	def ClrSts(self):
		del self._ClrSts
		self._ClrSts = None

	@property
	def ExctnDtTm(self):
		return self._ExctnDtTm

	@ExctnDtTm.setter
	def ExctnDtTm(self, value):
		self._ExctnDtTm = value if type(value) != auto else self.make_default("ExctnDtTm")

	@ExctnDtTm.deleter
	def ExctnDtTm(self):
		del self._ExctnDtTm
		self._ExctnDtTm = None

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if type(value) != auto else self.make_default("EvtDt")

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = None

	@property
	def GnlColl(self):
		return self._GnlColl

	@GnlColl.setter
	def GnlColl(self, value):
		self._GnlColl = value if type(value) != auto else self.make_default("GnlColl")

	@GnlColl.deleter
	def GnlColl(self):
		del self._GnlColl
		self._GnlColl = None

	@property
	def PrncplAmt(self):
		return self._PrncplAmt

	@PrncplAmt.setter
	def PrncplAmt(self, value):
		self._PrncplAmt = value if type(value) != auto else self.make_default("PrncplAmt")

	@PrncplAmt.deleter
	def PrncplAmt(self):
		del self._PrncplAmt
		self._PrncplAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UnqTradIdr', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmt', type=MasterAgreement7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinNtcePrd', type=Max20PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlstCallBckDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Term', type=ContractTerm7Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvryByVal', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollDlvryMtd', type=CollateralDeliveryMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSts', type=Cleared16Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRate27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlColl', type=SpecialCollateral1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplAmt', type=PrincipalAmount3, min=0, max=1, mutex_group=None, array=False),
	))

