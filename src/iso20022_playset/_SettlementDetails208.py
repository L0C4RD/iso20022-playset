from . import base_types
from .CentralCounterPartyEligibility5Choice import CentralCounterPartyEligibility5Choice
from .ExposureType24Choice import ExposureType24Choice
from .NettingEligibility5Choice import NettingEligibility5Choice
from .LetterOfGuarantee5Choice import LetterOfGuarantee5Choice
from .SecuritiesTransactionType60Choice import SecuritiesTransactionType60Choice
from .DeliveryReturn4Choice import DeliveryReturn4Choice
from .Registration11Choice import Registration11Choice
from .CashSettlementSystem5Choice import CashSettlementSystem5Choice
from .YesNoIndicator import YesNoIndicator
from .MarketClientSide7Choice import MarketClientSide7Choice
from .BeneficialOwnership5Choice import BeneficialOwnership5Choice
from .SettlementTransactionCondition28Choice import SettlementTransactionCondition28Choice
from .TaxCapacityParty5Choice import TaxCapacityParty5Choice
from .Restriction6Choice import Restriction6Choice
from .SettlingCapacity8Choice import SettlingCapacity8Choice
from .FXStandingInstruction5Choice import FXStandingInstruction5Choice
from .ModificationCancellationAllowed5Choice import ModificationCancellationAllowed5Choice
from .GenericIdentification47 import GenericIdentification47
from .Tracking5Choice import Tracking5Choice

class SettlementDetails208(base_types._BaseFieldType):

	__slots__ = ["_NetgElgblty", "_ElgblForColl", "_LttrOfGrnt", "_CCPElgblty", "_CshClrSys", "_BnfclOwnrsh", "_DlvryRtrRsn", "_RtrLeg", "_ModCxlAllwd", "_FxStgInstr", "_SctiesSubBalTp", "_MktClntSd", "_SttlmTxCond", "_TaxCpcty", "_Trckg", "_XpsrTp", "_CshSubBalTp", "_SttlgCpcty", "_LglRstrctns", "_StmpDtyTaxBsis", "_SctiesTxTp", "_Regn"]
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
	def LttrOfGrnt(self):
		return self._LttrOfGrnt

	@LttrOfGrnt.setter
	def LttrOfGrnt(self, value):
		self._LttrOfGrnt = value if type(value) != base_types.auto else self.make_default("LttrOfGrnt")

	@LttrOfGrnt.deleter
	def LttrOfGrnt(self):
		del self._LttrOfGrnt
		self._LttrOfGrnt = None

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
	def DlvryRtrRsn(self):
		return self._DlvryRtrRsn

	@DlvryRtrRsn.setter
	def DlvryRtrRsn(self, value):
		self._DlvryRtrRsn = value if type(value) != base_types.auto else self.make_default("DlvryRtrRsn")

	@DlvryRtrRsn.deleter
	def DlvryRtrRsn(self):
		del self._DlvryRtrRsn
		self._DlvryRtrRsn = None

	@property
	def RtrLeg(self):
		return self._RtrLeg

	@RtrLeg.setter
	def RtrLeg(self, value):
		self._RtrLeg = value if type(value) != base_types.auto else self.make_default("RtrLeg")

	@RtrLeg.deleter
	def RtrLeg(self):
		del self._RtrLeg
		self._RtrLeg = None

	@property
	def ModCxlAllwd(self):
		return self._ModCxlAllwd

	@ModCxlAllwd.setter
	def ModCxlAllwd(self, value):
		self._ModCxlAllwd = value if type(value) != base_types.auto else self.make_default("ModCxlAllwd")

	@ModCxlAllwd.deleter
	def ModCxlAllwd(self):
		del self._ModCxlAllwd
		self._ModCxlAllwd = None

	@property
	def FxStgInstr(self):
		return self._FxStgInstr

	@FxStgInstr.setter
	def FxStgInstr(self, value):
		self._FxStgInstr = value if type(value) != base_types.auto else self.make_default("FxStgInstr")

	@FxStgInstr.deleter
	def FxStgInstr(self):
		del self._FxStgInstr
		self._FxStgInstr = None

	@property
	def SctiesSubBalTp(self):
		return self._SctiesSubBalTp

	@SctiesSubBalTp.setter
	def SctiesSubBalTp(self, value):
		self._SctiesSubBalTp = value if type(value) != base_types.auto else self.make_default("SctiesSubBalTp")

	@SctiesSubBalTp.deleter
	def SctiesSubBalTp(self):
		del self._SctiesSubBalTp
		self._SctiesSubBalTp = None

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
	def Trckg(self):
		return self._Trckg

	@Trckg.setter
	def Trckg(self, value):
		self._Trckg = value if type(value) != base_types.auto else self.make_default("Trckg")

	@Trckg.deleter
	def Trckg(self):
		del self._Trckg
		self._Trckg = None

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if type(value) != base_types.auto else self.make_default("XpsrTp")

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = None

	@property
	def CshSubBalTp(self):
		return self._CshSubBalTp

	@CshSubBalTp.setter
	def CshSubBalTp(self, value):
		self._CshSubBalTp = value if type(value) != base_types.auto else self.make_default("CshSubBalTp")

	@CshSubBalTp.deleter
	def CshSubBalTp(self):
		del self._CshSubBalTp
		self._CshSubBalTp = None

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
	def SctiesTxTp(self):
		return self._SctiesTxTp

	@SctiesTxTp.setter
	def SctiesTxTp(self, value):
		self._SctiesTxTp = value if type(value) != base_types.auto else self.make_default("SctiesTxTp")

	@SctiesTxTp.deleter
	def SctiesTxTp(self):
		del self._SctiesTxTp
		self._SctiesTxTp = None

	@property
	def Regn(self):
		return self._Regn

	@Regn.setter
	def Regn(self, value):
		self._Regn = value if type(value) != base_types.auto else self.make_default("Regn")

	@Regn.deleter
	def Regn(self):
		del self._Regn
		self._Regn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetgElgblty', type=NettingEligibility5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgblForColl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrOfGrnt', type=LetterOfGuarantee5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CCPElgblty', type=CentralCounterPartyEligibility5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshClrSys', type=CashSettlementSystem5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnrsh', type=BeneficialOwnership5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryRtrRsn', type=DeliveryReturn4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrLeg', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModCxlAllwd', type=ModificationCancellationAllowed5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxStgInstr', type=FXStandingInstruction5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSubBalTp', type=GenericIdentification47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClntSd', type=MarketClientSide7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTxCond', type=SettlementTransactionCondition28Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxCpcty', type=TaxCapacityParty5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trckg', type=Tracking5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSubBalTp', type=GenericIdentification47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlgCpcty', type=SettlingCapacity8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglRstrctns', type=Restriction6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyTaxBsis', type=GenericIdentification47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesTxTp', type=SecuritiesTransactionType60Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Regn', type=Registration11Choice, min=0, max=1, mutex_group=None, array=False),
	))

