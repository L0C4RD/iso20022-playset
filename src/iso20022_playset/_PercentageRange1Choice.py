# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FromToPercentageRange1
from . import PercentageRangeBoundary1
from . import PercentageRate

class PercentageRange1Choice(base_types._BaseFieldType):

	__slots__ = ["_EQ", "_Fr", "_FrTo", "_NEQ", "_To"]
	@property
	def EQ(self):
		return self._EQ

	@EQ.setter
	def EQ(self, value):
		self._EQ = value if value is not None else base_types.UninitialisedField(self, 'EQ', PercentageRate, False)

	@EQ.deleter
	def EQ(self):
		del self._EQ
		self._EQ = base_types.UninitialisedField(self, 'EQ', PercentageRate, False)

	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if value is not None else base_types.UninitialisedField(self, 'Fr', PercentageRangeBoundary1, False)

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = base_types.UninitialisedField(self, 'Fr', PercentageRangeBoundary1, False)

	@property
	def FrTo(self):
		return self._FrTo

	@FrTo.setter
	def FrTo(self, value):
		self._FrTo = value if value is not None else base_types.UninitialisedField(self, 'FrTo', FromToPercentageRange1, False)

	@FrTo.deleter
	def FrTo(self):
		del self._FrTo
		self._FrTo = base_types.UninitialisedField(self, 'FrTo', FromToPercentageRange1, False)

	@property
	def NEQ(self):
		return self._NEQ

	@NEQ.setter
	def NEQ(self, value):
		self._NEQ = value if value is not None else base_types.UninitialisedField(self, 'NEQ', PercentageRate, False)

	@NEQ.deleter
	def NEQ(self):
		del self._NEQ
		self._NEQ = base_types.UninitialisedField(self, 'NEQ', PercentageRate, False)

	@property
	def To(self):
		return self._To

	@To.setter
	def To(self, value):
		self._To = value if value is not None else base_types.UninitialisedField(self, 'To', PercentageRangeBoundary1, False)

	@To.deleter
	def To(self):
		del self._To
		self._To = base_types.UninitialisedField(self, 'To', PercentageRangeBoundary1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EQ', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Fr', type=PercentageRangeBoundary1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrTo', type=FromToPercentageRange1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NEQ', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='To', type=PercentageRangeBoundary1, min=0, max=1, mutex_group=1, array=False),
	))