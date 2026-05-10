from . import base_types
from .CashParties24 import CashParties24
from .SettlementParties35 import SettlementParties35

class SecuritiesOrCash1Choice(base_types._BaseFieldType):

	__slots__ = ["_CshPtiesDtls", "_SctiesDtls"]
	@property
	def CshPtiesDtls(self):
		return self._CshPtiesDtls

	@CshPtiesDtls.setter
	def CshPtiesDtls(self, value):
		self._CshPtiesDtls = value if type(value) != base_types.auto else self.make_default("CshPtiesDtls")

	@CshPtiesDtls.deleter
	def CshPtiesDtls(self):
		del self._CshPtiesDtls
		self._CshPtiesDtls = None

	@property
	def SctiesDtls(self):
		return self._SctiesDtls

	@SctiesDtls.setter
	def SctiesDtls(self, value):
		self._SctiesDtls = value if type(value) != base_types.auto else self.make_default("SctiesDtls")

	@SctiesDtls.deleter
	def SctiesDtls(self):
		del self._SctiesDtls
		self._SctiesDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshPtiesDtls', type=CashParties24, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesDtls', type=SettlementParties35, min=0, max=1, mutex_group=1, array=False),
	))

