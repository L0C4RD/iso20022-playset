# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StoredValueData8 import StoredValueData8
from ._TransactionIdentifier1 import TransactionIdentifier1

class StoredValueRequest8(base_types._BaseFieldType):

	__slots__ = ["_Data", "_SaleTxId"]
	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if type(value) != base_types.auto else self.make_default("Data")

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = None

	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if type(value) != base_types.auto else self.make_default("SaleTxId")

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Data', type=StoredValueData8, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
	))