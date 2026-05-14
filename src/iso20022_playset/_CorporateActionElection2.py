# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionOption1FormatChoice import CorporateActionOption1FormatChoice
from ._Exact3NumericText import Exact3NumericText
from ._Max350Text import Max350Text
from ._UnitOrFaceAmount1Choice import UnitOrFaceAmount1Choice

class CorporateActionElection2(base_types._BaseFieldType):

	__slots__ = ["_NewInstdQty", "_OptnNb", "_OptnTp", "_Rsn"]
	@property
	def NewInstdQty(self):
		return self._NewInstdQty

	@NewInstdQty.setter
	def NewInstdQty(self, value):
		self._NewInstdQty = value if type(value) != base_types.auto else self.make_default("NewInstdQty")

	@NewInstdQty.deleter
	def NewInstdQty(self):
		del self._NewInstdQty
		self._NewInstdQty = None

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

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewInstdQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))