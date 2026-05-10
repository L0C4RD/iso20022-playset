from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class SpecialCondition1(base_types._BaseFieldType):

	__slots__ = ["_IncmgAmtToOthrAcct", "_OutgngAmt", "_PmtFrOthrAcct", "_IncmgAmt"]
	@property
	def IncmgAmtToOthrAcct(self):
		return self._IncmgAmtToOthrAcct

	@IncmgAmtToOthrAcct.setter
	def IncmgAmtToOthrAcct(self, value):
		self._IncmgAmtToOthrAcct = value if type(value) != base_types.auto else self.make_default("IncmgAmtToOthrAcct")

	@IncmgAmtToOthrAcct.deleter
	def IncmgAmtToOthrAcct(self):
		del self._IncmgAmtToOthrAcct
		self._IncmgAmtToOthrAcct = None

	@property
	def OutgngAmt(self):
		return self._OutgngAmt

	@OutgngAmt.setter
	def OutgngAmt(self, value):
		self._OutgngAmt = value if type(value) != base_types.auto else self.make_default("OutgngAmt")

	@OutgngAmt.deleter
	def OutgngAmt(self):
		del self._OutgngAmt
		self._OutgngAmt = None

	@property
	def PmtFrOthrAcct(self):
		return self._PmtFrOthrAcct

	@PmtFrOthrAcct.setter
	def PmtFrOthrAcct(self, value):
		self._PmtFrOthrAcct = value if type(value) != base_types.auto else self.make_default("PmtFrOthrAcct")

	@PmtFrOthrAcct.deleter
	def PmtFrOthrAcct(self):
		del self._PmtFrOthrAcct
		self._PmtFrOthrAcct = None

	@property
	def IncmgAmt(self):
		return self._IncmgAmt

	@IncmgAmt.setter
	def IncmgAmt(self, value):
		self._IncmgAmt = value if type(value) != base_types.auto else self.make_default("IncmgAmt")

	@IncmgAmt.deleter
	def IncmgAmt(self):
		del self._IncmgAmt
		self._IncmgAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IncmgAmtToOthrAcct', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutgngAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrOthrAcct', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmgAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

