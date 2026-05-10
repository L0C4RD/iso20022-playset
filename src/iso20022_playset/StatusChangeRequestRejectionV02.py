from . import base_types
from .TransactionStatus3 import TransactionStatus3
from .Reason2 import Reason2
from .MessageIdentification1 import MessageIdentification1
from .SimpleIdentificationInformation import SimpleIdentificationInformation

class StatusChangeRequestRejectionV02(base_types._BaseFieldType):

	__slots__ = ["_RjctnRsn", "_TxId", "_SubmitrTxRef", "_RjctdStsChng", "_RjctnId"]
	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if type(value) != base_types.auto else self.make_default("RjctnRsn")

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = None

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
	def RjctdStsChng(self):
		return self._RjctdStsChng

	@RjctdStsChng.setter
	def RjctdStsChng(self, value):
		self._RjctdStsChng = value if type(value) != base_types.auto else self.make_default("RjctdStsChng")

	@RjctdStsChng.deleter
	def RjctdStsChng(self):
		del self._RjctdStsChng
		self._RjctdStsChng = None

	@property
	def RjctnId(self):
		return self._RjctnId

	@RjctnId.setter
	def RjctnId(self, value):
		self._RjctnId = value if type(value) != base_types.auto else self.make_default("RjctnId")

	@RjctnId.deleter
	def RjctnId(self):
		del self._RjctnId
		self._RjctnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctnRsn', type=Reason2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdStsChng', type=TransactionStatus3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

