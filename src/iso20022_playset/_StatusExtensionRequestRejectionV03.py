# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MessageIdentification1 import MessageIdentification1
from ._Reason2 import Reason2
from ._SimpleIdentificationInformation import SimpleIdentificationInformation
from ._TransactionStatus4 import TransactionStatus4

class StatusExtensionRequestRejectionV03(base_types._BaseFieldType):

	__slots__ = ["_RjctnId", "_RjctnRsn", "_StsNotToBeXtnded", "_SubmitrTxRef", "_TxId"]
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
	def StsNotToBeXtnded(self):
		return self._StsNotToBeXtnded

	@StsNotToBeXtnded.setter
	def StsNotToBeXtnded(self, value):
		self._StsNotToBeXtnded = value if type(value) != base_types.auto else self.make_default("StsNotToBeXtnded")

	@StsNotToBeXtnded.deleter
	def StsNotToBeXtnded(self):
		del self._StsNotToBeXtnded
		self._StsNotToBeXtnded = None

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
		base_types.FieldEntry(name='RjctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=Reason2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsNotToBeXtnded', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
	))