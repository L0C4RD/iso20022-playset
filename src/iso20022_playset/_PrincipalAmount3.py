from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class PrincipalAmount3(base_types._BaseFieldType):

	__slots__ = ["_MtrtyDtAmt", "_ValDtAmt"]
	@property
	def MtrtyDtAmt(self):
		return self._MtrtyDtAmt

	@MtrtyDtAmt.setter
	def MtrtyDtAmt(self, value):
		self._MtrtyDtAmt = value if type(value) != base_types.auto else self.make_default("MtrtyDtAmt")

	@MtrtyDtAmt.deleter
	def MtrtyDtAmt(self):
		del self._MtrtyDtAmt
		self._MtrtyDtAmt = None

	@property
	def ValDtAmt(self):
		return self._ValDtAmt

	@ValDtAmt.setter
	def ValDtAmt(self, value):
		self._ValDtAmt = value if type(value) != base_types.auto else self.make_default("ValDtAmt")

	@ValDtAmt.deleter
	def ValDtAmt(self):
		del self._ValDtAmt
		self._ValDtAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtrtyDtAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDtAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

