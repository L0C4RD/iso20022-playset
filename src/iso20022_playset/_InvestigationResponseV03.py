# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestigationRequest50
from . import InvestigationResponse23
from . import SupplementaryData1

class InvestigationResponseV03(base_types._BaseFieldType):

	__slots__ = ["_InvstgtnRspn", "_OrgnlInvstgtnReq", "_SplmtryData"]
	@property
	def InvstgtnRspn(self):
		return self._InvstgtnRspn

	@InvstgtnRspn.setter
	def InvstgtnRspn(self, value):
		self._InvstgtnRspn = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnRspn', InvestigationResponse23, False)

	@InvstgtnRspn.deleter
	def InvstgtnRspn(self):
		del self._InvstgtnRspn
		self._InvstgtnRspn = base_types.UninitialisedField(self, 'InvstgtnRspn', InvestigationResponse23, False)

	@property
	def OrgnlInvstgtnReq(self):
		return self._OrgnlInvstgtnReq

	@OrgnlInvstgtnReq.setter
	def OrgnlInvstgtnReq(self, value):
		self._OrgnlInvstgtnReq = value if value is not None else base_types.UninitialisedField(self, 'OrgnlInvstgtnReq', InvestigationRequest50, False)

	@OrgnlInvstgtnReq.deleter
	def OrgnlInvstgtnReq(self):
		del self._OrgnlInvstgtnReq
		self._OrgnlInvstgtnReq = base_types.UninitialisedField(self, 'OrgnlInvstgtnReq', InvestigationRequest50, False)

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
		base_types.FieldEntry(name='InvstgtnRspn', type=InvestigationResponse23, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInvstgtnReq', type=InvestigationRequest50, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))