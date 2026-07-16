# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Max6NumericText
from . import TemporaryServicesCharge1Code

class Amount12(base_types._BaseFieldType):

	__slots__ = ["_Hrs", "_OthrTp", "_Rate", "_Tp"]
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
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

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
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TemporaryServicesCharge1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TemporaryServicesCharge1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hrs', type=Max6NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TemporaryServicesCharge1Code, min=0, max=1, mutex_group=None, array=False),
	))