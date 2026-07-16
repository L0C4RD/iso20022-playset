# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max30DecimalNumber
from . import SecurityIdentification19

class NetworkFee1(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_NtwkFeeQty"]
	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

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
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtwkFeeQty', type=Max30DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))