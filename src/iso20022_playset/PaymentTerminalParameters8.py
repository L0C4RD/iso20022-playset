from . import base_types
from .Max35Text import Max35Text
from .ClockSynchronisation3 import ClockSynchronisation3
from .LocalDateTime1 import LocalDateTime1
from .TerminalManagementAction3Code import TerminalManagementAction3Code
from .Max70Text import Max70Text
from .Max256Text import Max256Text
from .Max10000Binary import Max10000Binary
from .PositiveNumber import PositiveNumber
from .Max8Text import Max8Text

class PaymentTerminalParameters8(base_types._BaseFieldType):

	__slots__ = ["_ParamFrmtIdr", "_OthrParams", "_LclDtTm", "_OthrParamsLngth", "_OffsetEnd", "_Vrsn", "_OffsetStart", "_VndrId", "_ActnTp", "_ClckSynctn", "_TmZoneLine"]
	@property
	def ParamFrmtIdr(self):
		return self._ParamFrmtIdr

	@ParamFrmtIdr.setter
	def ParamFrmtIdr(self, value):
		self._ParamFrmtIdr = value if type(value) != auto else self.make_default("ParamFrmtIdr")

	@ParamFrmtIdr.deleter
	def ParamFrmtIdr(self):
		del self._ParamFrmtIdr
		self._ParamFrmtIdr = None

	@property
	def OthrParams(self):
		return self._OthrParams

	@OthrParams.setter
	def OthrParams(self, value):
		self._OthrParams = value if type(value) != auto else self.make_default("OthrParams")

	@OthrParams.deleter
	def OthrParams(self):
		del self._OthrParams
		self._OthrParams = None

	@property
	def LclDtTm(self):
		return self._LclDtTm

	@LclDtTm.setter
	def LclDtTm(self, value):
		self._LclDtTm = value if type(value) != auto else self.make_default("LclDtTm")

	@LclDtTm.deleter
	def LclDtTm(self):
		del self._LclDtTm
		self._LclDtTm = None

	@property
	def OthrParamsLngth(self):
		return self._OthrParamsLngth

	@OthrParamsLngth.setter
	def OthrParamsLngth(self, value):
		self._OthrParamsLngth = value if type(value) != auto else self.make_default("OthrParamsLngth")

	@OthrParamsLngth.deleter
	def OthrParamsLngth(self):
		del self._OthrParamsLngth
		self._OthrParamsLngth = None

	@property
	def OffsetEnd(self):
		return self._OffsetEnd

	@OffsetEnd.setter
	def OffsetEnd(self, value):
		self._OffsetEnd = value if type(value) != auto else self.make_default("OffsetEnd")

	@OffsetEnd.deleter
	def OffsetEnd(self):
		del self._OffsetEnd
		self._OffsetEnd = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def OffsetStart(self):
		return self._OffsetStart

	@OffsetStart.setter
	def OffsetStart(self, value):
		self._OffsetStart = value if type(value) != auto else self.make_default("OffsetStart")

	@OffsetStart.deleter
	def OffsetStart(self):
		del self._OffsetStart
		self._OffsetStart = None

	@property
	def VndrId(self):
		return self._VndrId

	@VndrId.setter
	def VndrId(self, value):
		self._VndrId = value if type(value) != auto else self.make_default("VndrId")

	@VndrId.deleter
	def VndrId(self):
		del self._VndrId
		self._VndrId = None

	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	@property
	def ClckSynctn(self):
		return self._ClckSynctn

	@ClckSynctn.setter
	def ClckSynctn(self, value):
		self._ClckSynctn = value if type(value) != auto else self.make_default("ClckSynctn")

	@ClckSynctn.deleter
	def ClckSynctn(self):
		del self._ClckSynctn
		self._ClckSynctn = None

	@property
	def TmZoneLine(self):
		return self._TmZoneLine

	@TmZoneLine.setter
	def TmZoneLine(self, value):
		self._TmZoneLine = value if type(value) != auto else self.make_default("TmZoneLine")

	@TmZoneLine.deleter
	def TmZoneLine(self):
		del self._TmZoneLine
		self._TmZoneLine = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ParamFrmtIdr', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrParams', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclDtTm', type=LocalDateTime1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrParamsLngth', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetEnd', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetStart', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VndrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClckSynctn', type=ClockSynchronisation3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmZoneLine', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
	))

