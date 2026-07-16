# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClockSynchronisation3
from . import LocalDateTime1
from . import Max10000Binary
from . import Max256Text
from . import Max35Text
from . import Max70Text
from . import Max8Text
from . import PositiveNumber
from . import TerminalManagementAction3Code

class PaymentTerminalParameters8(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_ClckSynctn", "_LclDtTm", "_OffsetEnd", "_OffsetStart", "_OthrParams", "_OthrParamsLngth", "_ParamFrmtIdr", "_TmZoneLine", "_VndrId", "_Vrsn"]
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
	def ClckSynctn(self):
		return self._ClckSynctn

	@ClckSynctn.setter
	def ClckSynctn(self, value):
		self._ClckSynctn = value if value is not None else base_types.UninitialisedField(self, 'ClckSynctn', ClockSynchronisation3, False)

	@ClckSynctn.deleter
	def ClckSynctn(self):
		del self._ClckSynctn
		self._ClckSynctn = base_types.UninitialisedField(self, 'ClckSynctn', ClockSynchronisation3, False)

	@property
	def LclDtTm(self):
		return self._LclDtTm

	@LclDtTm.setter
	def LclDtTm(self, value):
		self._LclDtTm = value if value is not None else base_types.UninitialisedField(self, 'LclDtTm', LocalDateTime1, True)

	@LclDtTm.deleter
	def LclDtTm(self):
		del self._LclDtTm
		self._LclDtTm = base_types.UninitialisedField(self, 'LclDtTm', LocalDateTime1, True)

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
	def OthrParams(self):
		return self._OthrParams

	@OthrParams.setter
	def OthrParams(self, value):
		self._OthrParams = value if value is not None else base_types.UninitialisedField(self, 'OthrParams', Max10000Binary, False)

	@OthrParams.deleter
	def OthrParams(self):
		del self._OthrParams
		self._OthrParams = base_types.UninitialisedField(self, 'OthrParams', Max10000Binary, False)

	@property
	def OthrParamsLngth(self):
		return self._OthrParamsLngth

	@OthrParamsLngth.setter
	def OthrParamsLngth(self, value):
		self._OthrParamsLngth = value if value is not None else base_types.UninitialisedField(self, 'OthrParamsLngth', PositiveNumber, False)

	@OthrParamsLngth.deleter
	def OthrParamsLngth(self):
		del self._OthrParamsLngth
		self._OthrParamsLngth = base_types.UninitialisedField(self, 'OthrParamsLngth', PositiveNumber, False)

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
	def TmZoneLine(self):
		return self._TmZoneLine

	@TmZoneLine.setter
	def TmZoneLine(self, value):
		self._TmZoneLine = value if value is not None else base_types.UninitialisedField(self, 'TmZoneLine', Max70Text, True)

	@TmZoneLine.deleter
	def TmZoneLine(self):
		del self._TmZoneLine
		self._TmZoneLine = base_types.UninitialisedField(self, 'TmZoneLine', Max70Text, True)

	@property
	def VndrId(self):
		return self._VndrId

	@VndrId.setter
	def VndrId(self, value):
		self._VndrId = value if value is not None else base_types.UninitialisedField(self, 'VndrId', Max35Text, False)

	@VndrId.deleter
	def VndrId(self):
		del self._VndrId
		self._VndrId = base_types.UninitialisedField(self, 'VndrId', Max35Text, False)

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
		base_types.FieldEntry(name='ClckSynctn', type=ClockSynchronisation3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclDtTm', type=LocalDateTime1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OffsetEnd', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetStart', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrParams', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrParamsLngth', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ParamFrmtIdr', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmZoneLine', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VndrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))