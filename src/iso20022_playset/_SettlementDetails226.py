# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AutomaticBorrowing6Choice
from . import BeneficialOwnership4Choice
from . import BlockTrade4Choice
from . import CashSettlementSystem6Choice
from . import CentralCounterPartyEligibility4Choice
from . import FXStandingInstruction4Choice
from . import GenericIdentification30
from . import MarketClientSide6Choice
from . import NettingEligibility4Choice
from . import PriorityNumeric4Choice
from . import Restriction5Choice
from . import SecuritiesRTGS4Choice
from . import SettlementSystemMethod4Choice
from . import SettlementTransactionCondition45Choice
from . import SettlementTransactionCondition5Code
from . import SettlingCapacity7Choice
from . import TaxCapacityParty4Choice
from . import Tracking4Choice
from . import YesNoIndicator

class SettlementDetails226(base_types._BaseFieldType):

	__slots__ = ["_AutomtcBrrwg", "_BlckTrad", "_BnfclOwnrsh", "_CCPElgblty", "_CshClrSys", "_ElgblForColl", "_FxStgInstr", "_HldInd", "_LglRstrctns", "_MktClntSd", "_NetgElgblty", "_PrtlSttlmInd", "_Prty", "_SctiesRTGS", "_StmpDtyTaxBsis", "_SttlgCpcty", "_SttlmSysMtd", "_SttlmTxCond", "_TaxCpcty", "_Trckg"]
	@property
	def AutomtcBrrwg(self):
		return self._AutomtcBrrwg

	@AutomtcBrrwg.setter
	def AutomtcBrrwg(self, value):
		self._AutomtcBrrwg = value if value is not None else base_types.UninitialisedField(self, 'AutomtcBrrwg', AutomaticBorrowing6Choice, False)

	@AutomtcBrrwg.deleter
	def AutomtcBrrwg(self):
		del self._AutomtcBrrwg
		self._AutomtcBrrwg = base_types.UninitialisedField(self, 'AutomtcBrrwg', AutomaticBorrowing6Choice, False)

	@property
	def BlckTrad(self):
		return self._BlckTrad

	@BlckTrad.setter
	def BlckTrad(self, value):
		self._BlckTrad = value if value is not None else base_types.UninitialisedField(self, 'BlckTrad', BlockTrade4Choice, False)

	@BlckTrad.deleter
	def BlckTrad(self):
		del self._BlckTrad
		self._BlckTrad = base_types.UninitialisedField(self, 'BlckTrad', BlockTrade4Choice, False)

	@property
	def BnfclOwnrsh(self):
		return self._BnfclOwnrsh

	@BnfclOwnrsh.setter
	def BnfclOwnrsh(self, value):
		self._BnfclOwnrsh = value if value is not None else base_types.UninitialisedField(self, 'BnfclOwnrsh', BeneficialOwnership4Choice, False)

	@BnfclOwnrsh.deleter
	def BnfclOwnrsh(self):
		del self._BnfclOwnrsh
		self._BnfclOwnrsh = base_types.UninitialisedField(self, 'BnfclOwnrsh', BeneficialOwnership4Choice, False)

	@property
	def CCPElgblty(self):
		return self._CCPElgblty

	@CCPElgblty.setter
	def CCPElgblty(self, value):
		self._CCPElgblty = value if value is not None else base_types.UninitialisedField(self, 'CCPElgblty', CentralCounterPartyEligibility4Choice, False)

	@CCPElgblty.deleter
	def CCPElgblty(self):
		del self._CCPElgblty
		self._CCPElgblty = base_types.UninitialisedField(self, 'CCPElgblty', CentralCounterPartyEligibility4Choice, False)

	@property
	def CshClrSys(self):
		return self._CshClrSys

	@CshClrSys.setter
	def CshClrSys(self, value):
		self._CshClrSys = value if value is not None else base_types.UninitialisedField(self, 'CshClrSys', CashSettlementSystem6Choice, False)

	@CshClrSys.deleter
	def CshClrSys(self):
		del self._CshClrSys
		self._CshClrSys = base_types.UninitialisedField(self, 'CshClrSys', CashSettlementSystem6Choice, False)

	@property
	def ElgblForColl(self):
		return self._ElgblForColl

	@ElgblForColl.setter
	def ElgblForColl(self, value):
		self._ElgblForColl = value if value is not None else base_types.UninitialisedField(self, 'ElgblForColl', YesNoIndicator, False)

	@ElgblForColl.deleter
	def ElgblForColl(self):
		del self._ElgblForColl
		self._ElgblForColl = base_types.UninitialisedField(self, 'ElgblForColl', YesNoIndicator, False)

	@property
	def FxStgInstr(self):
		return self._FxStgInstr

	@FxStgInstr.setter
	def FxStgInstr(self, value):
		self._FxStgInstr = value if value is not None else base_types.UninitialisedField(self, 'FxStgInstr', FXStandingInstruction4Choice, False)

	@FxStgInstr.deleter
	def FxStgInstr(self):
		del self._FxStgInstr
		self._FxStgInstr = base_types.UninitialisedField(self, 'FxStgInstr', FXStandingInstruction4Choice, False)

	@property
	def HldInd(self):
		return self._HldInd

	@HldInd.setter
	def HldInd(self, value):
		self._HldInd = value if value is not None else base_types.UninitialisedField(self, 'HldInd', YesNoIndicator, False)

	@HldInd.deleter
	def HldInd(self):
		del self._HldInd
		self._HldInd = base_types.UninitialisedField(self, 'HldInd', YesNoIndicator, False)

	@property
	def LglRstrctns(self):
		return self._LglRstrctns

	@LglRstrctns.setter
	def LglRstrctns(self, value):
		self._LglRstrctns = value if value is not None else base_types.UninitialisedField(self, 'LglRstrctns', Restriction5Choice, False)

	@LglRstrctns.deleter
	def LglRstrctns(self):
		del self._LglRstrctns
		self._LglRstrctns = base_types.UninitialisedField(self, 'LglRstrctns', Restriction5Choice, False)

	@property
	def MktClntSd(self):
		return self._MktClntSd

	@MktClntSd.setter
	def MktClntSd(self, value):
		self._MktClntSd = value if value is not None else base_types.UninitialisedField(self, 'MktClntSd', MarketClientSide6Choice, False)

	@MktClntSd.deleter
	def MktClntSd(self):
		del self._MktClntSd
		self._MktClntSd = base_types.UninitialisedField(self, 'MktClntSd', MarketClientSide6Choice, False)

	@property
	def NetgElgblty(self):
		return self._NetgElgblty

	@NetgElgblty.setter
	def NetgElgblty(self, value):
		self._NetgElgblty = value if value is not None else base_types.UninitialisedField(self, 'NetgElgblty', NettingEligibility4Choice, False)

	@NetgElgblty.deleter
	def NetgElgblty(self):
		del self._NetgElgblty
		self._NetgElgblty = base_types.UninitialisedField(self, 'NetgElgblty', NettingEligibility4Choice, False)

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
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, False)

	@property
	def SctiesRTGS(self):
		return self._SctiesRTGS

	@SctiesRTGS.setter
	def SctiesRTGS(self, value):
		self._SctiesRTGS = value if value is not None else base_types.UninitialisedField(self, 'SctiesRTGS', SecuritiesRTGS4Choice, False)

	@SctiesRTGS.deleter
	def SctiesRTGS(self):
		del self._SctiesRTGS
		self._SctiesRTGS = base_types.UninitialisedField(self, 'SctiesRTGS', SecuritiesRTGS4Choice, False)

	@property
	def StmpDtyTaxBsis(self):
		return self._StmpDtyTaxBsis

	@StmpDtyTaxBsis.setter
	def StmpDtyTaxBsis(self, value):
		self._StmpDtyTaxBsis = value if value is not None else base_types.UninitialisedField(self, 'StmpDtyTaxBsis', GenericIdentification30, False)

	@StmpDtyTaxBsis.deleter
	def StmpDtyTaxBsis(self):
		del self._StmpDtyTaxBsis
		self._StmpDtyTaxBsis = base_types.UninitialisedField(self, 'StmpDtyTaxBsis', GenericIdentification30, False)

	@property
	def SttlgCpcty(self):
		return self._SttlgCpcty

	@SttlgCpcty.setter
	def SttlgCpcty(self, value):
		self._SttlgCpcty = value if value is not None else base_types.UninitialisedField(self, 'SttlgCpcty', SettlingCapacity7Choice, False)

	@SttlgCpcty.deleter
	def SttlgCpcty(self):
		del self._SttlgCpcty
		self._SttlgCpcty = base_types.UninitialisedField(self, 'SttlgCpcty', SettlingCapacity7Choice, False)

	@property
	def SttlmSysMtd(self):
		return self._SttlmSysMtd

	@SttlmSysMtd.setter
	def SttlmSysMtd(self, value):
		self._SttlmSysMtd = value if value is not None else base_types.UninitialisedField(self, 'SttlmSysMtd', SettlementSystemMethod4Choice, False)

	@SttlmSysMtd.deleter
	def SttlmSysMtd(self):
		del self._SttlmSysMtd
		self._SttlmSysMtd = base_types.UninitialisedField(self, 'SttlmSysMtd', SettlementSystemMethod4Choice, False)

	@property
	def SttlmTxCond(self):
		return self._SttlmTxCond

	@SttlmTxCond.setter
	def SttlmTxCond(self, value):
		self._SttlmTxCond = value if value is not None else base_types.UninitialisedField(self, 'SttlmTxCond', SettlementTransactionCondition45Choice, True)

	@SttlmTxCond.deleter
	def SttlmTxCond(self):
		del self._SttlmTxCond
		self._SttlmTxCond = base_types.UninitialisedField(self, 'SttlmTxCond', SettlementTransactionCondition45Choice, True)

	@property
	def TaxCpcty(self):
		return self._TaxCpcty

	@TaxCpcty.setter
	def TaxCpcty(self, value):
		self._TaxCpcty = value if value is not None else base_types.UninitialisedField(self, 'TaxCpcty', TaxCapacityParty4Choice, False)

	@TaxCpcty.deleter
	def TaxCpcty(self):
		del self._TaxCpcty
		self._TaxCpcty = base_types.UninitialisedField(self, 'TaxCpcty', TaxCapacityParty4Choice, False)

	@property
	def Trckg(self):
		return self._Trckg

	@Trckg.setter
	def Trckg(self, value):
		self._Trckg = value if value is not None else base_types.UninitialisedField(self, 'Trckg', Tracking4Choice, False)

	@Trckg.deleter
	def Trckg(self):
		del self._Trckg
		self._Trckg = base_types.UninitialisedField(self, 'Trckg', Tracking4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AutomtcBrrwg', type=AutomaticBorrowing6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckTrad', type=BlockTrade4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnrsh', type=BeneficialOwnership4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CCPElgblty', type=CentralCounterPartyEligibility4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshClrSys', type=CashSettlementSystem6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgblForColl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxStgInstr', type=FXStandingInstruction4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglRstrctns', type=Restriction5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClntSd', type=MarketClientSide6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetgElgblty', type=NettingEligibility4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlSttlmInd', type=SettlementTransactionCondition5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesRTGS', type=SecuritiesRTGS4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyTaxBsis', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlgCpcty', type=SettlingCapacity7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSysMtd', type=SettlementSystemMethod4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTxCond', type=SettlementTransactionCondition45Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxCpcty', type=TaxCapacityParty4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trckg', type=Tracking4Choice, min=0, max=1, mutex_group=None, array=False),
	))