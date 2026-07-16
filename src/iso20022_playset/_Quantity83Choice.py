# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max30DecimalNumber

class Quantity83Choice(base_types._BaseFieldType):

	__slots__ = ["_ElctrncMnyTknSttlmQty", "_NtwkFeeQty"]
	@property
	def ElctrncMnyTknSttlmQty(self):
		return self._ElctrncMnyTknSttlmQty

	@ElctrncMnyTknSttlmQty.setter
	def ElctrncMnyTknSttlmQty(self, value):
		self._ElctrncMnyTknSttlmQty = value if value is not None else base_types.UninitialisedField(self, 'ElctrncMnyTknSttlmQty', Max30DecimalNumber, False)

	@ElctrncMnyTknSttlmQty.deleter
	def ElctrncMnyTknSttlmQty(self):
		del self._ElctrncMnyTknSttlmQty
		self._ElctrncMnyTknSttlmQty = base_types.UninitialisedField(self, 'ElctrncMnyTknSttlmQty', Max30DecimalNumber, False)

	@property
	def NtwkFeeQty(self):
		return self._NtwkFeeQty

	@NtwkFeeQty.setter
	def NtwkFeeQty(self, value):
		self._NtwkFeeQty = value if value is not None else base_types.UninitialisedField(self, 'NtwkFeeQty', Max30DecimalNumber, False)

	@NtwkFeeQty.deleter
	def NtwkFeeQty(self):
		del self._NtwkFeeQty
		self._NtwkFeeQty = base_types.UninitialisedField(self, 'NtwkFeeQty', Max30DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElctrncMnyTknSttlmQty', type=Max30DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtwkFeeQty', type=Max30DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))