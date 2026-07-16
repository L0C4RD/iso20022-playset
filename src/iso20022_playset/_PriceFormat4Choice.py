# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountPrice1
from . import DecimalNumber
from . import PriceRate1
from . import PriceValueType5FormatChoice

class PriceFormat4Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_IndxPts", "_NotSpcfd", "_Rate"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', AmountPrice1, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', AmountPrice1, False)

	@property
	def IndxPts(self):
		return self._IndxPts

	@IndxPts.setter
	def IndxPts(self, value):
		self._IndxPts = value if value is not None else base_types.UninitialisedField(self, 'IndxPts', DecimalNumber, False)

	@IndxPts.deleter
	def IndxPts(self):
		del self._IndxPts
		self._IndxPts = base_types.UninitialisedField(self, 'IndxPts', DecimalNumber, False)

	@property
	def NotSpcfd(self):
		return self._NotSpcfd

	@NotSpcfd.setter
	def NotSpcfd(self, value):
		self._NotSpcfd = value if value is not None else base_types.UninitialisedField(self, 'NotSpcfd', PriceValueType5FormatChoice, False)

	@NotSpcfd.deleter
	def NotSpcfd(self):
		del self._NotSpcfd
		self._NotSpcfd = base_types.UninitialisedField(self, 'NotSpcfd', PriceValueType5FormatChoice, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PriceRate1, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PriceRate1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=AmountPrice1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxPts', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfd', type=PriceValueType5FormatChoice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=PriceRate1, min=0, max=1, mutex_group=1, array=False),
	))