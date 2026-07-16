# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyAndAmount
from . import DocumentIdentification7
from . import Max35Text
from . import TransactionStatus4

class ReportLine1(base_types._BaseFieldType):

	__slots__ = ["_AcmltdNetAmt", "_PurchsOrdrRef", "_PurchsOrdrTtlNetAmt", "_TxId", "_TxSts"]
	@property
	def AcmltdNetAmt(self):
		return self._AcmltdNetAmt

	@AcmltdNetAmt.setter
	def AcmltdNetAmt(self, value):
		self._AcmltdNetAmt = value if value is not None else base_types.UninitialisedField(self, 'AcmltdNetAmt', CurrencyAndAmount, False)

	@AcmltdNetAmt.deleter
	def AcmltdNetAmt(self):
		del self._AcmltdNetAmt
		self._AcmltdNetAmt = base_types.UninitialisedField(self, 'AcmltdNetAmt', CurrencyAndAmount, False)

	@property
	def PurchsOrdrRef(self):
		return self._PurchsOrdrRef

	@PurchsOrdrRef.setter
	def PurchsOrdrRef(self, value):
		self._PurchsOrdrRef = value if value is not None else base_types.UninitialisedField(self, 'PurchsOrdrRef', DocumentIdentification7, False)

	@PurchsOrdrRef.deleter
	def PurchsOrdrRef(self):
		del self._PurchsOrdrRef
		self._PurchsOrdrRef = base_types.UninitialisedField(self, 'PurchsOrdrRef', DocumentIdentification7, False)

	@property
	def PurchsOrdrTtlNetAmt(self):
		return self._PurchsOrdrTtlNetAmt

	@PurchsOrdrTtlNetAmt.setter
	def PurchsOrdrTtlNetAmt(self, value):
		self._PurchsOrdrTtlNetAmt = value if value is not None else base_types.UninitialisedField(self, 'PurchsOrdrTtlNetAmt', CurrencyAndAmount, False)

	@PurchsOrdrTtlNetAmt.deleter
	def PurchsOrdrTtlNetAmt(self):
		del self._PurchsOrdrTtlNetAmt
		self._PurchsOrdrTtlNetAmt = base_types.UninitialisedField(self, 'PurchsOrdrTtlNetAmt', CurrencyAndAmount, False)

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
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if value is not None else base_types.UninitialisedField(self, 'TxSts', TransactionStatus4, False)

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = base_types.UninitialisedField(self, 'TxSts', TransactionStatus4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcmltdNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsOrdrRef', type=DocumentIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsOrdrTtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
	))