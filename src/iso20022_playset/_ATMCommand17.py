from . import base_types
from .ATMCommand7Code import ATMCommand7Code
from .ATMCommandIdentification1 import ATMCommandIdentification1
from .TMSContactLevel2Code import TMSContactLevel2Code
from .ISODateTime import ISODateTime
from .ATMCommandParameters1Choice import ATMCommandParameters1Choice

class ATMCommand17(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_CmdParams", "_DtTm", "_CmdId", "_Urgcy"]
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

	@property
	def CmdParams(self):
		return self._CmdParams

	@CmdParams.setter
	def CmdParams(self, value):
		self._CmdParams = value if type(value) != base_types.auto else self.make_default("CmdParams")

	@CmdParams.deleter
	def CmdParams(self):
		del self._CmdParams
		self._CmdParams = None

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != base_types.auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

	@property
	def CmdId(self):
		return self._CmdId

	@CmdId.setter
	def CmdId(self, value):
		self._CmdId = value if type(value) != base_types.auto else self.make_default("CmdId")

	@CmdId.deleter
	def CmdId(self):
		del self._CmdId
		self._CmdId = None

	@property
	def Urgcy(self):
		return self._Urgcy

	@Urgcy.setter
	def Urgcy(self, value):
		self._Urgcy = value if type(value) != base_types.auto else self.make_default("Urgcy")

	@Urgcy.deleter
	def Urgcy(self):
		del self._Urgcy
		self._Urgcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=ATMCommand7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdParams', type=ATMCommandParameters1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdId', type=ATMCommandIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Urgcy', type=TMSContactLevel2Code, min=1, max=1, mutex_group=None, array=False),
	))

