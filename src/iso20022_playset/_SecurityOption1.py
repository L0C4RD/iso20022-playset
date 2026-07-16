# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionDate3
from . import CorporateActionPrice4
from . import CreditDebitCode
from . import FinancialInstrumentDescription3
from . import FractionDispositionType1FormatChoice
from . import Period1
from . import QuantityToQuantityRatio1
from . import ShareRanking1FormatChoice
from . import UnitOrFaceAmount1Choice
from . import YesNoIndicator

class SecurityOption1(base_types._BaseFieldType):

	__slots__ = ["_AddtlQtyForExstgScties", "_AddtlQtyForSbcbdRsltntScties", "_CdtDbtInd", "_DtDtls", "_FrctnDspstn", "_MinExrcblMltplSctiesQty", "_MinExrcblSctiesQty", "_NewBrdLotSctiesQty", "_NewDnmtnSctiesQty", "_PricDtls", "_SctiesQty", "_SctyId", "_ShrRnkg", "_TempFinInstrmInd", "_TradgPrd"]
	@property
	def AddtlQtyForExstgScties(self):
		return self._AddtlQtyForExstgScties

	@AddtlQtyForExstgScties.setter
	def AddtlQtyForExstgScties(self, value):
		self._AddtlQtyForExstgScties = value if value is not None else base_types.UninitialisedField(self, 'AddtlQtyForExstgScties', QuantityToQuantityRatio1, False)

	@AddtlQtyForExstgScties.deleter
	def AddtlQtyForExstgScties(self):
		del self._AddtlQtyForExstgScties
		self._AddtlQtyForExstgScties = base_types.UninitialisedField(self, 'AddtlQtyForExstgScties', QuantityToQuantityRatio1, False)

	@property
	def AddtlQtyForSbcbdRsltntScties(self):
		return self._AddtlQtyForSbcbdRsltntScties

	@AddtlQtyForSbcbdRsltntScties.setter
	def AddtlQtyForSbcbdRsltntScties(self, value):
		self._AddtlQtyForSbcbdRsltntScties = value if value is not None else base_types.UninitialisedField(self, 'AddtlQtyForSbcbdRsltntScties', QuantityToQuantityRatio1, False)

	@AddtlQtyForSbcbdRsltntScties.deleter
	def AddtlQtyForSbcbdRsltntScties(self):
		del self._AddtlQtyForSbcbdRsltntScties
		self._AddtlQtyForSbcbdRsltntScties = base_types.UninitialisedField(self, 'AddtlQtyForSbcbdRsltntScties', QuantityToQuantityRatio1, False)

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate3, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate3, False)

	@property
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if value is not None else base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType1FormatChoice, False)

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType1FormatChoice, False)

	@property
	def MinExrcblMltplSctiesQty(self):
		return self._MinExrcblMltplSctiesQty

	@MinExrcblMltplSctiesQty.setter
	def MinExrcblMltplSctiesQty(self, value):
		self._MinExrcblMltplSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'MinExrcblMltplSctiesQty', UnitOrFaceAmount1Choice, False)

	@MinExrcblMltplSctiesQty.deleter
	def MinExrcblMltplSctiesQty(self):
		del self._MinExrcblMltplSctiesQty
		self._MinExrcblMltplSctiesQty = base_types.UninitialisedField(self, 'MinExrcblMltplSctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def MinExrcblSctiesQty(self):
		return self._MinExrcblSctiesQty

	@MinExrcblSctiesQty.setter
	def MinExrcblSctiesQty(self, value):
		self._MinExrcblSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'MinExrcblSctiesQty', UnitOrFaceAmount1Choice, False)

	@MinExrcblSctiesQty.deleter
	def MinExrcblSctiesQty(self):
		del self._MinExrcblSctiesQty
		self._MinExrcblSctiesQty = base_types.UninitialisedField(self, 'MinExrcblSctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def NewBrdLotSctiesQty(self):
		return self._NewBrdLotSctiesQty

	@NewBrdLotSctiesQty.setter
	def NewBrdLotSctiesQty(self, value):
		self._NewBrdLotSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'NewBrdLotSctiesQty', UnitOrFaceAmount1Choice, False)

	@NewBrdLotSctiesQty.deleter
	def NewBrdLotSctiesQty(self):
		del self._NewBrdLotSctiesQty
		self._NewBrdLotSctiesQty = base_types.UninitialisedField(self, 'NewBrdLotSctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def NewDnmtnSctiesQty(self):
		return self._NewDnmtnSctiesQty

	@NewDnmtnSctiesQty.setter
	def NewDnmtnSctiesQty(self, value):
		self._NewDnmtnSctiesQty = value if value is not None else base_types.UninitialisedField(self, 'NewDnmtnSctiesQty', UnitOrFaceAmount1Choice, False)

	@NewDnmtnSctiesQty.deleter
	def NewDnmtnSctiesQty(self):
		del self._NewDnmtnSctiesQty
		self._NewDnmtnSctiesQty = base_types.UninitialisedField(self, 'NewDnmtnSctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice4, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice4, False)

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if value is not None else base_types.UninitialisedField(self, 'SctiesQty', UnitOrFaceAmount1Choice, False)

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = base_types.UninitialisedField(self, 'SctiesQty', UnitOrFaceAmount1Choice, False)

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if value is not None else base_types.UninitialisedField(self, 'SctyId', FinancialInstrumentDescription3, False)

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = base_types.UninitialisedField(self, 'SctyId', FinancialInstrumentDescription3, False)

	@property
	def ShrRnkg(self):
		return self._ShrRnkg

	@ShrRnkg.setter
	def ShrRnkg(self, value):
		self._ShrRnkg = value if value is not None else base_types.UninitialisedField(self, 'ShrRnkg', ShareRanking1FormatChoice, False)

	@ShrRnkg.deleter
	def ShrRnkg(self):
		del self._ShrRnkg
		self._ShrRnkg = base_types.UninitialisedField(self, 'ShrRnkg', ShareRanking1FormatChoice, False)

	@property
	def TempFinInstrmInd(self):
		return self._TempFinInstrmInd

	@TempFinInstrmInd.setter
	def TempFinInstrmInd(self, value):
		self._TempFinInstrmInd = value if value is not None else base_types.UninitialisedField(self, 'TempFinInstrmInd', YesNoIndicator, False)

	@TempFinInstrmInd.deleter
	def TempFinInstrmInd(self):
		del self._TempFinInstrmInd
		self._TempFinInstrmInd = base_types.UninitialisedField(self, 'TempFinInstrmInd', YesNoIndicator, False)

	@property
	def TradgPrd(self):
		return self._TradgPrd

	@TradgPrd.setter
	def TradgPrd(self, value):
		self._TradgPrd = value if value is not None else base_types.UninitialisedField(self, 'TradgPrd', Period1, False)

	@TradgPrd.deleter
	def TradgPrd(self):
		del self._TradgPrd
		self._TradgPrd = base_types.UninitialisedField(self, 'TradgPrd', Period1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlQtyForExstgScties', type=QuantityToQuantityRatio1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlQtyForSbcbdRsltntScties', type=QuantityToQuantityRatio1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinExrcblMltplSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinExrcblSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewBrdLotSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewDnmtnSctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=FinancialInstrumentDescription3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrRnkg', type=ShareRanking1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempFinInstrmInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
	))