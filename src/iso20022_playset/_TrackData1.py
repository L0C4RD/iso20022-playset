# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact1NumericText
from . import Max140Text

class TrackData1(base_types._BaseFieldType):

	__slots__ = ["_TrckNb", "_TrckVal"]
	@property
	def TrckNb(self):
		return self._TrckNb

	@TrckNb.setter
	def TrckNb(self, value):
		self._TrckNb = value if value is not None else base_types.UninitialisedField(self, 'TrckNb', Exact1NumericText, False)

	@TrckNb.deleter
	def TrckNb(self):
		del self._TrckNb
		self._TrckNb = base_types.UninitialisedField(self, 'TrckNb', Exact1NumericText, False)

	@property
	def TrckVal(self):
		return self._TrckVal

	@TrckVal.setter
	def TrckVal(self, value):
		self._TrckVal = value if value is not None else base_types.UninitialisedField(self, 'TrckVal', Max140Text, False)

	@TrckVal.deleter
	def TrckVal(self):
		del self._TrckVal
		self._TrckVal = base_types.UninitialisedField(self, 'TrckVal', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrckNb', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckVal', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))