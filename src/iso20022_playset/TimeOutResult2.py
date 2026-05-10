from . import base_types
import TransactionStatus5

class TimeOutResult2(base_types._BaseFieldType):

	__slots__ = ["_TxFutrSts"]
	@property
	def TxFutrSts(self):
		return self._TxFutrSts

	@TxFutrSts.setter
	def TxFutrSts(self, value):
		self._TxFutrSts = value if type(value) != auto else self.make_default("TxFutrSts")

	@TxFutrSts.deleter
	def TxFutrSts(self):
		del self._TxFutrSts
		self._TxFutrSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxFutrSts', type=TransactionStatus5, min=1, max=1, mutex_group=None, array=False),
	))

