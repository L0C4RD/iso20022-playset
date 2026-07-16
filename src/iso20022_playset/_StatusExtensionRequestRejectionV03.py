# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageIdentification1
from . import Reason2
from . import SimpleIdentificationInformation
from . import TransactionStatus4

class StatusExtensionRequestRejectionV03(base_types._BaseFieldType):

	__slots__ = ["_RjctnId", "_RjctnRsn", "_StsNotToBeXtnded", "_SubmitrTxRef", "_TxId"]
	@property
	def RjctnId(self):
		return self._RjctnId

	@RjctnId.setter
	def RjctnId(self, value):
		self._RjctnId = value if value is not None else base_types.UninitialisedField(self, 'RjctnId', MessageIdentification1, False)

	@RjctnId.deleter
	def RjctnId(self):
		del self._RjctnId
		self._RjctnId = base_types.UninitialisedField(self, 'RjctnId', MessageIdentification1, False)

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsn', Reason2, False)

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = base_types.UninitialisedField(self, 'RjctnRsn', Reason2, False)

	@property
	def StsNotToBeXtnded(self):
		return self._StsNotToBeXtnded

	@StsNotToBeXtnded.setter
	def StsNotToBeXtnded(self, value):
		self._StsNotToBeXtnded = value if value is not None else base_types.UninitialisedField(self, 'StsNotToBeXtnded', TransactionStatus4, False)

	@StsNotToBeXtnded.deleter
	def StsNotToBeXtnded(self):
		del self._StsNotToBeXtnded
		self._StsNotToBeXtnded = base_types.UninitialisedField(self, 'StsNotToBeXtnded', TransactionStatus4, False)

	@property
	def SubmitrTxRef(self):
		return self._SubmitrTxRef

	@SubmitrTxRef.setter
	def SubmitrTxRef(self, value):
		self._SubmitrTxRef = value if value is not None else base_types.UninitialisedField(self, 'SubmitrTxRef', SimpleIdentificationInformation, False)

	@SubmitrTxRef.deleter
	def SubmitrTxRef(self):
		del self._SubmitrTxRef
		self._SubmitrTxRef = base_types.UninitialisedField(self, 'SubmitrTxRef', SimpleIdentificationInformation, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', SimpleIdentificationInformation, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', SimpleIdentificationInformation, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=Reason2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsNotToBeXtnded', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
	))