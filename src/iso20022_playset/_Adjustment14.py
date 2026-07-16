# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Max70Text
from . import PercentageRate
from . import TrueFalseIndicator

class Adjustment14(base_types._BaseFieldType):

	__slots__ = ["_AddtlTp", "_Amt", "_Desc", "_Pctg", "_PrmtnCd", "_PrmtnCpnNb", "_PrmtnElgblty", "_Qty", "_Rsn", "_TaxOnOrgnlAmt", "_Tp", "_UnitPric"]
	@property
	def AddtlTp(self):
		return self._AddtlTp

	@AddtlTp.setter
	def AddtlTp(self, value):
		self._AddtlTp = value if value is not None else base_types.UninitialisedField(self, 'AddtlTp', Max35Text, False)

	@AddtlTp.deleter
	def AddtlTp(self):
		del self._AddtlTp
		self._AddtlTp = base_types.UninitialisedField(self, 'AddtlTp', Max35Text, False)

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
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max70Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max70Text, False)

	@property
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if value is not None else base_types.UninitialisedField(self, 'Pctg', PercentageRate, False)

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = base_types.UninitialisedField(self, 'Pctg', PercentageRate, False)

	@property
	def PrmtnCd(self):
		return self._PrmtnCd

	@PrmtnCd.setter
	def PrmtnCd(self, value):
		self._PrmtnCd = value if value is not None else base_types.UninitialisedField(self, 'PrmtnCd', Max35Text, False)

	@PrmtnCd.deleter
	def PrmtnCd(self):
		del self._PrmtnCd
		self._PrmtnCd = base_types.UninitialisedField(self, 'PrmtnCd', Max35Text, False)

	@property
	def PrmtnCpnNb(self):
		return self._PrmtnCpnNb

	@PrmtnCpnNb.setter
	def PrmtnCpnNb(self, value):
		self._PrmtnCpnNb = value if value is not None else base_types.UninitialisedField(self, 'PrmtnCpnNb', Max35Text, False)

	@PrmtnCpnNb.deleter
	def PrmtnCpnNb(self):
		del self._PrmtnCpnNb
		self._PrmtnCpnNb = base_types.UninitialisedField(self, 'PrmtnCpnNb', Max35Text, False)

	@property
	def PrmtnElgblty(self):
		return self._PrmtnElgblty

	@PrmtnElgblty.setter
	def PrmtnElgblty(self, value):
		self._PrmtnElgblty = value if value is not None else base_types.UninitialisedField(self, 'PrmtnElgblty', TrueFalseIndicator, False)

	@PrmtnElgblty.deleter
	def PrmtnElgblty(self):
		del self._PrmtnElgblty
		self._PrmtnElgblty = base_types.UninitialisedField(self, 'PrmtnElgblty', TrueFalseIndicator, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', DecimalNumber, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', DecimalNumber, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', Max35Text, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', Max35Text, False)

	@property
	def TaxOnOrgnlAmt(self):
		return self._TaxOnOrgnlAmt

	@TaxOnOrgnlAmt.setter
	def TaxOnOrgnlAmt(self, value):
		self._TaxOnOrgnlAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxOnOrgnlAmt', TrueFalseIndicator, False)

	@TaxOnOrgnlAmt.deleter
	def TaxOnOrgnlAmt(self):
		del self._TaxOnOrgnlAmt
		self._TaxOnOrgnlAmt = base_types.UninitialisedField(self, 'TaxOnOrgnlAmt', TrueFalseIndicator, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', ImpliedCurrencyAndAmount, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmtnCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmtnCpnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmtnElgblty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnOrgnlAmt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))