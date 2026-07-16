# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection34
from . import BillingBalanceType1Choice
from . import BillingCurrencyType1Code

class BillingBalance1(base_types._BaseFieldType):

	__slots__ = ["_CcyTp", "_Tp", "_Val"]
	@property
	def CcyTp(self):
		return self._CcyTp

	@CcyTp.setter
	def CcyTp(self, value):
		self._CcyTp = value if value is not None else base_types.UninitialisedField(self, 'CcyTp', BillingCurrencyType1Code, False)

	@CcyTp.deleter
	def CcyTp(self):
		del self._CcyTp
		self._CcyTp = base_types.UninitialisedField(self, 'CcyTp', BillingCurrencyType1Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', BillingBalanceType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', BillingBalanceType1Choice, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', AmountAndDirection34, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', AmountAndDirection34, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyTp', type=BillingCurrencyType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BillingBalanceType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
	))