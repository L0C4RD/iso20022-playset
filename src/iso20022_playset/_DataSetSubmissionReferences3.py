# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DocumentIdentification7 import DocumentIdentification7
from ._Max35Text import Max35Text
from ._YesNoIndicator import YesNoIndicator

class DataSetSubmissionReferences3(base_types._BaseFieldType):

	__slots__ = ["_ForcdMtch", "_PurchsOrdrRef", "_SubmitrTxRef", "_TxId"]
	@property
	def ForcdMtch(self):
		return self._ForcdMtch

	@ForcdMtch.setter
	def ForcdMtch(self, value):
		self._ForcdMtch = value if type(value) != base_types.auto else self.make_default("ForcdMtch")

	@ForcdMtch.deleter
	def ForcdMtch(self):
		del self._ForcdMtch
		self._ForcdMtch = None

	@property
	def PurchsOrdrRef(self):
		return self._PurchsOrdrRef

	@PurchsOrdrRef.setter
	def PurchsOrdrRef(self, value):
		self._PurchsOrdrRef = value if type(value) != base_types.auto else self.make_default("PurchsOrdrRef")

	@PurchsOrdrRef.deleter
	def PurchsOrdrRef(self):
		del self._PurchsOrdrRef
		self._PurchsOrdrRef = None

	@property
	def SubmitrTxRef(self):
		return self._SubmitrTxRef

	@SubmitrTxRef.setter
	def SubmitrTxRef(self, value):
		self._SubmitrTxRef = value if type(value) != base_types.auto else self.make_default("SubmitrTxRef")

	@SubmitrTxRef.deleter
	def SubmitrTxRef(self):
		del self._SubmitrTxRef
		self._SubmitrTxRef = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ForcdMtch', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsOrdrRef', type=DocumentIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))