from . import base_types
from ._ATMCommand15 import ATMCommand15
from ._SecurityParameters9 import SecurityParameters9
from ._Max140Binary import Max140Binary
from ._ATMCommand16 import ATMCommand16
from ._ATMEnvironment15 import ATMEnvironment15
from ._ATMSecurityContext3 import ATMSecurityContext3

class ATMKeyDownloadRequest5(base_types._BaseFieldType):

	__slots__ = ["_CmdRslt", "_ATMSctyParams", "_ATMSctyCntxt", "_HstChllng", "_Envt", "_CmdCntxt"]
	@property
	def ATMSctyCntxt(self):
		return self._ATMSctyCntxt

	@ATMSctyCntxt.setter
	def ATMSctyCntxt(self, value):
		self._ATMSctyCntxt = value if type(value) != base_types.auto else self.make_default("ATMSctyCntxt")

	@ATMSctyCntxt.deleter
	def ATMSctyCntxt(self):
		del self._ATMSctyCntxt
		self._ATMSctyCntxt = None

	@property
	def ATMSctyParams(self):
		return self._ATMSctyParams

	@ATMSctyParams.setter
	def ATMSctyParams(self, value):
		self._ATMSctyParams = value if type(value) != base_types.auto else self.make_default("ATMSctyParams")

	@ATMSctyParams.deleter
	def ATMSctyParams(self):
		del self._ATMSctyParams
		self._ATMSctyParams = None

	@property
	def CmdCntxt(self):
		return self._CmdCntxt

	@CmdCntxt.setter
	def CmdCntxt(self, value):
		self._CmdCntxt = value if type(value) != base_types.auto else self.make_default("CmdCntxt")

	@CmdCntxt.deleter
	def CmdCntxt(self):
		del self._CmdCntxt
		self._CmdCntxt = None

	@property
	def CmdRslt(self):
		return self._CmdRslt

	@CmdRslt.setter
	def CmdRslt(self, value):
		self._CmdRslt = value if type(value) != base_types.auto else self.make_default("CmdRslt")

	@CmdRslt.deleter
	def CmdRslt(self):
		del self._CmdRslt
		self._CmdRslt = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def HstChllng(self):
		return self._HstChllng

	@HstChllng.setter
	def HstChllng(self, value):
		self._HstChllng = value if type(value) != base_types.auto else self.make_default("HstChllng")

	@HstChllng.deleter
	def HstChllng(self):
		del self._HstChllng
		self._HstChllng = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMSctyCntxt', type=ATMSecurityContext3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMSctyParams', type=SecurityParameters9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdCntxt', type=ATMCommand16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmdRslt', type=ATMCommand15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
	))

