import base_types
import SecuritiesProceeds1
import CashProceeds1
import TaxVoucher1

class ProceedsMovement1(base_types._BaseFieldType):

	__slots__ = ["_CshPrcdsMvmntDtls", "_TaxDtls", "_SctiesPrcdsMvmntDtls"]
	@property
	def CshPrcdsMvmntDtls(self):
		return self._CshPrcdsMvmntDtls

	@CshPrcdsMvmntDtls.setter
	def CshPrcdsMvmntDtls(self, value):
		self._CshPrcdsMvmntDtls = value if type(value) != auto else self.make_default("CshPrcdsMvmntDtls")

	@CshPrcdsMvmntDtls.deleter
	def CshPrcdsMvmntDtls(self):
		del self._CshPrcdsMvmntDtls
		self._CshPrcdsMvmntDtls = None

	@property
	def TaxDtls(self):
		return self._TaxDtls

	@TaxDtls.setter
	def TaxDtls(self, value):
		self._TaxDtls = value if type(value) != auto else self.make_default("TaxDtls")

	@TaxDtls.deleter
	def TaxDtls(self):
		del self._TaxDtls
		self._TaxDtls = None

	@property
	def SctiesPrcdsMvmntDtls(self):
		return self._SctiesPrcdsMvmntDtls

	@SctiesPrcdsMvmntDtls.setter
	def SctiesPrcdsMvmntDtls(self, value):
		self._SctiesPrcdsMvmntDtls = value if type(value) != auto else self.make_default("SctiesPrcdsMvmntDtls")

	@SctiesPrcdsMvmntDtls.deleter
	def SctiesPrcdsMvmntDtls(self):
		del self._SctiesPrcdsMvmntDtls
		self._SctiesPrcdsMvmntDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshPrcdsMvmntDtls', type=CashProceeds1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxDtls', type=TaxVoucher1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesPrcdsMvmntDtls', type=SecuritiesProceeds1, min=0, max=None, mutex_group=None, array=True),
	))

