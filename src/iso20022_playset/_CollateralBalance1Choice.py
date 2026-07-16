# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Collateral1
from . import MarginCollateral1

class CollateralBalance1Choice(base_types._BaseFieldType):

	__slots__ = ["_CollDtls", "_SgrtdIndpdntAmt", "_TtlColl"]
	@property
	def CollDtls(self):
		return self._CollDtls

	@CollDtls.setter
	def CollDtls(self, value):
		self._CollDtls = value if value is not None else base_types.UninitialisedField(self, 'CollDtls', Collateral1, False)

	@CollDtls.deleter
	def CollDtls(self):
		del self._CollDtls
		self._CollDtls = base_types.UninitialisedField(self, 'CollDtls', Collateral1, False)

	@property
	def SgrtdIndpdntAmt(self):
		return self._SgrtdIndpdntAmt

	@SgrtdIndpdntAmt.setter
	def SgrtdIndpdntAmt(self, value):
		self._SgrtdIndpdntAmt = value if value is not None else base_types.UninitialisedField(self, 'SgrtdIndpdntAmt', MarginCollateral1, False)

	@SgrtdIndpdntAmt.deleter
	def SgrtdIndpdntAmt(self):
		del self._SgrtdIndpdntAmt
		self._SgrtdIndpdntAmt = base_types.UninitialisedField(self, 'SgrtdIndpdntAmt', MarginCollateral1, False)

	@property
	def TtlColl(self):
		return self._TtlColl

	@TtlColl.setter
	def TtlColl(self, value):
		self._TtlColl = value if value is not None else base_types.UninitialisedField(self, 'TtlColl', ActiveCurrencyAndAmount, False)

	@TtlColl.deleter
	def TtlColl(self):
		del self._TtlColl
		self._TtlColl = base_types.UninitialisedField(self, 'TtlColl', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollDtls', type=Collateral1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=MarginCollateral1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TtlColl', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))