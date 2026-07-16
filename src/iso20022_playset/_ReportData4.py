# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Entry2Code
from . import Exact4AlphaNumericText
from . import ISODate
from . import ISODateTime
from . import Max35Text

class ReportData4(base_types._BaseFieldType):

	__slots__ = ["_DtAndTmStmp", "_MsgId", "_SchdlTp", "_SttlmSsnIdr", "_Tp", "_ValDt"]
	@property
	def DtAndTmStmp(self):
		return self._DtAndTmStmp

	@DtAndTmStmp.setter
	def DtAndTmStmp(self, value):
		self._DtAndTmStmp = value if value is not None else base_types.UninitialisedField(self, 'DtAndTmStmp', ISODateTime, False)

	@DtAndTmStmp.deleter
	def DtAndTmStmp(self):
		del self._DtAndTmStmp
		self._DtAndTmStmp = base_types.UninitialisedField(self, 'DtAndTmStmp', ISODateTime, False)

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
	def SchdlTp(self):
		return self._SchdlTp

	@SchdlTp.setter
	def SchdlTp(self, value):
		self._SchdlTp = value if value is not None else base_types.UninitialisedField(self, 'SchdlTp', Exact4AlphaNumericText, False)

	@SchdlTp.deleter
	def SchdlTp(self):
		del self._SchdlTp
		self._SchdlTp = base_types.UninitialisedField(self, 'SchdlTp', Exact4AlphaNumericText, False)

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

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Entry2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Entry2Code, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtAndTmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchdlTp', type=Exact4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Entry2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))