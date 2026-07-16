# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DerivativeClassification1
from . import DerivativeUnderlyingLeg1
from . import Option14

class Derivative3(base_types._BaseFieldType):

	__slots__ = ["_DerivClssfctn", "_DerivUndrlygLeg", "_OptnAttrbts"]
	@property
	def DerivClssfctn(self):
		return self._DerivClssfctn

	@DerivClssfctn.setter
	def DerivClssfctn(self, value):
		self._DerivClssfctn = value if value is not None else base_types.UninitialisedField(self, 'DerivClssfctn', DerivativeClassification1, False)

	@DerivClssfctn.deleter
	def DerivClssfctn(self):
		del self._DerivClssfctn
		self._DerivClssfctn = base_types.UninitialisedField(self, 'DerivClssfctn', DerivativeClassification1, False)

	@property
	def DerivUndrlygLeg(self):
		return self._DerivUndrlygLeg

	@DerivUndrlygLeg.setter
	def DerivUndrlygLeg(self, value):
		self._DerivUndrlygLeg = value if value is not None else base_types.UninitialisedField(self, 'DerivUndrlygLeg', DerivativeUnderlyingLeg1, False)

	@DerivUndrlygLeg.deleter
	def DerivUndrlygLeg(self):
		del self._DerivUndrlygLeg
		self._DerivUndrlygLeg = base_types.UninitialisedField(self, 'DerivUndrlygLeg', DerivativeUnderlyingLeg1, False)

	@property
	def OptnAttrbts(self):
		return self._OptnAttrbts

	@OptnAttrbts.setter
	def OptnAttrbts(self, value):
		self._OptnAttrbts = value if value is not None else base_types.UninitialisedField(self, 'OptnAttrbts', Option14, False)

	@OptnAttrbts.deleter
	def OptnAttrbts(self):
		del self._OptnAttrbts
		self._OptnAttrbts = base_types.UninitialisedField(self, 'OptnAttrbts', Option14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DerivClssfctn', type=DerivativeClassification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivUndrlygLeg', type=DerivativeUnderlyingLeg1, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnAttrbts', type=Option14, min=0, max=1, mutex_group=None, array=False),
	))