from . import base_types
from .SimpleIdentificationInformation import SimpleIdentificationInformation
from .TransactionStatus4 import TransactionStatus4
from .Reason2 import Reason2
from .MessageIdentification1 import MessageIdentification1

class StatusExtensionRequestRejectionV03(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_RjctnId", "_StsNotToBeXtnded", "_RjctnRsn", "_SubmitrTxRef"]
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
	def RjctnId(self):
		return self._RjctnId

	@RjctnId.setter
	def RjctnId(self, value):
		self._RjctnId = value if type(value) != auto else self.make_default("RjctnId")

	@RjctnId.deleter
	def RjctnId(self):
		del self._RjctnId
		self._RjctnId = None

	@property
	def StsNotToBeXtnded(self):
		return self._StsNotToBeXtnded

	@StsNotToBeXtnded.setter
	def StsNotToBeXtnded(self, value):
		self._StsNotToBeXtnded = value if type(value) != auto else self.make_default("StsNotToBeXtnded")

	@StsNotToBeXtnded.deleter
	def StsNotToBeXtnded(self):
		del self._StsNotToBeXtnded
		self._StsNotToBeXtnded = None

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if type(value) != auto else self.make_default("RjctnRsn")

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsNotToBeXtnded', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=Reason2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
	))

