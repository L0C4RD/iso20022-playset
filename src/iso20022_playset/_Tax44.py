# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AddendumTaxType4Code
from . import CreditDebit3Code
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import PercentageRate
from . import TrueFalseIndicator

class Tax44(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CdtDbt", "_Desc", "_InclInTtl", "_Rate", "_Tp", "_XmptRsn", "_Xmptn"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if value is not None else base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max35Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max35Text, False)

	@property
	def InclInTtl(self):
		return self._InclInTtl

	@InclInTtl.setter
	def InclInTtl(self, value):
		self._InclInTtl = value if value is not None else base_types.UninitialisedField(self, 'InclInTtl', TrueFalseIndicator, False)

	@InclInTtl.deleter
	def InclInTtl(self):
		del self._InclInTtl
		self._InclInTtl = base_types.UninitialisedField(self, 'InclInTtl', TrueFalseIndicator, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', AddendumTaxType4Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', AddendumTaxType4Code, False)

	@property
	def XmptRsn(self):
		return self._XmptRsn

	@XmptRsn.setter
	def XmptRsn(self, value):
		self._XmptRsn = value if value is not None else base_types.UninitialisedField(self, 'XmptRsn', Max35Text, False)

	@XmptRsn.deleter
	def XmptRsn(self):
		del self._XmptRsn
		self._XmptRsn = base_types.UninitialisedField(self, 'XmptRsn', Max35Text, False)

	@property
	def Xmptn(self):
		return self._Xmptn

	@Xmptn.setter
	def Xmptn(self, value):
		self._Xmptn = value if value is not None else base_types.UninitialisedField(self, 'Xmptn', TrueFalseIndicator, False)

	@Xmptn.deleter
	def Xmptn(self):
		del self._Xmptn
		self._Xmptn = base_types.UninitialisedField(self, 'Xmptn', TrueFalseIndicator, False)

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