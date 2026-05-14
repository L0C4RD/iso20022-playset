# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DataModification1Code import DataModification1Code
from ._Intermediary46 import Intermediary46

class ModificationScope40(base_types._BaseFieldType):

	__slots__ = ["_Intrmy", "_ModScpIndctn"]
	@property
	def Intrmy(self):
		return self._Intrmy

	@Intrmy.setter
	def Intrmy(self, value):
		self._Intrmy = value if type(value) != base_types.auto else self.make_default("Intrmy")

	@Intrmy.deleter
	def Intrmy(self):
		del self._Intrmy
		self._Intrmy = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Intrmy', type=Intermediary46, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
	))