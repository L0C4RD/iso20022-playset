# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionOption1FormatChoice
from . import Exact3NumericText
from . import UnitOrFaceAmount1Choice

class CorporateActionElection1(base_types._BaseFieldType):

	__slots__ = ["_OptnNb", "_OptnTp", "_OrgnlInstdQty", "_RmngQty"]
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
	def OrgnlInstdQty(self):
		return self._OrgnlInstdQty

	@OrgnlInstdQty.setter
	def OrgnlInstdQty(self, value):
		self._OrgnlInstdQty = value if value is not None else base_types.UninitialisedField(self, 'OrgnlInstdQty', UnitOrFaceAmount1Choice, False)

	@OrgnlInstdQty.deleter
	def OrgnlInstdQty(self):
		del self._OrgnlInstdQty
		self._OrgnlInstdQty = base_types.UninitialisedField(self, 'OrgnlInstdQty', UnitOrFaceAmount1Choice, False)

	@property
	def RmngQty(self):
		return self._RmngQty

	@RmngQty.setter
	def RmngQty(self, value):
		self._RmngQty = value if value is not None else base_types.UninitialisedField(self, 'RmngQty', UnitOrFaceAmount1Choice, False)

	@RmngQty.deleter
	def RmngQty(self):
		del self._RmngQty
		self._RmngQty = base_types.UninitialisedField(self, 'RmngQty', UnitOrFaceAmount1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstdQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
	))