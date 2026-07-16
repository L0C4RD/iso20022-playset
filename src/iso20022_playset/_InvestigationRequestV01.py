# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestigationReason2
from . import InvestigationRequest2
from . import SupplementaryData1

class InvestigationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_InvstgtnData", "_InvstgtnReq", "_SplmtryData"]
	@property
	def InvstgtnData(self):
		return self._InvstgtnData

	@InvstgtnData.setter
	def InvstgtnData(self, value):
		self._InvstgtnData = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnData', InvestigationReason2, True)

	@InvstgtnData.deleter
	def InvstgtnData(self):
		del self._InvstgtnData
		self._InvstgtnData = base_types.UninitialisedField(self, 'InvstgtnData', InvestigationReason2, True)

	@property
	def InvstgtnReq(self):
		return self._InvstgtnReq

	@InvstgtnReq.setter
	def InvstgtnReq(self, value):
		self._InvstgtnReq = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnReq', InvestigationRequest2, False)

	@InvstgtnReq.deleter
	def InvstgtnReq(self):
		del self._InvstgtnReq
		self._InvstgtnReq = base_types.UninitialisedField(self, 'InvstgtnReq', InvestigationRequest2, False)

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
		base_types.FieldEntry(name='InvstgtnData', type=InvestigationReason2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstgtnReq', type=InvestigationRequest2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))