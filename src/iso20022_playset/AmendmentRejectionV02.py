from . import base_types
import RejectionReason1Choice
import MessageIdentification1
import Count1
import SimpleIdentificationInformation

class AmendmentRejectionV02(base_types._BaseFieldType):

	__slots__ = ["_SubmitrTxRef", "_TxId", "_RjctnId", "_DltaRptRef", "_RjctnRsn", "_RjctdAmdmntNb"]
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
	def DltaRptRef(self):
		return self._DltaRptRef

	@DltaRptRef.setter
	def DltaRptRef(self, value):
		self._DltaRptRef = value if type(value) != auto else self.make_default("DltaRptRef")

	@DltaRptRef.deleter
	def DltaRptRef(self):
		del self._DltaRptRef
		self._DltaRptRef = None

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
	def RjctdAmdmntNb(self):
		return self._RjctdAmdmntNb

	@RjctdAmdmntNb.setter
	def RjctdAmdmntNb(self, value):
		self._RjctdAmdmntNb = value if type(value) != auto else self.make_default("RjctdAmdmntNb")

	@RjctdAmdmntNb.deleter
	def RjctdAmdmntNb(self):
		del self._RjctdAmdmntNb
		self._RjctdAmdmntNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DltaRptRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=RejectionReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdAmdmntNb', type=Count1, min=1, max=1, mutex_group=None, array=False),
	))

