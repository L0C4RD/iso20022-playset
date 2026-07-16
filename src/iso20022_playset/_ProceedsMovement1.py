# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashProceeds1
from . import SecuritiesProceeds1
from . import TaxVoucher1

class ProceedsMovement1(base_types._BaseFieldType):

	__slots__ = ["_CshPrcdsMvmntDtls", "_SctiesPrcdsMvmntDtls", "_TaxDtls"]
	@property
	def CshPrcdsMvmntDtls(self):
		return self._CshPrcdsMvmntDtls

	@CshPrcdsMvmntDtls.setter
	def CshPrcdsMvmntDtls(self, value):
		self._CshPrcdsMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'CshPrcdsMvmntDtls', CashProceeds1, True)

	@CshPrcdsMvmntDtls.deleter
	def CshPrcdsMvmntDtls(self):
		del self._CshPrcdsMvmntDtls
		self._CshPrcdsMvmntDtls = base_types.UninitialisedField(self, 'CshPrcdsMvmntDtls', CashProceeds1, True)

	@property
	def SctiesPrcdsMvmntDtls(self):
		return self._SctiesPrcdsMvmntDtls

	@SctiesPrcdsMvmntDtls.setter
	def SctiesPrcdsMvmntDtls(self, value):
		self._SctiesPrcdsMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesPrcdsMvmntDtls', SecuritiesProceeds1, True)

	@SctiesPrcdsMvmntDtls.deleter
	def SctiesPrcdsMvmntDtls(self):
		del self._SctiesPrcdsMvmntDtls
		self._SctiesPrcdsMvmntDtls = base_types.UninitialisedField(self, 'SctiesPrcdsMvmntDtls', SecuritiesProceeds1, True)

	@property
	def TaxDtls(self):
		return self._TaxDtls

	@TaxDtls.setter
	def TaxDtls(self, value):
		self._TaxDtls = value if value is not None else base_types.UninitialisedField(self, 'TaxDtls', TaxVoucher1, False)

	@TaxDtls.deleter
	def TaxDtls(self):
		del self._TaxDtls
		self._TaxDtls = base_types.UninitialisedField(self, 'TaxDtls', TaxVoucher1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshPrcdsMvmntDtls', type=CashProceeds1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesPrcdsMvmntDtls', type=SecuritiesProceeds1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxDtls', type=TaxVoucher1, min=0, max=1, mutex_group=None, array=False),
	))