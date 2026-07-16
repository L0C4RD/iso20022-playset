# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import YesNoIndicator

class QuantityRangeBoundary1(base_types._BaseFieldType):

	__slots__ = ["_Bdry", "_Incl"]
	@property
	def Bdry(self):
		return self._Bdry

	@Bdry.setter
	def Bdry(self, value):
		self._Bdry = value if value is not None else base_types.UninitialisedField(self, 'Bdry', DecimalNumber, False)

	@Bdry.deleter
	def Bdry(self):
		del self._Bdry
		self._Bdry = base_types.UninitialisedField(self, 'Bdry', DecimalNumber, False)

	@property
	def Incl(self):
		return self._Incl

	@Incl.setter
	def Incl(self, value):
		self._Incl = value if value is not None else base_types.UninitialisedField(self, 'Incl', YesNoIndicator, False)

	@Incl.deleter
	def Incl(self):
		del self._Incl
		self._Incl = base_types.UninitialisedField(self, 'Incl', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bdry', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incl', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))