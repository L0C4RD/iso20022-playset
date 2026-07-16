# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LongPaymentIdentification4
from . import Max35Text
from . import Max70Text
from . import QueueTransactionIdentification1
from . import ShortPaymentIdentification4
from . import UUIDv4Identifier

class PaymentIdentification8Choice(base_types._BaseFieldType):

	__slots__ = ["_LngBizId", "_PrtryId", "_QId", "_ShrtBizId", "_TxId", "_UETR"]
	@property
	def LngBizId(self):
		return self._LngBizId

	@LngBizId.setter
	def LngBizId(self, value):
		self._LngBizId = value if value is not None else base_types.UninitialisedField(self, 'LngBizId', LongPaymentIdentification4, False)

	@LngBizId.deleter
	def LngBizId(self):
		del self._LngBizId
		self._LngBizId = base_types.UninitialisedField(self, 'LngBizId', LongPaymentIdentification4, False)

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if value is not None else base_types.UninitialisedField(self, 'PrtryId', Max70Text, False)

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = base_types.UninitialisedField(self, 'PrtryId', Max70Text, False)

	@property
	def QId(self):
		return self._QId

	@QId.setter
	def QId(self, value):
		self._QId = value if value is not None else base_types.UninitialisedField(self, 'QId', QueueTransactionIdentification1, False)

	@QId.deleter
	def QId(self):
		del self._QId
		self._QId = base_types.UninitialisedField(self, 'QId', QueueTransactionIdentification1, False)

	@property
	def ShrtBizId(self):
		return self._ShrtBizId

	@ShrtBizId.setter
	def ShrtBizId(self, value):
		self._ShrtBizId = value if value is not None else base_types.UninitialisedField(self, 'ShrtBizId', ShortPaymentIdentification4, False)

	@ShrtBizId.deleter
	def ShrtBizId(self):
		del self._ShrtBizId
		self._ShrtBizId = base_types.UninitialisedField(self, 'ShrtBizId', ShortPaymentIdentification4, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@property
	def UETR(self):
		return self._UETR

	@UETR.setter
	def UETR(self, value):
		self._UETR = value if value is not None else base_types.UninitialisedField(self, 'UETR', UUIDv4Identifier, False)

	@UETR.deleter
	def UETR(self):
		del self._UETR
		self._UETR = base_types.UninitialisedField(self, 'UETR', UUIDv4Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LngBizId', type=LongPaymentIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=Max70Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QId', type=QueueTransactionIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ShrtBizId', type=ShortPaymentIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=1, array=False),
	))