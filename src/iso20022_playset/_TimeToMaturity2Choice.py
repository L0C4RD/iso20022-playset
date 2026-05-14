# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SpecialPurpose2Code import SpecialPurpose2Code
from ._TimeToMaturityPeriod2 import TimeToMaturityPeriod2

class TimeToMaturity2Choice(base_types._BaseFieldType):

	__slots__ = ["_Prd", "_Spcl"]
	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != base_types.auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	@property
	def Spcl(self):
		return self._Spcl

	@Spcl.setter
	def Spcl(self, value):
		self._Spcl = value if type(value) != base_types.auto else self.make_default("Spcl")

	@Spcl.deleter
	def Spcl(self):
		del self._Spcl
		self._Spcl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prd', type=TimeToMaturityPeriod2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Spcl', type=SpecialPurpose2Code, min=0, max=1, mutex_group=1, array=False),
	))