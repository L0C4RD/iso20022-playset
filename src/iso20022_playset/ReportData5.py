from . import base_types
from .Value import Value
from .CallIn1Code import CallIn1Code
from .ISODateTime import ISODateTime
from .PayInCallItem import PayInCallItem
from .ISODate import ISODate
from .Exact4AlphaNumericText import Exact4AlphaNumericText
from .Max35Text import Max35Text

class ReportData5(base_types._BaseFieldType):

	__slots__ = ["_AcctVal", "_DtAndTmStmp", "_MsgId", "_PayInCallAmt", "_SttlmSsnIdr", "_ValDt", "_Tp"]
	@property
	def AcctVal(self):
		return self._AcctVal

	@AcctVal.setter
	def AcctVal(self, value):
		self._AcctVal = value if type(value) != base_types.auto else self.make_default("AcctVal")

	@AcctVal.deleter
	def AcctVal(self):
		del self._AcctVal
		self._AcctVal = None

	@property
	def DtAndTmStmp(self):
		return self._DtAndTmStmp

	@DtAndTmStmp.setter
	def DtAndTmStmp(self, value):
		self._DtAndTmStmp = value if type(value) != base_types.auto else self.make_default("DtAndTmStmp")

	@DtAndTmStmp.deleter
	def DtAndTmStmp(self):
		del self._DtAndTmStmp
		self._DtAndTmStmp = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def PayInCallAmt(self):
		return self._PayInCallAmt

	@PayInCallAmt.setter
	def PayInCallAmt(self, value):
		self._PayInCallAmt = value if type(value) != base_types.auto else self.make_default("PayInCallAmt")

	@PayInCallAmt.deleter
	def PayInCallAmt(self):
		del self._PayInCallAmt
		self._PayInCallAmt = None

	@property
	def SttlmSsnIdr(self):
		return self._SttlmSsnIdr

	@SttlmSsnIdr.setter
	def SttlmSsnIdr(self, value):
		self._SttlmSsnIdr = value if type(value) != base_types.auto else self.make_default("SttlmSsnIdr")

	@SttlmSsnIdr.deleter
	def SttlmSsnIdr(self):
		del self._SttlmSsnIdr
		self._SttlmSsnIdr = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctVal', type=Value, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtAndTmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PayInCallAmt', type=PayInCallItem, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CallIn1Code, min=1, max=1, mutex_group=None, array=False),
	))

