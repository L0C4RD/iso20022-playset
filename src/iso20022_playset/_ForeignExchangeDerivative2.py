# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AssetClassSubProductType19Code

class ForeignExchangeDerivative2(base_types._BaseFieldType):

	__slots__ = ["_CtrctSubTp"]
	@property
	def CtrctSubTp(self):
		return self._CtrctSubTp

	@CtrctSubTp.setter
	def CtrctSubTp(self, value):
		self._CtrctSubTp = value if value is not None else base_types.UninitialisedField(self, 'CtrctSubTp', AssetClassSubProductType19Code, False)

	@CtrctSubTp.deleter
	def CtrctSubTp(self):
		del self._CtrctSubTp
		self._CtrctSubTp = base_types.UninitialisedField(self, 'CtrctSubTp', AssetClassSubProductType19Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctSubTp', type=AssetClassSubProductType19Code, min=1, max=1, mutex_group=None, array=False),
	))