from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._NettingCutOff2 import NettingCutOff2
from ._RequestData2 import RequestData2

class NettingCutOffReferenceDataUpdateRequestV02(base_types._BaseFieldType):

	__slots__ = ["_NetgCutOffReq", "_SplmtryData", "_ReqData"]
	@property
	def NetgCutOffReq(self):
		return self._NetgCutOffReq

	@NetgCutOffReq.setter
	def NetgCutOffReq(self, value):
		self._NetgCutOffReq = value if type(value) != base_types.auto else self.make_default("NetgCutOffReq")

	@NetgCutOffReq.deleter
	def NetgCutOffReq(self):
		del self._NetgCutOffReq
		self._NetgCutOffReq = None

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
	def ReqData(self):
		return self._ReqData

	@ReqData.setter
	def ReqData(self, value):
		self._ReqData = value if type(value) != base_types.auto else self.make_default("ReqData")

	@ReqData.deleter
	def ReqData(self):
		del self._ReqData
		self._ReqData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetgCutOffReq', type=NettingCutOff2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqData', type=RequestData2, min=1, max=1, mutex_group=None, array=False),
	))

