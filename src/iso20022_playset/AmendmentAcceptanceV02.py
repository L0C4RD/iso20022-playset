from . import base_types
from .Count1 import Count1
from .MessageIdentification1 import MessageIdentification1
from .SimpleIdentificationInformation import SimpleIdentificationInformation

class AmendmentAcceptanceV02(base_types._BaseFieldType):

	__slots__ = ["_AccptdAmdmntNb", "_DltaRptRef", "_SubmitrTxRef", "_TxId", "_AccptncId"]
	@property
	def AccptdAmdmntNb(self):
		return self._AccptdAmdmntNb

	@AccptdAmdmntNb.setter
	def AccptdAmdmntNb(self, value):
		self._AccptdAmdmntNb = value if type(value) != base_types.auto else self.make_default("AccptdAmdmntNb")

	@AccptdAmdmntNb.deleter
	def AccptdAmdmntNb(self):
		del self._AccptdAmdmntNb
		self._AccptdAmdmntNb = None

	@property
	def DltaRptRef(self):
		return self._DltaRptRef

	@DltaRptRef.setter
	def DltaRptRef(self, value):
		self._DltaRptRef = value if type(value) != base_types.auto else self.make_default("DltaRptRef")

	@DltaRptRef.deleter
	def DltaRptRef(self):
		del self._DltaRptRef
		self._DltaRptRef = None

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

	@property
	def AccptncId(self):
		return self._AccptncId

	@AccptncId.setter
	def AccptncId(self, value):
		self._AccptncId = value if type(value) != base_types.auto else self.make_default("AccptncId")

	@AccptncId.deleter
	def AccptncId(self):
		del self._AccptncId
		self._AccptncId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdAmdmntNb', type=Count1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DltaRptRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptncId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

