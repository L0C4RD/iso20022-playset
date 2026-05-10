from . import base_types
import ISODate
import YesNoIndicator
import DateAndDateTime2Choice
import IncomePreference2Code
import DeliveryParameters4
import ActiveCurrencyAndAmount
import AdditionalReference10
import PhysicalTransferType1Code
import FundSettlementParameters15
import ForeignExchangeTerms37
import FormOfSecurity1Code
import StampDutyType2Code
import Intermediary43
import PartyIdentification139
import Fees2
import BeneficiaryCertificationCompletion1Code
import Tax38
import Account31

class DeliverInformation20(base_types._BaseFieldType):

	__slots__ = ["_FctvSttlmDt", "_DmtrlsdInd", "_PhysTrf", "_SttlmPtiesDtls", "_FXDtls", "_ReqdSttlmDt", "_TrfrRegdAcct", "_SctiesForm", "_SttlmAmt", "_IncmPref", "_Fees", "_StmpDty", "_IndvTax", "_IntrmyInf", "_NetAmt", "_PhysTrfDtls", "_ClntRef", "_ReqdTradDt", "_BnfcryCertfctnCmpltn", "_Trfr"]
	@property
	def FctvSttlmDt(self):
		return self._FctvSttlmDt

	@FctvSttlmDt.setter
	def FctvSttlmDt(self, value):
		self._FctvSttlmDt = value if type(value) != auto else self.make_default("FctvSttlmDt")

	@FctvSttlmDt.deleter
	def FctvSttlmDt(self):
		del self._FctvSttlmDt
		self._FctvSttlmDt = None

	@property
	def DmtrlsdInd(self):
		return self._DmtrlsdInd

	@DmtrlsdInd.setter
	def DmtrlsdInd(self, value):
		self._DmtrlsdInd = value if type(value) != auto else self.make_default("DmtrlsdInd")

	@DmtrlsdInd.deleter
	def DmtrlsdInd(self):
		del self._DmtrlsdInd
		self._DmtrlsdInd = None

	@property
	def PhysTrf(self):
		return self._PhysTrf

	@PhysTrf.setter
	def PhysTrf(self, value):
		self._PhysTrf = value if type(value) != auto else self.make_default("PhysTrf")

	@PhysTrf.deleter
	def PhysTrf(self):
		del self._PhysTrf
		self._PhysTrf = None

	@property
	def SttlmPtiesDtls(self):
		return self._SttlmPtiesDtls

	@SttlmPtiesDtls.setter
	def SttlmPtiesDtls(self, value):
		self._SttlmPtiesDtls = value if type(value) != auto else self.make_default("SttlmPtiesDtls")

	@SttlmPtiesDtls.deleter
	def SttlmPtiesDtls(self):
		del self._SttlmPtiesDtls
		self._SttlmPtiesDtls = None

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if type(value) != auto else self.make_default("FXDtls")

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = None

	@property
	def ReqdSttlmDt(self):
		return self._ReqdSttlmDt

	@ReqdSttlmDt.setter
	def ReqdSttlmDt(self, value):
		self._ReqdSttlmDt = value if type(value) != auto else self.make_default("ReqdSttlmDt")

	@ReqdSttlmDt.deleter
	def ReqdSttlmDt(self):
		del self._ReqdSttlmDt
		self._ReqdSttlmDt = None

	@property
	def TrfrRegdAcct(self):
		return self._TrfrRegdAcct

	@TrfrRegdAcct.setter
	def TrfrRegdAcct(self, value):
		self._TrfrRegdAcct = value if type(value) != auto else self.make_default("TrfrRegdAcct")

	@TrfrRegdAcct.deleter
	def TrfrRegdAcct(self):
		del self._TrfrRegdAcct
		self._TrfrRegdAcct = None

	@property
	def SctiesForm(self):
		return self._SctiesForm

	@SctiesForm.setter
	def SctiesForm(self, value):
		self._SctiesForm = value if type(value) != auto else self.make_default("SctiesForm")

	@SctiesForm.deleter
	def SctiesForm(self):
		del self._SctiesForm
		self._SctiesForm = None

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if type(value) != auto else self.make_default("IncmPref")

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = None

	@property
	def Fees(self):
		return self._Fees

	@Fees.setter
	def Fees(self, value):
		self._Fees = value if type(value) != auto else self.make_default("Fees")

	@Fees.deleter
	def Fees(self):
		del self._Fees
		self._Fees = None

	@property
	def StmpDty(self):
		return self._StmpDty

	@StmpDty.setter
	def StmpDty(self, value):
		self._StmpDty = value if type(value) != auto else self.make_default("StmpDty")

	@StmpDty.deleter
	def StmpDty(self):
		del self._StmpDty
		self._StmpDty = None

	@property
	def IndvTax(self):
		return self._IndvTax

	@IndvTax.setter
	def IndvTax(self, value):
		self._IndvTax = value if type(value) != auto else self.make_default("IndvTax")

	@IndvTax.deleter
	def IndvTax(self):
		del self._IndvTax
		self._IndvTax = None

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if type(value) != auto else self.make_default("IntrmyInf")

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	@property
	def PhysTrfDtls(self):
		return self._PhysTrfDtls

	@PhysTrfDtls.setter
	def PhysTrfDtls(self, value):
		self._PhysTrfDtls = value if type(value) != auto else self.make_default("PhysTrfDtls")

	@PhysTrfDtls.deleter
	def PhysTrfDtls(self):
		del self._PhysTrfDtls
		self._PhysTrfDtls = None

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def ReqdTradDt(self):
		return self._ReqdTradDt

	@ReqdTradDt.setter
	def ReqdTradDt(self, value):
		self._ReqdTradDt = value if type(value) != auto else self.make_default("ReqdTradDt")

	@ReqdTradDt.deleter
	def ReqdTradDt(self):
		del self._ReqdTradDt
		self._ReqdTradDt = None

	@property
	def BnfcryCertfctnCmpltn(self):
		return self._BnfcryCertfctnCmpltn

	@BnfcryCertfctnCmpltn.setter
	def BnfcryCertfctnCmpltn(self, value):
		self._BnfcryCertfctnCmpltn = value if type(value) != auto else self.make_default("BnfcryCertfctnCmpltn")

	@BnfcryCertfctnCmpltn.deleter
	def BnfcryCertfctnCmpltn(self):
		del self._BnfcryCertfctnCmpltn
		self._BnfcryCertfctnCmpltn = None

	@property
	def Trfr(self):
		return self._Trfr

	@Trfr.setter
	def Trfr(self, value):
		self._Trfr = value if type(value) != auto else self.make_default("Trfr")

	@Trfr.deleter
	def Trfr(self):
		del self._Trfr
		self._Trfr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FctvSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmtrlsdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysTrf', type=PhysicalTransferType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPtiesDtls', type=FundSettlementParameters15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms37, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqdSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfrRegdAcct', type=Account31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fees', type=Fees2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmpDty', type=StampDutyType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvTax', type=Tax38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysTrfDtls', type=DeliveryParameters4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdTradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryCertfctnCmpltn', type=BeneficiaryCertificationCompletion1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trfr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
	))

