import base_types
import ATMCommand7Code
import ATMCommandParameters3Choice
import TMSContactLevel2Code
import ATMCommandIdentification1
import ISODateTime
import Max70Text
import ATMCommandReason1Code

class ATMCommand14(base_types._BaseFieldType):

	__slots__ = ["_TracRsn", "_Tp", "_Rsn", "_CmdParams", "_CmdId", "_Urgcy", "_AddtlRsnInf", "_DtTm"]
	@property
	def TracRsn(self):
		return self._TracRsn

	@TracRsn.setter
	def TracRsn(self, value):
		self._TracRsn = value if type(value) != auto else self.make_default("TracRsn")

	@TracRsn.deleter
	def TracRsn(self):
		del self._TracRsn
		self._TracRsn = None

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
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def CmdParams(self):
		return self._CmdParams

	@CmdParams.setter
	def CmdParams(self, value):
		self._CmdParams = value if type(value) != auto else self.make_default("CmdParams")

	@CmdParams.deleter
	def CmdParams(self):
		del self._CmdParams
		self._CmdParams = None

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
	def Urgcy(self):
		return self._Urgcy

	@Urgcy.setter
	def Urgcy(self, value):
		self._Urgcy = value if type(value) != auto else self.make_default("Urgcy")

	@Urgcy.deleter
	def Urgcy(self):
		del self._Urgcy
		self._Urgcy = None

	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if type(value) != auto else self.make_default("AddtlRsnInf")

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = None

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TracRsn', type=ATMCommandReason1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=ATMCommand7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=ATMCommandReason1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdParams', type=ATMCommandParameters3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdId', type=ATMCommandIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Urgcy', type=TMSContactLevel2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRsnInf', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

