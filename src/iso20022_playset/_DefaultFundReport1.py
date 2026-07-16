# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection21
from . import Collateral3
from . import DefaultFund1

class DefaultFundReport1(base_types._BaseFieldType):

	__slots__ = ["_CollDesc", "_DfltFndClctn", "_NetXcssOrDfcit"]
	@property
	def CollDesc(self):
		return self._CollDesc

	@CollDesc.setter
	def CollDesc(self, value):
		self._CollDesc = value if value is not None else base_types.UninitialisedField(self, 'CollDesc', Collateral3, True)

	@CollDesc.deleter
	def CollDesc(self):
		del self._CollDesc
		self._CollDesc = base_types.UninitialisedField(self, 'CollDesc', Collateral3, True)

	@property
	def DfltFndClctn(self):
		return self._DfltFndClctn

	@DfltFndClctn.setter
	def DfltFndClctn(self, value):
		self._DfltFndClctn = value if value is not None else base_types.UninitialisedField(self, 'DfltFndClctn', DefaultFund1, True)

	@DfltFndClctn.deleter
	def DfltFndClctn(self):
		del self._DfltFndClctn
		self._DfltFndClctn = base_types.UninitialisedField(self, 'DfltFndClctn', DefaultFund1, True)

	@property
	def NetXcssOrDfcit(self):
		return self._NetXcssOrDfcit

	@NetXcssOrDfcit.setter
	def NetXcssOrDfcit(self, value):
		self._NetXcssOrDfcit = value if value is not None else base_types.UninitialisedField(self, 'NetXcssOrDfcit', AmountAndDirection21, False)

	@NetXcssOrDfcit.deleter
	def NetXcssOrDfcit(self):
		del self._NetXcssOrDfcit
		self._NetXcssOrDfcit = base_types.UninitialisedField(self, 'NetXcssOrDfcit', AmountAndDirection21, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollDesc', type=Collateral3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltFndClctn', type=DefaultFund1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetXcssOrDfcit', type=AmountAndDirection21, min=1, max=1, mutex_group=None, array=False),
	))