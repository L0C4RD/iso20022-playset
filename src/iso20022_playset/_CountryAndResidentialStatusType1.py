# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CountryCode import CountryCode
from ._ResidentialStatus1Code import ResidentialStatus1Code

class CountryAndResidentialStatusType1(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_ResdtlSts"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def ResdtlSts(self):
		return self._ResdtlSts

	@ResdtlSts.setter
	def ResdtlSts(self, value):
		self._ResdtlSts = value if type(value) != base_types.auto else self.make_default("ResdtlSts")

	@ResdtlSts.deleter
	def ResdtlSts(self):
		del self._ResdtlSts
		self._ResdtlSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ResdtlSts', type=ResidentialStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))