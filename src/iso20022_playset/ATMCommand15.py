import base_types
import ATMCommand7Code
import ATMCommandIdentification1
import ISODateTime
import TerminalManagementActionResult2Code
import Max140Text

class ATMCommand15(base_types._BaseFieldType):

	__slots__ = ["_ReqrdDtTm", "_AddtlErrInf", "_CmdId", "_Tp", "_PrcdDtTm", "_Rslt"]
	@property
	def ReqrdDtTm(self):
		return self._ReqrdDtTm

	@ReqrdDtTm.setter
	def ReqrdDtTm(self, value):
		self._ReqrdDtTm = value if type(value) != auto else self.make_default("ReqrdDtTm")

	@ReqrdDtTm.deleter
	def ReqrdDtTm(self):
		del self._ReqrdDtTm
		self._ReqrdDtTm = None

	@property
	def AddtlErrInf(self):
		return self._AddtlErrInf

	@AddtlErrInf.setter
	def AddtlErrInf(self, value):
		self._AddtlErrInf = value if type(value) != auto else self.make_default("AddtlErrInf")

	@AddtlErrInf.deleter
	def AddtlErrInf(self):
		del self._AddtlErrInf
		self._AddtlErrInf = None

	@property
	def CmdId(self):
		return self._CmdId

	@CmdId.setter
	def CmdId(self, value):
		self._CmdId = value if type(value) != auto else self.make_default("CmdId")

	@CmdId.deleter
	def CmdId(self):
		del self._CmdId
		self._CmdId = None

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
	def PrcdDtTm(self):
		return self._PrcdDtTm

	@PrcdDtTm.setter
	def PrcdDtTm(self, value):
		self._PrcdDtTm = value if type(value) != auto else self.make_default("PrcdDtTm")

	@PrcdDtTm.deleter
	def PrcdDtTm(self):
		del self._PrcdDtTm
		self._PrcdDtTm = None

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqrdDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlErrInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdId', type=ATMCommandIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ATMCommand7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcdDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=TerminalManagementActionResult2Code, min=1, max=1, mutex_group=None, array=False),
	))

