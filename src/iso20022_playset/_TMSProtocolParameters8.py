# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataSetCategory10Code
from . import GenericIdentification176
from . import Max1025Text
from . import Max256Text
from . import Max35Text
from . import Max8Text
from . import MessageItemCondition2
from . import TerminalManagementAction3Code
from . import TrueFalseIndicator

class TMSProtocolParameters8(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_ApplId", "_FileTrf", "_HstId", "_InitgPtyId", "_MntncSvc", "_MsgItm", "_POIId", "_PrtcolVrsn", "_RcptPtyId", "_TermnlMgrId", "_Vrsn", "_XtrnlyTpSpprtd"]
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
		self._ApplId = value if value is not None else base_types.UninitialisedField(self, 'ApplId', Max35Text, True)

	@ApplId.deleter
	def ApplId(self):
		del self._ApplId
		self._ApplId = base_types.UninitialisedField(self, 'ApplId', Max35Text, True)

	@property
	def FileTrf(self):
		return self._FileTrf

	@FileTrf.setter
	def FileTrf(self, value):
		self._FileTrf = value if value is not None else base_types.UninitialisedField(self, 'FileTrf', TrueFalseIndicator, False)

	@FileTrf.deleter
	def FileTrf(self):
		del self._FileTrf
		self._FileTrf = base_types.UninitialisedField(self, 'FileTrf', TrueFalseIndicator, False)

	@property
	def HstId(self):
		return self._HstId

	@HstId.setter
	def HstId(self, value):
		self._HstId = value if value is not None else base_types.UninitialisedField(self, 'HstId', Max35Text, False)

	@HstId.deleter
	def HstId(self):
		del self._HstId
		self._HstId = base_types.UninitialisedField(self, 'HstId', Max35Text, False)

	@property
	def InitgPtyId(self):
		return self._InitgPtyId

	@InitgPtyId.setter
	def InitgPtyId(self, value):
		self._InitgPtyId = value if value is not None else base_types.UninitialisedField(self, 'InitgPtyId', Max35Text, False)

	@InitgPtyId.deleter
	def InitgPtyId(self):
		del self._InitgPtyId
		self._InitgPtyId = base_types.UninitialisedField(self, 'InitgPtyId', Max35Text, False)

	@property
	def MntncSvc(self):
		return self._MntncSvc

	@MntncSvc.setter
	def MntncSvc(self, value):
		self._MntncSvc = value if value is not None else base_types.UninitialisedField(self, 'MntncSvc', DataSetCategory10Code, True)

	@MntncSvc.deleter
	def MntncSvc(self):
		del self._MntncSvc
		self._MntncSvc = base_types.UninitialisedField(self, 'MntncSvc', DataSetCategory10Code, True)

	@property
	def MsgItm(self):
		return self._MsgItm

	@MsgItm.setter
	def MsgItm(self, value):
		self._MsgItm = value if value is not None else base_types.UninitialisedField(self, 'MsgItm', MessageItemCondition2, True)

	@MsgItm.deleter
	def MsgItm(self):
		del self._MsgItm
		self._MsgItm = base_types.UninitialisedField(self, 'MsgItm', MessageItemCondition2, True)

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if value is not None else base_types.UninitialisedField(self, 'POIId', Max35Text, False)

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = base_types.UninitialisedField(self, 'POIId', Max35Text, False)

	@property
	def PrtcolVrsn(self):
		return self._PrtcolVrsn

	@PrtcolVrsn.setter
	def PrtcolVrsn(self, value):
		self._PrtcolVrsn = value if value is not None else base_types.UninitialisedField(self, 'PrtcolVrsn', Max8Text, False)

	@PrtcolVrsn.deleter
	def PrtcolVrsn(self):
		del self._PrtcolVrsn
		self._PrtcolVrsn = base_types.UninitialisedField(self, 'PrtcolVrsn', Max8Text, False)

	@property
	def RcptPtyId(self):
		return self._RcptPtyId

	@RcptPtyId.setter
	def RcptPtyId(self, value):
		self._RcptPtyId = value if value is not None else base_types.UninitialisedField(self, 'RcptPtyId', Max35Text, False)

	@RcptPtyId.deleter
	def RcptPtyId(self):
		del self._RcptPtyId
		self._RcptPtyId = base_types.UninitialisedField(self, 'RcptPtyId', Max35Text, False)

	@property
	def TermnlMgrId(self):
		return self._TermnlMgrId

	@TermnlMgrId.setter
	def TermnlMgrId(self, value):
		self._TermnlMgrId = value if value is not None else base_types.UninitialisedField(self, 'TermnlMgrId', GenericIdentification176, False)

	@TermnlMgrId.deleter
	def TermnlMgrId(self):
		del self._TermnlMgrId
		self._TermnlMgrId = base_types.UninitialisedField(self, 'TermnlMgrId', GenericIdentification176, False)

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

	@property
	def XtrnlyTpSpprtd(self):
		return self._XtrnlyTpSpprtd

	@XtrnlyTpSpprtd.setter
	def XtrnlyTpSpprtd(self, value):
		self._XtrnlyTpSpprtd = value if value is not None else base_types.UninitialisedField(self, 'XtrnlyTpSpprtd', Max1025Text, True)

	@XtrnlyTpSpprtd.deleter
	def XtrnlyTpSpprtd(self):
		del self._XtrnlyTpSpprtd
		self._XtrnlyTpSpprtd = base_types.UninitialisedField(self, 'XtrnlyTpSpprtd', Max1025Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FileTrf', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncSvc', type=DataSetCategory10Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgItm', type=MessageItemCondition2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcolVrsn', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptPtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermnlMgrId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtrnlyTpSpprtd', type=Max1025Text, min=0, max=None, mutex_group=None, array=True),
	))