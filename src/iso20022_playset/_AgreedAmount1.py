from . import base_types
from ._Amount1 import Amount1

class AgreedAmount1(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmt", "_VartnMrgnAmt"]
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
	def VartnMrgnAmt(self):
		return self._VartnMrgnAmt

	@VartnMrgnAmt.setter
	def VartnMrgnAmt(self, value):
		self._VartnMrgnAmt = value if type(value) != base_types.auto else self.make_default("VartnMrgnAmt")

	@VartnMrgnAmt.deleter
	def VartnMrgnAmt(self):
		del self._VartnMrgnAmt
		self._VartnMrgnAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=Amount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnAmt', type=Amount1, min=1, max=1, mutex_group=None, array=False),
	))

