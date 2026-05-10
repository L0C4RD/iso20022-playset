from . import base_types
from ._ExpectedCollateralMovement2 import ExpectedCollateralMovement2

class ExpectedCollateral2(base_types._BaseFieldType):

	__slots__ = ["_VartnMrgn", "_SgrtdIndpdntAmt"]
	@property
	def SgrtdIndpdntAmt(self):
		return self._SgrtdIndpdntAmt

	@SgrtdIndpdntAmt.setter
	def SgrtdIndpdntAmt(self, value):
		self._SgrtdIndpdntAmt = value if type(value) != base_types.auto else self.make_default("SgrtdIndpdntAmt")

	@SgrtdIndpdntAmt.deleter
	def SgrtdIndpdntAmt(self):
		del self._SgrtdIndpdntAmt
		self._SgrtdIndpdntAmt = None

	@property
	def VartnMrgn(self):
		return self._VartnMrgn

	@VartnMrgn.setter
	def VartnMrgn(self, value):
		self._VartnMrgn = value if type(value) != base_types.auto else self.make_default("VartnMrgn")

	@VartnMrgn.deleter
	def VartnMrgn(self):
		del self._VartnMrgn
		self._VartnMrgn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=ExpectedCollateralMovement2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgn', type=ExpectedCollateralMovement2, min=1, max=1, mutex_group=None, array=False),
	))

