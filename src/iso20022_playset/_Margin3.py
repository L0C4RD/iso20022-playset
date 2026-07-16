# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount2
from . import Margin4
from . import VariationMargin3

class Margin3(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgn", "_OthrMrgn", "_VartnMrgn"]
	@property
	def InitlMrgn(self):
		return self._InitlMrgn

	@InitlMrgn.setter
	def InitlMrgn(self, value):
		self._InitlMrgn = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgn', Amount2, False)

	@InitlMrgn.deleter
	def InitlMrgn(self):
		del self._InitlMrgn
		self._InitlMrgn = base_types.UninitialisedField(self, 'InitlMrgn', Amount2, False)

	@property
	def OthrMrgn(self):
		return self._OthrMrgn

	@OthrMrgn.setter
	def OthrMrgn(self, value):
		self._OthrMrgn = value if value is not None else base_types.UninitialisedField(self, 'OthrMrgn', Margin4, True)

	@OthrMrgn.deleter
	def OthrMrgn(self):
		del self._OthrMrgn
		self._OthrMrgn = base_types.UninitialisedField(self, 'OthrMrgn', Margin4, True)

	@property
	def VartnMrgn(self):
		return self._VartnMrgn

	@VartnMrgn.setter
	def VartnMrgn(self, value):
		self._VartnMrgn = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgn', VariationMargin3, True)

	@VartnMrgn.deleter
	def VartnMrgn(self):
		del self._VartnMrgn
		self._VartnMrgn = base_types.UninitialisedField(self, 'VartnMrgn', VariationMargin3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgn', type=Amount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrMrgn', type=Margin4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VartnMrgn', type=VariationMargin3, min=0, max=None, mutex_group=None, array=True),
	))