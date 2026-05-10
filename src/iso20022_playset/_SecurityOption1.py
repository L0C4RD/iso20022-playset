from . import base_types
from ._UnitOrFaceAmount1Choice import UnitOrFaceAmount1Choice
from ._CorporateActionPrice4 import CorporateActionPrice4
from ._CreditDebitCode import CreditDebitCode
from ._ShareRanking1FormatChoice import ShareRanking1FormatChoice
from ._FractionDispositionType1FormatChoice import FractionDispositionType1FormatChoice
from ._Period1 import Period1
from ._FinancialInstrumentDescription3 import FinancialInstrumentDescription3
from ._CorporateActionDate3 import CorporateActionDate3
from ._YesNoIndicator import YesNoIndicator
from ._QuantityToQuantityRatio1 import QuantityToQuantityRatio1

class SecurityOption1(base_types._BaseFieldType):

	__slots__ = ["_NewDnmtnSctiesQty", "_NewBrdLotSctiesQty", "_AddtlQtyForExstgScties", "_FrctnDspstn", "_SctiesQty", "_MinExrcblSctiesQty", "_DtDtls", "_AddtlQtyForSbcbdRsltntScties", "_PricDtls", "_ShrRnkg", "_SctyId", "_TempFinInstrmInd", "_TradgPrd", "_CdtDbtInd", "_MinExrcblMltplSctiesQty"]
	@property
	def NewDnmtnSctiesQty(self):
		return self._NewDnmtnSctiesQty

	@NewDnmtnSctiesQty.setter
	def NewDnmtnSctiesQty(self, value):
		self._NewDnmtnSctiesQty = value if type(value) != base_types.auto else self.make_default("NewDnmtnSctiesQty")

	@NewDnmtnSctiesQty.deleter
	def NewDnmtnSctiesQty(self):
		del self._NewDnmtnSctiesQty
		self._NewDnmtnSctiesQty = None

	@property
	def NewBrdLotSctiesQty(self):
		return self._NewBrdLotSctiesQty

	@NewBrdLotSctiesQty.setter
	def NewBrdLotSctiesQty(self, value):
		self._NewBrdLotSctiesQty = value if type(value) != base_types.auto else self.make_default("NewBrdLotSctiesQty")

	@NewBrdLotSctiesQty.deleter
	def NewBrdLotSctiesQty(self):
		del self._NewBrdLotSctiesQty
		self._NewBrdLotSctiesQty = None

	@property
	def AddtlQtyForExstgScties(self):
		return self._AddtlQtyForExstgScties

	@AddtlQtyForExstgScties.setter
	def AddtlQtyForExstgScties(self, value):
		self._AddtlQtyForExstgScties = value if type(value) != base_types.auto else self.make_default("AddtlQtyForExstgScties")

	@AddtlQtyForExstgScties.deleter
	def AddtlQtyForExstgScties(self):
		del self._AddtlQtyForExstgScties
		self._AddtlQtyForExstgScties = None

	@property
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if type(value) != base_types.auto else self.make_default("FrctnDspstn")

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = None

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if type(value) != base_types.auto else self.make_default("SctiesQty")

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = None

	@property
	def MinExrcblSctiesQty(self):
		return self._MinExrcblSctiesQty

	@MinExrcblSctiesQty.setter
	def MinExrcblSctiesQty(self, value):
		self._MinExrcblSctiesQty = value if type(value) != base_types.auto else self.make_default("MinExrcblSctiesQty")

	@MinExrcblSctiesQty.deleter
	def MinExrcblSctiesQty(self):
		del self._MinExrcblSctiesQty
		self._MinExrcblSctiesQty = None

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if type(value) != base_types.auto else self.make_default("DtDtls")

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = None

	@property
	def AddtlQtyForSbcbdRsltntScties(self):
		return self._AddtlQtyForSbcbdRsltntScties

	@AddtlQtyForSbcbdRsltntScties.setter
	def AddtlQtyForSbcbdRsltntScties(self, value):
		self._AddtlQtyForSbcbdRsltntScties = value if type(value) != base_types.auto else self.make_default("AddtlQtyForSbcbdRsltntScties")

	@AddtlQtyForSbcbdRsltntScties.deleter
	def AddtlQtyForSbcbdRsltntScties(self):
		del self._AddtlQtyForSbcbdRsltntScties
		self._AddtlQtyForSbcbdRsltntScties = None

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != base_types.auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def ShrRnkg(self):
		return self._ShrRnkg

	@ShrRnkg.setter
	def ShrRnkg(self, value):
		self._ShrRnkg = value if type(value) != base_types.auto else self.make_default("ShrRnkg")

	@ShrRnkg.deleter
	def ShrRnkg(self):
		del self._ShrRnkg
		self._ShrRnkg = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != base_types.auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	@property
	def TempFinInstrmInd(self):
		return self._TempFinInstrmInd

	@TempFinInstrmInd.setter
	def TempFinInstrmInd(self, value):
		self._TempFinInstrmInd = value if type(value) != base_types.auto else self.make_default("TempFinInstrmInd")

	@TempFinInstrmInd.deleter
	def TempFinInstrmInd(self):
		del self._TempFinInstrmInd
		self._TempFinInstrmInd = None

	@property
	def TradgPrd(self):
		return self._TradgPrd

	@TradgPrd.setter
	def TradgPrd(self, value):
		self._TradgPrd = value if type(value) != base_types.auto else self.make_default("TradgPrd")

	@TradgPrd.deleter
	def TradgPrd(self):
		del self._TradgPrd
		self._TradgPrd = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def MinExrcblMltplSctiesQty(self):
		return self._MinExrcblMltplSctiesQty

	@MinExrcblMltplSctiesQty.setter
	def MinExrcblMltplSctiesQty(self, value):
		self._MinExrcblMltplSctiesQty = value if type(value) != base_types.auto else self.make_default("MinExrcblMltplSctiesQty")

	@MinExrcblMltplSctiesQty.deleter
	def MinExrcblMltplSctiesQty(self):
		del self._MinExrcblMltplSctiesQty
		self._MinExrcblMltplSctiesQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewDnmtnSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewBrdLotSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlQtyForExstgScties', type=QuantityToQuantityRatio1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinExrcblSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlQtyForSbcbdRsltntScties', type=QuantityToQuantityRatio1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrRnkg', type=ShareRanking1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=FinancialInstrumentDescription3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempFinInstrmInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinExrcblMltplSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
	))

