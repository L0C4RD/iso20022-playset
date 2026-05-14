# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContentInformationType39 import ContentInformationType39
from ._CryptographicKey19 import CryptographicKey19
from ._DataSetCategory20Code import DataSetCategory20Code
from ._DataSetIdentification11 import DataSetIdentification11
from ._DeviceRequest9 import DeviceRequest9
from ._ErrorAction5 import ErrorAction5
from ._GenericIdentification176 import GenericIdentification176
from ._Max10KBinary import Max10KBinary
from ._Max140Binary import Max140Binary
from ._Max3000Binary import Max3000Binary
from ._Max35Text import Max35Text
from ._Max5000Binary import Max5000Binary
from ._MessageItemCondition2 import MessageItemCondition2
from ._NetworkParameters7 import NetworkParameters7
from ._ProcessRetry3 import ProcessRetry3
from ._ProcessTiming5 import ProcessTiming5
from ._TerminalManagementAction5Code import TerminalManagementAction5Code
from ._TerminalManagementActionTrigger1Code import TerminalManagementActionTrigger1Code
from ._TerminalManagementAdditionalProcess1Code import TerminalManagementAdditionalProcess1Code

class TMSAction14(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AddtlPrc", "_CmpntTp", "_DataSetId", "_DlgtnProof", "_DlgtnScpDef", "_DlgtnScpId", "_DvcReq", "_ErrActn", "_Key", "_KeyNcphrmntCert", "_MsgItm", "_PrtctdDlgtnProof", "_ReTry", "_RmotAccs", "_TMChllng", "_TMSPrtcol", "_TMSPrtcolVrsn", "_TermnlMgrId", "_TmCond", "_Tp", "_Trggr"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def AddtlPrc(self):
		return self._AddtlPrc

	@AddtlPrc.setter
	def AddtlPrc(self, value):
		self._AddtlPrc = value if type(value) != base_types.auto else self.make_default("AddtlPrc")

	@AddtlPrc.deleter
	def AddtlPrc(self):
		del self._AddtlPrc
		self._AddtlPrc = None

	@property
	def CmpntTp(self):
		return self._CmpntTp

	@CmpntTp.setter
	def CmpntTp(self, value):
		self._CmpntTp = value if type(value) != base_types.auto else self.make_default("CmpntTp")

	@CmpntTp.deleter
	def CmpntTp(self):
		del self._CmpntTp
		self._CmpntTp = None

	@property
	def DataSetId(self):
		return self._DataSetId

	@DataSetId.setter
	def DataSetId(self, value):
		self._DataSetId = value if type(value) != base_types.auto else self.make_default("DataSetId")

	@DataSetId.deleter
	def DataSetId(self):
		del self._DataSetId
		self._DataSetId = None

	@property
	def DlgtnProof(self):
		return self._DlgtnProof

	@DlgtnProof.setter
	def DlgtnProof(self, value):
		self._DlgtnProof = value if type(value) != base_types.auto else self.make_default("DlgtnProof")

	@DlgtnProof.deleter
	def DlgtnProof(self):
		del self._DlgtnProof
		self._DlgtnProof = None

	@property
	def DlgtnScpDef(self):
		return self._DlgtnScpDef

	@DlgtnScpDef.setter
	def DlgtnScpDef(self, value):
		self._DlgtnScpDef = value if type(value) != base_types.auto else self.make_default("DlgtnScpDef")

	@DlgtnScpDef.deleter
	def DlgtnScpDef(self):
		del self._DlgtnScpDef
		self._DlgtnScpDef = None

	@property
	def DlgtnScpId(self):
		return self._DlgtnScpId

	@DlgtnScpId.setter
	def DlgtnScpId(self, value):
		self._DlgtnScpId = value if type(value) != base_types.auto else self.make_default("DlgtnScpId")

	@DlgtnScpId.deleter
	def DlgtnScpId(self):
		del self._DlgtnScpId
		self._DlgtnScpId = None

	@property
	def DvcReq(self):
		return self._DvcReq

	@DvcReq.setter
	def DvcReq(self, value):
		self._DvcReq = value if type(value) != base_types.auto else self.make_default("DvcReq")

	@DvcReq.deleter
	def DvcReq(self):
		del self._DvcReq
		self._DvcReq = None

	@property
	def ErrActn(self):
		return self._ErrActn

	@ErrActn.setter
	def ErrActn(self, value):
		self._ErrActn = value if type(value) != base_types.auto else self.make_default("ErrActn")

	@ErrActn.deleter
	def ErrActn(self):
		del self._ErrActn
		self._ErrActn = None

	@property
	def Key(self):
		return self._Key

	@Key.setter
	def Key(self, value):
		self._Key = value if type(value) != base_types.auto else self.make_default("Key")

	@Key.deleter
	def Key(self):
		del self._Key
		self._Key = None

	@property
	def KeyNcphrmntCert(self):
		return self._KeyNcphrmntCert

	@KeyNcphrmntCert.setter
	def KeyNcphrmntCert(self, value):
		self._KeyNcphrmntCert = value if type(value) != base_types.auto else self.make_default("KeyNcphrmntCert")

	@KeyNcphrmntCert.deleter
	def KeyNcphrmntCert(self):
		del self._KeyNcphrmntCert
		self._KeyNcphrmntCert = None

	@property
	def MsgItm(self):
		return self._MsgItm

	@MsgItm.setter
	def MsgItm(self, value):
		self._MsgItm = value if type(value) != base_types.auto else self.make_default("MsgItm")

	@MsgItm.deleter
	def MsgItm(self):
		del self._MsgItm
		self._MsgItm = None

	@property
	def PrtctdDlgtnProof(self):
		return self._PrtctdDlgtnProof

	@PrtctdDlgtnProof.setter
	def PrtctdDlgtnProof(self, value):
		self._PrtctdDlgtnProof = value if type(value) != base_types.auto else self.make_default("PrtctdDlgtnProof")

	@PrtctdDlgtnProof.deleter
	def PrtctdDlgtnProof(self):
		del self._PrtctdDlgtnProof
		self._PrtctdDlgtnProof = None

	@property
	def ReTry(self):
		return self._ReTry

	@ReTry.setter
	def ReTry(self, value):
		self._ReTry = value if type(value) != base_types.auto else self.make_default("ReTry")

	@ReTry.deleter
	def ReTry(self):
		del self._ReTry
		self._ReTry = None

	@property
	def RmotAccs(self):
		return self._RmotAccs

	@RmotAccs.setter
	def RmotAccs(self, value):
		self._RmotAccs = value if type(value) != base_types.auto else self.make_default("RmotAccs")

	@RmotAccs.deleter
	def RmotAccs(self):
		del self._RmotAccs
		self._RmotAccs = None

	@property
	def TMChllng(self):
		return self._TMChllng

	@TMChllng.setter
	def TMChllng(self, value):
		self._TMChllng = value if type(value) != base_types.auto else self.make_default("TMChllng")

	@TMChllng.deleter
	def TMChllng(self):
		del self._TMChllng
		self._TMChllng = None

	@property
	def TMSPrtcol(self):
		return self._TMSPrtcol

	@TMSPrtcol.setter
	def TMSPrtcol(self, value):
		self._TMSPrtcol = value if type(value) != base_types.auto else self.make_default("TMSPrtcol")

	@TMSPrtcol.deleter
	def TMSPrtcol(self):
		del self._TMSPrtcol
		self._TMSPrtcol = None

	@property
	def TMSPrtcolVrsn(self):
		return self._TMSPrtcolVrsn

	@TMSPrtcolVrsn.setter
	def TMSPrtcolVrsn(self, value):
		self._TMSPrtcolVrsn = value if type(value) != base_types.auto else self.make_default("TMSPrtcolVrsn")

	@TMSPrtcolVrsn.deleter
	def TMSPrtcolVrsn(self):
		del self._TMSPrtcolVrsn
		self._TMSPrtcolVrsn = None

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
	def TmCond(self):
		return self._TmCond

	@TmCond.setter
	def TmCond(self, value):
		self._TmCond = value if type(value) != base_types.auto else self.make_default("TmCond")

	@TmCond.deleter
	def TmCond(self):
		del self._TmCond
		self._TmCond = None

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
	def Trggr(self):
		return self._Trggr

	@Trggr.setter
	def Trggr(self, value):
		self._Trggr = value if type(value) != base_types.auto else self.make_default("Trggr")

	@Trggr.deleter
	def Trggr(self):
		del self._Trggr
		self._Trggr = None

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