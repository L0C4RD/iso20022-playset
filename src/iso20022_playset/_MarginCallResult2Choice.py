from . import base_types
from ._MarginCallResult2 import MarginCallResult2
from ._Result1 import Result1

class MarginCallResult2Choice(base_types._BaseFieldType):

	__slots__ = ["_MrgnCallRsltDtls", "_SgrtdIndpdntAmt", "_MrgnCallAmt"]
	@property
	def MrgnCallRsltDtls(self):
		return self._MrgnCallRsltDtls

	@MrgnCallRsltDtls.setter
	def MrgnCallRsltDtls(self, value):
		self._MrgnCallRsltDtls = value if type(value) != base_types.auto else self.make_default("MrgnCallRsltDtls")

	@MrgnCallRsltDtls.deleter
	def MrgnCallRsltDtls(self):
		del self._MrgnCallRsltDtls
		self._MrgnCallRsltDtls = None

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
	def MrgnCallAmt(self):
		return self._MrgnCallAmt

	@MrgnCallAmt.setter
	def MrgnCallAmt(self, value):
		self._MrgnCallAmt = value if type(value) != base_types.auto else self.make_default("MrgnCallAmt")

	@MrgnCallAmt.deleter
	def MrgnCallAmt(self):
		del self._MrgnCallAmt
		self._MrgnCallAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MrgnCallRsltDtls', type=MarginCallResult2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=Result1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MrgnCallAmt', type=Result1, min=0, max=1, mutex_group=1, array=False),
	))

