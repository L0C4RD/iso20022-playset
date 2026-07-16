# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationAddress11
from . import Max35Text
from . import MeetingReference10
from . import NotificationType2Code
from . import Pagination1
from . import Participation6
from . import SecurityPosition22
from . import SupplementaryData1
from . import Vote20

class MeetingResultDisseminationV10(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_MtgRef", "_MtgRsltDssmntnId", "_MtgRsltsDssmntnTp", "_Pgntn", "_Prtcptn", "_PrvsMtgRsltsDssmntnId", "_Scty", "_SplmtryData", "_VoteRslt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CommunicationAddress11, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CommunicationAddress11, False)

	@property
	def MtgRef(self):
		return self._MtgRef

	@MtgRef.setter
	def MtgRef(self, value):
		self._MtgRef = value if value is not None else base_types.UninitialisedField(self, 'MtgRef', MeetingReference10, False)

	@MtgRef.deleter
	def MtgRef(self):
		del self._MtgRef
		self._MtgRef = base_types.UninitialisedField(self, 'MtgRef', MeetingReference10, False)

	@property
	def MtgRsltDssmntnId(self):
		return self._MtgRsltDssmntnId

	@MtgRsltDssmntnId.setter
	def MtgRsltDssmntnId(self, value):
		self._MtgRsltDssmntnId = value if value is not None else base_types.UninitialisedField(self, 'MtgRsltDssmntnId', Max35Text, False)

	@MtgRsltDssmntnId.deleter
	def MtgRsltDssmntnId(self):
		del self._MtgRsltDssmntnId
		self._MtgRsltDssmntnId = base_types.UninitialisedField(self, 'MtgRsltDssmntnId', Max35Text, False)

	@property
	def MtgRsltsDssmntnTp(self):
		return self._MtgRsltsDssmntnTp

	@MtgRsltsDssmntnTp.setter
	def MtgRsltsDssmntnTp(self, value):
		self._MtgRsltsDssmntnTp = value if value is not None else base_types.UninitialisedField(self, 'MtgRsltsDssmntnTp', NotificationType2Code, False)

	@MtgRsltsDssmntnTp.deleter
	def MtgRsltsDssmntnTp(self):
		del self._MtgRsltsDssmntnTp
		self._MtgRsltsDssmntnTp = base_types.UninitialisedField(self, 'MtgRsltsDssmntnTp', NotificationType2Code, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def Prtcptn(self):
		return self._Prtcptn

	@Prtcptn.setter
	def Prtcptn(self, value):
		self._Prtcptn = value if value is not None else base_types.UninitialisedField(self, 'Prtcptn', Participation6, False)

	@Prtcptn.deleter
	def Prtcptn(self):
		del self._Prtcptn
		self._Prtcptn = base_types.UninitialisedField(self, 'Prtcptn', Participation6, False)

	@property
	def PrvsMtgRsltsDssmntnId(self):
		return self._PrvsMtgRsltsDssmntnId

	@PrvsMtgRsltsDssmntnId.setter
	def PrvsMtgRsltsDssmntnId(self, value):
		self._PrvsMtgRsltsDssmntnId = value if value is not None else base_types.UninitialisedField(self, 'PrvsMtgRsltsDssmntnId', Max35Text, False)

	@PrvsMtgRsltsDssmntnId.deleter
	def PrvsMtgRsltsDssmntnId(self):
		del self._PrvsMtgRsltsDssmntnId
		self._PrvsMtgRsltsDssmntnId = base_types.UninitialisedField(self, 'PrvsMtgRsltsDssmntnId', Max35Text, False)

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if value is not None else base_types.UninitialisedField(self, 'Scty', SecurityPosition22, True)

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = base_types.UninitialisedField(self, 'Scty', SecurityPosition22, True)

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

	@property
	def VoteRslt(self):
		return self._VoteRslt

	@VoteRslt.setter
	def VoteRslt(self, value):
		self._VoteRslt = value if value is not None else base_types.UninitialisedField(self, 'VoteRslt', Vote20, True)

	@VoteRslt.deleter
	def VoteRslt(self):
		del self._VoteRslt
		self._VoteRslt = base_types.UninitialisedField(self, 'VoteRslt', Vote20, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=CommunicationAddress11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRef', type=MeetingReference10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRsltDssmntnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRsltsDssmntnTp', type=NotificationType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtcptn', type=Participation6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsMtgRsltsDssmntnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Scty', type=SecurityPosition22, min=1, max=200, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VoteRslt', type=Vote20, min=1, max=1000, mutex_group=None, array=True),
	))