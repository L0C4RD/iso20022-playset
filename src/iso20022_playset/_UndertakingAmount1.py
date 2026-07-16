# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Max2000Text
from . import PercentageRate

class UndertakingAmount1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Amt", "_PlusTlrnce"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def PlusTlrnce(self):
		return self._PlusTlrnce

	@PlusTlrnce.setter
	def PlusTlrnce(self, value):
		self._PlusTlrnce = value if value is not None else base_types.UninitialisedField(self, 'PlusTlrnce', PercentageRate, False)

	@PlusTlrnce.deleter
	def PlusTlrnce(self):
		del self._PlusTlrnce
		self._PlusTlrnce = base_types.UninitialisedField(self, 'PlusTlrnce', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlusTlrnce', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))