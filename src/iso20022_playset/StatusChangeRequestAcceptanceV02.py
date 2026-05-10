from . import base_types
from .SimpleIdentificationInformation import SimpleIdentificationInformation
from .TransactionStatus3 import TransactionStatus3
from .MessageIdentification1 import MessageIdentification1

class StatusChangeRequestAcceptanceV02(base_types._BaseFieldType):

	__slots__ = ["_SubmitrTxRef", "_AccptdSts", "_TxId", "_AccptncId"]
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
	def AccptdSts(self):
		return self._AccptdSts

	@AccptdSts.setter
	def AccptdSts(self, value):
		self._AccptdSts = value if type(value) != auto else self.make_default("AccptdSts")

	@AccptdSts.deleter
	def AccptdSts(self):
		del self._AccptdSts
		self._AccptdSts = None

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
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptdSts', type=TransactionStatus3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptncId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

