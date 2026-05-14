# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionOption43Choice import CorporateActionOption43Choice
from ._OptionNumber1Choice import OptionNumber1Choice
from ._Quantity55Choice import Quantity55Choice

class CorporateActionOption202(base_types._BaseFieldType):

	__slots__ = ["_InstdQty", "_OptnNb", "_OptnTp"]
	@property
	def InstdQty(self):
		return self._InstdQty

	@InstdQty.setter
	def InstdQty(self, value):
		self._InstdQty = value if type(value) != base_types.auto else self.make_default("InstdQty")

	@InstdQty.deleter
	def InstdQty(self):
		del self._InstdQty
		self._InstdQty = None

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != base_types.auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstdQty', type=Quantity55Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=OptionNumber1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption43Choice, min=1, max=1, mutex_group=None, array=False),
	))