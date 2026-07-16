# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Count1
from . import MessageIdentification1
from . import RejectionReason1Choice
from . import SimpleIdentificationInformation

class AmendmentRejectionV02(base_types._BaseFieldType):

	__slots__ = ["_DltaRptRef", "_RjctdAmdmntNb", "_RjctnId", "_RjctnRsn", "_SubmitrTxRef", "_TxId"]
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
	def RjctdAmdmntNb(self):
		return self._RjctdAmdmntNb

	@RjctdAmdmntNb.setter
	def RjctdAmdmntNb(self, value):
		self._RjctdAmdmntNb = value if value is not None else base_types.UninitialisedField(self, 'RjctdAmdmntNb', Count1, False)

	@RjctdAmdmntNb.deleter
	def RjctdAmdmntNb(self):
		del self._RjctdAmdmntNb
		self._RjctdAmdmntNb = base_types.UninitialisedField(self, 'RjctdAmdmntNb', Count1, False)

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
		self._RjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason1Choice, False)

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason1Choice, False)

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
		base_types.FieldEntry(name='DltaRptRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdAmdmntNb', type=Count1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=RejectionReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
	))