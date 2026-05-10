from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._MandateAmendment8 import MandateAmendment8
from ._GroupHeader110 import GroupHeader110

class MandateAmendmentRequestV08(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_UndrlygAmdmntDtls", "_SplmtryData"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != base_types.auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def UndrlygAmdmntDtls(self):
		return self._UndrlygAmdmntDtls

	@UndrlygAmdmntDtls.setter
	def UndrlygAmdmntDtls(self, value):
		self._UndrlygAmdmntDtls = value if type(value) != base_types.auto else self.make_default("UndrlygAmdmntDtls")

	@UndrlygAmdmntDtls.deleter
	def UndrlygAmdmntDtls(self):
		del self._UndrlygAmdmntDtls
		self._UndrlygAmdmntDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader110, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygAmdmntDtls', type=MandateAmendment8, min=1, max=None, mutex_group=None, array=True),
	))

