# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount
from . import Max6NumericText
from . import TemporaryServicesCharge2Code

class TemporaryServiceChargeRate1(base_types._BaseFieldType):

	__slots__ = ["_Hrs", "_Rate", "_Tp"]
	@property
	def Hrs(self):
		return self._Hrs

	@Hrs.setter
	def Hrs(self, value):
		self._Hrs = value if value is not None else base_types.UninitialisedField(self, 'Hrs', Max6NumericText, False)

	@Hrs.deleter
	def Hrs(self):
		del self._Hrs
		self._Hrs = base_types.UninitialisedField(self, 'Hrs', Max6NumericText, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', ImpliedCurrencyAndAmount, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', ImpliedCurrencyAndAmount, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TemporaryServicesCharge2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TemporaryServicesCharge2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hrs', type=Max6NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TemporaryServicesCharge2Code, min=0, max=1, mutex_group=None, array=False),
	))