# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import SNA2008SectorIdentifier

class SectorAndLocation1(base_types._BaseFieldType):

	__slots__ = ["_Lctn", "_Sctr"]
	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if value is not None else base_types.UninitialisedField(self, 'Lctn', CountryCode, False)

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = base_types.UninitialisedField(self, 'Lctn', CountryCode, False)

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if value is not None else base_types.UninitialisedField(self, 'Sctr', SNA2008SectorIdentifier, False)

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = base_types.UninitialisedField(self, 'Sctr', SNA2008SectorIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lctn', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=SNA2008SectorIdentifier, min=1, max=1, mutex_group=None, array=False),
	))