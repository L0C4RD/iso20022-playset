# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Adjustment14
from . import DecimalNumber
from . import ImpliedCurrencyAndAmount
from . import Max140Text
from . import Max35Text
from . import Max70Text
from . import ProductCodeType1Code
from . import Tax41
from . import TrueFalseIndicator
from . import UnitOfMeasure1Code

class SaleItem4(base_types._BaseFieldType):

	__slots__ = ["_AddtlPdctCd", "_AddtlPdctCdTp", "_AdjstdAmt", "_Adjstmnt", "_InsrncAmt", "_InsrncInd", "_NonAdjstdTtlAmt", "_NonAdjstdUnitPric", "_OthrUnitOfMeasr", "_PdctCd", "_PdctCdModfr", "_PdctCdTp", "_PdctDesc", "_PdctQty", "_PdctTp", "_Tax", "_TtlAmt", "_UnitOfMeasr"]
	@property
	def AddtlPdctCd(self):
		return self._AddtlPdctCd

	@AddtlPdctCd.setter
	def AddtlPdctCd(self, value):
		self._AddtlPdctCd = value if value is not None else base_types.UninitialisedField(self, 'AddtlPdctCd', Max70Text, False)

	@AddtlPdctCd.deleter
	def AddtlPdctCd(self):
		del self._AddtlPdctCd
		self._AddtlPdctCd = base_types.UninitialisedField(self, 'AddtlPdctCd', Max70Text, False)

	@property
	def AddtlPdctCdTp(self):
		return self._AddtlPdctCdTp

	@AddtlPdctCdTp.setter
	def AddtlPdctCdTp(self, value):
		self._AddtlPdctCdTp = value if value is not None else base_types.UninitialisedField(self, 'AddtlPdctCdTp', Max35Text, False)

	@AddtlPdctCdTp.deleter
	def AddtlPdctCdTp(self):
		del self._AddtlPdctCdTp
		self._AddtlPdctCdTp = base_types.UninitialisedField(self, 'AddtlPdctCdTp', Max35Text, False)

	@property
	def AdjstdAmt(self):
		return self._AdjstdAmt

	@AdjstdAmt.setter
	def AdjstdAmt(self, value):
		self._AdjstdAmt = value if value is not None else base_types.UninitialisedField(self, 'AdjstdAmt', ImpliedCurrencyAndAmount, False)

	@AdjstdAmt.deleter
	def AdjstdAmt(self):
		del self._AdjstdAmt
		self._AdjstdAmt = base_types.UninitialisedField(self, 'AdjstdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if value is not None else base_types.UninitialisedField(self, 'Adjstmnt', Adjustment14, True)

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = base_types.UninitialisedField(self, 'Adjstmnt', Adjustment14, True)

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
	def InsrncInd(self):
		return self._InsrncInd

	@InsrncInd.setter
	def InsrncInd(self, value):
		self._InsrncInd = value if value is not None else base_types.UninitialisedField(self, 'InsrncInd', TrueFalseIndicator, False)

	@InsrncInd.deleter
	def InsrncInd(self):
		del self._InsrncInd
		self._InsrncInd = base_types.UninitialisedField(self, 'InsrncInd', TrueFalseIndicator, False)

	@property
	def NonAdjstdTtlAmt(self):
		return self._NonAdjstdTtlAmt

	@NonAdjstdTtlAmt.setter
	def NonAdjstdTtlAmt(self, value):
		self._NonAdjstdTtlAmt = value if value is not None else base_types.UninitialisedField(self, 'NonAdjstdTtlAmt', ImpliedCurrencyAndAmount, False)

	@NonAdjstdTtlAmt.deleter
	def NonAdjstdTtlAmt(self):
		del self._NonAdjstdTtlAmt
		self._NonAdjstdTtlAmt = base_types.UninitialisedField(self, 'NonAdjstdTtlAmt', ImpliedCurrencyAndAmount, False)

	@property
	def NonAdjstdUnitPric(self):
		return self._NonAdjstdUnitPric

	@NonAdjstdUnitPric.setter
	def NonAdjstdUnitPric(self, value):
		self._NonAdjstdUnitPric = value if value is not None else base_types.UninitialisedField(self, 'NonAdjstdUnitPric', ImpliedCurrencyAndAmount, False)

	@NonAdjstdUnitPric.deleter
	def NonAdjstdUnitPric(self):
		del self._NonAdjstdUnitPric
		self._NonAdjstdUnitPric = base_types.UninitialisedField(self, 'NonAdjstdUnitPric', ImpliedCurrencyAndAmount, False)

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
	def PdctCdModfr(self):
		return self._PdctCdModfr

	@PdctCdModfr.setter
	def PdctCdModfr(self, value):
		self._PdctCdModfr = value if value is not None else base_types.UninitialisedField(self, 'PdctCdModfr', DecimalNumber, False)

	@PdctCdModfr.deleter
	def PdctCdModfr(self):
		del self._PdctCdModfr
		self._PdctCdModfr = base_types.UninitialisedField(self, 'PdctCdModfr', DecimalNumber, False)

	@property
	def PdctCdTp(self):
		return self._PdctCdTp

	@PdctCdTp.setter
	def PdctCdTp(self, value):
		self._PdctCdTp = value if value is not None else base_types.UninitialisedField(self, 'PdctCdTp', ProductCodeType1Code, False)

	@PdctCdTp.deleter
	def PdctCdTp(self):
		del self._PdctCdTp
		self._PdctCdTp = base_types.UninitialisedField(self, 'PdctCdTp', ProductCodeType1Code, False)

	@property
	def PdctDesc(self):
		return self._PdctDesc

	@PdctDesc.setter
	def PdctDesc(self, value):
		self._PdctDesc = value if value is not None else base_types.UninitialisedField(self, 'PdctDesc', Max140Text, False)

	@PdctDesc.deleter
	def PdctDesc(self):
		del self._PdctDesc
		self._PdctDesc = base_types.UninitialisedField(self, 'PdctDesc', Max140Text, False)

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
	def PdctTp(self):
		return self._PdctTp

	@PdctTp.setter
	def PdctTp(self, value):
		self._PdctTp = value if value is not None else base_types.UninitialisedField(self, 'PdctTp', Max35Text, False)

	@PdctTp.deleter
	def PdctTp(self):
		del self._PdctTp
		self._PdctTp = base_types.UninitialisedField(self, 'PdctTp', Max35Text, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlPdctCd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlPdctCdTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdjstdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InsrncAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonAdjstdTtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonAdjstdUnitPric', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrUnitOfMeasr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCdModfr', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCdTp', type=ProductCodeType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctDesc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure1Code, min=0, max=1, mutex_group=None, array=False),
	))