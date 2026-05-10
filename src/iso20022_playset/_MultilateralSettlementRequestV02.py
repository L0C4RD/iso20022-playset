from . import base_types
from ._GroupHeader104 import GroupHeader104
from ._MultilateralSettlementRequest3 import MultilateralSettlementRequest3
from ._SupplementaryData1 import SupplementaryData1

class MultilateralSettlementRequestV02(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_SplmtryData", "_SttlmReq"]
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
	def SttlmReq(self):
		return self._SttlmReq

	@SttlmReq.setter
	def SttlmReq(self, value):
		self._SttlmReq = value if type(value) != base_types.auto else self.make_default("SttlmReq")

	@SttlmReq.deleter
	def SttlmReq(self):
		del self._SttlmReq
		self._SttlmReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader104, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmReq', type=MultilateralSettlementRequest3, min=1, max=None, mutex_group=None, array=True),
	))

