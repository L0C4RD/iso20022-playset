# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BeneficialOwnership5Choice
from . import CashSettlementSystem5Choice
from . import CentralCounterPartyEligibility5Choice
from . import DeliveryReturn4Choice
from . import ExposureType24Choice
from . import FXStandingInstruction5Choice
from . import GenericIdentification47
from . import LetterOfGuarantee5Choice
from . import MarketClientSide7Choice
from . import ModificationCancellationAllowed5Choice
from . import NettingEligibility5Choice
from . import Registration11Choice
from . import Restriction6Choice
from . import SecuritiesTransactionType60Choice
from . import SettlementTransactionCondition28Choice
from . import SettlingCapacity8Choice
from . import TaxCapacityParty5Choice
from . import Tracking5Choice
from . import YesNoIndicator

class SettlementDetails208(base_types._BaseFieldType):

	__slots__ = ["_BnfclOwnrsh", "_CCPElgblty", "_CshClrSys", "_CshSubBalTp", "_DlvryRtrRsn", "_ElgblForColl", "_FxStgInstr", "_LglRstrctns", "_LttrOfGrnt", "_MktClntSd", "_ModCxlAllwd", "_NetgElgblty", "_Regn", "_RtrLeg", "_SctiesSubBalTp", "_SctiesTxTp", "_StmpDtyTaxBsis", "_SttlgCpcty", "_SttlmTxCond", "_TaxCpcty", "_Trckg", "_XpsrTp"]
	@property
	def BnfclOwnrsh(self):
		return self._BnfclOwnrsh

	@BnfclOwnrsh.setter
	def BnfclOwnrsh(self, value):
		self._BnfclOwnrsh = value if value is not None else base_types.UninitialisedField(self, 'BnfclOwnrsh', BeneficialOwnership5Choice, False)

	@BnfclOwnrsh.deleter
	def BnfclOwnrsh(self):
		del self._BnfclOwnrsh
		self._BnfclOwnrsh = base_types.UninitialisedField(self, 'BnfclOwnrsh', BeneficialOwnership5Choice, False)

	@property
	def CCPElgblty(self):
		return self._CCPElgblty

	@CCPElgblty.setter
	def CCPElgblty(self, value):
		self._CCPElgblty = value if value is not None else base_types.UninitialisedField(self, 'CCPElgblty', CentralCounterPartyEligibility5Choice, False)

	@CCPElgblty.deleter
	def CCPElgblty(self):
		del self._CCPElgblty
		self._CCPElgblty = base_types.UninitialisedField(self, 'CCPElgblty', CentralCounterPartyEligibility5Choice, False)

	@property
	def CshClrSys(self):
		return self._CshClrSys

	@CshClrSys.setter
	def CshClrSys(self, value):
		self._CshClrSys = value if value is not None else base_types.UninitialisedField(self, 'CshClrSys', CashSettlementSystem5Choice, False)

	@CshClrSys.deleter
	def CshClrSys(self):
		del self._CshClrSys
		self._CshClrSys = base_types.UninitialisedField(self, 'CshClrSys', CashSettlementSystem5Choice, False)

	@property
	def CshSubBalTp(self):
		return self._CshSubBalTp

	@CshSubBalTp.setter
	def CshSubBalTp(self, value):
		self._CshSubBalTp = value if value is not None else base_types.UninitialisedField(self, 'CshSubBalTp', GenericIdentification47, False)

	@CshSubBalTp.deleter
	def CshSubBalTp(self):
		del self._CshSubBalTp
		self._CshSubBalTp = base_types.UninitialisedField(self, 'CshSubBalTp', GenericIdentification47, False)

	@property
	def DlvryRtrRsn(self):
		return self._DlvryRtrRsn

	@DlvryRtrRsn.setter
	def DlvryRtrRsn(self, value):
		self._DlvryRtrRsn = value if value is not None else base_types.UninitialisedField(self, 'DlvryRtrRsn', DeliveryReturn4Choice, False)

	@DlvryRtrRsn.deleter
	def DlvryRtrRsn(self):
		del self._DlvryRtrRsn
		self._DlvryRtrRsn = base_types.UninitialisedField(self, 'DlvryRtrRsn', DeliveryReturn4Choice, False)

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
		self._FxStgInstr = value if value is not None else base_types.UninitialisedField(self, 'FxStgInstr', FXStandingInstruction5Choice, False)

	@FxStgInstr.deleter
	def FxStgInstr(self):
		del self._FxStgInstr
		self._FxStgInstr = base_types.UninitialisedField(self, 'FxStgInstr', FXStandingInstruction5Choice, False)

	@property
	def LglRstrctns(self):
		return self._LglRstrctns

	@LglRstrctns.setter
	def LglRstrctns(self, value):
		self._LglRstrctns = value if value is not None else base_types.UninitialisedField(self, 'LglRstrctns', Restriction6Choice, False)

	@LglRstrctns.deleter
	def LglRstrctns(self):
		del self._LglRstrctns
		self._LglRstrctns = base_types.UninitialisedField(self, 'LglRstrctns', Restriction6Choice, False)

	@property
	def LttrOfGrnt(self):
		return self._LttrOfGrnt

	@LttrOfGrnt.setter
	def LttrOfGrnt(self, value):
		self._LttrOfGrnt = value if value is not None else base_types.UninitialisedField(self, 'LttrOfGrnt', LetterOfGuarantee5Choice, False)

	@LttrOfGrnt.deleter
	def LttrOfGrnt(self):
		del self._LttrOfGrnt
		self._LttrOfGrnt = base_types.UninitialisedField(self, 'LttrOfGrnt', LetterOfGuarantee5Choice, False)

	@property
	def MktClntSd(self):
		return self._MktClntSd

	@MktClntSd.setter
	def MktClntSd(self, value):
		self._MktClntSd = value if value is not None else base_types.UninitialisedField(self, 'MktClntSd', MarketClientSide7Choice, False)

	@MktClntSd.deleter
	def MktClntSd(self):
		del self._MktClntSd
		self._MktClntSd = base_types.UninitialisedField(self, 'MktClntSd', MarketClientSide7Choice, False)

	@property
	def ModCxlAllwd(self):
		return self._ModCxlAllwd

	@ModCxlAllwd.setter
	def ModCxlAllwd(self, value):
		self._ModCxlAllwd = value if value is not None else base_types.UninitialisedField(self, 'ModCxlAllwd', ModificationCancellationAllowed5Choice, False)

	@ModCxlAllwd.deleter
	def ModCxlAllwd(self):
		del self._ModCxlAllwd
		self._ModCxlAllwd = base_types.UninitialisedField(self, 'ModCxlAllwd', ModificationCancellationAllowed5Choice, False)

	@property
	def NetgElgblty(self):
		return self._NetgElgblty

	@NetgElgblty.setter
	def NetgElgblty(self, value):
		self._NetgElgblty = value if value is not None else base_types.UninitialisedField(self, 'NetgElgblty', NettingEligibility5Choice, False)

	@NetgElgblty.deleter
	def NetgElgblty(self):
		del self._NetgElgblty
		self._NetgElgblty = base_types.UninitialisedField(self, 'NetgElgblty', NettingEligibility5Choice, False)

	@property
	def Regn(self):
		return self._Regn

	@Regn.setter
	def Regn(self, value):
		self._Regn = value if value is not None else base_types.UninitialisedField(self, 'Regn', Registration11Choice, False)

	@Regn.deleter
	def Regn(self):
		del self._Regn
		self._Regn = base_types.UninitialisedField(self, 'Regn', Registration11Choice, False)

	@property
	def RtrLeg(self):
		return self._RtrLeg

	@RtrLeg.setter
	def RtrLeg(self, value):
		self._RtrLeg = value if value is not None else base_types.UninitialisedField(self, 'RtrLeg', YesNoIndicator, False)

	@RtrLeg.deleter
	def RtrLeg(self):
		del self._RtrLeg
		self._RtrLeg = base_types.UninitialisedField(self, 'RtrLeg', YesNoIndicator, False)

	@property
	def SctiesSubBalTp(self):
		return self._SctiesSubBalTp

	@SctiesSubBalTp.setter
	def SctiesSubBalTp(self, value):
		self._SctiesSubBalTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesSubBalTp', GenericIdentification47, False)

	@SctiesSubBalTp.deleter
	def SctiesSubBalTp(self):
		del self._SctiesSubBalTp
		self._SctiesSubBalTp = base_types.UninitialisedField(self, 'SctiesSubBalTp', GenericIdentification47, False)

	@property
	def SctiesTxTp(self):
		return self._SctiesTxTp

	@SctiesTxTp.setter
	def SctiesTxTp(self, value):
		self._SctiesTxTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxTp', SecuritiesTransactionType60Choice, False)

	@SctiesTxTp.deleter
	def SctiesTxTp(self):
		del self._SctiesTxTp
		self._SctiesTxTp = base_types.UninitialisedField(self, 'SctiesTxTp', SecuritiesTransactionType60Choice, False)

	@property
	def StmpDtyTaxBsis(self):
		return self._StmpDtyTaxBsis

	@StmpDtyTaxBsis.setter
	def StmpDtyTaxBsis(self, value):
		self._StmpDtyTaxBsis = value if value is not None else base_types.UninitialisedField(self, 'StmpDtyTaxBsis', GenericIdentification47, False)

	@StmpDtyTaxBsis.deleter
	def StmpDtyTaxBsis(self):
		del self._StmpDtyTaxBsis
		self._StmpDtyTaxBsis = base_types.UninitialisedField(self, 'StmpDtyTaxBsis', GenericIdentification47, False)

	@property
	def SttlgCpcty(self):
		return self._SttlgCpcty

	@SttlgCpcty.setter
	def SttlgCpcty(self, value):
		self._SttlgCpcty = value if value is not None else base_types.UninitialisedField(self, 'SttlgCpcty', SettlingCapacity8Choice, False)

	@SttlgCpcty.deleter
	def SttlgCpcty(self):
		del self._SttlgCpcty
		self._SttlgCpcty = base_types.UninitialisedField(self, 'SttlgCpcty', SettlingCapacity8Choice, False)

	@property
	def SttlmTxCond(self):
		return self._SttlmTxCond

	@SttlmTxCond.setter
	def SttlmTxCond(self, value):
		self._SttlmTxCond = value if value is not None else base_types.UninitialisedField(self, 'SttlmTxCond', SettlementTransactionCondition28Choice, True)

	@SttlmTxCond.deleter
	def SttlmTxCond(self):
		del self._SttlmTxCond
		self._SttlmTxCond = base_types.UninitialisedField(self, 'SttlmTxCond', SettlementTransactionCondition28Choice, True)

	@property
	def TaxCpcty(self):
		return self._TaxCpcty

	@TaxCpcty.setter
	def TaxCpcty(self, value):
		self._TaxCpcty = value if value is not None else base_types.UninitialisedField(self, 'TaxCpcty', TaxCapacityParty5Choice, False)

	@TaxCpcty.deleter
	def TaxCpcty(self):
		del self._TaxCpcty
		self._TaxCpcty = base_types.UninitialisedField(self, 'TaxCpcty', TaxCapacityParty5Choice, False)

	@property
	def Trckg(self):
		return self._Trckg

	@Trckg.setter
	def Trckg(self, value):
		self._Trckg = value if value is not None else base_types.UninitialisedField(self, 'Trckg', Tracking5Choice, False)

	@Trckg.deleter
	def Trckg(self):
		del self._Trckg
		self._Trckg = base_types.UninitialisedField(self, 'Trckg', Tracking5Choice, False)

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if value is not None else base_types.UninitialisedField(self, 'XpsrTp', ExposureType24Choice, False)

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = base_types.UninitialisedField(self, 'XpsrTp', ExposureType24Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BnfclOwnrsh', type=BeneficialOwnership5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CCPElgblty', type=CentralCounterPartyEligibility5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshClrSys', type=CashSettlementSystem5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSubBalTp', type=GenericIdentification47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryRtrRsn', type=DeliveryReturn4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgblForColl', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxStgInstr', type=FXStandingInstruction5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglRstrctns', type=Restriction6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrOfGrnt', type=LetterOfGuarantee5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClntSd', type=MarketClientSide7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModCxlAllwd', type=ModificationCancellationAllowed5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetgElgblty', type=NettingEligibility5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Regn', type=Registration11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrLeg', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSubBalTp', type=GenericIdentification47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesTxTp', type=SecuritiesTransactionType60Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyTaxBsis', type=GenericIdentification47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlgCpcty', type=SettlingCapacity8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTxCond', type=SettlementTransactionCondition28Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxCpcty', type=TaxCapacityParty5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trckg', type=Tracking5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType24Choice, min=0, max=1, mutex_group=None, array=False),
	))