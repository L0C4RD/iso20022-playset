# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountPrice4
from . import PriceValueType10Code

class PriceFormat58Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtPric", "_NotSpcfdPric"]
	@property
	def AmtPric(self):
		return self._AmtPric

	@AmtPric.setter
	def AmtPric(self, value):
		self._AmtPric = value if value is not None else base_types.UninitialisedField(self, 'AmtPric', AmountPrice4, False)

	@AmtPric.deleter
	def AmtPric(self):
		del self._AmtPric
		self._AmtPric = base_types.UninitialisedField(self, 'AmtPric', AmountPrice4, False)

	@property
	def NotSpcfdPric(self):
		return self._NotSpcfdPric

	@NotSpcfdPric.setter
	def NotSpcfdPric(self, value):
		self._NotSpcfdPric = value if value is not None else base_types.UninitialisedField(self, 'NotSpcfdPric', PriceValueType10Code, False)

	@NotSpcfdPric.deleter
	def NotSpcfdPric(self):
		del self._NotSpcfdPric
		self._NotSpcfdPric = base_types.UninitialisedField(self, 'NotSpcfdPric', PriceValueType10Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtPric', type=AmountPrice4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdPric', type=PriceValueType10Code, min=0, max=1, mutex_group=1, array=False),
	))