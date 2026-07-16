# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IndividualPerson43
from . import ProxyType3Code

class Proxy11(base_types._BaseFieldType):

	__slots__ = ["_PrsnDtls", "_PrxyTp"]
	@property
	def PrsnDtls(self):
		return self._PrsnDtls

	@PrsnDtls.setter
	def PrsnDtls(self, value):
		self._PrsnDtls = value if value is not None else base_types.UninitialisedField(self, 'PrsnDtls', IndividualPerson43, False)

	@PrsnDtls.deleter
	def PrsnDtls(self):
		del self._PrsnDtls
		self._PrsnDtls = base_types.UninitialisedField(self, 'PrsnDtls', IndividualPerson43, False)

	@property
	def PrxyTp(self):
		return self._PrxyTp

	@PrxyTp.setter
	def PrxyTp(self, value):
		self._PrxyTp = value if value is not None else base_types.UninitialisedField(self, 'PrxyTp', ProxyType3Code, False)

	@PrxyTp.deleter
	def PrxyTp(self):
		del self._PrxyTp
		self._PrxyTp = base_types.UninitialisedField(self, 'PrxyTp', ProxyType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrsnDtls', type=IndividualPerson43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrxyTp', type=ProxyType3Code, min=1, max=1, mutex_group=None, array=False),
	))