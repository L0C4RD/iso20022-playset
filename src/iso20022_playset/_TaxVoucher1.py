# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BaseOneRate
from . import ForeignExchangeTerms9
from . import ISODate
from . import PercentageRate
from . import PriceValue1
from . import UnitOrFaceAmount1Choice

class TaxVoucher1(base_types._BaseFieldType):

	__slots__ = ["_AlltdShrsCost", "_BrgnDt", "_BrgnSttlmDt", "_ChrgAmt", "_ComssnAmt", "_CshAmtBrghtFwd", "_CshAmtCrrdFwd", "_FXDtls", "_GrssAmt", "_NetAmt", "_NtnlDvddPybl", "_NtnlTax", "_RcrdDtHldg", "_ScripDvddRinvstmtPricPerShr", "_StmpDtyAmt", "_TaxCdt", "_TaxCdtRate", "_TaxDdctn", "_TaxVchrRate", "_WhldgTaxAmt", "_WhldgTaxRate"]
	@property
	def AlltdShrsCost(self):
		return self._AlltdShrsCost

	@AlltdShrsCost.setter
	def AlltdShrsCost(self, value):
		self._AlltdShrsCost = value if value is not None else base_types.UninitialisedField(self, 'AlltdShrsCost', PriceValue1, False)

	@AlltdShrsCost.deleter
	def AlltdShrsCost(self):
		del self._AlltdShrsCost
		self._AlltdShrsCost = base_types.UninitialisedField(self, 'AlltdShrsCost', PriceValue1, False)

	@property
	def BrgnDt(self):
		return self._BrgnDt

	@BrgnDt.setter
	def BrgnDt(self, value):
		self._BrgnDt = value if value is not None else base_types.UninitialisedField(self, 'BrgnDt', ISODate, False)

	@BrgnDt.deleter
	def BrgnDt(self):
		del self._BrgnDt
		self._BrgnDt = base_types.UninitialisedField(self, 'BrgnDt', ISODate, False)

	@property
	def BrgnSttlmDt(self):
		return self._BrgnSttlmDt

	@BrgnSttlmDt.setter
	def BrgnSttlmDt(self, value):
		self._BrgnSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'BrgnSttlmDt', ISODate, False)

	@BrgnSttlmDt.deleter
	def BrgnSttlmDt(self):
		del self._BrgnSttlmDt
		self._BrgnSttlmDt = base_types.UninitialisedField(self, 'BrgnSttlmDt', ISODate, False)

	@property
	def ChrgAmt(self):
		return self._ChrgAmt

	@ChrgAmt.setter
	def ChrgAmt(self, value):
		self._ChrgAmt = value if value is not None else base_types.UninitialisedField(self, 'ChrgAmt', ActiveCurrencyAndAmount, False)

	@ChrgAmt.deleter
	def ChrgAmt(self):
		del self._ChrgAmt
		self._ChrgAmt = base_types.UninitialisedField(self, 'ChrgAmt', ActiveCurrencyAndAmount, False)

	@property
	def ComssnAmt(self):
		return self._ComssnAmt

	@ComssnAmt.setter
	def ComssnAmt(self, value):
		self._ComssnAmt = value if value is not None else base_types.UninitialisedField(self, 'ComssnAmt', ActiveCurrencyAndAmount, False)

	@ComssnAmt.deleter
	def ComssnAmt(self):
		del self._ComssnAmt
		self._ComssnAmt = base_types.UninitialisedField(self, 'ComssnAmt', ActiveCurrencyAndAmount, False)

	@property
	def CshAmtBrghtFwd(self):
		return self._CshAmtBrghtFwd

	@CshAmtBrghtFwd.setter
	def CshAmtBrghtFwd(self, value):
		self._CshAmtBrghtFwd = value if value is not None else base_types.UninitialisedField(self, 'CshAmtBrghtFwd', ActiveCurrencyAndAmount, False)

	@CshAmtBrghtFwd.deleter
	def CshAmtBrghtFwd(self):
		del self._CshAmtBrghtFwd
		self._CshAmtBrghtFwd = base_types.UninitialisedField(self, 'CshAmtBrghtFwd', ActiveCurrencyAndAmount, False)

	@property
	def CshAmtCrrdFwd(self):
		return self._CshAmtCrrdFwd

	@CshAmtCrrdFwd.setter
	def CshAmtCrrdFwd(self, value):
		self._CshAmtCrrdFwd = value if value is not None else base_types.UninitialisedField(self, 'CshAmtCrrdFwd', ActiveCurrencyAndAmount, False)

	@CshAmtCrrdFwd.deleter
	def CshAmtCrrdFwd(self):
		del self._CshAmtCrrdFwd
		self._CshAmtCrrdFwd = base_types.UninitialisedField(self, 'CshAmtCrrdFwd', ActiveCurrencyAndAmount, False)

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms9, False)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms9, False)

	@property
	def GrssAmt(self):
		return self._GrssAmt

	@GrssAmt.setter
	def GrssAmt(self, value):
		self._GrssAmt = value if value is not None else base_types.UninitialisedField(self, 'GrssAmt', ActiveCurrencyAndAmount, False)

	@GrssAmt.deleter
	def GrssAmt(self):
		del self._GrssAmt
		self._GrssAmt = base_types.UninitialisedField(self, 'GrssAmt', ActiveCurrencyAndAmount, False)

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
	def NtnlDvddPybl(self):
		return self._NtnlDvddPybl

	@NtnlDvddPybl.setter
	def NtnlDvddPybl(self, value):
		self._NtnlDvddPybl = value if value is not None else base_types.UninitialisedField(self, 'NtnlDvddPybl', ActiveCurrencyAndAmount, False)

	@NtnlDvddPybl.deleter
	def NtnlDvddPybl(self):
		del self._NtnlDvddPybl
		self._NtnlDvddPybl = base_types.UninitialisedField(self, 'NtnlDvddPybl', ActiveCurrencyAndAmount, False)

	@property
	def NtnlTax(self):
		return self._NtnlTax

	@NtnlTax.setter
	def NtnlTax(self, value):
		self._NtnlTax = value if value is not None else base_types.UninitialisedField(self, 'NtnlTax', ActiveCurrencyAndAmount, False)

	@NtnlTax.deleter
	def NtnlTax(self):
		del self._NtnlTax
		self._NtnlTax = base_types.UninitialisedField(self, 'NtnlTax', ActiveCurrencyAndAmount, False)

	@property
	def RcrdDtHldg(self):
		return self._RcrdDtHldg

	@RcrdDtHldg.setter
	def RcrdDtHldg(self, value):
		self._RcrdDtHldg = value if value is not None else base_types.UninitialisedField(self, 'RcrdDtHldg', UnitOrFaceAmount1Choice, False)

	@RcrdDtHldg.deleter
	def RcrdDtHldg(self):
		del self._RcrdDtHldg
		self._RcrdDtHldg = base_types.UninitialisedField(self, 'RcrdDtHldg', UnitOrFaceAmount1Choice, False)

	@property
	def ScripDvddRinvstmtPricPerShr(self):
		return self._ScripDvddRinvstmtPricPerShr

	@ScripDvddRinvstmtPricPerShr.setter
	def ScripDvddRinvstmtPricPerShr(self, value):
		self._ScripDvddRinvstmtPricPerShr = value if value is not None else base_types.UninitialisedField(self, 'ScripDvddRinvstmtPricPerShr', PriceValue1, False)

	@ScripDvddRinvstmtPricPerShr.deleter
	def ScripDvddRinvstmtPricPerShr(self):
		del self._ScripDvddRinvstmtPricPerShr
		self._ScripDvddRinvstmtPricPerShr = base_types.UninitialisedField(self, 'ScripDvddRinvstmtPricPerShr', PriceValue1, False)

	@property
	def StmpDtyAmt(self):
		return self._StmpDtyAmt

	@StmpDtyAmt.setter
	def StmpDtyAmt(self, value):
		self._StmpDtyAmt = value if value is not None else base_types.UninitialisedField(self, 'StmpDtyAmt', ActiveCurrencyAndAmount, False)

	@StmpDtyAmt.deleter
	def StmpDtyAmt(self):
		del self._StmpDtyAmt
		self._StmpDtyAmt = base_types.UninitialisedField(self, 'StmpDtyAmt', ActiveCurrencyAndAmount, False)

	@property
	def TaxCdt(self):
		return self._TaxCdt

	@TaxCdt.setter
	def TaxCdt(self, value):
		self._TaxCdt = value if value is not None else base_types.UninitialisedField(self, 'TaxCdt', ActiveCurrencyAndAmount, False)

	@TaxCdt.deleter
	def TaxCdt(self):
		del self._TaxCdt
		self._TaxCdt = base_types.UninitialisedField(self, 'TaxCdt', ActiveCurrencyAndAmount, False)

	@property
	def TaxCdtRate(self):
		return self._TaxCdtRate

	@TaxCdtRate.setter
	def TaxCdtRate(self, value):
		self._TaxCdtRate = value if value is not None else base_types.UninitialisedField(self, 'TaxCdtRate', PercentageRate, False)

	@TaxCdtRate.deleter
	def TaxCdtRate(self):
		del self._TaxCdtRate
		self._TaxCdtRate = base_types.UninitialisedField(self, 'TaxCdtRate', PercentageRate, False)

	@property
	def TaxDdctn(self):
		return self._TaxDdctn

	@TaxDdctn.setter
	def TaxDdctn(self, value):
		self._TaxDdctn = value if value is not None else base_types.UninitialisedField(self, 'TaxDdctn', ActiveCurrencyAndAmount, False)

	@TaxDdctn.deleter
	def TaxDdctn(self):
		del self._TaxDdctn
		self._TaxDdctn = base_types.UninitialisedField(self, 'TaxDdctn', ActiveCurrencyAndAmount, False)

	@property
	def TaxVchrRate(self):
		return self._TaxVchrRate

	@TaxVchrRate.setter
	def TaxVchrRate(self, value):
		self._TaxVchrRate = value if value is not None else base_types.UninitialisedField(self, 'TaxVchrRate', BaseOneRate, False)

	@TaxVchrRate.deleter
	def TaxVchrRate(self):
		del self._TaxVchrRate
		self._TaxVchrRate = base_types.UninitialisedField(self, 'TaxVchrRate', BaseOneRate, False)

	@property
	def WhldgTaxAmt(self):
		return self._WhldgTaxAmt

	@WhldgTaxAmt.setter
	def WhldgTaxAmt(self, value):
		self._WhldgTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxAmt', ActiveCurrencyAndAmount, False)

	@WhldgTaxAmt.deleter
	def WhldgTaxAmt(self):
		del self._WhldgTaxAmt
		self._WhldgTaxAmt = base_types.UninitialisedField(self, 'WhldgTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def WhldgTaxRate(self):
		return self._WhldgTaxRate

	@WhldgTaxRate.setter
	def WhldgTaxRate(self, value):
		self._WhldgTaxRate = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxRate', PercentageRate, False)

	@WhldgTaxRate.deleter
	def WhldgTaxRate(self):
		del self._WhldgTaxRate
		self._WhldgTaxRate = base_types.UninitialisedField(self, 'WhldgTaxRate', PercentageRate, False)

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