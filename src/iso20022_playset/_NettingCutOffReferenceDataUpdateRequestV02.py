# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NettingCutOff2
from . import RequestData2
from . import SupplementaryData1

class NettingCutOffReferenceDataUpdateRequestV02(base_types._BaseFieldType):

	__slots__ = ["_NetgCutOffReq", "_ReqData", "_SplmtryData"]
	@property
	def NetgCutOffReq(self):
		return self._NetgCutOffReq

	@NetgCutOffReq.setter
	def NetgCutOffReq(self, value):
		self._NetgCutOffReq = value if value is not None else base_types.UninitialisedField(self, 'NetgCutOffReq', NettingCutOff2, True)

	@NetgCutOffReq.deleter
	def NetgCutOffReq(self):
		del self._NetgCutOffReq
		self._NetgCutOffReq = base_types.UninitialisedField(self, 'NetgCutOffReq', NettingCutOff2, True)

	@property
	def ReqData(self):
		return self._ReqData

	@ReqData.setter
	def ReqData(self, value):
		self._ReqData = value if value is not None else base_types.UninitialisedField(self, 'ReqData', RequestData2, False)

	@ReqData.deleter
	def ReqData(self):
		del self._ReqData
		self._ReqData = base_types.UninitialisedField(self, 'ReqData', RequestData2, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetgCutOffReq', type=NettingCutOff2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqData', type=RequestData2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))