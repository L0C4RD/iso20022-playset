# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import StatusAdviceReport3
from . import StatusReportRecord3
from . import SupplementaryData1

class MessageReportHeader4(base_types._BaseFieldType):

	__slots__ = ["_MsgRptIdr", "_MsgSts", "_RcrdSts", "_SplmtryData"]
	@property
	def MsgRptIdr(self):
		return self._MsgRptIdr

	@MsgRptIdr.setter
	def MsgRptIdr(self, value):
		self._MsgRptIdr = value if value is not None else base_types.UninitialisedField(self, 'MsgRptIdr', Max140Text, False)

	@MsgRptIdr.deleter
	def MsgRptIdr(self):
		del self._MsgRptIdr
		self._MsgRptIdr = base_types.UninitialisedField(self, 'MsgRptIdr', Max140Text, False)

	@property
	def MsgSts(self):
		return self._MsgSts

	@MsgSts.setter
	def MsgSts(self, value):
		self._MsgSts = value if value is not None else base_types.UninitialisedField(self, 'MsgSts', StatusAdviceReport3, False)

	@MsgSts.deleter
	def MsgSts(self):
		del self._MsgSts
		self._MsgSts = base_types.UninitialisedField(self, 'MsgSts', StatusAdviceReport3, False)

	@property
	def RcrdSts(self):
		return self._RcrdSts

	@RcrdSts.setter
	def RcrdSts(self, value):
		self._RcrdSts = value if value is not None else base_types.UninitialisedField(self, 'RcrdSts', StatusReportRecord3, True)

	@RcrdSts.deleter
	def RcrdSts(self):
		del self._RcrdSts
		self._RcrdSts = base_types.UninitialisedField(self, 'RcrdSts', StatusReportRecord3, True)

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
		base_types.FieldEntry(name='MsgRptIdr', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgSts', type=StatusAdviceReport3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdSts', type=StatusReportRecord3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))