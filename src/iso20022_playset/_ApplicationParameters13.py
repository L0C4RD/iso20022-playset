# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType40
from . import Max100KBinary
from . import Max256Text
from . import Max35Text
from . import Max8Text
from . import PositiveNumber
from . import TerminalManagementAction3Code

class ApplicationParameters13(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_ApplId", "_NcrptdParams", "_OffsetEnd", "_OffsetStart", "_ParamFrmtIdr", "_Params", "_ParamsLngth", "_Vrsn"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction3Code, False)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction3Code, False)

	@property
	def ApplId(self):
		return self._ApplId

	@ApplId.setter
	def ApplId(self, value):
		self._ApplId = value if value is not None else base_types.UninitialisedField(self, 'ApplId', Max35Text, False)

	@ApplId.deleter
	def ApplId(self):
		del self._ApplId
		self._ApplId = base_types.UninitialisedField(self, 'ApplId', Max35Text, False)

	@property
	def NcrptdParams(self):
		return self._NcrptdParams

	@NcrptdParams.setter
	def NcrptdParams(self, value):
		self._NcrptdParams = value if value is not None else base_types.UninitialisedField(self, 'NcrptdParams', ContentInformationType40, False)

	@NcrptdParams.deleter
	def NcrptdParams(self):
		del self._NcrptdParams
		self._NcrptdParams = base_types.UninitialisedField(self, 'NcrptdParams', ContentInformationType40, False)

	@property
	def OffsetEnd(self):
		return self._OffsetEnd

	@OffsetEnd.setter
	def OffsetEnd(self, value):
		self._OffsetEnd = value if value is not None else base_types.UninitialisedField(self, 'OffsetEnd', PositiveNumber, False)

	@OffsetEnd.deleter
	def OffsetEnd(self):
		del self._OffsetEnd
		self._OffsetEnd = base_types.UninitialisedField(self, 'OffsetEnd', PositiveNumber, False)

	@property
	def OffsetStart(self):
		return self._OffsetStart

	@OffsetStart.setter
	def OffsetStart(self, value):
		self._OffsetStart = value if value is not None else base_types.UninitialisedField(self, 'OffsetStart', PositiveNumber, False)

	@OffsetStart.deleter
	def OffsetStart(self):
		del self._OffsetStart
		self._OffsetStart = base_types.UninitialisedField(self, 'OffsetStart', PositiveNumber, False)

	@property
	def ParamFrmtIdr(self):
		return self._ParamFrmtIdr

	@ParamFrmtIdr.setter
	def ParamFrmtIdr(self, value):
		self._ParamFrmtIdr = value if value is not None else base_types.UninitialisedField(self, 'ParamFrmtIdr', Max8Text, False)

	@ParamFrmtIdr.deleter
	def ParamFrmtIdr(self):
		del self._ParamFrmtIdr
		self._ParamFrmtIdr = base_types.UninitialisedField(self, 'ParamFrmtIdr', Max8Text, False)

	@property
	def Params(self):
		return self._Params

	@Params.setter
	def Params(self, value):
		self._Params = value if value is not None else base_types.UninitialisedField(self, 'Params', Max100KBinary, True)

	@Params.deleter
	def Params(self):
		del self._Params
		self._Params = base_types.UninitialisedField(self, 'Params', Max100KBinary, True)

	@property
	def ParamsLngth(self):
		return self._ParamsLngth

	@ParamsLngth.setter
	def ParamsLngth(self, value):
		self._ParamsLngth = value if value is not None else base_types.UninitialisedField(self, 'ParamsLngth', PositiveNumber, False)

	@ParamsLngth.deleter
	def ParamsLngth(self):
		del self._ParamsLngth
		self._ParamsLngth = base_types.UninitialisedField(self, 'ParamsLngth', PositiveNumber, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Max256Text, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdParams', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetEnd', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetStart', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ParamFrmtIdr', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Params', type=Max100KBinary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ParamsLngth', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))