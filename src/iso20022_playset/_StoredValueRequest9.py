# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StoredValueData9
from . import TransactionIdentifier1

class StoredValueRequest9(base_types._BaseFieldType):

	__slots__ = ["_Data", "_SaleTxId"]
	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if value is not None else base_types.UninitialisedField(self, 'Data', StoredValueData9, True)

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = base_types.UninitialisedField(self, 'Data', StoredValueData9, True)

	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if value is not None else base_types.UninitialisedField(self, 'SaleTxId', TransactionIdentifier1, False)

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = base_types.UninitialisedField(self, 'SaleTxId', TransactionIdentifier1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Data', type=StoredValueData9, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
	))