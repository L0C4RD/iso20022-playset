# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageIdentification1
from . import Reason2
from . import SimpleIdentificationInformation
from . import TransactionStatus3

class StatusChangeRequestV02(base_types._BaseFieldType):

	__slots__ = ["_ReqId", "_ReqRsn", "_ReqdSts", "_SubmitrTxRef", "_TxId"]
	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if value is not None else base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@property
	def ReqRsn(self):
		return self._ReqRsn

	@ReqRsn.setter
	def ReqRsn(self, value):
		self._ReqRsn = value if value is not None else base_types.UninitialisedField(self, 'ReqRsn', Reason2, False)

	@ReqRsn.deleter
	def ReqRsn(self):
		del self._ReqRsn
		self._ReqRsn = base_types.UninitialisedField(self, 'ReqRsn', Reason2, False)

	@property
	def ReqdSts(self):
		return self._ReqdSts

	@ReqdSts.setter
	def ReqdSts(self, value):
		self._ReqdSts = value if value is not None else base_types.UninitialisedField(self, 'ReqdSts', TransactionStatus3, False)

	@ReqdSts.deleter
	def ReqdSts(self):
		del self._ReqdSts
		self._ReqdSts = base_types.UninitialisedField(self, 'ReqdSts', TransactionStatus3, False)

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
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqRsn', type=Reason2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSts', type=TransactionStatus3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
	))