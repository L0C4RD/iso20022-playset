# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import TradeTransactionIdentification24

class MissingMarginTransactionData2(base_types._BaseFieldType):

	__slots__ = ["_CollTmStmp", "_TxId"]
	@property
	def CollTmStmp(self):
		return self._CollTmStmp

	@CollTmStmp.setter
	def CollTmStmp(self, value):
		self._CollTmStmp = value if value is not None else base_types.UninitialisedField(self, 'CollTmStmp', ISODateTime, False)

	@CollTmStmp.deleter
	def CollTmStmp(self):
		del self._CollTmStmp
		self._CollTmStmp = base_types.UninitialisedField(self, 'CollTmStmp', ISODateTime, False)

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
		base_types.FieldEntry(name='CollTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TradeTransactionIdentification24, min=1, max=1, mutex_group=None, array=False),
	))