import base_types
import Amount1
import AgreedAmount1

class AgreedAmount1Choice(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmt", "_AgrdAmtDtls"]
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

	@property
	def AgrdAmtDtls(self):
		return self._AgrdAmtDtls

	@AgrdAmtDtls.setter
	def AgrdAmtDtls(self, value):
		self._AgrdAmtDtls = value if type(value) != auto else self.make_default("AgrdAmtDtls")

	@AgrdAmtDtls.deleter
	def AgrdAmtDtls(self):
		del self._AgrdAmtDtls
		self._AgrdAmtDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=Amount1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgrdAmtDtls', type=AgreedAmount1, min=0, max=1, mutex_group=1, array=False),
	))

