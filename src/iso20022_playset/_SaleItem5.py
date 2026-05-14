# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Adjustment14 import Adjustment14
from ._DecimalNumber import DecimalNumber
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._ProductCodeType1Code import ProductCodeType1Code
from ._Tax44 import Tax44
from ._TrueFalseIndicator import TrueFalseIndicator
from ._UnitOfMeasure1Code import UnitOfMeasure1Code

class SaleItem5(base_types._BaseFieldType):

	__slots__ = ["_AddtlPdctCd", "_AddtlPdctCdTp", "_AdjstdAmt", "_Adjstmnt", "_InsrncAmt", "_InsrncInd", "_NonAdjstdTtlAmt", "_NonAdjstdUnitPric", "_OthrUnitOfMeasr", "_PdctCd", "_PdctCdModfr", "_PdctCdTp", "_PdctDesc", "_PdctQty", "_PdctTp", "_Tax", "_TtlAmt", "_UnitOfMeasr"]
	@property
	def AddtlPdctCd(self):
		return self._AddtlPdctCd

	@AddtlPdctCd.setter
	def AddtlPdctCd(self, value):
		self._AddtlPdctCd = value if type(value) != base_types.auto else self.make_default("AddtlPdctCd")

	@AddtlPdctCd.deleter
	def AddtlPdctCd(self):
		del self._AddtlPdctCd
		self._AddtlPdctCd = None

	@property
	def AddtlPdctCdTp(self):
		return self._AddtlPdctCdTp

	@AddtlPdctCdTp.setter
	def AddtlPdctCdTp(self, value):
		self._AddtlPdctCdTp = value if type(value) != base_types.auto else self.make_default("AddtlPdctCdTp")

	@AddtlPdctCdTp.deleter
	def AddtlPdctCdTp(self):
		del self._AddtlPdctCdTp
		self._AddtlPdctCdTp = None

	@property
	def AdjstdAmt(self):
		return self._AdjstdAmt

	@AdjstdAmt.setter
	def AdjstdAmt(self, value):
		self._AdjstdAmt = value if type(value) != base_types.auto else self.make_default("AdjstdAmt")

	@AdjstdAmt.deleter
	def AdjstdAmt(self):
		del self._AdjstdAmt
		self._AdjstdAmt = None

	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if type(value) != base_types.auto else self.make_default("Adjstmnt")

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = None

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
	def InsrncInd(self):
		return self._InsrncInd

	@InsrncInd.setter
	def InsrncInd(self, value):
		self._InsrncInd = value if type(value) != base_types.auto else self.make_default("InsrncInd")

	@InsrncInd.deleter
	def InsrncInd(self):
		del self._InsrncInd
		self._InsrncInd = None

	@property
	def NonAdjstdTtlAmt(self):
		return self._NonAdjstdTtlAmt

	@NonAdjstdTtlAmt.setter
	def NonAdjstdTtlAmt(self, value):
		self._NonAdjstdTtlAmt = value if type(value) != base_types.auto else self.make_default("NonAdjstdTtlAmt")

	@NonAdjstdTtlAmt.deleter
	def NonAdjstdTtlAmt(self):
		del self._NonAdjstdTtlAmt
		self._NonAdjstdTtlAmt = None

	@property
	def NonAdjstdUnitPric(self):
		return self._NonAdjstdUnitPric

	@NonAdjstdUnitPric.setter
	def NonAdjstdUnitPric(self, value):
		self._NonAdjstdUnitPric = value if type(value) != base_types.auto else self.make_default("NonAdjstdUnitPric")

	@NonAdjstdUnitPric.deleter
	def NonAdjstdUnitPric(self):
		del self._NonAdjstdUnitPric
		self._NonAdjstdUnitPric = None

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
	def PdctCdModfr(self):
		return self._PdctCdModfr

	@PdctCdModfr.setter
	def PdctCdModfr(self, value):
		self._PdctCdModfr = value if type(value) != base_types.auto else self.make_default("PdctCdModfr")

	@PdctCdModfr.deleter
	def PdctCdModfr(self):
		del self._PdctCdModfr
		self._PdctCdModfr = None

	@property
	def PdctCdTp(self):
		return self._PdctCdTp

	@PdctCdTp.setter
	def PdctCdTp(self, value):
		self._PdctCdTp = value if type(value) != base_types.auto else self.make_default("PdctCdTp")

	@PdctCdTp.deleter
	def PdctCdTp(self):
		del self._PdctCdTp
		self._PdctCdTp = None

	@property
	def PdctDesc(self):
		return self._PdctDesc

	@PdctDesc.setter
	def PdctDesc(self, value):
		self._PdctDesc = value if type(value) != base_types.auto else self.make_default("PdctDesc")

	@PdctDesc.deleter
	def PdctDesc(self):
		del self._PdctDesc
		self._PdctDesc = None

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
	def PdctTp(self):
		return self._PdctTp

	@PdctTp.setter
	def PdctTp(self, value):
		self._PdctTp = value if type(value) != base_types.auto else self.make_default("PdctTp")

	@PdctTp.deleter
	def PdctTp(self):
		del self._PdctTp
		self._PdctTp = None

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
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != base_types.auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

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
		base_types.FieldEntry(name='Tax', type=Tax44, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure1Code, min=0, max=1, mutex_group=None, array=False),
	))