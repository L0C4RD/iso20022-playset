from . import base_types
from ._AddendumTaxType4Code import AddendumTaxType4Code
from ._CreditDebit3Code import CreditDebit3Code
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max35Text import Max35Text
from ._PercentageRate import PercentageRate
from ._TrueFalseIndicator import TrueFalseIndicator

class Tax44(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CdtDbt", "_Desc", "_InclInTtl", "_Rate", "_Tp", "_XmptRsn", "_Xmptn"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

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
	def InclInTtl(self):
		return self._InclInTtl

	@InclInTtl.setter
	def InclInTtl(self, value):
		self._InclInTtl = value if type(value) != base_types.auto else self.make_default("InclInTtl")

	@InclInTtl.deleter
	def InclInTtl(self):
		del self._InclInTtl
		self._InclInTtl = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def XmptRsn(self):
		return self._XmptRsn

	@XmptRsn.setter
	def XmptRsn(self, value):
		self._XmptRsn = value if type(value) != base_types.auto else self.make_default("XmptRsn")

	@XmptRsn.deleter
	def XmptRsn(self):
		del self._XmptRsn
		self._XmptRsn = None

	@property
	def Xmptn(self):
		return self._Xmptn

	@Xmptn.setter
	def Xmptn(self, value):
		self._Xmptn = value if type(value) != base_types.auto else self.make_default("Xmptn")

	@Xmptn.deleter
	def Xmptn(self):
		del self._Xmptn
		self._Xmptn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InclInTtl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=AddendumTaxType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xmptn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

