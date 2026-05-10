import base_types
import TransactionIdentifier1
import StoredValueData8

class StoredValueRequest8(base_types._BaseFieldType):

	__slots__ = ["_SaleTxId", "_Data"]
	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if type(value) != auto else self.make_default("SaleTxId")

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = None

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if type(value) != auto else self.make_default("Data")

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Data', type=StoredValueData8, min=1, max=None, mutex_group=None, array=True),
	))

