import base_types
import ActiveCurrencyAndAmount
import Collateral1
import MarginCollateral1

class CollateralBalance1Choice(base_types._BaseFieldType):

	__slots__ = ["_CollDtls", "_TtlColl", "_SgrtdIndpdntAmt"]
	@property
	def CollDtls(self):
		return self._CollDtls

	@CollDtls.setter
	def CollDtls(self, value):
		self._CollDtls = value if type(value) != auto else self.make_default("CollDtls")

	@CollDtls.deleter
	def CollDtls(self):
		del self._CollDtls
		self._CollDtls = None

	@property
	def TtlColl(self):
		return self._TtlColl

	@TtlColl.setter
	def TtlColl(self, value):
		self._TtlColl = value if type(value) != auto else self.make_default("TtlColl")

	@TtlColl.deleter
	def TtlColl(self):
		del self._TtlColl
		self._TtlColl = None

	@property
	def SgrtdIndpdntAmt(self):
		return self._SgrtdIndpdntAmt

	@SgrtdIndpdntAmt.setter
	def SgrtdIndpdntAmt(self, value):
		self._SgrtdIndpdntAmt = value if type(value) != auto else self.make_default("SgrtdIndpdntAmt")

	@SgrtdIndpdntAmt.deleter
	def SgrtdIndpdntAmt(self):
		del self._SgrtdIndpdntAmt
		self._SgrtdIndpdntAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollDtls', type=Collateral1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TtlColl', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=MarginCollateral1, min=0, max=1, mutex_group=1, array=False),
	))

