# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AmountAndDirection20
from . import Collateral6
from . import MarginResult1Choice

class MarginCalculation1(base_types._BaseFieldType):

	__slots__ = ["_CollOnDpst", "_MinRqrmntDpst", "_MrgnRslt", "_TtlMrgnAmt"]
	@property
	def CollOnDpst(self):
		return self._CollOnDpst

	@CollOnDpst.setter
	def CollOnDpst(self, value):
		self._CollOnDpst = value if value is not None else base_types.UninitialisedField(self, 'CollOnDpst', Collateral6, True)

	@CollOnDpst.deleter
	def CollOnDpst(self):
		del self._CollOnDpst
		self._CollOnDpst = base_types.UninitialisedField(self, 'CollOnDpst', Collateral6, True)

	@property
	def MinRqrmntDpst(self):
		return self._MinRqrmntDpst

	@MinRqrmntDpst.setter
	def MinRqrmntDpst(self, value):
		self._MinRqrmntDpst = value if value is not None else base_types.UninitialisedField(self, 'MinRqrmntDpst', ActiveCurrencyAndAmount, False)

	@MinRqrmntDpst.deleter
	def MinRqrmntDpst(self):
		del self._MinRqrmntDpst
		self._MinRqrmntDpst = base_types.UninitialisedField(self, 'MinRqrmntDpst', ActiveCurrencyAndAmount, False)

	@property
	def MrgnRslt(self):
		return self._MrgnRslt

	@MrgnRslt.setter
	def MrgnRslt(self, value):
		self._MrgnRslt = value if value is not None else base_types.UninitialisedField(self, 'MrgnRslt', MarginResult1Choice, False)

	@MrgnRslt.deleter
	def MrgnRslt(self):
		del self._MrgnRslt
		self._MrgnRslt = base_types.UninitialisedField(self, 'MrgnRslt', MarginResult1Choice, False)

	@property
	def TtlMrgnAmt(self):
		return self._TtlMrgnAmt

	@TtlMrgnAmt.setter
	def TtlMrgnAmt(self, value):
		self._TtlMrgnAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlMrgnAmt', AmountAndDirection20, False)

	@TtlMrgnAmt.deleter
	def TtlMrgnAmt(self):
		del self._TtlMrgnAmt
		self._TtlMrgnAmt = base_types.UninitialisedField(self, 'TtlMrgnAmt', AmountAndDirection20, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollOnDpst', type=Collateral6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MinRqrmntDpst', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRslt', type=MarginResult1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlMrgnAmt', type=AmountAndDirection20, min=1, max=1, mutex_group=None, array=False),
	))