# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SpecialPurpose2Code
from . import TimeToMaturityPeriod2

class TimeToMaturity2Choice(base_types._BaseFieldType):

	__slots__ = ["_Prd", "_Spcl"]
	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', TimeToMaturityPeriod2, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', TimeToMaturityPeriod2, False)

	@property
	def Spcl(self):
		return self._Spcl

	@Spcl.setter
	def Spcl(self, value):
		self._Spcl = value if value is not None else base_types.UninitialisedField(self, 'Spcl', SpecialPurpose2Code, False)

	@Spcl.deleter
	def Spcl(self):
		del self._Spcl
		self._Spcl = base_types.UninitialisedField(self, 'Spcl', SpecialPurpose2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prd', type=TimeToMaturityPeriod2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Spcl', type=SpecialPurpose2Code, min=0, max=1, mutex_group=1, array=False),
	))