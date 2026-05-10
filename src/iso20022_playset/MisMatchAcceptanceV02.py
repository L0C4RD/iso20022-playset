import base_types
import SimpleIdentificationInformation
import MessageIdentification1

class MisMatchAcceptanceV02(base_types._BaseFieldType):

	__slots__ = ["_DataSetMtchRptRef", "_TxId", "_SubmitrTxRef", "_AccptncId"]
	@property
	def DataSetMtchRptRef(self):
		return self._DataSetMtchRptRef

	@DataSetMtchRptRef.setter
	def DataSetMtchRptRef(self, value):
		self._DataSetMtchRptRef = value if type(value) != auto else self.make_default("DataSetMtchRptRef")

	@DataSetMtchRptRef.deleter
	def DataSetMtchRptRef(self):
		del self._DataSetMtchRptRef
		self._DataSetMtchRptRef = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def SubmitrTxRef(self):
		return self._SubmitrTxRef

	@SubmitrTxRef.setter
	def SubmitrTxRef(self, value):
		self._SubmitrTxRef = value if type(value) != auto else self.make_default("SubmitrTxRef")

	@SubmitrTxRef.deleter
	def SubmitrTxRef(self):
		del self._SubmitrTxRef
		self._SubmitrTxRef = None

	@property
	def AccptncId(self):
		return self._AccptncId

	@AccptncId.setter
	def AccptncId(self, value):
		self._AccptncId = value if type(value) != auto else self.make_default("AccptncId")

	@AccptncId.deleter
	def AccptncId(self):
		del self._AccptncId
		self._AccptncId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSetMtchRptRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptncId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

