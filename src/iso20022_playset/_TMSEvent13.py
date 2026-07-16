# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DeviceResponse9
from . import ISODateTime
from . import Max35Text
from . import Max70Text
from . import TMSActionIdentification10
from . import TerminalManagementActionResult5Code

class TMSEvent13(base_types._BaseFieldType):

	__slots__ = ["_ActnId", "_AddtlErrInf", "_DvcRspn", "_Rslt", "_TermnlMgrId", "_TmStmp"]
	@property
	def ActnId(self):
		return self._ActnId

	@ActnId.setter
	def ActnId(self, value):
		self._ActnId = value if value is not None else base_types.UninitialisedField(self, 'ActnId', TMSActionIdentification10, False)

	@ActnId.deleter
	def ActnId(self):
		del self._ActnId
		self._ActnId = base_types.UninitialisedField(self, 'ActnId', TMSActionIdentification10, False)

	@property
	def AddtlErrInf(self):
		return self._AddtlErrInf

	@AddtlErrInf.setter
	def AddtlErrInf(self, value):
		self._AddtlErrInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlErrInf', Max70Text, False)

	@AddtlErrInf.deleter
	def AddtlErrInf(self):
		del self._AddtlErrInf
		self._AddtlErrInf = base_types.UninitialisedField(self, 'AddtlErrInf', Max70Text, False)

	@property
	def DvcRspn(self):
		return self._DvcRspn

	@DvcRspn.setter
	def DvcRspn(self, value):
		self._DvcRspn = value if value is not None else base_types.UninitialisedField(self, 'DvcRspn', DeviceResponse9, False)

	@DvcRspn.deleter
	def DvcRspn(self):
		del self._DvcRspn
		self._DvcRspn = base_types.UninitialisedField(self, 'DvcRspn', DeviceResponse9, False)

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', TerminalManagementActionResult5Code, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', TerminalManagementActionResult5Code, False)

	@property
	def TermnlMgrId(self):
		return self._TermnlMgrId

	@TermnlMgrId.setter
	def TermnlMgrId(self, value):
		self._TermnlMgrId = value if value is not None else base_types.UninitialisedField(self, 'TermnlMgrId', Max35Text, False)

	@TermnlMgrId.deleter
	def TermnlMgrId(self):
		del self._TermnlMgrId
		self._TermnlMgrId = base_types.UninitialisedField(self, 'TermnlMgrId', Max35Text, False)

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if value is not None else base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = base_types.UninitialisedField(self, 'TmStmp', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnId', type=TMSActionIdentification10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlErrInf', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcRspn', type=DeviceResponse9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=TerminalManagementActionResult5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermnlMgrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))