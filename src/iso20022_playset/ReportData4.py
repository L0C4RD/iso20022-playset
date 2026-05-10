import base_types
import Max35Text
import ISODateTime
import Exact4AlphaNumericText
import Entry2Code
import ISODate

class ReportData4(base_types._BaseFieldType):

	__slots__ = ["_ValDt", "_MsgId", "_Tp", "_DtAndTmStmp", "_SttlmSsnIdr", "_SchdlTp"]
	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def DtAndTmStmp(self):
		return self._DtAndTmStmp

	@DtAndTmStmp.setter
	def DtAndTmStmp(self, value):
		self._DtAndTmStmp = value if type(value) != auto else self.make_default("DtAndTmStmp")

	@DtAndTmStmp.deleter
	def DtAndTmStmp(self):
		del self._DtAndTmStmp
		self._DtAndTmStmp = None

	@property
	def SttlmSsnIdr(self):
		return self._SttlmSsnIdr

	@SttlmSsnIdr.setter
	def SttlmSsnIdr(self, value):
		self._SttlmSsnIdr = value if type(value) != auto else self.make_default("SttlmSsnIdr")

	@SttlmSsnIdr.deleter
	def SttlmSsnIdr(self):
		del self._SttlmSsnIdr
		self._SttlmSsnIdr = None

	@property
	def SchdlTp(self):
		return self._SchdlTp

	@SchdlTp.setter
	def SchdlTp(self, value):
		self._SchdlTp = value if type(value) != auto else self.make_default("SchdlTp")

	@SchdlTp.deleter
	def SchdlTp(self):
		del self._SchdlTp
		self._SchdlTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Entry2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAndTmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchdlTp', type=Exact4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
	))

