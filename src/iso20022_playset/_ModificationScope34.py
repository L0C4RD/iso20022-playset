# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DataModification1Code import DataModification1Code
from ._PostalAddress21 import PostalAddress21

class ModificationScope34(base_types._BaseFieldType):

	__slots__ = ["_ModScpIndctn", "_PstlAdr"]
	@property
	def ModScpIndctn(self):
		return self._ModScpIndctn

	@ModScpIndctn.setter
	def ModScpIndctn(self, value):
		self._ModScpIndctn = value if type(value) != base_types.auto else self.make_default("ModScpIndctn")

	@ModScpIndctn.deleter
	def ModScpIndctn(self):
		del self._ModScpIndctn
		self._ModScpIndctn = None

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if type(value) != base_types.auto else self.make_default("PstlAdr")

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress21, min=1, max=1, mutex_group=None, array=False),
	))