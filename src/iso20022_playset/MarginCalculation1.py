from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .Collateral6 import Collateral6
from .AmountAndDirection20 import AmountAndDirection20
from .MarginResult1Choice import MarginResult1Choice

class MarginCalculation1(base_types._BaseFieldType):

	__slots__ = ["_MrgnRslt", "_TtlMrgnAmt", "_MinRqrmntDpst", "_CollOnDpst"]
	@property
	def MrgnRslt(self):
		return self._MrgnRslt

	@MrgnRslt.setter
	def MrgnRslt(self, value):
		self._MrgnRslt = value if type(value) != base_types.auto else self.make_default("MrgnRslt")

	@MrgnRslt.deleter
	def MrgnRslt(self):
		del self._MrgnRslt
		self._MrgnRslt = None

	@property
	def TtlMrgnAmt(self):
		return self._TtlMrgnAmt

	@TtlMrgnAmt.setter
	def TtlMrgnAmt(self, value):
		self._TtlMrgnAmt = value if type(value) != base_types.auto else self.make_default("TtlMrgnAmt")

	@TtlMrgnAmt.deleter
	def TtlMrgnAmt(self):
		del self._TtlMrgnAmt
		self._TtlMrgnAmt = None

	@property
	def MinRqrmntDpst(self):
		return self._MinRqrmntDpst

	@MinRqrmntDpst.setter
	def MinRqrmntDpst(self, value):
		self._MinRqrmntDpst = value if type(value) != base_types.auto else self.make_default("MinRqrmntDpst")

	@MinRqrmntDpst.deleter
	def MinRqrmntDpst(self):
		del self._MinRqrmntDpst
		self._MinRqrmntDpst = None

	@property
	def CollOnDpst(self):
		return self._CollOnDpst

	@CollOnDpst.setter
	def CollOnDpst(self, value):
		self._CollOnDpst = value if type(value) != base_types.auto else self.make_default("CollOnDpst")

	@CollOnDpst.deleter
	def CollOnDpst(self):
		del self._CollOnDpst
		self._CollOnDpst = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MrgnRslt', type=MarginResult1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlMrgnAmt', type=AmountAndDirection20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinRqrmntDpst', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollOnDpst', type=Collateral6, min=0, max=None, mutex_group=None, array=True),
	))

