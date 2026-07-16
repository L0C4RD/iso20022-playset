# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account38
from . import ActiveCurrencyAndAmount
from . import AdditionalReference10
from . import BeneficiaryCertificationCompletion1Code
from . import DeliveryParameters4
from . import Fees2
from . import ForeignExchangeTerms37
from . import FormOfSecurity1Code
from . import FundSettlementParameters26
from . import ISODate
from . import IncomePreference2Code
from . import Intermediary43
from . import PartyIdentification139
from . import PhysicalTransferType1Code
from . import StampDutyType2Code
from . import Tax38
from . import YesNoIndicator

class DeliverInformation22(base_types._BaseFieldType):

	__slots__ = ["_BnfcryCertfctnCmpltn", "_ClntRef", "_DmtrlsdInd", "_FXDtls", "_Fees", "_IncmPref", "_IndvTax", "_IntrmyInf", "_NetAmt", "_PhysTrf", "_PhysTrfDtls", "_ReqdSttlmDt", "_ReqdTradDt", "_SctiesForm", "_StmpDty", "_SttlmAmt", "_SttlmPtiesDtls", "_Trfr", "_TrfrRegdAcct"]
	@property
	def BnfcryCertfctnCmpltn(self):
		return self._BnfcryCertfctnCmpltn

	@BnfcryCertfctnCmpltn.setter
	def BnfcryCertfctnCmpltn(self, value):
		self._BnfcryCertfctnCmpltn = value if value is not None else base_types.UninitialisedField(self, 'BnfcryCertfctnCmpltn', BeneficiaryCertificationCompletion1Code, False)

	@BnfcryCertfctnCmpltn.deleter
	def BnfcryCertfctnCmpltn(self):
		del self._BnfcryCertfctnCmpltn
		self._BnfcryCertfctnCmpltn = base_types.UninitialisedField(self, 'BnfcryCertfctnCmpltn', BeneficiaryCertificationCompletion1Code, False)

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if value is not None else base_types.UninitialisedField(self, 'ClntRef', AdditionalReference10, False)

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = base_types.UninitialisedField(self, 'ClntRef', AdditionalReference10, False)

	@property
	def DmtrlsdInd(self):
		return self._DmtrlsdInd

	@DmtrlsdInd.setter
	def DmtrlsdInd(self, value):
		self._DmtrlsdInd = value if value is not None else base_types.UninitialisedField(self, 'DmtrlsdInd', YesNoIndicator, False)

	@DmtrlsdInd.deleter
	def DmtrlsdInd(self):
		del self._DmtrlsdInd
		self._DmtrlsdInd = base_types.UninitialisedField(self, 'DmtrlsdInd', YesNoIndicator, False)

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms37, True)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms37, True)

	@property
	def Fees(self):
		return self._Fees

	@Fees.setter
	def Fees(self, value):
		self._Fees = value if value is not None else base_types.UninitialisedField(self, 'Fees', Fees2, True)

	@Fees.deleter
	def Fees(self):
		del self._Fees
		self._Fees = base_types.UninitialisedField(self, 'Fees', Fees2, True)

	@property
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if value is not None else base_types.UninitialisedField(self, 'IncmPref', IncomePreference2Code, False)

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = base_types.UninitialisedField(self, 'IncmPref', IncomePreference2Code, False)

	@property
	def IndvTax(self):
		return self._IndvTax

	@IndvTax.setter
	def IndvTax(self, value):
		self._IndvTax = value if value is not None else base_types.UninitialisedField(self, 'IndvTax', Tax38, True)

	@IndvTax.deleter
	def IndvTax(self):
		del self._IndvTax
		self._IndvTax = base_types.UninitialisedField(self, 'IndvTax', Tax38, True)

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if value is not None else base_types.UninitialisedField(self, 'IntrmyInf', Intermediary43, True)

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = base_types.UninitialisedField(self, 'IntrmyInf', Intermediary43, True)

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if value is not None else base_types.UninitialisedField(self, 'NetAmt', ActiveCurrencyAndAmount, False)

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = base_types.UninitialisedField(self, 'NetAmt', ActiveCurrencyAndAmount, False)

	@property
	def PhysTrf(self):
		return self._PhysTrf

	@PhysTrf.setter
	def PhysTrf(self, value):
		self._PhysTrf = value if value is not None else base_types.UninitialisedField(self, 'PhysTrf', PhysicalTransferType1Code, False)

	@PhysTrf.deleter
	def PhysTrf(self):
		del self._PhysTrf
		self._PhysTrf = base_types.UninitialisedField(self, 'PhysTrf', PhysicalTransferType1Code, False)

	@property
	def PhysTrfDtls(self):
		return self._PhysTrfDtls

	@PhysTrfDtls.setter
	def PhysTrfDtls(self, value):
		self._PhysTrfDtls = value if value is not None else base_types.UninitialisedField(self, 'PhysTrfDtls', DeliveryParameters4, False)

	@PhysTrfDtls.deleter
	def PhysTrfDtls(self):
		del self._PhysTrfDtls
		self._PhysTrfDtls = base_types.UninitialisedField(self, 'PhysTrfDtls', DeliveryParameters4, False)

	@property
	def ReqdSttlmDt(self):
		return self._ReqdSttlmDt

	@ReqdSttlmDt.setter
	def ReqdSttlmDt(self, value):
		self._ReqdSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdSttlmDt', ISODate, False)

	@ReqdSttlmDt.deleter
	def ReqdSttlmDt(self):
		del self._ReqdSttlmDt
		self._ReqdSttlmDt = base_types.UninitialisedField(self, 'ReqdSttlmDt', ISODate, False)

	@property
	def ReqdTradDt(self):
		return self._ReqdTradDt

	@ReqdTradDt.setter
	def ReqdTradDt(self, value):
		self._ReqdTradDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdTradDt', ISODate, False)

	@ReqdTradDt.deleter
	def ReqdTradDt(self):
		del self._ReqdTradDt
		self._ReqdTradDt = base_types.UninitialisedField(self, 'ReqdTradDt', ISODate, False)

	@property
	def SctiesForm(self):
		return self._SctiesForm

	@SctiesForm.setter
	def SctiesForm(self, value):
		self._SctiesForm = value if value is not None else base_types.UninitialisedField(self, 'SctiesForm', FormOfSecurity1Code, False)

	@SctiesForm.deleter
	def SctiesForm(self):
		del self._SctiesForm
		self._SctiesForm = base_types.UninitialisedField(self, 'SctiesForm', FormOfSecurity1Code, False)

	@property
	def StmpDty(self):
		return self._StmpDty

	@StmpDty.setter
	def StmpDty(self, value):
		self._StmpDty = value if value is not None else base_types.UninitialisedField(self, 'StmpDty', StampDutyType2Code, False)

	@StmpDty.deleter
	def StmpDty(self):
		del self._StmpDty
		self._StmpDty = base_types.UninitialisedField(self, 'StmpDty', StampDutyType2Code, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', ActiveCurrencyAndAmount, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', ActiveCurrencyAndAmount, False)

	@property
	def SttlmPtiesDtls(self):
		return self._SttlmPtiesDtls

	@SttlmPtiesDtls.setter
	def SttlmPtiesDtls(self, value):
		self._SttlmPtiesDtls = value if value is not None else base_types.UninitialisedField(self, 'SttlmPtiesDtls', FundSettlementParameters26, False)

	@SttlmPtiesDtls.deleter
	def SttlmPtiesDtls(self):
		del self._SttlmPtiesDtls
		self._SttlmPtiesDtls = base_types.UninitialisedField(self, 'SttlmPtiesDtls', FundSettlementParameters26, False)

	@property
	def Trfr(self):
		return self._Trfr

	@Trfr.setter
	def Trfr(self, value):
		self._Trfr = value if value is not None else base_types.UninitialisedField(self, 'Trfr', PartyIdentification139, False)

	@Trfr.deleter
	def Trfr(self):
		del self._Trfr
		self._Trfr = base_types.UninitialisedField(self, 'Trfr', PartyIdentification139, False)

	@property
	def TrfrRegdAcct(self):
		return self._TrfrRegdAcct

	@TrfrRegdAcct.setter
	def TrfrRegdAcct(self, value):
		self._TrfrRegdAcct = value if value is not None else base_types.UninitialisedField(self, 'TrfrRegdAcct', Account38, False)

	@TrfrRegdAcct.deleter
	def TrfrRegdAcct(self):
		del self._TrfrRegdAcct
		self._TrfrRegdAcct = base_types.UninitialisedField(self, 'TrfrRegdAcct', Account38, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BnfcryCertfctnCmpltn', type=BeneficiaryCertificationCompletion1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmtrlsdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms37, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Fees', type=Fees2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvTax', type=Tax38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysTrf', type=PhysicalTransferType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysTrfDtls', type=DeliveryParameters4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdTradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDty', type=StampDutyType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPtiesDtls', type=FundSettlementParameters26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trfr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfrRegdAcct', type=Account38, min=0, max=1, mutex_group=None, array=False),
	))