# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType39
from . import CryptographicKey19
from . import DataSetCategory20Code
from . import DataSetIdentification11
from . import DeviceRequest9
from . import ErrorAction5
from . import GenericIdentification176
from . import Max10KBinary
from . import Max140Binary
from . import Max3000Binary
from . import Max35Text
from . import Max5000Binary
from . import MessageItemCondition2
from . import NetworkParameters7
from . import ProcessRetry3
from . import ProcessTiming5
from . import TerminalManagementAction5Code
from . import TerminalManagementActionTrigger1Code
from . import TerminalManagementAdditionalProcess1Code

class TMSAction14(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AddtlPrc", "_CmpntTp", "_DataSetId", "_DlgtnProof", "_DlgtnScpDef", "_DlgtnScpId", "_DvcReq", "_ErrActn", "_Key", "_KeyNcphrmntCert", "_MsgItm", "_PrtctdDlgtnProof", "_ReTry", "_RmotAccs", "_TMChllng", "_TMSPrtcol", "_TMSPrtcolVrsn", "_TermnlMgrId", "_TmCond", "_Tp", "_Trggr"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max3000Binary, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max3000Binary, True)

	@property
	def AddtlPrc(self):
		return self._AddtlPrc

	@AddtlPrc.setter
	def AddtlPrc(self, value):
		self._AddtlPrc = value if value is not None else base_types.UninitialisedField(self, 'AddtlPrc', TerminalManagementAdditionalProcess1Code, True)

	@AddtlPrc.deleter
	def AddtlPrc(self):
		del self._AddtlPrc
		self._AddtlPrc = base_types.UninitialisedField(self, 'AddtlPrc', TerminalManagementAdditionalProcess1Code, True)

	@property
	def CmpntTp(self):
		return self._CmpntTp

	@CmpntTp.setter
	def CmpntTp(self, value):
		self._CmpntTp = value if value is not None else base_types.UninitialisedField(self, 'CmpntTp', DataSetCategory20Code, True)

	@CmpntTp.deleter
	def CmpntTp(self):
		del self._CmpntTp
		self._CmpntTp = base_types.UninitialisedField(self, 'CmpntTp', DataSetCategory20Code, True)

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if value is not None else base_types.UninitialisedField(self, 'DataSetId', DataSetIdentification11, False)

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = base_types.UninitialisedField(self, 'DataSetId', DataSetIdentification11, False)

	@property
	def DlgtnProof(self):
		return self._DlgtnProof

	@DlgtnProof.setter
	def DlgtnProof(self, value):
		self._DlgtnProof = value if value is not None else base_types.UninitialisedField(self, 'DlgtnProof', Max5000Binary, False)

	@DlgtnProof.deleter
	def DlgtnProof(self):
		del self._DlgtnProof
		self._DlgtnProof = base_types.UninitialisedField(self, 'DlgtnProof', Max5000Binary, False)

	@property
	def DlgtnScpDef(self):
		return self._DlgtnScpDef

	@DlgtnScpDef.setter
	def DlgtnScpDef(self, value):
		self._DlgtnScpDef = value if value is not None else base_types.UninitialisedField(self, 'DlgtnScpDef', Max3000Binary, False)

	@DlgtnScpDef.deleter
	def DlgtnScpDef(self):
		del self._DlgtnScpDef
		self._DlgtnScpDef = base_types.UninitialisedField(self, 'DlgtnScpDef', Max3000Binary, False)

	@property
	def DlgtnScpId(self):
		return self._DlgtnScpId

	@DlgtnScpId.setter
	def DlgtnScpId(self, value):
		self._DlgtnScpId = value if value is not None else base_types.UninitialisedField(self, 'DlgtnScpId', Max35Text, False)

	@DlgtnScpId.deleter
	def DlgtnScpId(self):
		del self._DlgtnScpId
		self._DlgtnScpId = base_types.UninitialisedField(self, 'DlgtnScpId', Max35Text, False)

	@property
	def DvcReq(self):
		return self._DvcReq

	@DvcReq.setter
	def DvcReq(self, value):
		self._DvcReq = value if value is not None else base_types.UninitialisedField(self, 'DvcReq', DeviceRequest9, False)

	@DvcReq.deleter
	def DvcReq(self):
		del self._DvcReq
		self._DvcReq = base_types.UninitialisedField(self, 'DvcReq', DeviceRequest9, False)

	@property
	def ErrActn(self):
		return self._ErrActn

	@ErrActn.setter
	def ErrActn(self, value):
		self._ErrActn = value if value is not None else base_types.UninitialisedField(self, 'ErrActn', ErrorAction5, True)

	@ErrActn.deleter
	def ErrActn(self):
		del self._ErrActn
		self._ErrActn = base_types.UninitialisedField(self, 'ErrActn', ErrorAction5, True)

	@property
	def Key(self):
		return self._Key

	@Key.setter
	def Key(self, value):
		self._Key = value if value is not None else base_types.UninitialisedField(self, 'Key', CryptographicKey19, True)

	@Key.deleter
	def Key(self):
		del self._Key
		self._Key = base_types.UninitialisedField(self, 'Key', CryptographicKey19, True)

	@property
	def KeyNcphrmntCert(self):
		return self._KeyNcphrmntCert

	@KeyNcphrmntCert.setter
	def KeyNcphrmntCert(self, value):
		self._KeyNcphrmntCert = value if value is not None else base_types.UninitialisedField(self, 'KeyNcphrmntCert', Max10KBinary, True)

	@KeyNcphrmntCert.deleter
	def KeyNcphrmntCert(self):
		del self._KeyNcphrmntCert
		self._KeyNcphrmntCert = base_types.UninitialisedField(self, 'KeyNcphrmntCert', Max10KBinary, True)

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
	def PrtctdDlgtnProof(self):
		return self._PrtctdDlgtnProof

	@PrtctdDlgtnProof.setter
	def PrtctdDlgtnProof(self, value):
		self._PrtctdDlgtnProof = value if value is not None else base_types.UninitialisedField(self, 'PrtctdDlgtnProof', ContentInformationType39, False)

	@PrtctdDlgtnProof.deleter
	def PrtctdDlgtnProof(self):
		del self._PrtctdDlgtnProof
		self._PrtctdDlgtnProof = base_types.UninitialisedField(self, 'PrtctdDlgtnProof', ContentInformationType39, False)

	@property
	def ReTry(self):
		return self._ReTry

	@ReTry.setter
	def ReTry(self, value):
		self._ReTry = value if value is not None else base_types.UninitialisedField(self, 'ReTry', ProcessRetry3, False)

	@ReTry.deleter
	def ReTry(self):
		del self._ReTry
		self._ReTry = base_types.UninitialisedField(self, 'ReTry', ProcessRetry3, False)

	@property
	def RmotAccs(self):
		return self._RmotAccs

	@RmotAccs.setter
	def RmotAccs(self, value):
		self._RmotAccs = value if value is not None else base_types.UninitialisedField(self, 'RmotAccs', NetworkParameters7, False)

	@RmotAccs.deleter
	def RmotAccs(self):
		del self._RmotAccs
		self._RmotAccs = base_types.UninitialisedField(self, 'RmotAccs', NetworkParameters7, False)

	@property
	def TMChllng(self):
		return self._TMChllng

	@TMChllng.setter
	def TMChllng(self, value):
		self._TMChllng = value if value is not None else base_types.UninitialisedField(self, 'TMChllng', Max140Binary, False)

	@TMChllng.deleter
	def TMChllng(self):
		del self._TMChllng
		self._TMChllng = base_types.UninitialisedField(self, 'TMChllng', Max140Binary, False)

	@property
	def TMSPrtcol(self):
		return self._TMSPrtcol

	@TMSPrtcol.setter
	def TMSPrtcol(self, value):
		self._TMSPrtcol = value if value is not None else base_types.UninitialisedField(self, 'TMSPrtcol', Max35Text, False)

	@TMSPrtcol.deleter
	def TMSPrtcol(self):
		del self._TMSPrtcol
		self._TMSPrtcol = base_types.UninitialisedField(self, 'TMSPrtcol', Max35Text, False)

	@property
	def TMSPrtcolVrsn(self):
		return self._TMSPrtcolVrsn

	@TMSPrtcolVrsn.setter
	def TMSPrtcolVrsn(self, value):
		self._TMSPrtcolVrsn = value if value is not None else base_types.UninitialisedField(self, 'TMSPrtcolVrsn', Max35Text, False)

	@TMSPrtcolVrsn.deleter
	def TMSPrtcolVrsn(self):
		del self._TMSPrtcolVrsn
		self._TMSPrtcolVrsn = base_types.UninitialisedField(self, 'TMSPrtcolVrsn', Max35Text, False)

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
	def TmCond(self):
		return self._TmCond

	@TmCond.setter
	def TmCond(self, value):
		self._TmCond = value if value is not None else base_types.UninitialisedField(self, 'TmCond', ProcessTiming5, False)

	@TmCond.deleter
	def TmCond(self):
		del self._TmCond
		self._TmCond = base_types.UninitialisedField(self, 'TmCond', ProcessTiming5, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TerminalManagementAction5Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TerminalManagementAction5Code, False)

	@property
	def Trggr(self):
		return self._Trggr

	@Trggr.setter
	def Trggr(self, value):
		self._Trggr = value if value is not None else base_types.UninitialisedField(self, 'Trggr', TerminalManagementActionTrigger1Code, False)

	@Trggr.deleter
	def Trggr(self):
		del self._Trggr
		self._Trggr = base_types.UninitialisedField(self, 'Trggr', TerminalManagementActionTrigger1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max3000Binary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlPrc', type=TerminalManagementAdditionalProcess1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CmpntTp', type=DataSetCategory20Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DataSetId', type=DataSetIdentification11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnProof', type=Max5000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnScpDef', type=Max3000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlgtnScpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcReq', type=DeviceRequest9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ErrActn', type=ErrorAction5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Key', type=CryptographicKey19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='KeyNcphrmntCert', type=Max10KBinary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgItm', type=MessageItemCondition2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdDlgtnProof', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReTry', type=ProcessRetry3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmotAccs', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSPrtcol', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSPrtcolVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermnlMgrId', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmCond', type=ProcessTiming5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TerminalManagementAction5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trggr', type=TerminalManagementActionTrigger1Code, min=1, max=1, mutex_group=None, array=False),
	))