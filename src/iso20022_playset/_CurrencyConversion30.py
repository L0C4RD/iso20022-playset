# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyConversion29
from . import TrueFalseIndicator

class CurrencyConversion30(base_types._BaseFieldType):

	__slots__ = ["_AccptdByCrdhldr", "_Convs"]
	@property
	def AccptdByCrdhldr(self):
		return self._AccptdByCrdhldr

	@AccptdByCrdhldr.setter
	def AccptdByCrdhldr(self, value):
		self._AccptdByCrdhldr = value if value is not None else base_types.UninitialisedField(self, 'AccptdByCrdhldr', TrueFalseIndicator, False)

	@AccptdByCrdhldr.deleter
	def AccptdByCrdhldr(self):
		del self._AccptdByCrdhldr
		self._AccptdByCrdhldr = base_types.UninitialisedField(self, 'AccptdByCrdhldr', TrueFalseIndicator, False)

	@property
	def Convs(self):
		return self._Convs

	@Convs.setter
	def Convs(self, value):
		self._Convs = value if value is not None else base_types.UninitialisedField(self, 'Convs', CurrencyConversion29, False)

	@Convs.deleter
	def Convs(self):
		del self._Convs
		self._Convs = base_types.UninitialisedField(self, 'Convs', CurrencyConversion29, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdByCrdhldr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Convs', type=CurrencyConversion29, min=0, max=1, mutex_group=None, array=False),
	))