# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommand5Code
from . import ATMCommandIdentification1
from . import ISODateTime
from . import Max140Text
from . import TerminalManagementActionResult2Code

class ATMCommand8(base_types._BaseFieldType):

	__slots__ = ["_AddtlErrInf", "_CmdId", "_PrcdDtTm", "_ReqrdDtTm", "_Rslt", "_Tp"]
	@property
	def AddtlErrInf(self):
		return self._AddtlErrInf

	@AddtlErrInf.setter
	def AddtlErrInf(self, value):
		self._AddtlErrInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlErrInf', Max140Text, False)

	@AddtlErrInf.deleter
	def AddtlErrInf(self):
		del self._AddtlErrInf
		self._AddtlErrInf = base_types.UninitialisedField(self, 'AddtlErrInf', Max140Text, False)

	@property
	def CmdId(self):
		return self._CmdId

	@CmdId.setter
	def CmdId(self, value):
		self._CmdId = value if value is not None else base_types.UninitialisedField(self, 'CmdId', ATMCommandIdentification1, False)

	@CmdId.deleter
	def CmdId(self):
		del self._CmdId
		self._CmdId = base_types.UninitialisedField(self, 'CmdId', ATMCommandIdentification1, False)

	@property
	def PrcdDtTm(self):
		return self._PrcdDtTm

	@PrcdDtTm.setter
	def PrcdDtTm(self, value):
		self._PrcdDtTm = value if value is not None else base_types.UninitialisedField(self, 'PrcdDtTm', ISODateTime, False)

	@PrcdDtTm.deleter
	def PrcdDtTm(self):
		del self._PrcdDtTm
		self._PrcdDtTm = base_types.UninitialisedField(self, 'PrcdDtTm', ISODateTime, False)

	@property
	def ReqrdDtTm(self):
		return self._ReqrdDtTm

	@ReqrdDtTm.setter
	def ReqrdDtTm(self, value):
		self._ReqrdDtTm = value if value is not None else base_types.UninitialisedField(self, 'ReqrdDtTm', ISODateTime, False)

	@ReqrdDtTm.deleter
	def ReqrdDtTm(self):
		del self._ReqrdDtTm
		self._ReqrdDtTm = base_types.UninitialisedField(self, 'ReqrdDtTm', ISODateTime, False)

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', TerminalManagementActionResult2Code, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', TerminalManagementActionResult2Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ATMCommand5Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ATMCommand5Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlErrInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdId', type=ATMCommandIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcdDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=TerminalManagementActionResult2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ATMCommand5Code, min=1, max=1, mutex_group=None, array=False),
	))