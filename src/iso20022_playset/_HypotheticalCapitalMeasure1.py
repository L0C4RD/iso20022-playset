# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Max35Text

class HypotheticalCapitalMeasure1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_DfltWtrfllId"]
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
	def DfltWtrfllId(self):
		return self._DfltWtrfllId

	@DfltWtrfllId.setter
	def DfltWtrfllId(self, value):
		self._DfltWtrfllId = value if value is not None else base_types.UninitialisedField(self, 'DfltWtrfllId', Max35Text, False)

	@DfltWtrfllId.deleter
	def DfltWtrfllId(self):
		del self._DfltWtrfllId
		self._DfltWtrfllId = base_types.UninitialisedField(self, 'DfltWtrfllId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfltWtrfllId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))