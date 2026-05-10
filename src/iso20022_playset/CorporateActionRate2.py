import base_types
import RatioFormat2Choice
import RelatedTaxType1
import RatioFormat1Choice
import AmountAndRateFormat2Choice
import ForeignExchangeTerms8
import ActiveCurrencyAndAmount
import RateFormat1Choice
import RateAndAmountFormat1Choice
import NetDividendRate1Choice
import GrossDividendRate1Choice

class CorporateActionRate2(base_types._BaseFieldType):

	__slots__ = ["_GrmnLclTax3", "_GrssDvdd", "_OrgnlAmt", "_XchgRate", "_WhldgOfLclTax", "_MaxAllwdOvrsbcpt", "_Chrgs", "_FsclStmp", "_GrmnLclTax1", "_SlctnFee", "_AddtlQtyForExstgScties", "_CshIncntiv", "_GrmnLclTax2", "_WhldgOfFrgnTax", "_AplblRate", "_TaxOnPrft", "_WhldgTax", "_TaxOnIncm", "_TaxRclm", "_NewSctiesToUndrlygScties", "_AddtlTax", "_RltdTax", "_NonResdtRate", "_PrvsnlDvdd", "_GrmnLclTax4", "_IntrstForUsdPmt", "_NetDvdd", "_FnlDvdd", "_Prratn", "_AddtlQtyForSbcbdRsltntScties", "_FullyFrnkd", "_NewToOd", "_IndxFctr"]
	@property
	def GrmnLclTax3(self):
		return self._GrmnLclTax3

	@GrmnLclTax3.setter
	def GrmnLclTax3(self, value):
		self._GrmnLclTax3 = value if type(value) != auto else self.make_default("GrmnLclTax3")

	@GrmnLclTax3.deleter
	def GrmnLclTax3(self):
		del self._GrmnLclTax3
		self._GrmnLclTax3 = None

	@property
	def GrssDvdd(self):
		return self._GrssDvdd

	@GrssDvdd.setter
	def GrssDvdd(self, value):
		self._GrssDvdd = value if type(value) != auto else self.make_default("GrssDvdd")

	@GrssDvdd.deleter
	def GrssDvdd(self):
		del self._GrssDvdd
		self._GrssDvdd = None

	@property
	def OrgnlAmt(self):
		return self._OrgnlAmt

	@OrgnlAmt.setter
	def OrgnlAmt(self, value):
		self._OrgnlAmt = value if type(value) != auto else self.make_default("OrgnlAmt")

	@OrgnlAmt.deleter
	def OrgnlAmt(self):
		del self._OrgnlAmt
		self._OrgnlAmt = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	@property
	def WhldgOfLclTax(self):
		return self._WhldgOfLclTax

	@WhldgOfLclTax.setter
	def WhldgOfLclTax(self, value):
		self._WhldgOfLclTax = value if type(value) != auto else self.make_default("WhldgOfLclTax")

	@WhldgOfLclTax.deleter
	def WhldgOfLclTax(self):
		del self._WhldgOfLclTax
		self._WhldgOfLclTax = None

	@property
	def MaxAllwdOvrsbcpt(self):
		return self._MaxAllwdOvrsbcpt

	@MaxAllwdOvrsbcpt.setter
	def MaxAllwdOvrsbcpt(self, value):
		self._MaxAllwdOvrsbcpt = value if type(value) != auto else self.make_default("MaxAllwdOvrsbcpt")

	@MaxAllwdOvrsbcpt.deleter
	def MaxAllwdOvrsbcpt(self):
		del self._MaxAllwdOvrsbcpt
		self._MaxAllwdOvrsbcpt = None

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if type(value) != auto else self.make_default("Chrgs")

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = None

	@property
	def FsclStmp(self):
		return self._FsclStmp

	@FsclStmp.setter
	def FsclStmp(self, value):
		self._FsclStmp = value if type(value) != auto else self.make_default("FsclStmp")

	@FsclStmp.deleter
	def FsclStmp(self):
		del self._FsclStmp
		self._FsclStmp = None

	@property
	def GrmnLclTax1(self):
		return self._GrmnLclTax1

	@GrmnLclTax1.setter
	def GrmnLclTax1(self, value):
		self._GrmnLclTax1 = value if type(value) != auto else self.make_default("GrmnLclTax1")

	@GrmnLclTax1.deleter
	def GrmnLclTax1(self):
		del self._GrmnLclTax1
		self._GrmnLclTax1 = None

	@property
	def SlctnFee(self):
		return self._SlctnFee

	@SlctnFee.setter
	def SlctnFee(self, value):
		self._SlctnFee = value if type(value) != auto else self.make_default("SlctnFee")

	@SlctnFee.deleter
	def SlctnFee(self):
		del self._SlctnFee
		self._SlctnFee = None

	@property
	def AddtlQtyForExstgScties(self):
		return self._AddtlQtyForExstgScties

	@AddtlQtyForExstgScties.setter
	def AddtlQtyForExstgScties(self, value):
		self._AddtlQtyForExstgScties = value if type(value) != auto else self.make_default("AddtlQtyForExstgScties")

	@AddtlQtyForExstgScties.deleter
	def AddtlQtyForExstgScties(self):
		del self._AddtlQtyForExstgScties
		self._AddtlQtyForExstgScties = None

	@property
	def CshIncntiv(self):
		return self._CshIncntiv

	@CshIncntiv.setter
	def CshIncntiv(self, value):
		self._CshIncntiv = value if type(value) != auto else self.make_default("CshIncntiv")

	@CshIncntiv.deleter
	def CshIncntiv(self):
		del self._CshIncntiv
		self._CshIncntiv = None

	@property
	def GrmnLclTax2(self):
		return self._GrmnLclTax2

	@GrmnLclTax2.setter
	def GrmnLclTax2(self, value):
		self._GrmnLclTax2 = value if type(value) != auto else self.make_default("GrmnLclTax2")

	@GrmnLclTax2.deleter
	def GrmnLclTax2(self):
		del self._GrmnLclTax2
		self._GrmnLclTax2 = None

	@property
	def WhldgOfFrgnTax(self):
		return self._WhldgOfFrgnTax

	@WhldgOfFrgnTax.setter
	def WhldgOfFrgnTax(self, value):
		self._WhldgOfFrgnTax = value if type(value) != auto else self.make_default("WhldgOfFrgnTax")

	@WhldgOfFrgnTax.deleter
	def WhldgOfFrgnTax(self):
		del self._WhldgOfFrgnTax
		self._WhldgOfFrgnTax = None

	@property
	def AplblRate(self):
		return self._AplblRate

	@AplblRate.setter
	def AplblRate(self, value):
		self._AplblRate = value if type(value) != auto else self.make_default("AplblRate")

	@AplblRate.deleter
	def AplblRate(self):
		del self._AplblRate
		self._AplblRate = None

	@property
	def TaxOnPrft(self):
		return self._TaxOnPrft

	@TaxOnPrft.setter
	def TaxOnPrft(self, value):
		self._TaxOnPrft = value if type(value) != auto else self.make_default("TaxOnPrft")

	@TaxOnPrft.deleter
	def TaxOnPrft(self):
		del self._TaxOnPrft
		self._TaxOnPrft = None

	@property
	def WhldgTax(self):
		return self._WhldgTax

	@WhldgTax.setter
	def WhldgTax(self, value):
		self._WhldgTax = value if type(value) != auto else self.make_default("WhldgTax")

	@WhldgTax.deleter
	def WhldgTax(self):
		del self._WhldgTax
		self._WhldgTax = None

	@property
	def TaxOnIncm(self):
		return self._TaxOnIncm

	@TaxOnIncm.setter
	def TaxOnIncm(self, value):
		self._TaxOnIncm = value if type(value) != auto else self.make_default("TaxOnIncm")

	@TaxOnIncm.deleter
	def TaxOnIncm(self):
		del self._TaxOnIncm
		self._TaxOnIncm = None

	@property
	def TaxRclm(self):
		return self._TaxRclm

	@TaxRclm.setter
	def TaxRclm(self, value):
		self._TaxRclm = value if type(value) != auto else self.make_default("TaxRclm")

	@TaxRclm.deleter
	def TaxRclm(self):
		del self._TaxRclm
		self._TaxRclm = None

	@property
	def NewSctiesToUndrlygScties(self):
		return self._NewSctiesToUndrlygScties

	@NewSctiesToUndrlygScties.setter
	def NewSctiesToUndrlygScties(self, value):
		self._NewSctiesToUndrlygScties = value if type(value) != auto else self.make_default("NewSctiesToUndrlygScties")

	@NewSctiesToUndrlygScties.deleter
	def NewSctiesToUndrlygScties(self):
		del self._NewSctiesToUndrlygScties
		self._NewSctiesToUndrlygScties = None

	@property
	def AddtlTax(self):
		return self._AddtlTax

	@AddtlTax.setter
	def AddtlTax(self, value):
		self._AddtlTax = value if type(value) != auto else self.make_default("AddtlTax")

	@AddtlTax.deleter
	def AddtlTax(self):
		del self._AddtlTax
		self._AddtlTax = None

	@property
	def RltdTax(self):
		return self._RltdTax

	@RltdTax.setter
	def RltdTax(self, value):
		self._RltdTax = value if type(value) != auto else self.make_default("RltdTax")

	@RltdTax.deleter
	def RltdTax(self):
		del self._RltdTax
		self._RltdTax = None

	@property
	def NonResdtRate(self):
		return self._NonResdtRate

	@NonResdtRate.setter
	def NonResdtRate(self, value):
		self._NonResdtRate = value if type(value) != auto else self.make_default("NonResdtRate")

	@NonResdtRate.deleter
	def NonResdtRate(self):
		del self._NonResdtRate
		self._NonResdtRate = None

	@property
	def PrvsnlDvdd(self):
		return self._PrvsnlDvdd

	@PrvsnlDvdd.setter
	def PrvsnlDvdd(self, value):
		self._PrvsnlDvdd = value if type(value) != auto else self.make_default("PrvsnlDvdd")

	@PrvsnlDvdd.deleter
	def PrvsnlDvdd(self):
		del self._PrvsnlDvdd
		self._PrvsnlDvdd = None

	@property
	def GrmnLclTax4(self):
		return self._GrmnLclTax4

	@GrmnLclTax4.setter
	def GrmnLclTax4(self, value):
		self._GrmnLclTax4 = value if type(value) != auto else self.make_default("GrmnLclTax4")

	@GrmnLclTax4.deleter
	def GrmnLclTax4(self):
		del self._GrmnLclTax4
		self._GrmnLclTax4 = None

	@property
	def IntrstForUsdPmt(self):
		return self._IntrstForUsdPmt

	@IntrstForUsdPmt.setter
	def IntrstForUsdPmt(self, value):
		self._IntrstForUsdPmt = value if type(value) != auto else self.make_default("IntrstForUsdPmt")

	@IntrstForUsdPmt.deleter
	def IntrstForUsdPmt(self):
		del self._IntrstForUsdPmt
		self._IntrstForUsdPmt = None

	@property
	def NetDvdd(self):
		return self._NetDvdd

	@NetDvdd.setter
	def NetDvdd(self, value):
		self._NetDvdd = value if type(value) != auto else self.make_default("NetDvdd")

	@NetDvdd.deleter
	def NetDvdd(self):
		del self._NetDvdd
		self._NetDvdd = None

	@property
	def FnlDvdd(self):
		return self._FnlDvdd

	@FnlDvdd.setter
	def FnlDvdd(self, value):
		self._FnlDvdd = value if type(value) != auto else self.make_default("FnlDvdd")

	@FnlDvdd.deleter
	def FnlDvdd(self):
		del self._FnlDvdd
		self._FnlDvdd = None

	@property
	def Prratn(self):
		return self._Prratn

	@Prratn.setter
	def Prratn(self, value):
		self._Prratn = value if type(value) != auto else self.make_default("Prratn")

	@Prratn.deleter
	def Prratn(self):
		del self._Prratn
		self._Prratn = None

	@property
	def AddtlQtyForSbcbdRsltntScties(self):
		return self._AddtlQtyForSbcbdRsltntScties

	@AddtlQtyForSbcbdRsltntScties.setter
	def AddtlQtyForSbcbdRsltntScties(self, value):
		self._AddtlQtyForSbcbdRsltntScties = value if type(value) != auto else self.make_default("AddtlQtyForSbcbdRsltntScties")

	@AddtlQtyForSbcbdRsltntScties.deleter
	def AddtlQtyForSbcbdRsltntScties(self):
		del self._AddtlQtyForSbcbdRsltntScties
		self._AddtlQtyForSbcbdRsltntScties = None

	@property
	def FullyFrnkd(self):
		return self._FullyFrnkd

	@FullyFrnkd.setter
	def FullyFrnkd(self, value):
		self._FullyFrnkd = value if type(value) != auto else self.make_default("FullyFrnkd")

	@FullyFrnkd.deleter
	def FullyFrnkd(self):
		del self._FullyFrnkd
		self._FullyFrnkd = None

	@property
	def NewToOd(self):
		return self._NewToOd

	@NewToOd.setter
	def NewToOd(self, value):
		self._NewToOd = value if type(value) != auto else self.make_default("NewToOd")

	@NewToOd.deleter
	def NewToOd(self):
		del self._NewToOd
		self._NewToOd = None

	@property
	def IndxFctr(self):
		return self._IndxFctr

	@IndxFctr.setter
	def IndxFctr(self, value):
		self._IndxFctr = value if type(value) != auto else self.make_default("IndxFctr")

	@IndxFctr.deleter
	def IndxFctr(self):
		del self._IndxFctr
		self._IndxFctr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrmnLclTax3', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssDvdd', type=GrossDividendRate1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=ForeignExchangeTerms8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgOfLclTax', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxAllwdOvrsbcpt', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclStmp', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax1', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlctnFee', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlQtyForExstgScties', type=RatioFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshIncntiv', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax2', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgOfFrgnTax', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblRate', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnPrft', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTax', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnIncm', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclm', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewSctiesToUndrlygScties', type=RatioFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTax', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdTax', type=RelatedTaxType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonResdtRate', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsnlDvdd', type=AmountAndRateFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrmnLclTax4', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstForUsdPmt', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetDvdd', type=NetDividendRate1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlDvdd', type=AmountAndRateFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prratn', type=RateFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlQtyForSbcbdRsltntScties', type=RatioFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullyFrnkd', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewToOd', type=RatioFormat2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxFctr', type=RateAndAmountFormat1Choice, min=0, max=1, mutex_group=None, array=False),
	))

