from . import base_types
from .Max35Text import Max35Text
from .Max256Text import Max256Text
from .TerminalManagementAction3Code import TerminalManagementAction3Code
from .PositiveNumber import PositiveNumber
from .ContentInformationType40 import ContentInformationType40
from .Max100KBinary import Max100KBinary
from .Max8Text import Max8Text

class ApplicationParameters13(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_ApplId", "_OffsetStart", "_ParamFrmtIdr", "_Params", "_ParamsLngth", "_OffsetEnd", "_NcrptdParams", "_Vrsn"]
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
	def ApplId(self):
		return self._ApplId

	@ApplId.setter
	def ApplId(self, value):
		self._ApplId = value if type(value) != base_types.auto else self.make_default("ApplId")

	@ApplId.deleter
	def ApplId(self):
		del self._ApplId
		self._ApplId = None

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
	def Params(self):
		return self._Params

	@Params.setter
	def Params(self, value):
		self._Params = value if type(value) != base_types.auto else self.make_default("Params")

	@Params.deleter
	def Params(self):
		del self._Params
		self._Params = None

	@property
	def ParamsLngth(self):
		return self._ParamsLngth

	@ParamsLngth.setter
	def ParamsLngth(self, value):
		self._ParamsLngth = value if type(value) != base_types.auto else self.make_default("ParamsLngth")

	@ParamsLngth.deleter
	def ParamsLngth(self):
		del self._ParamsLngth
		self._ParamsLngth = None

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
	def NcrptdParams(self):
		return self._NcrptdParams

	@NcrptdParams.setter
	def NcrptdParams(self, value):
		self._NcrptdParams = value if type(value) != base_types.auto else self.make_default("NcrptdParams")

	@NcrptdParams.deleter
	def NcrptdParams(self):
		del self._NcrptdParams
		self._NcrptdParams = None

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
		base_types.FieldEntry(name='ApplId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetStart', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ParamFrmtIdr', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Params', type=Max100KBinary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ParamsLngth', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetEnd', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdParams', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))

