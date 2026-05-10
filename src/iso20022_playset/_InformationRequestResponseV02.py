from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .Max35Text import Max35Text
from .StatusResponse1Code import StatusResponse1Code
from .ReturnIndicator2 import ReturnIndicator2
from .SearchCriteria2Choice import SearchCriteria2Choice

class InformationRequestResponseV02(base_types._BaseFieldType):

	__slots__ = ["_SchCrit", "_RtrInd", "_InvstgtnId", "_SplmtryData", "_RspnId", "_RspnSts"]
	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if type(value) != base_types.auto else self.make_default("SchCrit")

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = None

	@property
	def RtrInd(self):
		return self._RtrInd

	@RtrInd.setter
	def RtrInd(self, value):
		self._RtrInd = value if type(value) != base_types.auto else self.make_default("RtrInd")

	@RtrInd.deleter
	def RtrInd(self):
		del self._RtrInd
		self._RtrInd = None

	@property
	def InvstgtnId(self):
		return self._InvstgtnId

	@InvstgtnId.setter
	def InvstgtnId(self, value):
		self._InvstgtnId = value if type(value) != base_types.auto else self.make_default("InvstgtnId")

	@InvstgtnId.deleter
	def InvstgtnId(self):
		del self._InvstgtnId
		self._InvstgtnId = None

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
	def RspnId(self):
		return self._RspnId

	@RspnId.setter
	def RspnId(self, value):
		self._RspnId = value if type(value) != base_types.auto else self.make_default("RspnId")

	@RspnId.deleter
	def RspnId(self):
		del self._RspnId
		self._RspnId = None

	@property
	def RspnSts(self):
		return self._RspnSts

	@RspnSts.setter
	def RspnSts(self, value):
		self._RspnSts = value if type(value) != base_types.auto else self.make_default("RspnSts")

	@RspnSts.deleter
	def RspnSts(self):
		del self._RspnSts
		self._RspnSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SchCrit', type=SearchCriteria2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrInd', type=ReturnIndicator2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstgtnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RspnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSts', type=StatusResponse1Code, min=1, max=1, mutex_group=None, array=False),
	))

