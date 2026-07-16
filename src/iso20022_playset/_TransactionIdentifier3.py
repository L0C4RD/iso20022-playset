# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max35Text

class TransactionIdentifier3(base_types._BaseFieldType):

	__slots__ = ["_HstTxDtTm", "_TxDtTm", "_TxRef"]
	@property
	def HstTxDtTm(self):
		return self._HstTxDtTm

	@HstTxDtTm.setter
	def HstTxDtTm(self, value):
		self._HstTxDtTm = value if value is not None else base_types.UninitialisedField(self, 'HstTxDtTm', ISODateTime, False)

	@HstTxDtTm.deleter
	def HstTxDtTm(self):
		del self._HstTxDtTm
		self._HstTxDtTm = base_types.UninitialisedField(self, 'HstTxDtTm', ISODateTime, False)

	@property
	def TxDtTm(self):
		return self._TxDtTm

	@TxDtTm.setter
	def TxDtTm(self, value):
		self._TxDtTm = value if value is not None else base_types.UninitialisedField(self, 'TxDtTm', ISODateTime, False)

	@TxDtTm.deleter
	def TxDtTm(self):
		del self._TxDtTm
		self._TxDtTm = base_types.UninitialisedField(self, 'TxDtTm', ISODateTime, False)

	@property
	def TxRef(self):
		return self._TxRef

	@TxRef.setter
	def TxRef(self, value):
		self._TxRef = value if value is not None else base_types.UninitialisedField(self, 'TxRef', Max35Text, False)

	@TxRef.deleter
	def TxRef(self):
		del self._TxRef
		self._TxRef = base_types.UninitialisedField(self, 'TxRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstTxDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))