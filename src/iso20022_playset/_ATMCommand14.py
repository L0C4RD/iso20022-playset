# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommand7Code
from . import ATMCommandIdentification1
from . import ATMCommandParameters3Choice
from . import ATMCommandReason1Code
from . import ISODateTime
from . import Max70Text
from . import TMSContactLevel2Code

class ATMCommand14(base_types._BaseFieldType):

	__slots__ = ["_AddtlRsnInf", "_CmdId", "_CmdParams", "_DtTm", "_Rsn", "_Tp", "_TracRsn", "_Urgcy"]
	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlRsnInf', Max70Text, False)

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = base_types.UninitialisedField(self, 'AddtlRsnInf', Max70Text, False)

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
	def CmdParams(self):
		return self._CmdParams

	@CmdParams.setter
	def CmdParams(self, value):
		self._CmdParams = value if value is not None else base_types.UninitialisedField(self, 'CmdParams', ATMCommandParameters3Choice, False)

	@CmdParams.deleter
	def CmdParams(self):
		del self._CmdParams
		self._CmdParams = base_types.UninitialisedField(self, 'CmdParams', ATMCommandParameters3Choice, False)

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if value is not None else base_types.UninitialisedField(self, 'DtTm', ISODateTime, False)

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = base_types.UninitialisedField(self, 'DtTm', ISODateTime, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', ATMCommandReason1Code, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', ATMCommandReason1Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ATMCommand7Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ATMCommand7Code, False)

	@property
	def TracRsn(self):
		return self._TracRsn

	@TracRsn.setter
	def TracRsn(self, value):
		self._TracRsn = value if value is not None else base_types.UninitialisedField(self, 'TracRsn', ATMCommandReason1Code, True)

	@TracRsn.deleter
	def TracRsn(self):
		del self._TracRsn
		self._TracRsn = base_types.UninitialisedField(self, 'TracRsn', ATMCommandReason1Code, True)

	@property
	def Urgcy(self):
		return self._Urgcy

	@Urgcy.setter
	def Urgcy(self, value):
		self._Urgcy = value if value is not None else base_types.UninitialisedField(self, 'Urgcy', TMSContactLevel2Code, False)

	@Urgcy.deleter
	def Urgcy(self):
		del self._Urgcy
		self._Urgcy = base_types.UninitialisedField(self, 'Urgcy', TMSContactLevel2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRsnInf', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdId', type=ATMCommandIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdParams', type=ATMCommandParameters3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=ATMCommandReason1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ATMCommand7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TracRsn', type=ATMCommandReason1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Urgcy', type=TMSContactLevel2Code, min=1, max=1, mutex_group=None, array=False),
	))