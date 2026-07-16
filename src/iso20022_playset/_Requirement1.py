# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarginRequirement1

class Requirement1(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmtRqrmnt", "_VartnMrgnRqrmnt"]
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

	@property
	def VartnMrgnRqrmnt(self):
		return self._VartnMrgnRqrmnt

	@VartnMrgnRqrmnt.setter
	def VartnMrgnRqrmnt(self, value):
		self._VartnMrgnRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnRqrmnt', MarginRequirement1, False)

	@VartnMrgnRqrmnt.deleter
	def VartnMrgnRqrmnt(self):
		del self._VartnMrgnRqrmnt
		self._VartnMrgnRqrmnt = base_types.UninitialisedField(self, 'VartnMrgnRqrmnt', MarginRequirement1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmtRqrmnt', type=MarginRequirement1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRqrmnt', type=MarginRequirement1, min=1, max=1, mutex_group=None, array=False),
	))