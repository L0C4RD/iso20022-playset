# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceValueType1Code
from . import YesNoIndicator

class YieldedOrValueType1Choice(base_types._BaseFieldType):

	__slots__ = ["_ValTp", "_Yldd"]
	@property
	def ValTp(self):
		return self._ValTp

	@ValTp.setter
	def ValTp(self, value):
		self._ValTp = value if value is not None else base_types.UninitialisedField(self, 'ValTp', PriceValueType1Code, False)

	@ValTp.deleter
	def ValTp(self):
		del self._ValTp
		self._ValTp = base_types.UninitialisedField(self, 'ValTp', PriceValueType1Code, False)

	@property
	def Yldd(self):
		return self._Yldd

	@Yldd.setter
	def Yldd(self, value):
		self._Yldd = value if value is not None else base_types.UninitialisedField(self, 'Yldd', YesNoIndicator, False)

	@Yldd.deleter
	def Yldd(self):
		del self._Yldd
		self._Yldd = base_types.UninitialisedField(self, 'Yldd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValTp', type=PriceValueType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Yldd', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
	))