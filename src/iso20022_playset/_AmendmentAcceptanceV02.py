# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Count1
from . import MessageIdentification1
from . import SimpleIdentificationInformation

class AmendmentAcceptanceV02(base_types._BaseFieldType):

	__slots__ = ["_AccptdAmdmntNb", "_AccptncId", "_DltaRptRef", "_SubmitrTxRef", "_TxId"]
	@property
	def AccptdAmdmntNb(self):
		return self._AccptdAmdmntNb

	@AccptdAmdmntNb.setter
	def AccptdAmdmntNb(self, value):
		self._AccptdAmdmntNb = value if value is not None else base_types.UninitialisedField(self, 'AccptdAmdmntNb', Count1, False)

	@AccptdAmdmntNb.deleter
	def AccptdAmdmntNb(self):
		del self._AccptdAmdmntNb
		self._AccptdAmdmntNb = base_types.UninitialisedField(self, 'AccptdAmdmntNb', Count1, False)

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
	def DltaRptRef(self):
		return self._DltaRptRef

	@DltaRptRef.setter
	def DltaRptRef(self, value):
		self._DltaRptRef = value if value is not None else base_types.UninitialisedField(self, 'DltaRptRef', MessageIdentification1, False)

	@DltaRptRef.deleter
	def DltaRptRef(self):
		del self._DltaRptRef
		self._DltaRptRef = base_types.UninitialisedField(self, 'DltaRptRef', MessageIdentification1, False)

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
		base_types.FieldEntry(name='AccptdAmdmntNb', type=Count1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptncId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DltaRptRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
	))