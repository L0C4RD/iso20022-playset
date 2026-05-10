import base_types
import Vote20
import SecurityPosition22
import Pagination1
import CommunicationAddress11
import Max35Text
import SupplementaryData1
import MeetingReference10
import NotificationType2Code
import Participation6

class MeetingResultDisseminationV10(base_types._BaseFieldType):

	__slots__ = ["_VoteRslt", "_SplmtryData", "_MtgRsltsDssmntnTp", "_Scty", "_PrvsMtgRsltsDssmntnId", "_Pgntn", "_AddtlInf", "_MtgRsltDssmntnId", "_MtgRef", "_Prtcptn"]
	@property
	def VoteRslt(self):
		return self._VoteRslt

	@VoteRslt.setter
	def VoteRslt(self, value):
		self._VoteRslt = value if type(value) != auto else self.make_default("VoteRslt")

	@VoteRslt.deleter
	def VoteRslt(self):
		del self._VoteRslt
		self._VoteRslt = None

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

	@property
	def MtgRsltsDssmntnTp(self):
		return self._MtgRsltsDssmntnTp

	@MtgRsltsDssmntnTp.setter
	def MtgRsltsDssmntnTp(self, value):
		self._MtgRsltsDssmntnTp = value if type(value) != auto else self.make_default("MtgRsltsDssmntnTp")

	@MtgRsltsDssmntnTp.deleter
	def MtgRsltsDssmntnTp(self):
		del self._MtgRsltsDssmntnTp
		self._MtgRsltsDssmntnTp = None

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if type(value) != auto else self.make_default("Scty")

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = None

	@property
	def PrvsMtgRsltsDssmntnId(self):
		return self._PrvsMtgRsltsDssmntnId

	@PrvsMtgRsltsDssmntnId.setter
	def PrvsMtgRsltsDssmntnId(self, value):
		self._PrvsMtgRsltsDssmntnId = value if type(value) != auto else self.make_default("PrvsMtgRsltsDssmntnId")

	@PrvsMtgRsltsDssmntnId.deleter
	def PrvsMtgRsltsDssmntnId(self):
		del self._PrvsMtgRsltsDssmntnId
		self._PrvsMtgRsltsDssmntnId = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def MtgRsltDssmntnId(self):
		return self._MtgRsltDssmntnId

	@MtgRsltDssmntnId.setter
	def MtgRsltDssmntnId(self, value):
		self._MtgRsltDssmntnId = value if type(value) != auto else self.make_default("MtgRsltDssmntnId")

	@MtgRsltDssmntnId.deleter
	def MtgRsltDssmntnId(self):
		del self._MtgRsltDssmntnId
		self._MtgRsltDssmntnId = None

	@property
	def MtgRef(self):
		return self._MtgRef

	@MtgRef.setter
	def MtgRef(self, value):
		self._MtgRef = value if type(value) != auto else self.make_default("MtgRef")

	@MtgRef.deleter
	def MtgRef(self):
		del self._MtgRef
		self._MtgRef = None

	@property
	def Prtcptn(self):
		return self._Prtcptn

	@Prtcptn.setter
	def Prtcptn(self, value):
		self._Prtcptn = value if type(value) != auto else self.make_default("Prtcptn")

	@Prtcptn.deleter
	def Prtcptn(self):
		del self._Prtcptn
		self._Prtcptn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VoteRslt', type=Vote20, min=1, max=1000, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtgRsltsDssmntnTp', type=NotificationType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Scty', type=SecurityPosition22, min=1, max=200, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsMtgRsltsDssmntnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CommunicationAddress11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRsltDssmntnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRef', type=MeetingReference10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtcptn', type=Participation6, min=0, max=1, mutex_group=None, array=False),
	))

