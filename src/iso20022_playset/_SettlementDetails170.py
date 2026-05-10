from . import base_types
from ._Restriction5Choice import Restriction5Choice
from ._BeneficialOwnership4Choice import BeneficialOwnership4Choice
from ._GenericIdentification30 import GenericIdentification30
from ._CentralCounterPartyEligibility4Choice import CentralCounterPartyEligibility4Choice
from ._SecuritiesRTGS4Choice import SecuritiesRTGS4Choice
from ._BlockTrade4Choice import BlockTrade4Choice
from ._NettingEligibility4Choice import NettingEligibility4Choice
from ._SettlementTransactionCondition18Choice import SettlementTransactionCondition18Choice
from ._CashSettlementSystem4Choice import CashSettlementSystem4Choice
from ._SettlementSystemMethod4Choice import SettlementSystemMethod4Choice
from ._MarketClientSide6Choice import MarketClientSide6Choice
from ._SettlingCapacity7Choice import SettlingCapacity7Choice
from ._TaxCapacityParty4Choice import TaxCapacityParty4Choice
from ._YesNoIndicator import YesNoIndicator
from ._SettlementTransactionCondition5Code import SettlementTransactionCondition5Code

class SettlementDetails170(base_types._BaseFieldType):

	__slots__ = ["_SttlmTxCond", "_LglRstrctns", "_SctiesRTGS", "_BnfclOwnrsh", "_HldInd", "_TaxCpcty", "_PrtlSttlmInd", "_CshClrSys", "_SttlgCpcty", "_BlckTrad", "_StmpDtyTaxBsis", "_SttlmSysMtd", "_MktClntSd", "_CCPElgblty", "_ElgblForColl", "_NetgElgblty"]
	@property
	def SttlmTxCond(self):
		return self._SttlmTxCond

	@SttlmTxCond.setter
	def SttlmTxCond(self, value):
		self._SttlmTxCond = value if type(value) != base_types.auto else self.make_default("SttlmTxCond")

	@SttlmTxCond.deleter
	def SttlmTxCond(self):
		del self._SttlmTxCond
		self._SttlmTxCond = None

	@property
	def LglRstrctns(self):
		return self._LglRstrctns

	@LglRstrctns.setter
	def LglRstrctns(self, value):
		self._LglRstrctns = value if type(value) != base_types.auto else self.make_default("LglRstrctns")

	@LglRstrctns.deleter
	def LglRstrctns(self):
		del self._LglRstrctns
		self._LglRstrctns = None

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
	def BnfclOwnrsh(self):
		return self._BnfclOwnrsh

	@BnfclOwnrsh.setter
	def BnfclOwnrsh(self, value):
		self._BnfclOwnrsh = value if type(value) != base_types.auto else self.make_default("BnfclOwnrsh")

	@BnfclOwnrsh.deleter
	def BnfclOwnrsh(self):
		del self._BnfclOwnrsh
		self._BnfclOwnrsh = None

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
	def TaxCpcty(self):
		return self._TaxCpcty

	@TaxCpcty.setter
	def TaxCpcty(self, value):
		self._TaxCpcty = value if type(value) != base_types.auto else self.make_default("TaxCpcty")

	@TaxCpcty.deleter
	def TaxCpcty(self):
		del self._TaxCpcty
		self._TaxCpcty = None

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
	def CshClrSys(self):
		return self._CshClrSys

	@CshClrSys.setter
	def CshClrSys(self, value):
		self._CshClrSys = value if type(value) != base_types.auto else self.make_default("CshClrSys")

	@CshClrSys.deleter
	def CshClrSys(self):
		del self._CshClrSys
		self._CshClrSys = None

	@property
	def SttlgCpcty(self):
		return self._SttlgCpcty

	@SttlgCpcty.setter
	def SttlgCpcty(self, value):
		self._SttlgCpcty = value if type(value) != base_types.auto else self.make_default("SttlgCpcty")

	@SttlgCpcty.deleter
	def SttlgCpcty(self):
		del self._SttlgCpcty
		self._SttlgCpcty = None

	@property
	def BlckTrad(self):
		return self._BlckTrad

	@BlckTrad.setter
	def BlckTrad(self, value):
		self._BlckTrad = value if type(value) != base_types.auto else self.make_default("BlckTrad")

	@BlckTrad.deleter
	def BlckTrad(self):
		del self._BlckTrad
		self._BlckTrad = None

	@property
	def StmpDtyTaxBsis(self):
		return self._StmpDtyTaxBsis

	@StmpDtyTaxBsis.setter
	def StmpDtyTaxBsis(self, value):
		self._StmpDtyTaxBsis = value if type(value) != base_types.auto else self.make_default("StmpDtyTaxBsis")

	@StmpDtyTaxBsis.deleter
	def StmpDtyTaxBsis(self):
		del self._StmpDtyTaxBsis
		self._StmpDtyTaxBsis = None

	@property
	def SttlmSysMtd(self):
		return self._SttlmSysMtd

	@SttlmSysMtd.setter
	def SttlmSysMtd(self, value):
		self._SttlmSysMtd = value if type(value) != base_types.auto else self.make_default("SttlmSysMtd")

	@SttlmSysMtd.deleter
	def SttlmSysMtd(self):
		del self._SttlmSysMtd
		self._SttlmSysMtd = None

	@property
	def MktClntSd(self):
		return self._MktClntSd

	@MktClntSd.setter
	def MktClntSd(self, value):
		self._MktClntSd = value if type(value) != base_types.auto else self.make_default("MktClntSd")

	@MktClntSd.deleter
	def MktClntSd(self):
		del self._MktClntSd
		self._MktClntSd = None

	@property
	def CCPElgblty(self):
		return self._CCPElgblty

	@CCPElgblty.setter
	def CCPElgblty(self, value):
		self._CCPElgblty = value if type(value) != base_types.auto else self.make_default("CCPElgblty")

	@CCPElgblty.deleter
	def CCPElgblty(self):
		del self._CCPElgblty
		self._CCPElgblty = None

	@property
	def ElgblForColl(self):
		return self._ElgblForColl

	@ElgblForColl.setter
	def ElgblForColl(self, value):
		self._ElgblForColl = value if type(value) != base_types.auto else self.make_default("ElgblForColl")

	@ElgblForColl.deleter
	def ElgblForColl(self):
		del self._ElgblForColl
		self._ElgblForColl = None

	@property
	def NetgElgblty(self):
		return self._NetgElgblty

	@NetgElgblty.setter
	def NetgElgblty(self, value):
		self._NetgElgblty = value if type(value) != base_types.auto else self.make_default("NetgElgblty")

	@NetgElgblty.deleter
	def NetgElgblty(self):
		del self._NetgElgblty
		self._NetgElgblty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmTxCond', type=SettlementTransactionCondition18Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LglRstrctns', type=Restriction5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesRTGS', type=SecuritiesRTGS4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnrsh', type=BeneficialOwnership4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCpcty', type=TaxCapacityParty4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlSttlmInd', type=SettlementTransactionCondition5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshClrSys', type=CashSettlementSystem4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlgCpcty', type=SettlingCapacity7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckTrad', type=BlockTrade4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyTaxBsis', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSysMtd', type=SettlementSystemMethod4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClntSd', type=MarketClientSide6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CCPElgblty', type=CentralCounterPartyEligibility4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgblForColl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetgElgblty', type=NettingEligibility4Choice, min=0, max=1, mutex_group=None, array=False),
	))

