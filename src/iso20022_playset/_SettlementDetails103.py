from . import base_types
from ._Restriction6Choice import Restriction6Choice
from ._SettlementSystemMethod5Choice import SettlementSystemMethod5Choice
from ._GenericIdentification47 import GenericIdentification47
from ._Registration11Choice import Registration11Choice
from ._SecuritiesRTGS5Choice import SecuritiesRTGS5Choice
from ._TaxCapacityParty5Choice import TaxCapacityParty5Choice
from ._SettlementTransactionCondition21Choice import SettlementTransactionCondition21Choice

class SettlementDetails103(base_types._BaseFieldType):

	__slots__ = ["_TaxCpcty", "_SttlmTxCond", "_LglRstrctns", "_Regn", "_SctiesRTGS", "_StmpDtyTaxBsis", "_SttlmSysMtd"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='LglRstrctns', type=Restriction6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Regn', type=Registration11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesRTGS', type=SecuritiesRTGS5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmpDtyTaxBsis', type=GenericIdentification47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSysMtd', type=SettlementSystemMethod5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTxCond', type=SettlementTransactionCondition21Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxCpcty', type=TaxCapacityParty5Choice, min=0, max=1, mutex_group=None, array=False),
	))

