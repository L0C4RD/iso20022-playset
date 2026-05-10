from . import base_types
from .Result1 import Result1

class MarginCallResult2(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmt", "_VartnMrgnRslt"]
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
	def VartnMrgnRslt(self):
		return self._VartnMrgnRslt

	@VartnMrgnRslt.setter
	def VartnMrgnRslt(self, value):
		self._VartnMrgnRslt = value if type(value) != base_types.auto else self.make_default("VartnMrgnRslt")

	@VartnMrgnRslt.deleter
	def VartnMrgnRslt(self):
		del self._VartnMrgnRslt
		self._VartnMrgnRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=Result1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRslt', type=Result1, min=1, max=1, mutex_group=None, array=False),
	))

