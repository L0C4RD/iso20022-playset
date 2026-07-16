# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class AirportDescription1(base_types._BaseFieldType):

	__slots__ = ["_AirprtNm", "_Twn"]
	@property
	def AirprtNm(self):
		return self._AirprtNm

	@AirprtNm.setter
	def AirprtNm(self, value):
		self._AirprtNm = value if value is not None else base_types.UninitialisedField(self, 'AirprtNm', Max35Text, False)

	@AirprtNm.deleter
	def AirprtNm(self):
		del self._AirprtNm
		self._AirprtNm = base_types.UninitialisedField(self, 'AirprtNm', Max35Text, False)

	@property
	def Twn(self):
		return self._Twn

	@Twn.setter
	def Twn(self, value):
		self._Twn = value if value is not None else base_types.UninitialisedField(self, 'Twn', Max35Text, False)

	@Twn.deleter
	def Twn(self):
		del self._Twn
		self._Twn = base_types.UninitialisedField(self, 'Twn', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AirprtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Twn', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))