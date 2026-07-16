# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISOTime
from . import PlusOrMinusIndicator

class UTCOffset1(base_types._BaseFieldType):

	__slots__ = ["_NbOfHrs", "_Sgn"]
	@property
	def NbOfHrs(self):
		return self._NbOfHrs

	@NbOfHrs.setter
	def NbOfHrs(self, value):
		self._NbOfHrs = value if value is not None else base_types.UninitialisedField(self, 'NbOfHrs', ISOTime, False)

	@NbOfHrs.deleter
	def NbOfHrs(self):
		del self._NbOfHrs
		self._NbOfHrs = base_types.UninitialisedField(self, 'NbOfHrs', ISOTime, False)

	@property
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if value is not None else base_types.UninitialisedField(self, 'Sgn', PlusOrMinusIndicator, False)

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = base_types.UninitialisedField(self, 'Sgn', PlusOrMinusIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfHrs', type=ISOTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=1, max=1, mutex_group=None, array=False),
	))