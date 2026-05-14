# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MarginRequirement1 import MarginRequirement1

class Requirement1(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmtRqrmnt", "_VartnMrgnRqrmnt"]
	@property
	def SgrtdIndpdntAmtRqrmnt(self):
		return self._SgrtdIndpdntAmtRqrmnt

	@SgrtdIndpdntAmtRqrmnt.setter
	def SgrtdIndpdntAmtRqrmnt(self, value):
		self._SgrtdIndpdntAmtRqrmnt = value if type(value) != base_types.auto else self.make_default("SgrtdIndpdntAmtRqrmnt")

	@SgrtdIndpdntAmtRqrmnt.deleter
	def SgrtdIndpdntAmtRqrmnt(self):
		del self._SgrtdIndpdntAmtRqrmnt
		self._SgrtdIndpdntAmtRqrmnt = None

	@property
	def VartnMrgnRqrmnt(self):
		return self._VartnMrgnRqrmnt

	@VartnMrgnRqrmnt.setter
	def VartnMrgnRqrmnt(self, value):
		self._VartnMrgnRqrmnt = value if type(value) != base_types.auto else self.make_default("VartnMrgnRqrmnt")

	@VartnMrgnRqrmnt.deleter
	def VartnMrgnRqrmnt(self):
		del self._VartnMrgnRqrmnt
		self._VartnMrgnRqrmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmtRqrmnt', type=MarginRequirement1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRqrmnt', type=MarginRequirement1, min=1, max=1, mutex_group=None, array=False),
	))