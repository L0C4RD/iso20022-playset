from . import base_types
from ._Max10Text import Max10Text
from ._Max70Text import Max70Text
from ._UnitOfMeasure1Code import UnitOfMeasure1Code
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max35Text import Max35Text
from ._Tax41 import Tax41
from ._TrueFalseIndicator import TrueFalseIndicator
from ._AdditionalData1 import AdditionalData1
from ._CreditDebit3Code import CreditDebit3Code
from ._Max256Text import Max256Text
from ._Max50Text import Max50Text
from ._ISODate import ISODate
from ._DecimalNumber import DecimalNumber

class InvoiceLineItem3(base_types._BaseFieldType):

	__slots__ = ["_CdtDbt", "_AdjstmntCdtDbt", "_Desc", "_PdctQty", "_Insrnc", "_Rbllg", "_PdctCd", "_OthrUnitOfMeasr", "_PdctQlfr", "_UnitOfMeasr", "_ShppgDt", "_Dt", "_TtlAmt", "_CtrctNb", "_ShipToIndstryCd", "_AdjstmntAmt", "_AddtlData", "_VATInvcRef", "_AdjstmntRsn", "_MdclSvcs", "_UnitPric", "_ZeroCostToCstmr", "_InsrncAmt", "_TpOfSpply", "_Tax", "_OrdrDt"]
	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if type(value) != base_types.auto else self.make_default("CdtDbt")

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = None

	@property
	def AdjstmntCdtDbt(self):
		return self._AdjstmntCdtDbt

	@AdjstmntCdtDbt.setter
	def AdjstmntCdtDbt(self, value):
		self._AdjstmntCdtDbt = value if type(value) != base_types.auto else self.make_default("AdjstmntCdtDbt")

	@AdjstmntCdtDbt.deleter
	def AdjstmntCdtDbt(self):
		del self._AdjstmntCdtDbt
		self._AdjstmntCdtDbt = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def PdctQty(self):
		return self._PdctQty

	@PdctQty.setter
	def PdctQty(self, value):
		self._PdctQty = value if type(value) != base_types.auto else self.make_default("PdctQty")

	@PdctQty.deleter
	def PdctQty(self):
		del self._PdctQty
		self._PdctQty = None

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if type(value) != base_types.auto else self.make_default("Insrnc")

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = None

	@property
	def Rbllg(self):
		return self._Rbllg

	@Rbllg.setter
	def Rbllg(self, value):
		self._Rbllg = value if type(value) != base_types.auto else self.make_default("Rbllg")

	@Rbllg.deleter
	def Rbllg(self):
		del self._Rbllg
		self._Rbllg = None

	@property
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if type(value) != base_types.auto else self.make_default("PdctCd")

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = None

	@property
	def OthrUnitOfMeasr(self):
		return self._OthrUnitOfMeasr

	@OthrUnitOfMeasr.setter
	def OthrUnitOfMeasr(self, value):
		self._OthrUnitOfMeasr = value if type(value) != base_types.auto else self.make_default("OthrUnitOfMeasr")

	@OthrUnitOfMeasr.deleter
	def OthrUnitOfMeasr(self):
		del self._OthrUnitOfMeasr
		self._OthrUnitOfMeasr = None

	@property
	def PdctQlfr(self):
		return self._PdctQlfr

	@PdctQlfr.setter
	def PdctQlfr(self, value):
		self._PdctQlfr = value if type(value) != base_types.auto else self.make_default("PdctQlfr")

	@PdctQlfr.deleter
	def PdctQlfr(self):
		del self._PdctQlfr
		self._PdctQlfr = None

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != base_types.auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

	@property
	def ShppgDt(self):
		return self._ShppgDt

	@ShppgDt.setter
	def ShppgDt(self, value):
		self._ShppgDt = value if type(value) != base_types.auto else self.make_default("ShppgDt")

	@ShppgDt.deleter
	def ShppgDt(self):
		del self._ShppgDt
		self._ShppgDt = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != base_types.auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def CtrctNb(self):
		return self._CtrctNb

	@CtrctNb.setter
	def CtrctNb(self, value):
		self._CtrctNb = value if type(value) != base_types.auto else self.make_default("CtrctNb")

	@CtrctNb.deleter
	def CtrctNb(self):
		del self._CtrctNb
		self._CtrctNb = None

	@property
	def ShipToIndstryCd(self):
		return self._ShipToIndstryCd

	@ShipToIndstryCd.setter
	def ShipToIndstryCd(self, value):
		self._ShipToIndstryCd = value if type(value) != base_types.auto else self.make_default("ShipToIndstryCd")

	@ShipToIndstryCd.deleter
	def ShipToIndstryCd(self):
		del self._ShipToIndstryCd
		self._ShipToIndstryCd = None

	@property
	def AdjstmntAmt(self):
		return self._AdjstmntAmt

	@AdjstmntAmt.setter
	def AdjstmntAmt(self, value):
		self._AdjstmntAmt = value if type(value) != base_types.auto else self.make_default("AdjstmntAmt")

	@AdjstmntAmt.deleter
	def AdjstmntAmt(self):
		del self._AdjstmntAmt
		self._AdjstmntAmt = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def VATInvcRef(self):
		return self._VATInvcRef

	@VATInvcRef.setter
	def VATInvcRef(self, value):
		self._VATInvcRef = value if type(value) != base_types.auto else self.make_default("VATInvcRef")

	@VATInvcRef.deleter
	def VATInvcRef(self):
		del self._VATInvcRef
		self._VATInvcRef = None

	@property
	def AdjstmntRsn(self):
		return self._AdjstmntRsn

	@AdjstmntRsn.setter
	def AdjstmntRsn(self, value):
		self._AdjstmntRsn = value if type(value) != base_types.auto else self.make_default("AdjstmntRsn")

	@AdjstmntRsn.deleter
	def AdjstmntRsn(self):
		del self._AdjstmntRsn
		self._AdjstmntRsn = None

	@property
	def MdclSvcs(self):
		return self._MdclSvcs

	@MdclSvcs.setter
	def MdclSvcs(self, value):
		self._MdclSvcs = value if type(value) != base_types.auto else self.make_default("MdclSvcs")

	@MdclSvcs.deleter
	def MdclSvcs(self):
		del self._MdclSvcs
		self._MdclSvcs = None

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != base_types.auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	@property
	def ZeroCostToCstmr(self):
		return self._ZeroCostToCstmr

	@ZeroCostToCstmr.setter
	def ZeroCostToCstmr(self, value):
		self._ZeroCostToCstmr = value if type(value) != base_types.auto else self.make_default("ZeroCostToCstmr")

	@ZeroCostToCstmr.deleter
	def ZeroCostToCstmr(self):
		del self._ZeroCostToCstmr
		self._ZeroCostToCstmr = None

	@property
	def InsrncAmt(self):
		return self._InsrncAmt

	@InsrncAmt.setter
	def InsrncAmt(self, value):
		self._InsrncAmt = value if type(value) != base_types.auto else self.make_default("InsrncAmt")

	@InsrncAmt.deleter
	def InsrncAmt(self):
		del self._InsrncAmt
		self._InsrncAmt = None

	@property
	def TpOfSpply(self):
		return self._TpOfSpply

	@TpOfSpply.setter
	def TpOfSpply(self, value):
		self._TpOfSpply = value if type(value) != base_types.auto else self.make_default("TpOfSpply")

	@TpOfSpply.deleter
	def TpOfSpply(self):
		del self._TpOfSpply
		self._TpOfSpply = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def OrdrDt(self):
		return self._OrdrDt

	@OrdrDt.setter
	def OrdrDt(self, value):
		self._OrdrDt = value if type(value) != base_types.auto else self.make_default("OrdrDt")

	@OrdrDt.deleter
	def OrdrDt(self):
		del self._OrdrDt
		self._OrdrDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdjstmntCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rbllg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrUnitOfMeasr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQlfr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShipToIndstryCd', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdjstmntAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VATInvcRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdjstmntRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdclSvcs', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ZeroCostToCstmr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfSpply', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrdrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

