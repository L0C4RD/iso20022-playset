import base_types
import ExpectedCollateral2
import ExpectedCollateralMovement2

class ExpectedCollateral2Choice(base_types._BaseFieldType):

	__slots__ = ["_XpctdCollDtls", "_SgrtdIndpdntAmt"]
	@property
	def XpctdCollDtls(self):
		return self._XpctdCollDtls

	@XpctdCollDtls.setter
	def XpctdCollDtls(self, value):
		self._XpctdCollDtls = value if type(value) != auto else self.make_default("XpctdCollDtls")

	@XpctdCollDtls.deleter
	def XpctdCollDtls(self):
		del self._XpctdCollDtls
		self._XpctdCollDtls = None

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
		base_types.FieldEntry(name='XpctdCollDtls', type=ExpectedCollateral2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=ExpectedCollateralMovement2, min=0, max=1, mutex_group=1, array=False),
	))

