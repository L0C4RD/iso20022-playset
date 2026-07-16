# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageIdentification1
from . import SimpleIdentificationInformation
from . import TransactionStatus4

class StatusExtensionRequestAcceptanceV03(base_types._BaseFieldType):

	__slots__ = ["_AccptncId", "_SubmitrTxRef", "_TxId", "_XtndedSts"]
	@property
	def AccptncId(self):
		return self._AccptncId

	@AccptncId.setter
	def AccptncId(self, value):
		self._AccptncId = value if value is not None else base_types.UninitialisedField(self, 'AccptncId', MessageIdentification1, False)

	@AccptncId.deleter
	def AccptncId(self):
		del self._AccptncId
		self._AccptncId = base_types.UninitialisedField(self, 'AccptncId', MessageIdentification1, False)

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

	@property
	def XtndedSts(self):
		return self._XtndedSts

	@XtndedSts.setter
	def XtndedSts(self, value):
		self._XtndedSts = value if value is not None else base_types.UninitialisedField(self, 'XtndedSts', TransactionStatus4, False)

	@XtndedSts.deleter
	def XtndedSts(self):
		del self._XtndedSts
		self._XtndedSts = base_types.UninitialisedField(self, 'XtndedSts', TransactionStatus4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptncId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndedSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
	))