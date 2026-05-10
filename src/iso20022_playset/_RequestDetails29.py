from . import base_types
from ._Linkages66 import Linkages66
from ._GenericIdentification47 import GenericIdentification47
from ._YesNoIndicator import YesNoIndicator
from ._LinkageType4Choice import LinkageType4Choice
from ._UnilateralSplit4Choice import UnilateralSplit4Choice
from ._AutomaticBorrowing11Choice import AutomaticBorrowing11Choice
from ._RestrictionIdentification2 import RestrictionIdentification2
from ._SettlementTransactionCondition5Code import SettlementTransactionCondition5Code
from ._MatchingDenied4Choice import MatchingDenied4Choice
from ._HoldIndicator7 import HoldIndicator7
from ._SecuritiesRTGS5Choice import SecuritiesRTGS5Choice
from ._PriorityNumeric5Choice import PriorityNumeric5Choice
from ._References28 import References28

class RequestDetails29(base_types._BaseFieldType):

	__slots__ = ["_HldInd", "_Ref", "_RstrctnRef", "_SctiesRTGS", "_MtchgDnl", "_OthrPrcg", "_Lkg", "_Lnkgs", "_Prty", "_UnltrlSplt", "_PrtlSttlmInd", "_RtnInd", "_AutomtcBrrwg"]
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
		base_types.FieldEntry(name='AutomtcBrrwg', type=AutomaticBorrowing11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldInd', type=HoldIndicator7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lkg', type=LinkageType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages66, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtchgDnl', type=MatchingDenied4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPrcg', type=GenericIdentification47, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtlSttlmInd', type=SettlementTransactionCondition5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnRef', type=RestrictionIdentification2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RtnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesRTGS', type=SecuritiesRTGS5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnltrlSplt', type=UnilateralSplit4Choice, min=0, max=1, mutex_group=None, array=False),
	))

