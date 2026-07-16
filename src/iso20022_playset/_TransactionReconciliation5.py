# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Max70Text
from . import TransactionIdentifier1
from . import TransactionTotals12
from . import TrueFalseIndicator

class TransactionReconciliation5(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxData", "_ClsPrd", "_RcncltnId", "_RcncltnTxId", "_TxTtls"]
	@property
	def AddtlTxData(self):
		return self._AddtlTxData

	@AddtlTxData.setter
	def AddtlTxData(self, value):
		self._AddtlTxData = value if value is not None else base_types.UninitialisedField(self, 'AddtlTxData', Max70Text, False)

	@AddtlTxData.deleter
	def AddtlTxData(self):
		del self._AddtlTxData
		self._AddtlTxData = base_types.UninitialisedField(self, 'AddtlTxData', Max70Text, False)

	@property
	def ClsPrd(self):
		return self._ClsPrd

	@ClsPrd.setter
	def ClsPrd(self, value):
		self._ClsPrd = value if value is not None else base_types.UninitialisedField(self, 'ClsPrd', TrueFalseIndicator, False)

	@ClsPrd.deleter
	def ClsPrd(self):
		del self._ClsPrd
		self._ClsPrd = base_types.UninitialisedField(self, 'ClsPrd', TrueFalseIndicator, False)

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if value is not None else base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@property
	def RcncltnTxId(self):
		return self._RcncltnTxId

	@RcncltnTxId.setter
	def RcncltnTxId(self, value):
		self._RcncltnTxId = value if value is not None else base_types.UninitialisedField(self, 'RcncltnTxId', TransactionIdentifier1, False)

	@RcncltnTxId.deleter
	def RcncltnTxId(self):
		del self._RcncltnTxId
		self._RcncltnTxId = base_types.UninitialisedField(self, 'RcncltnTxId', TransactionIdentifier1, False)

	@property
	def TxTtls(self):
		return self._TxTtls

	@TxTtls.setter
	def TxTtls(self, value):
		self._TxTtls = value if value is not None else base_types.UninitialisedField(self, 'TxTtls', TransactionTotals12, True)

	@TxTtls.deleter
	def TxTtls(self):
		del self._TxTtls
		self._TxTtls = base_types.UninitialisedField(self, 'TxTtls', TransactionTotals12, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsPrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnTxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTtls', type=TransactionTotals12, min=0, max=None, mutex_group=None, array=True),
	))