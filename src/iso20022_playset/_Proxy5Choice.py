# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ProxyAppointmentInformation6
from . import ProxyNotAllowed1Code

class Proxy5Choice(base_types._BaseFieldType):

	__slots__ = ["_Prxy", "_PrxyNotAllwd"]
	@property
	def Prxy(self):
		return self._Prxy

	@Prxy.setter
	def Prxy(self, value):
		self._Prxy = value if value is not None else base_types.UninitialisedField(self, 'Prxy', ProxyAppointmentInformation6, False)

	@Prxy.deleter
	def Prxy(self):
		del self._Prxy
		self._Prxy = base_types.UninitialisedField(self, 'Prxy', ProxyAppointmentInformation6, False)

	@property
	def PrxyNotAllwd(self):
		return self._PrxyNotAllwd

	@PrxyNotAllwd.setter
	def PrxyNotAllwd(self, value):
		self._PrxyNotAllwd = value if value is not None else base_types.UninitialisedField(self, 'PrxyNotAllwd', ProxyNotAllowed1Code, False)

	@PrxyNotAllwd.deleter
	def PrxyNotAllwd(self):
		del self._PrxyNotAllwd
		self._PrxyNotAllwd = base_types.UninitialisedField(self, 'PrxyNotAllwd', ProxyNotAllowed1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prxy', type=ProxyAppointmentInformation6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrxyNotAllwd', type=ProxyNotAllowed1Code, min=0, max=1, mutex_group=1, array=False),
	))