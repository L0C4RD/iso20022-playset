from . import base_types
from ._FundType2Code import FundType2Code
from ._FinancialPartySectorType2Code import FinancialPartySectorType2Code

class FinancialPartyClassification1(base_types._BaseFieldType):

	__slots__ = ["_Clssfctn", "_InvstmtFndClssfctn"]
	@property
	def Clssfctn(self):
		return self._Clssfctn

	@Clssfctn.setter
	def Clssfctn(self, value):
		self._Clssfctn = value if type(value) != base_types.auto else self.make_default("Clssfctn")

	@Clssfctn.deleter
	def Clssfctn(self):
		del self._Clssfctn
		self._Clssfctn = None

	@property
	def InvstmtFndClssfctn(self):
		return self._InvstmtFndClssfctn

	@InvstmtFndClssfctn.setter
	def InvstmtFndClssfctn(self, value):
		self._InvstmtFndClssfctn = value if type(value) != base_types.auto else self.make_default("InvstmtFndClssfctn")

	@InvstmtFndClssfctn.deleter
	def InvstmtFndClssfctn(self):
		del self._InvstmtFndClssfctn
		self._InvstmtFndClssfctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clssfctn', type=FinancialPartySectorType2Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtFndClssfctn', type=FundType2Code, min=0, max=1, mutex_group=None, array=False),
	))

