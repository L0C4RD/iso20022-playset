# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransactionStatus5

class TimeOutResult2(base_types._BaseFieldType):

	__slots__ = ["_TxFutrSts"]
	@property
	def TxFutrSts(self):
		return self._TxFutrSts

	@TxFutrSts.setter
	def TxFutrSts(self, value):
		self._TxFutrSts = value if value is not None else base_types.UninitialisedField(self, 'TxFutrSts', TransactionStatus5, False)

	@TxFutrSts.deleter
	def TxFutrSts(self):
		del self._TxFutrSts
		self._TxFutrSts = base_types.UninitialisedField(self, 'TxFutrSts', TransactionStatus5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxFutrSts', type=TransactionStatus5, min=1, max=1, mutex_group=None, array=False),
	))