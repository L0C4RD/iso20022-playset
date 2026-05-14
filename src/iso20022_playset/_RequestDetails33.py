from . import base_types
from ._AutomaticBorrowing7Choice import AutomaticBorrowing7Choice
from ._GenericIdentification30 import GenericIdentification30
from ._HoldIndicator6 import HoldIndicator6
from ._LinkageType3Choice import LinkageType3Choice
from ._Linkages57 import Linkages57
from ._MatchingDenied3Choice import MatchingDenied3Choice
from ._PriorityNumeric4Choice import PriorityNumeric4Choice
from ._References32 import References32
from ._RestrictionIdentification1 import RestrictionIdentification1
from ._SecuritiesRTGS4Choice import SecuritiesRTGS4Choice
from ._SettlementTransactionCondition5Code import SettlementTransactionCondition5Code
from ._UnilateralSplit3Choice import UnilateralSplit3Choice
from ._YesNoIndicator import YesNoIndicator

class RequestDetails33(base_types._BaseFieldType):

	__slots__ = ["_AutomtcBrrwg", "_HldInd", "_Lkg", "_Lnkgs", "_MtchgDnl", "_OthrPrcg", "_PrtlSttlmInd", "_Prty", "_Ref", "_RstrctnRef", "_RtnInd", "_SctiesRTGS", "_UnltrlSplt"]
	@property
	def AutomtcBrrwg(self):
		return self._AutomtcBrrwg

	@AutomtcBrrwg.setter
	def AutomtcBrrwg(self, value):
		self._AutomtcBrrwg = value if type(value) != base_types.auto else self.make_default("AutomtcBrrwg")

	@AutomtcBrrwg.deleter
	def AutomtcBrrwg(self):
		del self._AutomtcBrrwg
		self._AutomtcBrrwg = None

	@property
	def HldInd(self):
		return self._HldInd

	@HldInd.setter
	def HldInd(self, value):
		self._HldInd = value if type(value) != base_types.auto else self.make_default("HldInd")

	@HldInd.deleter
	def HldInd(self):
		del self._HldInd
		self._HldInd = None

	@property
	def Lkg(self):
		return self._Lkg

	@Lkg.setter
	def Lkg(self, value):
		self._Lkg = value if type(value) != base_types.auto else self.make_default("Lkg")

	@Lkg.deleter
	def Lkg(self):
		del self._Lkg
		self._Lkg = None

	@property
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if type(value) != base_types.auto else self.make_default("Lnkgs")

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = None

	@property
	def MtchgDnl(self):
		return self._MtchgDnl

	@MtchgDnl.setter
	def MtchgDnl(self, value):
		self._MtchgDnl = value if type(value) != base_types.auto else self.make_default("MtchgDnl")

	@MtchgDnl.deleter
	def MtchgDnl(self):
		del self._MtchgDnl
		self._MtchgDnl = None

	@property
	def OthrPrcg(self):
		return self._OthrPrcg

	@OthrPrcg.setter
	def OthrPrcg(self, value):
		self._OthrPrcg = value if type(value) != base_types.auto else self.make_default("OthrPrcg")

	@OthrPrcg.deleter
	def OthrPrcg(self):
		del self._OthrPrcg
		self._OthrPrcg = None

	@property
	def PrtlSttlmInd(self):
		return self._PrtlSttlmInd

	@PrtlSttlmInd.setter
	def PrtlSttlmInd(self, value):
		self._PrtlSttlmInd = value if type(value) != base_types.auto else self.make_default("PrtlSttlmInd")

	@PrtlSttlmInd.deleter
	def PrtlSttlmInd(self):
		del self._PrtlSttlmInd
		self._PrtlSttlmInd = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != base_types.auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def RstrctnRef(self):
		return self._RstrctnRef

	@RstrctnRef.setter
	def RstrctnRef(self, value):
		self._RstrctnRef = value if type(value) != base_types.auto else self.make_default("RstrctnRef")

	@RstrctnRef.deleter
	def RstrctnRef(self):
		del self._RstrctnRef
		self._RstrctnRef = None

	@property
	def RtnInd(self):
		return self._RtnInd

	@RtnInd.setter
	def RtnInd(self, value):
		self._RtnInd = value if type(value) != base_types.auto else self.make_default("RtnInd")

	@RtnInd.deleter
	def RtnInd(self):
		del self._RtnInd
		self._RtnInd = None

	@property
	def SctiesRTGS(self):
		return self._SctiesRTGS

	@SctiesRTGS.setter
	def SctiesRTGS(self, value):
		self._SctiesRTGS = value if type(value) != base_types.auto else self.make_default("SctiesRTGS")

	@SctiesRTGS.deleter
	def SctiesRTGS(self):
		del self._SctiesRTGS
		self._SctiesRTGS = None

	@property
	def UnltrlSplt(self):
		return self._UnltrlSplt

	@UnltrlSplt.setter
	def UnltrlSplt(self, value):
		self._UnltrlSplt = value if type(value) != base_types.auto else self.make_default("UnltrlSplt")

	@UnltrlSplt.deleter
	def UnltrlSplt(self):
		del self._UnltrlSplt
		self._UnltrlSplt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AutomtcBrrwg', type=AutomaticBorrowing7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldInd', type=HoldIndicator6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lkg', type=LinkageType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages57, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtchgDnl', type=MatchingDenied3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPrcg', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtlSttlmInd', type=SettlementTransactionCondition5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References32, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnRef', type=RestrictionIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RtnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesRTGS', type=SecuritiesRTGS4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnltrlSplt', type=UnilateralSplit3Choice, min=0, max=1, mutex_group=None, array=False),
	))

