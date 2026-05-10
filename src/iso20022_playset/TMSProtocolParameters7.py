import base_types
import Max1025Text
import DataSetCategory10Code
import Max35Text
import TrueFalseIndicator
import Max256Text
import GenericIdentification176
import TerminalManagementAction3Code
import MessageItemCondition2
import Max8Text

class TMSProtocolParameters7(base_types._BaseFieldType):

	__slots__ = ["_Vrsn", "_RcptPtyId", "_HstId", "_FileTrf", "_MsgItm", "_PrtcolVrsn", "_InitgPtyId", "_TermnlMgrId", "_ApplId", "_XtrnlyTpSpprtd", "_ActnTp", "_POIId", "_MntncSvc"]
	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def RcptPtyId(self):
		return self._RcptPtyId

	@RcptPtyId.setter
	def RcptPtyId(self, value):
		self._RcptPtyId = value if type(value) != auto else self.make_default("RcptPtyId")

	@RcptPtyId.deleter
	def RcptPtyId(self):
		del self._RcptPtyId
		self._RcptPtyId = None

	@property
	def HstId(self):
		return self._HstId

	@HstId.setter
	def HstId(self, value):
		self._HstId = value if type(value) != auto else self.make_default("HstId")

	@HstId.deleter
	def HstId(self):
		del self._HstId
		self._HstId = None

	@property
	def FileTrf(self):
		return self._FileTrf

	@FileTrf.setter
	def FileTrf(self, value):
		self._FileTrf = value if type(value) != auto else self.make_default("FileTrf")

	@FileTrf.deleter
	def FileTrf(self):
		del self._FileTrf
		self._FileTrf = None

	@property
	def MsgItm(self):
		return self._MsgItm

	@MsgItm.setter
	def MsgItm(self, value):
		self._MsgItm = value if type(value) != auto else self.make_default("MsgItm")

	@MsgItm.deleter
	def MsgItm(self):
		del self._MsgItm
		self._MsgItm = None

	@property
	def PrtcolVrsn(self):
		return self._PrtcolVrsn

	@PrtcolVrsn.setter
	def PrtcolVrsn(self, value):
		self._PrtcolVrsn = value if type(value) != auto else self.make_default("PrtcolVrsn")

	@PrtcolVrsn.deleter
	def PrtcolVrsn(self):
		del self._PrtcolVrsn
		self._PrtcolVrsn = None

	@property
	def InitgPtyId(self):
		return self._InitgPtyId

	@InitgPtyId.setter
	def InitgPtyId(self, value):
		self._InitgPtyId = value if type(value) != auto else self.make_default("InitgPtyId")

	@InitgPtyId.deleter
	def InitgPtyId(self):
		del self._InitgPtyId
		self._InitgPtyId = None

	@property
	def TermnlMgrId(self):
		return self._TermnlMgrId

	@TermnlMgrId.setter
	def TermnlMgrId(self, value):
		self._TermnlMgrId = value if type(value) != auto else self.make_default("TermnlMgrId")

	@TermnlMgrId.deleter
	def TermnlMgrId(self):
		del self._TermnlMgrId
		self._TermnlMgrId = None

	@property
	def ApplId(self):
		return self._ApplId

	@ApplId.setter
	def ApplId(self, value):
		self._ApplId = value if type(value) != auto else self.make_default("ApplId")

	@ApplId.deleter
	def ApplId(self):
		del self._ApplId
		self._ApplId = None

	@property
	def XtrnlyTpSpprtd(self):
		return self._XtrnlyTpSpprtd

	@XtrnlyTpSpprtd.setter
	def XtrnlyTpSpprtd(self, value):
		self._XtrnlyTpSpprtd = value if type(value) != auto else self.make_default("XtrnlyTpSpprtd")

	@XtrnlyTpSpprtd.deleter
	def XtrnlyTpSpprtd(self):
		del self._XtrnlyTpSpprtd
		self._XtrnlyTpSpprtd = None

	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if type(value) != auto else self.make_default("POIId")

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = None

	@property
	def MntncSvc(self):
		return self._MntncSvc

	@MntncSvc.setter
	def MntncSvc(self, value):
		self._MntncSvc = value if type(value) != auto else self.make_default("MntncSvc")

	@MntncSvc.deleter
	def MntncSvc(self):
		del self._MntncSvc
		self._MntncSvc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptPtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileTrf', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgItm', type=MessageItemCondition2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtcolVrsn', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermnlMgrId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XtrnlyTpSpprtd', type=Max1025Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntncSvc', type=DataSetCategory10Code, min=1, max=None, mutex_group=None, array=True),
	))

