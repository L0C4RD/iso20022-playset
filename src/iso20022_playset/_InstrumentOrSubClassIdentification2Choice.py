# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AssetClassAndSubClassIdentification2
from . import InstrumentAndSubClassIdentification2

class InstrumentOrSubClassIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_AsstClssAndSubClss", "_ISINAndSubClss"]
	@property
	def AsstClssAndSubClss(self):
		return self._AsstClssAndSubClss

	@AsstClssAndSubClss.setter
	def AsstClssAndSubClss(self, value):
		self._AsstClssAndSubClss = value if value is not None else base_types.UninitialisedField(self, 'AsstClssAndSubClss', AssetClassAndSubClassIdentification2, False)

	@AsstClssAndSubClss.deleter
	def AsstClssAndSubClss(self):
		del self._AsstClssAndSubClss
		self._AsstClssAndSubClss = base_types.UninitialisedField(self, 'AsstClssAndSubClss', AssetClassAndSubClassIdentification2, False)

	@property
	def ISINAndSubClss(self):
		return self._ISINAndSubClss

	@ISINAndSubClss.setter
	def ISINAndSubClss(self, value):
		self._ISINAndSubClss = value if value is not None else base_types.UninitialisedField(self, 'ISINAndSubClss', InstrumentAndSubClassIdentification2, False)

	@ISINAndSubClss.deleter
	def ISINAndSubClss(self):
		del self._ISINAndSubClss
		self._ISINAndSubClss = base_types.UninitialisedField(self, 'ISINAndSubClss', InstrumentAndSubClassIdentification2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstClssAndSubClss', type=AssetClassAndSubClassIdentification2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ISINAndSubClss', type=InstrumentAndSubClassIdentification2, min=0, max=1, mutex_group=1, array=False),
	))