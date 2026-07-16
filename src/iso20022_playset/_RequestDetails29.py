# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AutomaticBorrowing11Choice
from . import GenericIdentification47
from . import HoldIndicator7
from . import LinkageType4Choice
from . import Linkages66
from . import MatchingDenied4Choice
from . import PriorityNumeric5Choice
from . import References28
from . import RestrictionIdentification2
from . import SecuritiesRTGS5Choice
from . import SettlementTransactionCondition5Code
from . import UnilateralSplit4Choice
from . import YesNoIndicator

class RequestDetails29(base_types._BaseFieldType):

	__slots__ = ["_AutomtcBrrwg", "_HldInd", "_Lkg", "_Lnkgs", "_MtchgDnl", "_OthrPrcg", "_PrtlSttlmInd", "_Prty", "_Ref", "_RstrctnRef", "_RtnInd", "_SctiesRTGS", "_UnltrlSplt"]
	@property
	def AutomtcBrrwg(self):
		return self._AutomtcBrrwg

	@AutomtcBrrwg.setter
	def AutomtcBrrwg(self, value):
		self._AutomtcBrrwg = value if value is not None else base_types.UninitialisedField(self, 'AutomtcBrrwg', AutomaticBorrowing11Choice, False)

	@AutomtcBrrwg.deleter
	def AutomtcBrrwg(self):
		del self._AutomtcBrrwg
		self._AutomtcBrrwg = base_types.UninitialisedField(self, 'AutomtcBrrwg', AutomaticBorrowing11Choice, False)

	@property
	def HldInd(self):
		return self._HldInd

	@HldInd.setter
	def HldInd(self, value):
		self._HldInd = value if value is not None else base_types.UninitialisedField(self, 'HldInd', HoldIndicator7, False)

	@HldInd.deleter
	def HldInd(self):
		del self._HldInd
		self._HldInd = base_types.UninitialisedField(self, 'HldInd', HoldIndicator7, False)

	@property
	def Lkg(self):
		return self._Lkg

	@Lkg.setter
	def Lkg(self, value):
		self._Lkg = value if value is not None else base_types.UninitialisedField(self, 'Lkg', LinkageType4Choice, False)

	@Lkg.deleter
	def Lkg(self):
		del self._Lkg
		self._Lkg = base_types.UninitialisedField(self, 'Lkg', LinkageType4Choice, False)

	@property
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if value is not None else base_types.UninitialisedField(self, 'Lnkgs', Linkages66, True)

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = base_types.UninitialisedField(self, 'Lnkgs', Linkages66, True)

	@property
	def MtchgDnl(self):
		return self._MtchgDnl

	@MtchgDnl.setter
	def MtchgDnl(self, value):
		self._MtchgDnl = value if value is not None else base_types.UninitialisedField(self, 'MtchgDnl', MatchingDenied4Choice, False)

	@MtchgDnl.deleter
	def MtchgDnl(self):
		del self._MtchgDnl
		self._MtchgDnl = base_types.UninitialisedField(self, 'MtchgDnl', MatchingDenied4Choice, False)

	@property
	def OthrPrcg(self):
		return self._OthrPrcg

	@OthrPrcg.setter
	def OthrPrcg(self, value):
		self._OthrPrcg = value if value is not None else base_types.UninitialisedField(self, 'OthrPrcg', GenericIdentification47, True)

	@OthrPrcg.deleter
	def OthrPrcg(self):
		del self._OthrPrcg
		self._OthrPrcg = base_types.UninitialisedField(self, 'OthrPrcg', GenericIdentification47, True)

	@property
	def PrtlSttlmInd(self):
		return self._PrtlSttlmInd

	@PrtlSttlmInd.setter
	def PrtlSttlmInd(self, value):
		self._PrtlSttlmInd = value if value is not None else base_types.UninitialisedField(self, 'PrtlSttlmInd', SettlementTransactionCondition5Code, False)

	@PrtlSttlmInd.deleter
	def PrtlSttlmInd(self):
		del self._PrtlSttlmInd
		self._PrtlSttlmInd = base_types.UninitialisedField(self, 'PrtlSttlmInd', SettlementTransactionCondition5Code, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', PriorityNumeric5Choice, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', PriorityNumeric5Choice, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', References28, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', References28, False)

	@property
	def RstrctnRef(self):
		return self._RstrctnRef

	@RstrctnRef.setter
	def RstrctnRef(self, value):
		self._RstrctnRef = value if value is not None else base_types.UninitialisedField(self, 'RstrctnRef', RestrictionIdentification2, True)

	@RstrctnRef.deleter
	def RstrctnRef(self):
		del self._RstrctnRef
		self._RstrctnRef = base_types.UninitialisedField(self, 'RstrctnRef', RestrictionIdentification2, True)

	@property
	def RtnInd(self):
		return self._RtnInd

	@RtnInd.setter
	def RtnInd(self, value):
		self._RtnInd = value if value is not None else base_types.UninitialisedField(self, 'RtnInd', YesNoIndicator, False)

	@RtnInd.deleter
	def RtnInd(self):
		del self._RtnInd
		self._RtnInd = base_types.UninitialisedField(self, 'RtnInd', YesNoIndicator, False)

	@property
	def SctiesRTGS(self):
		return self._SctiesRTGS

	@SctiesRTGS.setter
	def SctiesRTGS(self, value):
		self._SctiesRTGS = value if value is not None else base_types.UninitialisedField(self, 'SctiesRTGS', SecuritiesRTGS5Choice, False)

	@SctiesRTGS.deleter
	def SctiesRTGS(self):
		del self._SctiesRTGS
		self._SctiesRTGS = base_types.UninitialisedField(self, 'SctiesRTGS', SecuritiesRTGS5Choice, False)

	@property
	def UnltrlSplt(self):
		return self._UnltrlSplt

	@UnltrlSplt.setter
	def UnltrlSplt(self, value):
		self._UnltrlSplt = value if value is not None else base_types.UninitialisedField(self, 'UnltrlSplt', UnilateralSplit4Choice, False)

	@UnltrlSplt.deleter
	def UnltrlSplt(self):
		del self._UnltrlSplt
		self._UnltrlSplt = base_types.UninitialisedField(self, 'UnltrlSplt', UnilateralSplit4Choice, False)

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