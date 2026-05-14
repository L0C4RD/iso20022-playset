# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BeneficialOwnership4Choice import BeneficialOwnership4Choice
from ._CashSettlementSystem4Choice import CashSettlementSystem4Choice
from ._GenericIdentification30 import GenericIdentification30
from ._MarketClientSide6Choice import MarketClientSide6Choice
from ._Registration9Choice import Registration9Choice
from ._RepurchaseType13Choice import RepurchaseType13Choice
from ._SecuritiesRTGS4Choice import SecuritiesRTGS4Choice
from ._SecuritiesTransactionType45Choice import SecuritiesTransactionType45Choice
from ._SettlementTransactionCondition17Choice import SettlementTransactionCondition17Choice
from ._SettlementTransactionCondition5Code import SettlementTransactionCondition5Code
from ._YesNoIndicator import YesNoIndicator

class SettlementDetails168(base_types._BaseFieldType):

	__slots__ = ["_BnfclOwnrsh", "_CshClrSys", "_HldInd", "_MktClntSd", "_PrtlSttlmInd", "_Regn", "_RpTp", "_SctiesRTGS", "_SctiesTxTp", "_StmpDtyTaxBsis", "_SttlmTxCond"]
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
	def Regn(self):
		return self._Regn

	@Regn.setter
	def Regn(self, value):
		self._Regn = value if type(value) != base_types.auto else self.make_default("Regn")

	@Regn.deleter
	def Regn(self):
		del self._Regn
		self._Regn = None

	@property
	def RpTp(self):
		return self._RpTp

	@RpTp.setter
	def RpTp(self, value):
		self._RpTp = value if type(value) != base_types.auto else self.make_default("RpTp")

	@RpTp.deleter
	def RpTp(self):
		del self._RpTp
		self._RpTp = None

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
	def SttlmTxCond(self):
		return self._SttlmTxCond

	@SttlmTxCond.setter
	def SttlmTxCond(self, value):
		self._SttlmTxCond = value if type(value) != base_types.auto else self.make_default("SttlmTxCond")

	@SttlmTxCond.deleter
	def SttlmTxCond(self):
		del self._SttlmTxCond
		self._SttlmTxCond = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BnfclOwnrsh', type=BeneficialOwnership4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshClrSys', type=CashSettlementSystem4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktClntSd', type=MarketClientSide6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlSttlmInd', type=SettlementTransactionCondition5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Regn', type=Registration9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpTp', type=RepurchaseType13Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesRTGS', type=SecuritiesRTGS4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesTxTp', type=SecuritiesTransactionType45Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyTaxBsis', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTxCond', type=SettlementTransactionCondition17Choice, min=0, max=None, mutex_group=None, array=True),
	))