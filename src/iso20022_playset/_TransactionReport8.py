# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PaymentIdentification8Choice
from . import TransactionOrError6Choice

class TransactionReport8(base_types._BaseFieldType):

	__slots__ = ["_PmtId", "_TxOrErr"]
	@property
	def PmtId(self):
		return self._PmtId

	@PmtId.setter
	def PmtId(self, value):
		self._PmtId = value if value is not None else base_types.UninitialisedField(self, 'PmtId', PaymentIdentification8Choice, False)

	@PmtId.deleter
	def PmtId(self):
		del self._PmtId
		self._PmtId = base_types.UninitialisedField(self, 'PmtId', PaymentIdentification8Choice, False)

	@property
	def TxOrErr(self):
		return self._TxOrErr

	@TxOrErr.setter
	def TxOrErr(self, value):
		self._TxOrErr = value if value is not None else base_types.UninitialisedField(self, 'TxOrErr', TransactionOrError6Choice, False)

	@TxOrErr.deleter
	def TxOrErr(self):
		del self._TxOrErr
		self._TxOrErr = base_types.UninitialisedField(self, 'TxOrErr', TransactionOrError6Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtId', type=PaymentIdentification8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOrErr', type=TransactionOrError6Choice, min=1, max=1, mutex_group=None, array=False),
	))