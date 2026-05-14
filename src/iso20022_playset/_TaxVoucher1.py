# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._BaseOneRate import BaseOneRate
from ._ForeignExchangeTerms9 import ForeignExchangeTerms9
from ._ISODate import ISODate
from ._PercentageRate import PercentageRate
from ._PriceValue1 import PriceValue1
from ._UnitOrFaceAmount1Choice import UnitOrFaceAmount1Choice

class TaxVoucher1(base_types._BaseFieldType):

	__slots__ = ["_AlltdShrsCost", "_BrgnDt", "_BrgnSttlmDt", "_ChrgAmt", "_ComssnAmt", "_CshAmtBrghtFwd", "_CshAmtCrrdFwd", "_FXDtls", "_GrssAmt", "_NetAmt", "_NtnlDvddPybl", "_NtnlTax", "_RcrdDtHldg", "_ScripDvddRinvstmtPricPerShr", "_StmpDtyAmt", "_TaxCdt", "_TaxCdtRate", "_TaxDdctn", "_TaxVchrRate", "_WhldgTaxAmt", "_WhldgTaxRate"]
	@property
	def AlltdShrsCost(self):
		return self._AlltdShrsCost

	@AlltdShrsCost.setter
	def AlltdShrsCost(self, value):
		self._AlltdShrsCost = value if type(value) != base_types.auto else self.make_default("AlltdShrsCost")

	@AlltdShrsCost.deleter
	def AlltdShrsCost(self):
		del self._AlltdShrsCost
		self._AlltdShrsCost = None

	@property
	def BrgnDt(self):
		return self._BrgnDt

	@BrgnDt.setter
	def BrgnDt(self, value):
		self._BrgnDt = value if type(value) != base_types.auto else self.make_default("BrgnDt")

	@BrgnDt.deleter
	def BrgnDt(self):
		del self._BrgnDt
		self._BrgnDt = None

	@property
	def BrgnSttlmDt(self):
		return self._BrgnSttlmDt

	@BrgnSttlmDt.setter
	def BrgnSttlmDt(self, value):
		self._BrgnSttlmDt = value if type(value) != base_types.auto else self.make_default("BrgnSttlmDt")

	@BrgnSttlmDt.deleter
	def BrgnSttlmDt(self):
		del self._BrgnSttlmDt
		self._BrgnSttlmDt = None

	@property
	def ChrgAmt(self):
		return self._ChrgAmt

	@ChrgAmt.setter
	def ChrgAmt(self, value):
		self._ChrgAmt = value if type(value) != base_types.auto else self.make_default("ChrgAmt")

	@ChrgAmt.deleter
	def ChrgAmt(self):
		del self._ChrgAmt
		self._ChrgAmt = None

	@property
	def ComssnAmt(self):
		return self._ComssnAmt

	@ComssnAmt.setter
	def ComssnAmt(self, value):
		self._ComssnAmt = value if type(value) != base_types.auto else self.make_default("ComssnAmt")

	@ComssnAmt.deleter
	def ComssnAmt(self):
		del self._ComssnAmt
		self._ComssnAmt = None

	@property
	def CshAmtBrghtFwd(self):
		return self._CshAmtBrghtFwd

	@CshAmtBrghtFwd.setter
	def CshAmtBrghtFwd(self, value):
		self._CshAmtBrghtFwd = value if type(value) != base_types.auto else self.make_default("CshAmtBrghtFwd")

	@CshAmtBrghtFwd.deleter
	def CshAmtBrghtFwd(self):
		del self._CshAmtBrghtFwd
		self._CshAmtBrghtFwd = None

	@property
	def CshAmtCrrdFwd(self):
		return self._CshAmtCrrdFwd

	@CshAmtCrrdFwd.setter
	def CshAmtCrrdFwd(self, value):
		self._CshAmtCrrdFwd = value if type(value) != base_types.auto else self.make_default("CshAmtCrrdFwd")

	@CshAmtCrrdFwd.deleter
	def CshAmtCrrdFwd(self):
		del self._CshAmtCrrdFwd
		self._CshAmtCrrdFwd = None

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if type(value) != base_types.auto else self.make_default("FXDtls")

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = None

	@property
	def GrssAmt(self):
		return self._GrssAmt

	@GrssAmt.setter
	def GrssAmt(self, value):
		self._GrssAmt = value if type(value) != base_types.auto else self.make_default("GrssAmt")

	@GrssAmt.deleter
	def GrssAmt(self):
		del self._GrssAmt
		self._GrssAmt = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != base_types.auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	@property
	def NtnlDvddPybl(self):
		return self._NtnlDvddPybl

	@NtnlDvddPybl.setter
	def NtnlDvddPybl(self, value):
		self._NtnlDvddPybl = value if type(value) != base_types.auto else self.make_default("NtnlDvddPybl")

	@NtnlDvddPybl.deleter
	def NtnlDvddPybl(self):
		del self._NtnlDvddPybl
		self._NtnlDvddPybl = None

	@property
	def NtnlTax(self):
		return self._NtnlTax

	@NtnlTax.setter
	def NtnlTax(self, value):
		self._NtnlTax = value if type(value) != base_types.auto else self.make_default("NtnlTax")

	@NtnlTax.deleter
	def NtnlTax(self):
		del self._NtnlTax
		self._NtnlTax = None

	@property
	def RcrdDtHldg(self):
		return self._RcrdDtHldg

	@RcrdDtHldg.setter
	def RcrdDtHldg(self, value):
		self._RcrdDtHldg = value if type(value) != base_types.auto else self.make_default("RcrdDtHldg")

	@RcrdDtHldg.deleter
	def RcrdDtHldg(self):
		del self._RcrdDtHldg
		self._RcrdDtHldg = None

	@property
	def ScripDvddRinvstmtPricPerShr(self):
		return self._ScripDvddRinvstmtPricPerShr

	@ScripDvddRinvstmtPricPerShr.setter
	def ScripDvddRinvstmtPricPerShr(self, value):
		self._ScripDvddRinvstmtPricPerShr = value if type(value) != base_types.auto else self.make_default("ScripDvddRinvstmtPricPerShr")

	@ScripDvddRinvstmtPricPerShr.deleter
	def ScripDvddRinvstmtPricPerShr(self):
		del self._ScripDvddRinvstmtPricPerShr
		self._ScripDvddRinvstmtPricPerShr = None

	@property
	def StmpDtyAmt(self):
		return self._StmpDtyAmt

	@StmpDtyAmt.setter
	def StmpDtyAmt(self, value):
		self._StmpDtyAmt = value if type(value) != base_types.auto else self.make_default("StmpDtyAmt")

	@StmpDtyAmt.deleter
	def StmpDtyAmt(self):
		del self._StmpDtyAmt
		self._StmpDtyAmt = None

	@property
	def TaxCdt(self):
		return self._TaxCdt

	@TaxCdt.setter
	def TaxCdt(self, value):
		self._TaxCdt = value if type(value) != base_types.auto else self.make_default("TaxCdt")

	@TaxCdt.deleter
	def TaxCdt(self):
		del self._TaxCdt
		self._TaxCdt = None

	@property
	def TaxCdtRate(self):
		return self._TaxCdtRate

	@TaxCdtRate.setter
	def TaxCdtRate(self, value):
		self._TaxCdtRate = value if type(value) != base_types.auto else self.make_default("TaxCdtRate")

	@TaxCdtRate.deleter
	def TaxCdtRate(self):
		del self._TaxCdtRate
		self._TaxCdtRate = None

	@property
	def TaxDdctn(self):
		return self._TaxDdctn

	@TaxDdctn.setter
	def TaxDdctn(self, value):
		self._TaxDdctn = value if type(value) != base_types.auto else self.make_default("TaxDdctn")

	@TaxDdctn.deleter
	def TaxDdctn(self):
		del self._TaxDdctn
		self._TaxDdctn = None

	@property
	def TaxVchrRate(self):
		return self._TaxVchrRate

	@TaxVchrRate.setter
	def TaxVchrRate(self, value):
		self._TaxVchrRate = value if type(value) != base_types.auto else self.make_default("TaxVchrRate")

	@TaxVchrRate.deleter
	def TaxVchrRate(self):
		del self._TaxVchrRate
		self._TaxVchrRate = None

	@property
	def WhldgTaxAmt(self):
		return self._WhldgTaxAmt

	@WhldgTaxAmt.setter
	def WhldgTaxAmt(self, value):
		self._WhldgTaxAmt = value if type(value) != base_types.auto else self.make_default("WhldgTaxAmt")

	@WhldgTaxAmt.deleter
	def WhldgTaxAmt(self):
		del self._WhldgTaxAmt
		self._WhldgTaxAmt = None

	@property
	def WhldgTaxRate(self):
		return self._WhldgTaxRate

	@WhldgTaxRate.setter
	def WhldgTaxRate(self, value):
		self._WhldgTaxRate = value if type(value) != base_types.auto else self.make_default("WhldgTaxRate")

	@WhldgTaxRate.deleter
	def WhldgTaxRate(self):
		del self._WhldgTaxRate
		self._WhldgTaxRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AlltdShrsCost', type=PriceValue1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrgnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrgnSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComssnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAmtBrghtFwd', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAmtCrrdFwd', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlDvddPybl', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlTax', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdDtHldg', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScripDvddRinvstmtPricPerShr', type=PriceValue1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCdt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TaxCdtRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxDdctn', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TaxVchrRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))