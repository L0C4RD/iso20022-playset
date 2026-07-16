# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionOption1FormatChoice
from . import Exact3NumericText
from . import Max350Text
from . import UnitOrFaceAmount1Choice

class CorporateActionElection2(base_types._BaseFieldType):

	__slots__ = ["_NewInstdQty", "_OptnNb", "_OptnTp", "_Rsn"]
	@property
	def NewInstdQty(self):
		return self._NewInstdQty

	@NewInstdQty.setter
	def NewInstdQty(self, value):
		self._NewInstdQty = value if value is not None else base_types.UninitialisedField(self, 'NewInstdQty', UnitOrFaceAmount1Choice, False)

	@NewInstdQty.deleter
	def NewInstdQty(self):
		del self._NewInstdQty
		self._NewInstdQty = base_types.UninitialisedField(self, 'NewInstdQty', UnitOrFaceAmount1Choice, False)

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if value is not None else base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption1FormatChoice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption1FormatChoice, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', Max350Text, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewInstdQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))