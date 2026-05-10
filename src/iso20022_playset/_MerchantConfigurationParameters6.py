from . import base_types
from ._Max10000Binary import Max10000Binary
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._Max8Text import Max8Text
from ._NetworkParameters8 import NetworkParameters8
from ._PositiveNumber import PositiveNumber
from ._TerminalManagementAction3Code import TerminalManagementAction3Code

class MerchantConfigurationParameters6(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_MrchntId", "_OffsetEnd", "_OffsetStart", "_OthrParams", "_OthrParamsLngth", "_ParamFrmtIdr", "_Prxy", "_Vrsn"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != base_types.auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	@property
	def MrchntId(self):
		return self._MrchntId

	@MrchntId.setter
	def MrchntId(self, value):
		self._MrchntId = value if type(value) != base_types.auto else self.make_default("MrchntId")

	@MrchntId.deleter
	def MrchntId(self):
		del self._MrchntId
		self._MrchntId = None

	@property
	def OffsetEnd(self):
		return self._OffsetEnd

	@OffsetEnd.setter
	def OffsetEnd(self, value):
		self._OffsetEnd = value if type(value) != base_types.auto else self.make_default("OffsetEnd")

	@OffsetEnd.deleter
	def OffsetEnd(self):
		del self._OffsetEnd
		self._OffsetEnd = None

	@property
	def OffsetStart(self):
		return self._OffsetStart

	@OffsetStart.setter
	def OffsetStart(self, value):
		self._OffsetStart = value if type(value) != base_types.auto else self.make_default("OffsetStart")

	@OffsetStart.deleter
	def OffsetStart(self):
		del self._OffsetStart
		self._OffsetStart = None

	@property
	def OthrParams(self):
		return self._OthrParams

	@OthrParams.setter
	def OthrParams(self, value):
		self._OthrParams = value if type(value) != base_types.auto else self.make_default("OthrParams")

	@OthrParams.deleter
	def OthrParams(self):
		del self._OthrParams
		self._OthrParams = None

	@property
	def OthrParamsLngth(self):
		return self._OthrParamsLngth

	@OthrParamsLngth.setter
	def OthrParamsLngth(self, value):
		self._OthrParamsLngth = value if type(value) != base_types.auto else self.make_default("OthrParamsLngth")

	@OthrParamsLngth.deleter
	def OthrParamsLngth(self):
		del self._OthrParamsLngth
		self._OthrParamsLngth = None

	@property
	def ParamFrmtIdr(self):
		return self._ParamFrmtIdr

	@ParamFrmtIdr.setter
	def ParamFrmtIdr(self, value):
		self._ParamFrmtIdr = value if type(value) != base_types.auto else self.make_default("ParamFrmtIdr")

	@ParamFrmtIdr.deleter
	def ParamFrmtIdr(self):
		del self._ParamFrmtIdr
		self._ParamFrmtIdr = None

	@property
	def Prxy(self):
		return self._Prxy

	@Prxy.setter
	def Prxy(self, value):
		self._Prxy = value if type(value) != base_types.auto else self.make_default("Prxy")

	@Prxy.deleter
	def Prxy(self):
		del self._Prxy
		self._Prxy = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != base_types.auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetEnd', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetStart', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrParams', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrParamsLngth', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ParamFrmtIdr', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prxy', type=NetworkParameters8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))

