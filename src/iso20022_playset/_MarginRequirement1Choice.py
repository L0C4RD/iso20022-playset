# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarginRequirement1
from . import Requirement1

class MarginRequirement1Choice(base_types._BaseFieldType):

	__slots__ = ["_MrgnRqrmnt", "_SgrtdIndpdntAmtRqrmnt"]
	@property
	def MrgnRqrmnt(self):
		return self._MrgnRqrmnt

	@MrgnRqrmnt.setter
	def MrgnRqrmnt(self, value):
		self._MrgnRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'MrgnRqrmnt', Requirement1, False)

	@MrgnRqrmnt.deleter
	def MrgnRqrmnt(self):
		del self._MrgnRqrmnt
		self._MrgnRqrmnt = base_types.UninitialisedField(self, 'MrgnRqrmnt', Requirement1, False)

	@property
	def SgrtdIndpdntAmtRqrmnt(self):
		return self._SgrtdIndpdntAmtRqrmnt

	@SgrtdIndpdntAmtRqrmnt.setter
	def SgrtdIndpdntAmtRqrmnt(self, value):
		self._SgrtdIndpdntAmtRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'SgrtdIndpdntAmtRqrmnt', MarginRequirement1, False)

	@SgrtdIndpdntAmtRqrmnt.deleter
	def SgrtdIndpdntAmtRqrmnt(self):
		del self._SgrtdIndpdntAmtRqrmnt
		self._SgrtdIndpdntAmtRqrmnt = base_types.UninitialisedField(self, 'SgrtdIndpdntAmtRqrmnt', MarginRequirement1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MrgnRqrmnt', type=Requirement1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmtRqrmnt', type=MarginRequirement1, min=0, max=1, mutex_group=1, array=False),
	))