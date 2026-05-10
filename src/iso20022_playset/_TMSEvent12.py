from . import base_types
from .DeviceResponse8 import DeviceResponse8
from .Max35Text import Max35Text
from .TerminalManagementActionResult5Code import TerminalManagementActionResult5Code
from .ISODateTime import ISODateTime
from .Max70Text import Max70Text
from .TMSActionIdentification10 import TMSActionIdentification10

class TMSEvent12(base_types._BaseFieldType):

	__slots__ = ["_TmStmp", "_DvcRspn", "_AddtlErrInf", "_TermnlMgrId", "_Rslt", "_ActnId"]
	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if type(value) != base_types.auto else self.make_default("TmStmp")

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = None

	@property
	def DvcRspn(self):
		return self._DvcRspn

	@DvcRspn.setter
	def DvcRspn(self, value):
		self._DvcRspn = value if type(value) != base_types.auto else self.make_default("DvcRspn")

	@DvcRspn.deleter
	def DvcRspn(self):
		del self._DvcRspn
		self._DvcRspn = None

	@property
	def AddtlErrInf(self):
		return self._AddtlErrInf

	@AddtlErrInf.setter
	def AddtlErrInf(self, value):
		self._AddtlErrInf = value if type(value) != base_types.auto else self.make_default("AddtlErrInf")

	@AddtlErrInf.deleter
	def AddtlErrInf(self):
		del self._AddtlErrInf
		self._AddtlErrInf = None

	@property
	def TermnlMgrId(self):
		return self._TermnlMgrId

	@TermnlMgrId.setter
	def TermnlMgrId(self, value):
		self._TermnlMgrId = value if type(value) != base_types.auto else self.make_default("TermnlMgrId")

	@TermnlMgrId.deleter
	def TermnlMgrId(self):
		del self._TermnlMgrId
		self._TermnlMgrId = None

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != base_types.auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	@property
	def ActnId(self):
		return self._ActnId

	@ActnId.setter
	def ActnId(self, value):
		self._ActnId = value if type(value) != base_types.auto else self.make_default("ActnId")

	@ActnId.deleter
	def ActnId(self):
		del self._ActnId
		self._ActnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcRspn', type=DeviceResponse8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlErrInf', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermnlMgrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=TerminalManagementActionResult5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnId', type=TMSActionIdentification10, min=1, max=1, mutex_group=None, array=False),
	))

