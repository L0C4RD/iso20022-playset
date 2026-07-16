# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import InitialMarginExposure1

class InitialMarginRequirement1(base_types._BaseFieldType):

	__slots__ = ["_Cdt", "_InitlMrgnXpsr"]
	@property
	def Cdt(self):
		return self._Cdt

	@Cdt.setter
	def Cdt(self, value):
		self._Cdt = value if value is not None else base_types.UninitialisedField(self, 'Cdt', ActiveCurrencyAndAmount, False)

	@Cdt.deleter
	def Cdt(self):
		del self._Cdt
		self._Cdt = base_types.UninitialisedField(self, 'Cdt', ActiveCurrencyAndAmount, False)

	@property
	def InitlMrgnXpsr(self):
		return self._InitlMrgnXpsr

	@InitlMrgnXpsr.setter
	def InitlMrgnXpsr(self, value):
		self._InitlMrgnXpsr = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgnXpsr', InitialMarginExposure1, True)

	@InitlMrgnXpsr.deleter
	def InitlMrgnXpsr(self):
		del self._InitlMrgnXpsr
		self._InitlMrgnXpsr = base_types.UninitialisedField(self, 'InitlMrgnXpsr', InitialMarginExposure1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlMrgnXpsr', type=InitialMarginExposure1, min=1, max=None, mutex_group=None, array=True),
	))