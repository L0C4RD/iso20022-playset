# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NotionalAmountLegs5
from . import NotionalQuantityLegs5
from . import TradeTransactionIdentification24

class AbnormalValuesTransactionData2(base_types._BaseFieldType):

	__slots__ = ["_NtnlAmt", "_NtnlQty", "_TxId"]
	@property
	def NtnlAmt(self):
		return self._NtnlAmt

	@NtnlAmt.setter
	def NtnlAmt(self, value):
		self._NtnlAmt = value if value is not None else base_types.UninitialisedField(self, 'NtnlAmt', NotionalAmountLegs5, False)

	@NtnlAmt.deleter
	def NtnlAmt(self):
		del self._NtnlAmt
		self._NtnlAmt = base_types.UninitialisedField(self, 'NtnlAmt', NotionalAmountLegs5, False)

	@property
	def NtnlQty(self):
		return self._NtnlQty

	@NtnlQty.setter
	def NtnlQty(self, value):
		self._NtnlQty = value if value is not None else base_types.UninitialisedField(self, 'NtnlQty', NotionalQuantityLegs5, False)

	@NtnlQty.deleter
	def NtnlQty(self):
		del self._NtnlQty
		self._NtnlQty = base_types.UninitialisedField(self, 'NtnlQty', NotionalQuantityLegs5, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TradeTransactionIdentification24, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TradeTransactionIdentification24, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtnlAmt', type=NotionalAmountLegs5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlQty', type=NotionalQuantityLegs5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TradeTransactionIdentification24, min=1, max=1, mutex_group=None, array=False),
	))