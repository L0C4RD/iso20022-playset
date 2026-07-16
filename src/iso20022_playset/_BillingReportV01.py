# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BillingReportOrError6Choice
from . import MessageHeader11
from . import SupplementaryData1

class BillingReportV01(base_types._BaseFieldType):

	__slots__ = ["_BllgRptOrErr", "_MsgHdr", "_SplmtryData"]
	@property
	def BllgRptOrErr(self):
		return self._BllgRptOrErr

	@BllgRptOrErr.setter
	def BllgRptOrErr(self, value):
		self._BllgRptOrErr = value if value is not None else base_types.UninitialisedField(self, 'BllgRptOrErr', BillingReportOrError6Choice, False)

	@BllgRptOrErr.deleter
	def BllgRptOrErr(self):
		del self._BllgRptOrErr
		self._BllgRptOrErr = base_types.UninitialisedField(self, 'BllgRptOrErr', BillingReportOrError6Choice, False)

	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader11, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader11, False)

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
		base_types.FieldEntry(name='BllgRptOrErr', type=BillingReportOrError6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))