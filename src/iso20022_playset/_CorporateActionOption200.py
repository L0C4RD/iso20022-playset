# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionOption40Choice
from . import OptionNumber1Choice
from . import Quantity52Choice

class CorporateActionOption200(base_types._BaseFieldType):

	__slots__ = ["_InstdQty", "_OptnNb", "_OptnTp"]
	@property
	def InstdQty(self):
		return self._InstdQty

	@InstdQty.setter
	def InstdQty(self, value):
		self._InstdQty = value if value is not None else base_types.UninitialisedField(self, 'InstdQty', Quantity52Choice, False)

	@InstdQty.deleter
	def InstdQty(self):
		del self._InstdQty
		self._InstdQty = base_types.UninitialisedField(self, 'InstdQty', Quantity52Choice, False)

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if value is not None else base_types.UninitialisedField(self, 'OptnNb', OptionNumber1Choice, False)

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = base_types.UninitialisedField(self, 'OptnNb', OptionNumber1Choice, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption40Choice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption40Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstdQty', type=Quantity52Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=OptionNumber1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption40Choice, min=1, max=1, mutex_group=None, array=False),
	))