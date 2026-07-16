# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import Cleared16Choice
from . import CollateralDeliveryMethod1Code
from . import ContractTerm7Choice
from . import ISODate
from . import ISODateTime
from . import InterestRate27Choice
from . import MICIdentifier
from . import MasterAgreement7
from . import Max52Text
from . import PercentageRate
from . import SecurityCommodity9
from . import SpecialCollateral1Code
from . import TrueFalseIndicator

class LoanData145(base_types._BaseFieldType):

	__slots__ = ["_AsstTp", "_ClrSts", "_CollDlvryMtd", "_DlvryByVal", "_EvtDt", "_ExctnDtTm", "_GnlColl", "_LnVal", "_LndgFee", "_MstrAgrmt", "_RbtRate", "_Term", "_TermntnDt", "_TradgVn", "_UnqTradIdr", "_ValDt"]
	@property
	def AsstTp(self):
		return self._AsstTp

	@AsstTp.setter
	def AsstTp(self, value):
		self._AsstTp = value if value is not None else base_types.UninitialisedField(self, 'AsstTp', SecurityCommodity9, False)

	@AsstTp.deleter
	def AsstTp(self):
		del self._AsstTp
		self._AsstTp = base_types.UninitialisedField(self, 'AsstTp', SecurityCommodity9, False)

	@property
	def ClrSts(self):
		return self._ClrSts

	@ClrSts.setter
	def ClrSts(self, value):
		self._ClrSts = value if value is not None else base_types.UninitialisedField(self, 'ClrSts', Cleared16Choice, False)

	@ClrSts.deleter
	def ClrSts(self):
		del self._ClrSts
		self._ClrSts = base_types.UninitialisedField(self, 'ClrSts', Cleared16Choice, False)

	@property
	def CollDlvryMtd(self):
		return self._CollDlvryMtd

	@CollDlvryMtd.setter
	def CollDlvryMtd(self, value):
		self._CollDlvryMtd = value if value is not None else base_types.UninitialisedField(self, 'CollDlvryMtd', CollateralDeliveryMethod1Code, False)

	@CollDlvryMtd.deleter
	def CollDlvryMtd(self):
		del self._CollDlvryMtd
		self._CollDlvryMtd = base_types.UninitialisedField(self, 'CollDlvryMtd', CollateralDeliveryMethod1Code, False)

	@property
	def DlvryByVal(self):
		return self._DlvryByVal

	@DlvryByVal.setter
	def DlvryByVal(self, value):
		self._DlvryByVal = value if value is not None else base_types.UninitialisedField(self, 'DlvryByVal', TrueFalseIndicator, False)

	@DlvryByVal.deleter
	def DlvryByVal(self):
		del self._DlvryByVal
		self._DlvryByVal = base_types.UninitialisedField(self, 'DlvryByVal', TrueFalseIndicator, False)

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if value is not None else base_types.UninitialisedField(self, 'EvtDt', ISODate, False)

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = base_types.UninitialisedField(self, 'EvtDt', ISODate, False)

	@property
	def ExctnDtTm(self):
		return self._ExctnDtTm

	@ExctnDtTm.setter
	def ExctnDtTm(self, value):
		self._ExctnDtTm = value if value is not None else base_types.UninitialisedField(self, 'ExctnDtTm', ISODateTime, False)

	@ExctnDtTm.deleter
	def ExctnDtTm(self):
		del self._ExctnDtTm
		self._ExctnDtTm = base_types.UninitialisedField(self, 'ExctnDtTm', ISODateTime, False)

	@property
	def GnlColl(self):
		return self._GnlColl

	@GnlColl.setter
	def GnlColl(self, value):
		self._GnlColl = value if value is not None else base_types.UninitialisedField(self, 'GnlColl', SpecialCollateral1Code, False)

	@GnlColl.deleter
	def GnlColl(self):
		del self._GnlColl
		self._GnlColl = base_types.UninitialisedField(self, 'GnlColl', SpecialCollateral1Code, False)

	@property
	def LnVal(self):
		return self._LnVal

	@LnVal.setter
	def LnVal(self, value):
		self._LnVal = value if value is not None else base_types.UninitialisedField(self, 'LnVal', ActiveOrHistoricCurrencyAndAmount, False)

	@LnVal.deleter
	def LnVal(self):
		del self._LnVal
		self._LnVal = base_types.UninitialisedField(self, 'LnVal', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def LndgFee(self):
		return self._LndgFee

	@LndgFee.setter
	def LndgFee(self, value):
		self._LndgFee = value if value is not None else base_types.UninitialisedField(self, 'LndgFee', PercentageRate, False)

	@LndgFee.deleter
	def LndgFee(self):
		del self._LndgFee
		self._LndgFee = base_types.UninitialisedField(self, 'LndgFee', PercentageRate, False)

	@property
	def MstrAgrmt(self):
		return self._MstrAgrmt

	@MstrAgrmt.setter
	def MstrAgrmt(self, value):
		self._MstrAgrmt = value if value is not None else base_types.UninitialisedField(self, 'MstrAgrmt', MasterAgreement7, False)

	@MstrAgrmt.deleter
	def MstrAgrmt(self):
		del self._MstrAgrmt
		self._MstrAgrmt = base_types.UninitialisedField(self, 'MstrAgrmt', MasterAgreement7, False)

	@property
	def RbtRate(self):
		return self._RbtRate

	@RbtRate.setter
	def RbtRate(self, value):
		self._RbtRate = value if value is not None else base_types.UninitialisedField(self, 'RbtRate', InterestRate27Choice, False)

	@RbtRate.deleter
	def RbtRate(self):
		del self._RbtRate
		self._RbtRate = base_types.UninitialisedField(self, 'RbtRate', InterestRate27Choice, False)

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if value is not None else base_types.UninitialisedField(self, 'Term', ContractTerm7Choice, True)

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = base_types.UninitialisedField(self, 'Term', ContractTerm7Choice, True)

	@property
	def TermntnDt(self):
		return self._TermntnDt

	@TermntnDt.setter
	def TermntnDt(self, value):
		self._TermntnDt = value if value is not None else base_types.UninitialisedField(self, 'TermntnDt', ISODate, False)

	@TermntnDt.deleter
	def TermntnDt(self):
		del self._TermntnDt
		self._TermntnDt = base_types.UninitialisedField(self, 'TermntnDt', ISODate, False)

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if value is not None else base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, False)

	@property
	def UnqTradIdr(self):
		return self._UnqTradIdr

	@UnqTradIdr.setter
	def UnqTradIdr(self, value):
		self._UnqTradIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqTradIdr', Max52Text, False)

	@UnqTradIdr.deleter
	def UnqTradIdr(self):
		del self._UnqTradIdr
		self._UnqTradIdr = base_types.UninitialisedField(self, 'UnqTradIdr', Max52Text, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', ISODate, False)

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