# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import CreditDebit3Code
from . import DecimalNumber
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Max10Text
from . import Max256Text
from . import Max35Text
from . import Max50Text
from . import Max70Text
from . import Tax41
from . import TrueFalseIndicator
from . import UnitOfMeasure1Code

class InvoiceLineItem3(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_AdjstmntAmt", "_AdjstmntCdtDbt", "_AdjstmntRsn", "_CdtDbt", "_CtrctNb", "_Desc", "_Dt", "_Insrnc", "_InsrncAmt", "_MdclSvcs", "_OrdrDt", "_OthrUnitOfMeasr", "_PdctCd", "_PdctQlfr", "_PdctQty", "_Rbllg", "_ShipToIndstryCd", "_ShppgDt", "_Tax", "_TpOfSpply", "_TtlAmt", "_UnitOfMeasr", "_UnitPric", "_VATInvcRef", "_ZeroCostToCstmr"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def AdjstmntAmt(self):
		return self._AdjstmntAmt

	@AdjstmntAmt.setter
	def AdjstmntAmt(self, value):
		self._AdjstmntAmt = value if value is not None else base_types.UninitialisedField(self, 'AdjstmntAmt', ImpliedCurrencyAndAmount, False)

	@AdjstmntAmt.deleter
	def AdjstmntAmt(self):
		del self._AdjstmntAmt
		self._AdjstmntAmt = base_types.UninitialisedField(self, 'AdjstmntAmt', ImpliedCurrencyAndAmount, False)

	@property
	def AdjstmntCdtDbt(self):
		return self._AdjstmntCdtDbt

	@AdjstmntCdtDbt.setter
	def AdjstmntCdtDbt(self, value):
		self._AdjstmntCdtDbt = value if value is not None else base_types.UninitialisedField(self, 'AdjstmntCdtDbt', CreditDebit3Code, False)

	@AdjstmntCdtDbt.deleter
	def AdjstmntCdtDbt(self):
		del self._AdjstmntCdtDbt
		self._AdjstmntCdtDbt = base_types.UninitialisedField(self, 'AdjstmntCdtDbt', CreditDebit3Code, False)

	@property
	def AdjstmntRsn(self):
		return self._AdjstmntRsn

	@AdjstmntRsn.setter
	def AdjstmntRsn(self, value):
		self._AdjstmntRsn = value if value is not None else base_types.UninitialisedField(self, 'AdjstmntRsn', Max35Text, False)

	@AdjstmntRsn.deleter
	def AdjstmntRsn(self):
		del self._AdjstmntRsn
		self._AdjstmntRsn = base_types.UninitialisedField(self, 'AdjstmntRsn', Max35Text, False)

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if value is not None else base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@property
	def CtrctNb(self):
		return self._CtrctNb

	@CtrctNb.setter
	def CtrctNb(self, value):
		self._CtrctNb = value if value is not None else base_types.UninitialisedField(self, 'CtrctNb', Max70Text, False)

	@CtrctNb.deleter
	def CtrctNb(self):
		del self._CtrctNb
		self._CtrctNb = base_types.UninitialisedField(self, 'CtrctNb', Max70Text, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max256Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max256Text, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if value is not None else base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@property
	def InsrncAmt(self):
		return self._InsrncAmt

	@InsrncAmt.setter
	def InsrncAmt(self, value):
		self._InsrncAmt = value if value is not None else base_types.UninitialisedField(self, 'InsrncAmt', ImpliedCurrencyAndAmount, False)

	@InsrncAmt.deleter
	def InsrncAmt(self):
		del self._InsrncAmt
		self._InsrncAmt = base_types.UninitialisedField(self, 'InsrncAmt', ImpliedCurrencyAndAmount, False)

	@property
	def MdclSvcs(self):
		return self._MdclSvcs

	@MdclSvcs.setter
	def MdclSvcs(self, value):
		self._MdclSvcs = value if value is not None else base_types.UninitialisedField(self, 'MdclSvcs', TrueFalseIndicator, False)

	@MdclSvcs.deleter
	def MdclSvcs(self):
		del self._MdclSvcs
		self._MdclSvcs = base_types.UninitialisedField(self, 'MdclSvcs', TrueFalseIndicator, False)

	@property
	def OrdrDt(self):
		return self._OrdrDt

	@OrdrDt.setter
	def OrdrDt(self, value):
		self._OrdrDt = value if value is not None else base_types.UninitialisedField(self, 'OrdrDt', ISODate, False)

	@OrdrDt.deleter
	def OrdrDt(self):
		del self._OrdrDt
		self._OrdrDt = base_types.UninitialisedField(self, 'OrdrDt', ISODate, False)

	@property
	def OthrUnitOfMeasr(self):
		return self._OthrUnitOfMeasr

	@OthrUnitOfMeasr.setter
	def OthrUnitOfMeasr(self, value):
		self._OthrUnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'OthrUnitOfMeasr', Max35Text, False)

	@OthrUnitOfMeasr.deleter
	def OthrUnitOfMeasr(self):
		del self._OthrUnitOfMeasr
		self._OthrUnitOfMeasr = base_types.UninitialisedField(self, 'OthrUnitOfMeasr', Max35Text, False)

	@property
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if value is not None else base_types.UninitialisedField(self, 'PdctCd', Max70Text, False)

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = base_types.UninitialisedField(self, 'PdctCd', Max70Text, False)

	@property
	def PdctQlfr(self):
		return self._PdctQlfr

	@PdctQlfr.setter
	def PdctQlfr(self, value):
		self._PdctQlfr = value if value is not None else base_types.UninitialisedField(self, 'PdctQlfr', Max35Text, False)

	@PdctQlfr.deleter
	def PdctQlfr(self):
		del self._PdctQlfr
		self._PdctQlfr = base_types.UninitialisedField(self, 'PdctQlfr', Max35Text, False)

	@property
	def PdctQty(self):
		return self._PdctQty

	@PdctQty.setter
	def PdctQty(self, value):
		self._PdctQty = value if value is not None else base_types.UninitialisedField(self, 'PdctQty', DecimalNumber, False)

	@PdctQty.deleter
	def PdctQty(self):
		del self._PdctQty
		self._PdctQty = base_types.UninitialisedField(self, 'PdctQty', DecimalNumber, False)

	@property
	def Rbllg(self):
		return self._Rbllg

	@Rbllg.setter
	def Rbllg(self, value):
		self._Rbllg = value if value is not None else base_types.UninitialisedField(self, 'Rbllg', TrueFalseIndicator, False)

	@Rbllg.deleter
	def Rbllg(self):
		del self._Rbllg
		self._Rbllg = base_types.UninitialisedField(self, 'Rbllg', TrueFalseIndicator, False)

	@property
	def ShipToIndstryCd(self):
		return self._ShipToIndstryCd

	@ShipToIndstryCd.setter
	def ShipToIndstryCd(self, value):
		self._ShipToIndstryCd = value if value is not None else base_types.UninitialisedField(self, 'ShipToIndstryCd', Max50Text, False)

	@ShipToIndstryCd.deleter
	def ShipToIndstryCd(self):
		del self._ShipToIndstryCd
		self._ShipToIndstryCd = base_types.UninitialisedField(self, 'ShipToIndstryCd', Max50Text, False)

	@property
	def ShppgDt(self):
		return self._ShppgDt

	@ShppgDt.setter
	def ShppgDt(self, value):
		self._ShppgDt = value if value is not None else base_types.UninitialisedField(self, 'ShppgDt', ISODate, False)

	@ShppgDt.deleter
	def ShppgDt(self):
		del self._ShppgDt
		self._ShppgDt = base_types.UninitialisedField(self, 'ShppgDt', ISODate, False)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', Tax41, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', Tax41, True)

	@property
	def TpOfSpply(self):
		return self._TpOfSpply

	@TpOfSpply.setter
	def TpOfSpply(self, value):
		self._TpOfSpply = value if value is not None else base_types.UninitialisedField(self, 'TpOfSpply', Max10Text, False)

	@TpOfSpply.deleter
	def TpOfSpply(self):
		del self._TpOfSpply
		self._TpOfSpply = base_types.UninitialisedField(self, 'TpOfSpply', Max10Text, False)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure1Code, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure1Code, False)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', ImpliedCurrencyAndAmount, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', ImpliedCurrencyAndAmount, False)

	@property
	def VATInvcRef(self):
		return self._VATInvcRef

	@VATInvcRef.setter
	def VATInvcRef(self, value):
		self._VATInvcRef = value if value is not None else base_types.UninitialisedField(self, 'VATInvcRef', Max35Text, False)

	@VATInvcRef.deleter
	def VATInvcRef(self):
		del self._VATInvcRef
		self._VATInvcRef = base_types.UninitialisedField(self, 'VATInvcRef', Max35Text, False)

	@property
	def ZeroCostToCstmr(self):
		return self._ZeroCostToCstmr

	@ZeroCostToCstmr.setter
	def ZeroCostToCstmr(self, value):
		self._ZeroCostToCstmr = value if value is not None else base_types.UninitialisedField(self, 'ZeroCostToCstmr', TrueFalseIndicator, False)

	@ZeroCostToCstmr.deleter
	def ZeroCostToCstmr(self):
		del self._ZeroCostToCstmr
		self._ZeroCostToCstmr = base_types.UninitialisedField(self, 'ZeroCostToCstmr', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdjstmntAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdjstmntCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdjstmntRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdclSvcs', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrUnitOfMeasr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQlfr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rbllg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShipToIndstryCd', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TpOfSpply', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VATInvcRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ZeroCostToCstmr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))