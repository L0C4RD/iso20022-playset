from . import base_types
from ._AmountAndDirection21 import AmountAndDirection21
from ._Collateral3 import Collateral3
from ._DefaultFund1 import DefaultFund1

class DefaultFundReport1(base_types._BaseFieldType):

	__slots__ = ["_CollDesc", "_DfltFndClctn", "_NetXcssOrDfcit"]
	@property
	def CollDesc(self):
		return self._CollDesc

	@CollDesc.setter
	def CollDesc(self, value):
		self._CollDesc = value if type(value) != base_types.auto else self.make_default("CollDesc")

	@CollDesc.deleter
	def CollDesc(self):
		del self._CollDesc
		self._CollDesc = None

	@property
	def DfltFndClctn(self):
		return self._DfltFndClctn

	@DfltFndClctn.setter
	def DfltFndClctn(self, value):
		self._DfltFndClctn = value if type(value) != base_types.auto else self.make_default("DfltFndClctn")

	@DfltFndClctn.deleter
	def DfltFndClctn(self):
		del self._DfltFndClctn
		self._DfltFndClctn = None

	@property
	def NetXcssOrDfcit(self):
		return self._NetXcssOrDfcit

	@NetXcssOrDfcit.setter
	def NetXcssOrDfcit(self, value):
		self._NetXcssOrDfcit = value if type(value) != base_types.auto else self.make_default("NetXcssOrDfcit")

	@NetXcssOrDfcit.deleter
	def NetXcssOrDfcit(self):
		del self._NetXcssOrDfcit
		self._NetXcssOrDfcit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollDesc', type=Collateral3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltFndClctn', type=DefaultFund1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetXcssOrDfcit', type=AmountAndDirection21, min=1, max=1, mutex_group=None, array=False),
	))

