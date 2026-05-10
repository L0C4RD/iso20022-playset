from . import base_types
import InvestigationReason2
import InvestigationRequest2
import SupplementaryData1

class InvestigationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_InvstgtnReq", "_InvstgtnData", "_SplmtryData"]
	@property
	def InvstgtnReq(self):
		return self._InvstgtnReq

	@InvstgtnReq.setter
	def InvstgtnReq(self, value):
		self._InvstgtnReq = value if type(value) != auto else self.make_default("InvstgtnReq")

	@InvstgtnReq.deleter
	def InvstgtnReq(self):
		del self._InvstgtnReq
		self._InvstgtnReq = None

	@property
	def InvstgtnData(self):
		return self._InvstgtnData

	@InvstgtnData.setter
	def InvstgtnData(self, value):
		self._InvstgtnData = value if type(value) != auto else self.make_default("InvstgtnData")

	@InvstgtnData.deleter
	def InvstgtnData(self):
		del self._InvstgtnData
		self._InvstgtnData = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstgtnReq', type=InvestigationRequest2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnData', type=InvestigationReason2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

