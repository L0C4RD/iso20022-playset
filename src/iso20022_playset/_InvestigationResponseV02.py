# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvestigationRequest3 import InvestigationRequest3
from ._InvestigationResponse9 import InvestigationResponse9
from ._SupplementaryData1 import SupplementaryData1

class InvestigationResponseV02(base_types._BaseFieldType):

	__slots__ = ["_InvstgtnRspn", "_OrgnlInvstgtnReq", "_SplmtryData"]
	@property
	def InvstgtnRspn(self):
		return self._InvstgtnRspn

	@InvstgtnRspn.setter
	def InvstgtnRspn(self, value):
		self._InvstgtnRspn = value if type(value) != base_types.auto else self.make_default("InvstgtnRspn")

	@InvstgtnRspn.deleter
	def InvstgtnRspn(self):
		del self._InvstgtnRspn
		self._InvstgtnRspn = None

	@property
	def OrgnlInvstgtnReq(self):
		return self._OrgnlInvstgtnReq

	@OrgnlInvstgtnReq.setter
	def OrgnlInvstgtnReq(self, value):
		self._OrgnlInvstgtnReq = value if type(value) != base_types.auto else self.make_default("OrgnlInvstgtnReq")

	@OrgnlInvstgtnReq.deleter
	def OrgnlInvstgtnReq(self):
		del self._OrgnlInvstgtnReq
		self._OrgnlInvstgtnReq = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstgtnRspn', type=InvestigationResponse9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInvstgtnReq', type=InvestigationRequest3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))