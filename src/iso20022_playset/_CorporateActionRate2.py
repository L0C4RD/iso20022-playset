# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AmountAndRateFormat2Choice
from . import ForeignExchangeTerms8
from . import GrossDividendRate1Choice
from . import NetDividendRate1Choice
from . import RateAndAmountFormat1Choice
from . import RateFormat1Choice
from . import RatioFormat1Choice
from . import RatioFormat2Choice
from . import RelatedTaxType1

class CorporateActionRate2(base_types._BaseFieldType):

	__slots__ = ["_AddtlQtyForExstgScties", "_AddtlQtyForSbcbdRsltntScties", "_AddtlTax", "_AplblRate", "_Chrgs", "_CshIncntiv", "_FnlDvdd", "_FsclStmp", "_FullyFrnkd", "_GrmnLclTax1", "_GrmnLclTax2", "_GrmnLclTax3", "_GrmnLclTax4", "_GrssDvdd", "_IndxFctr", "_IntrstForUsdPmt", "_MaxAllwdOvrsbcpt", "_NetDvdd", "_NewSctiesToUndrlygScties", "_NewToOd", "_NonResdtRate", "_OrgnlAmt", "_Prratn", "_PrvsnlDvdd", "_RltdTax", "_SlctnFee", "_TaxOnIncm", "_TaxOnPrft", "_TaxRclm", "_WhldgOfFrgnTax", "_WhldgOfLclTax", "_WhldgTax", "_XchgRate"]
	@property
	def AddtlQtyForExstgScties(self):
		return self._AddtlQtyForExstgScties

	@AddtlQtyForExstgScties.setter
	def AddtlQtyForExstgScties(self, value):
		self._AddtlQtyForExstgScties = value if value is not None else base_types.UninitialisedField(self, 'AddtlQtyForExstgScties', RatioFormat1Choice, False)

	@AddtlQtyForExstgScties.deleter
	def AddtlQtyForExstgScties(self):
		del self._AddtlQtyForExstgScties
		self._AddtlQtyForExstgScties = base_types.UninitialisedField(self, 'AddtlQtyForExstgScties', RatioFormat1Choice, False)

	@property
	def AddtlQtyForSbcbdRsltntScties(self):
		return self._AddtlQtyForSbcbdRsltntScties

	@AddtlQtyForSbcbdRsltntScties.setter
	def AddtlQtyForSbcbdRsltntScties(self, value):
		self._AddtlQtyForSbcbdRsltntScties = value if value is not None else base_types.UninitialisedField(self, 'AddtlQtyForSbcbdRsltntScties', RatioFormat1Choice, False)

	@AddtlQtyForSbcbdRsltntScties.deleter
	def AddtlQtyForSbcbdRsltntScties(self):
		del self._AddtlQtyForSbcbdRsltntScties
		self._AddtlQtyForSbcbdRsltntScties = base_types.UninitialisedField(self, 'AddtlQtyForSbcbdRsltntScties', RatioFormat1Choice, False)

	@property
	def AddtlTax(self):
		return self._AddtlTax

	@AddtlTax.setter
	def AddtlTax(self, value):
		self._AddtlTax = value if value is not None else base_types.UninitialisedField(self, 'AddtlTax', RateAndAmountFormat1Choice, False)

	@AddtlTax.deleter
	def AddtlTax(self):
		del self._AddtlTax
		self._AddtlTax = base_types.UninitialisedField(self, 'AddtlTax', RateAndAmountFormat1Choice, False)

	@property
	def AplblRate(self):
		return self._AplblRate

	@AplblRate.setter
	def AplblRate(self, value):
		self._AplblRate = value if value is not None else base_types.UninitialisedField(self, 'AplblRate', RateFormat1Choice, False)

	@AplblRate.deleter
	def AplblRate(self):
		del self._AplblRate
		self._AplblRate = base_types.UninitialisedField(self, 'AplblRate', RateFormat1Choice, False)

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if value is not None else base_types.UninitialisedField(self, 'Chrgs', RateAndAmountFormat1Choice, False)

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = base_types.UninitialisedField(self, 'Chrgs', RateAndAmountFormat1Choice, False)

	@property
	def CshIncntiv(self):
		return self._CshIncntiv

	@CshIncntiv.setter
	def CshIncntiv(self, value):
		self._CshIncntiv = value if value is not None else base_types.UninitialisedField(self, 'CshIncntiv', RateFormat1Choice, False)

	@CshIncntiv.deleter
	def CshIncntiv(self):
		del self._CshIncntiv
		self._CshIncntiv = base_types.UninitialisedField(self, 'CshIncntiv', RateFormat1Choice, False)

	@property
	def FnlDvdd(self):
		return self._FnlDvdd

	@FnlDvdd.setter
	def FnlDvdd(self, value):
		self._FnlDvdd = value if value is not None else base_types.UninitialisedField(self, 'FnlDvdd', AmountAndRateFormat2Choice, False)

	@FnlDvdd.deleter
	def FnlDvdd(self):
		del self._FnlDvdd
		self._FnlDvdd = base_types.UninitialisedField(self, 'FnlDvdd', AmountAndRateFormat2Choice, False)

	@property
	def FsclStmp(self):
		return self._FsclStmp

	@FsclStmp.setter
	def FsclStmp(self, value):
		self._FsclStmp = value if value is not None else base_types.UninitialisedField(self, 'FsclStmp', RateFormat1Choice, False)

	@FsclStmp.deleter
	def FsclStmp(self):
		del self._FsclStmp
		self._FsclStmp = base_types.UninitialisedField(self, 'FsclStmp', RateFormat1Choice, False)

	@property
	def FullyFrnkd(self):
		return self._FullyFrnkd

	@FullyFrnkd.setter
	def FullyFrnkd(self, value):
		self._FullyFrnkd = value if value is not None else base_types.UninitialisedField(self, 'FullyFrnkd', RateAndAmountFormat1Choice, False)

	@FullyFrnkd.deleter
	def FullyFrnkd(self):
		del self._FullyFrnkd
		self._FullyFrnkd = base_types.UninitialisedField(self, 'FullyFrnkd', RateAndAmountFormat1Choice, False)

	@property
	def GrmnLclTax1(self):
		return self._GrmnLclTax1

	@GrmnLclTax1.setter
	def GrmnLclTax1(self, value):
		self._GrmnLclTax1 = value if value is not None else base_types.UninitialisedField(self, 'GrmnLclTax1', RateAndAmountFormat1Choice, False)

	@GrmnLclTax1.deleter
	def GrmnLclTax1(self):
		del self._GrmnLclTax1
		self._GrmnLclTax1 = base_types.UninitialisedField(self, 'GrmnLclTax1', RateAndAmountFormat1Choice, False)

	@property
	def GrmnLclTax2(self):
		return self._GrmnLclTax2

	@GrmnLclTax2.setter
	def GrmnLclTax2(self, value):
		self._GrmnLclTax2 = value if value is not None else base_types.UninitialisedField(self, 'GrmnLclTax2', RateAndAmountFormat1Choice, False)

	@GrmnLclTax2.deleter
	def GrmnLclTax2(self):
		del self._GrmnLclTax2
		self._GrmnLclTax2 = base_types.UninitialisedField(self, 'GrmnLclTax2', RateAndAmountFormat1Choice, False)

	@property
	def GrmnLclTax3(self):
		return self._GrmnLclTax3

	@GrmnLclTax3.setter
	def GrmnLclTax3(self, value):
		self._GrmnLclTax3 = value if value is not None else base_types.UninitialisedField(self, 'GrmnLclTax3', RateAndAmountFormat1Choice, False)

	@GrmnLclTax3.deleter
	def GrmnLclTax3(self):
		del self._GrmnLclTax3
		self._GrmnLclTax3 = base_types.UninitialisedField(self, 'GrmnLclTax3', RateAndAmountFormat1Choice, False)

	@property
	def GrmnLclTax4(self):
		return self._GrmnLclTax4

	@GrmnLclTax4.setter
	def GrmnLclTax4(self, value):
		self._GrmnLclTax4 = value if value is not None else base_types.UninitialisedField(self, 'GrmnLclTax4', RateAndAmountFormat1Choice, False)

	@GrmnLclTax4.deleter
	def GrmnLclTax4(self):
		del self._GrmnLclTax4
		self._GrmnLclTax4 = base_types.UninitialisedField(self, 'GrmnLclTax4', RateAndAmountFormat1Choice, False)

	@property
	def GrssDvdd(self):
		return self._GrssDvdd

	@GrssDvdd.setter
	def GrssDvdd(self, value):
		self._GrssDvdd = value if value is not None else base_types.UninitialisedField(self, 'GrssDvdd', GrossDividendRate1Choice, False)

	@GrssDvdd.deleter
	def GrssDvdd(self):
		del self._GrssDvdd
		self._GrssDvdd = base_types.UninitialisedField(self, 'GrssDvdd', GrossDividendRate1Choice, False)

	@property
	def IndxFctr(self):
		return self._IndxFctr

	@IndxFctr.setter
	def IndxFctr(self, value):
		self._IndxFctr = value if value is not None else base_types.UninitialisedField(self, 'IndxFctr', RateAndAmountFormat1Choice, False)

	@IndxFctr.deleter
	def IndxFctr(self):
		del self._IndxFctr
		self._IndxFctr = base_types.UninitialisedField(self, 'IndxFctr', RateAndAmountFormat1Choice, False)

	@property
	def IntrstForUsdPmt(self):
		return self._IntrstForUsdPmt

	@IntrstForUsdPmt.setter
	def IntrstForUsdPmt(self, value):
		self._IntrstForUsdPmt = value if value is not None else base_types.UninitialisedField(self, 'IntrstForUsdPmt', RateAndAmountFormat1Choice, False)

	@IntrstForUsdPmt.deleter
	def IntrstForUsdPmt(self):
		del self._IntrstForUsdPmt
		self._IntrstForUsdPmt = base_types.UninitialisedField(self, 'IntrstForUsdPmt', RateAndAmountFormat1Choice, False)

	@property
	def MaxAllwdOvrsbcpt(self):
		return self._MaxAllwdOvrsbcpt

	@MaxAllwdOvrsbcpt.setter
	def MaxAllwdOvrsbcpt(self, value):
		self._MaxAllwdOvrsbcpt = value if value is not None else base_types.UninitialisedField(self, 'MaxAllwdOvrsbcpt', RateFormat1Choice, False)

	@MaxAllwdOvrsbcpt.deleter
	def MaxAllwdOvrsbcpt(self):
		del self._MaxAllwdOvrsbcpt
		self._MaxAllwdOvrsbcpt = base_types.UninitialisedField(self, 'MaxAllwdOvrsbcpt', RateFormat1Choice, False)

	@property
	def NetDvdd(self):
		return self._NetDvdd

	@NetDvdd.setter
	def NetDvdd(self, value):
		self._NetDvdd = value if value is not None else base_types.UninitialisedField(self, 'NetDvdd', NetDividendRate1Choice, False)

	@NetDvdd.deleter
	def NetDvdd(self):
		del self._NetDvdd
		self._NetDvdd = base_types.UninitialisedField(self, 'NetDvdd', NetDividendRate1Choice, False)

	@property
	def NewSctiesToUndrlygScties(self):
		return self._NewSctiesToUndrlygScties

	@NewSctiesToUndrlygScties.setter
	def NewSctiesToUndrlygScties(self, value):
		self._NewSctiesToUndrlygScties = value if value is not None else base_types.UninitialisedField(self, 'NewSctiesToUndrlygScties', RatioFormat2Choice, False)

	@NewSctiesToUndrlygScties.deleter
	def NewSctiesToUndrlygScties(self):
		del self._NewSctiesToUndrlygScties
		self._NewSctiesToUndrlygScties = base_types.UninitialisedField(self, 'NewSctiesToUndrlygScties', RatioFormat2Choice, False)

	@property
	def NewToOd(self):
		return self._NewToOd

	@NewToOd.setter
	def NewToOd(self, value):
		self._NewToOd = value if value is not None else base_types.UninitialisedField(self, 'NewToOd', RatioFormat2Choice, False)

	@NewToOd.deleter
	def NewToOd(self):
		del self._NewToOd
		self._NewToOd = base_types.UninitialisedField(self, 'NewToOd', RatioFormat2Choice, False)

	@property
	def NonResdtRate(self):
		return self._NonResdtRate

	@NonResdtRate.setter
	def NonResdtRate(self, value):
		self._NonResdtRate = value if value is not None else base_types.UninitialisedField(self, 'NonResdtRate', RateAndAmountFormat1Choice, False)

	@NonResdtRate.deleter
	def NonResdtRate(self):
		del self._NonResdtRate
		self._NonResdtRate = base_types.UninitialisedField(self, 'NonResdtRate', RateAndAmountFormat1Choice, False)

	@property
	def OrgnlAmt(self):
		return self._OrgnlAmt

	@OrgnlAmt.setter
	def OrgnlAmt(self, value):
		self._OrgnlAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlAmt', ActiveCurrencyAndAmount, False)

	@OrgnlAmt.deleter
	def OrgnlAmt(self):
		del self._OrgnlAmt
		self._OrgnlAmt = base_types.UninitialisedField(self, 'OrgnlAmt', ActiveCurrencyAndAmount, False)

	@property
	def Prratn(self):
		return self._Prratn

	@Prratn.setter
	def Prratn(self, value):
		self._Prratn = value if value is not None else base_types.UninitialisedField(self, 'Prratn', RateFormat1Choice, False)

	@Prratn.deleter
	def Prratn(self):
		del self._Prratn
		self._Prratn = base_types.UninitialisedField(self, 'Prratn', RateFormat1Choice, False)

	@property
	def PrvsnlDvdd(self):
		return self._PrvsnlDvdd

	@PrvsnlDvdd.setter
	def PrvsnlDvdd(self, value):
		self._PrvsnlDvdd = value if value is not None else base_types.UninitialisedField(self, 'PrvsnlDvdd', AmountAndRateFormat2Choice, False)

	@PrvsnlDvdd.deleter
	def PrvsnlDvdd(self):
		del self._PrvsnlDvdd
		self._PrvsnlDvdd = base_types.UninitialisedField(self, 'PrvsnlDvdd', AmountAndRateFormat2Choice, False)

	@property
	def RltdTax(self):
		return self._RltdTax

	@RltdTax.setter
	def RltdTax(self, value):
		self._RltdTax = value if value is not None else base_types.UninitialisedField(self, 'RltdTax', RelatedTaxType1, False)

	@RltdTax.deleter
	def RltdTax(self):
		del self._RltdTax
		self._RltdTax = base_types.UninitialisedField(self, 'RltdTax', RelatedTaxType1, False)

	@property
	def SlctnFee(self):
		return self._SlctnFee

	@SlctnFee.setter
	def SlctnFee(self, value):
		self._SlctnFee = value if value is not None else base_types.UninitialisedField(self, 'SlctnFee', RateFormat1Choice, False)

	@SlctnFee.deleter
	def SlctnFee(self):
		del self._SlctnFee
		self._SlctnFee = base_types.UninitialisedField(self, 'SlctnFee', RateFormat1Choice, False)

	@property
	def TaxOnIncm(self):
		return self._TaxOnIncm

	@TaxOnIncm.setter
	def TaxOnIncm(self, value):
		self._TaxOnIncm = value if value is not None else base_types.UninitialisedField(self, 'TaxOnIncm', RateFormat1Choice, False)

	@TaxOnIncm.deleter
	def TaxOnIncm(self):
		del self._TaxOnIncm
		self._TaxOnIncm = base_types.UninitialisedField(self, 'TaxOnIncm', RateFormat1Choice, False)

	@property
	def TaxOnPrft(self):
		return self._TaxOnPrft

	@TaxOnPrft.setter
	def TaxOnPrft(self, value):
		self._TaxOnPrft = value if value is not None else base_types.UninitialisedField(self, 'TaxOnPrft', RateFormat1Choice, False)

	@TaxOnPrft.deleter
	def TaxOnPrft(self):
		del self._TaxOnPrft
		self._TaxOnPrft = base_types.UninitialisedField(self, 'TaxOnPrft', RateFormat1Choice, False)

	@property
	def TaxRclm(self):
		return self._TaxRclm

	@TaxRclm.setter
	def TaxRclm(self, value):
		self._TaxRclm = value if value is not None else base_types.UninitialisedField(self, 'TaxRclm', RateFormat1Choice, False)

	@TaxRclm.deleter
	def TaxRclm(self):
		del self._TaxRclm
		self._TaxRclm = base_types.UninitialisedField(self, 'TaxRclm', RateFormat1Choice, False)

	@property
	def WhldgOfFrgnTax(self):
		return self._WhldgOfFrgnTax

	@WhldgOfFrgnTax.setter
	def WhldgOfFrgnTax(self, value):
		self._WhldgOfFrgnTax = value if value is not None else base_types.UninitialisedField(self, 'WhldgOfFrgnTax', RateAndAmountFormat1Choice, False)

	@WhldgOfFrgnTax.deleter
	def WhldgOfFrgnTax(self):
		del self._WhldgOfFrgnTax
		self._WhldgOfFrgnTax = base_types.UninitialisedField(self, 'WhldgOfFrgnTax', RateAndAmountFormat1Choice, False)

	@property
	def WhldgOfLclTax(self):
		return self._WhldgOfLclTax

	@WhldgOfLclTax.setter
	def WhldgOfLclTax(self, value):
		self._WhldgOfLclTax = value if value is not None else base_types.UninitialisedField(self, 'WhldgOfLclTax', RateAndAmountFormat1Choice, False)

	@WhldgOfLclTax.deleter
	def WhldgOfLclTax(self):
		del self._WhldgOfLclTax
		self._WhldgOfLclTax = base_types.UninitialisedField(self, 'WhldgOfLclTax', RateAndAmountFormat1Choice, False)

	@property
	def WhldgTax(self):
		return self._WhldgTax

	@WhldgTax.setter
	def WhldgTax(self, value):
		self._WhldgTax = value if value is not None else base_types.UninitialisedField(self, 'WhldgTax', RateFormat1Choice, False)

	@WhldgTax.deleter
	def WhldgTax(self):
		del self._WhldgTax
		self._WhldgTax = base_types.UninitialisedField(self, 'WhldgTax', RateFormat1Choice, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', ForeignExchangeTerms8, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', ForeignExchangeTerms8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlQtyForExstgScties', type=RatioFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlQtyForSbcbdRsltntScties', type=RatioFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTax', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblRate', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshIncntiv', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlDvdd', type=AmountAndRateFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclStmp', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullyFrnkd', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax1', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax2', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax3', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax4', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssDvdd', type=GrossDividendRate1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxFctr', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstForUsdPmt', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxAllwdOvrsbcpt', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetDvdd', type=NetDividendRate1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewSctiesToUndrlygScties', type=RatioFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewToOd', type=RatioFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonResdtRate', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prratn', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsnlDvdd', type=AmountAndRateFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdTax', type=RelatedTaxType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlctnFee', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnIncm', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnPrft', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclm', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgOfFrgnTax', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgOfLclTax', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTax', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=ForeignExchangeTerms8, min=0, max=1, mutex_group=None, array=False),
	))