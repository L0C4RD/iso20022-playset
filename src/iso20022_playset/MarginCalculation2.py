from . import base_types
from .MarginResult1Choice import MarginResult1Choice
from .SecurityIdentification14 import SecurityIdentification14
from .Margin3 import Margin3
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .Collateral6 import Collateral6
from .Amount2 import Amount2
from .AmountAndDirection20 import AmountAndDirection20

class MarginCalculation2(base_types._BaseFieldType):

	__slots__ = ["_CollOnDpst", "_FinInstrmId", "_XpsrAmt", "_TtlMrgnAmt", "_MinRqrmntDpst", "_MrgnTpAmt", "_MrgnRslt"]
	@property
	def CollOnDpst(self):
		return self._CollOnDpst

	@CollOnDpst.setter
	def CollOnDpst(self, value):
		self._CollOnDpst = value if type(value) != auto else self.make_default("CollOnDpst")

	@CollOnDpst.deleter
	def CollOnDpst(self):
		del self._CollOnDpst
		self._CollOnDpst = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def XpsrAmt(self):
		return self._XpsrAmt

	@XpsrAmt.setter
	def XpsrAmt(self, value):
		self._XpsrAmt = value if type(value) != auto else self.make_default("XpsrAmt")

	@XpsrAmt.deleter
	def XpsrAmt(self):
		del self._XpsrAmt
		self._XpsrAmt = None

	@property
	def TtlMrgnAmt(self):
		return self._TtlMrgnAmt

	@TtlMrgnAmt.setter
	def TtlMrgnAmt(self, value):
		self._TtlMrgnAmt = value if type(value) != auto else self.make_default("TtlMrgnAmt")

	@TtlMrgnAmt.deleter
	def TtlMrgnAmt(self):
		del self._TtlMrgnAmt
		self._TtlMrgnAmt = None

	@property
	def MinRqrmntDpst(self):
		return self._MinRqrmntDpst

	@MinRqrmntDpst.setter
	def MinRqrmntDpst(self, value):
		self._MinRqrmntDpst = value if type(value) != auto else self.make_default("MinRqrmntDpst")

	@MinRqrmntDpst.deleter
	def MinRqrmntDpst(self):
		del self._MinRqrmntDpst
		self._MinRqrmntDpst = None

	@property
	def MrgnTpAmt(self):
		return self._MrgnTpAmt

	@MrgnTpAmt.setter
	def MrgnTpAmt(self, value):
		self._MrgnTpAmt = value if type(value) != auto else self.make_default("MrgnTpAmt")

	@MrgnTpAmt.deleter
	def MrgnTpAmt(self):
		del self._MrgnTpAmt
		self._MrgnTpAmt = None

	@property
	def MrgnRslt(self):
		return self._MrgnRslt

	@MrgnRslt.setter
	def MrgnRslt(self, value):
		self._MrgnRslt = value if type(value) != auto else self.make_default("MrgnRslt")

	@MrgnRslt.deleter
	def MrgnRslt(self):
		del self._MrgnRslt
		self._MrgnRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollOnDpst', type=Collateral6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrAmt', type=Amount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlMrgnAmt', type=AmountAndDirection20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinRqrmntDpst', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnTpAmt', type=Margin3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRslt', type=MarginResult1Choice, min=0, max=1, mutex_group=None, array=False),
	))

