# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CalculationBasis2Choice
from . import ChargeType11Choice
from . import PriceRateOrAmount3Choice

class Charge33(base_types._BaseFieldType):

	__slots__ = ["_ChrgsFees", "_ClctnBsis", "_Tp"]
	@property
	def ChrgsFees(self):
		return self._ChrgsFees

	@ChrgsFees.setter
	def ChrgsFees(self, value):
		self._ChrgsFees = value if value is not None else base_types.UninitialisedField(self, 'ChrgsFees', PriceRateOrAmount3Choice, False)

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = base_types.UninitialisedField(self, 'ChrgsFees', PriceRateOrAmount3Choice, False)

	@property
	def ClctnBsis(self):
		return self._ClctnBsis

	@ClctnBsis.setter
	def ClctnBsis(self, value):
		self._ClctnBsis = value if value is not None else base_types.UninitialisedField(self, 'ClctnBsis', CalculationBasis2Choice, False)

	@ClctnBsis.deleter
	def ClctnBsis(self):
		del self._ClctnBsis
		self._ClctnBsis = base_types.UninitialisedField(self, 'ClctnBsis', CalculationBasis2Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ChargeType11Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ChargeType11Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgsFees', type=PriceRateOrAmount3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnBsis', type=CalculationBasis2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType11Choice, min=1, max=1, mutex_group=None, array=False),
	))