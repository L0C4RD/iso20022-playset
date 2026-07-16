# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact4AlphaNumericText
from . import Max35Text
from . import RequestDetails5
from . import SupplementaryData1

class StaticDataReportV02(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_RptDtls", "_SplmtryData", "_SttlmSsnIdr"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@property
	def RptDtls(self):
		return self._RptDtls

	@RptDtls.setter
	def RptDtls(self, value):
		self._RptDtls = value if value is not None else base_types.UninitialisedField(self, 'RptDtls', RequestDetails5, False)

	@RptDtls.deleter
	def RptDtls(self):
		del self._RptDtls
		self._RptDtls = base_types.UninitialisedField(self, 'RptDtls', RequestDetails5, False)

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
	def SttlmSsnIdr(self):
		return self._SttlmSsnIdr

	@SttlmSsnIdr.setter
	def SttlmSsnIdr(self, value):
		self._SttlmSsnIdr = value if value is not None else base_types.UninitialisedField(self, 'SttlmSsnIdr', Exact4AlphaNumericText, False)

	@SttlmSsnIdr.deleter
	def SttlmSsnIdr(self):
		del self._SttlmSsnIdr
		self._SttlmSsnIdr = base_types.UninitialisedField(self, 'SttlmSsnIdr', Exact4AlphaNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtls', type=RequestDetails5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))