# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageHeader12
from . import SecuritiesAccountAuditTrailOrOperationalError3Choice
from . import SupplementaryData1

class SecuritiesAccountAuditTrailReportV01(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_RptOrErr", "_SplmtryData"]
	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader12, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader12, False)

	@property
	def RptOrErr(self):
		return self._RptOrErr

	@RptOrErr.setter
	def RptOrErr(self, value):
		self._RptOrErr = value if value is not None else base_types.UninitialisedField(self, 'RptOrErr', SecuritiesAccountAuditTrailOrOperationalError3Choice, False)

	@RptOrErr.deleter
	def RptOrErr(self):
		del self._RptOrErr
		self._RptOrErr = base_types.UninitialisedField(self, 'RptOrErr', SecuritiesAccountAuditTrailOrOperationalError3Choice, False)

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
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptOrErr', type=SecuritiesAccountAuditTrailOrOperationalError3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))