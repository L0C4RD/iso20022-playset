# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GroupHeader104
from . import MultilateralSettlementRequest3
from . import SupplementaryData1

class MultilateralSettlementRequestV02(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_SplmtryData", "_SttlmReq"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', GroupHeader104, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', GroupHeader104, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, False)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, False)

	@property
	def SttlmReq(self):
		return self._SttlmReq

	@SttlmReq.setter
	def SttlmReq(self, value):
		self._SttlmReq = value if value is not None else base_types.UninitialisedField(self, 'SttlmReq', MultilateralSettlementRequest3, True)

	@SttlmReq.deleter
	def SttlmReq(self):
		del self._SttlmReq
		self._SttlmReq = base_types.UninitialisedField(self, 'SttlmReq', MultilateralSettlementRequest3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader104, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmReq', type=MultilateralSettlementRequest3, min=1, max=None, mutex_group=None, array=True),
	))