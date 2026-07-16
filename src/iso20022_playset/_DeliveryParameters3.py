# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import NameAndAddress4

class DeliveryParameters3(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_IssdCertNb"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', NameAndAddress4, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', NameAndAddress4, False)

	@property
	def IssdCertNb(self):
		return self._IssdCertNb

	@IssdCertNb.setter
	def IssdCertNb(self, value):
		self._IssdCertNb = value if value is not None else base_types.UninitialisedField(self, 'IssdCertNb', Max35Text, False)

	@IssdCertNb.deleter
	def IssdCertNb(self):
		del self._IssdCertNb
		self._IssdCertNb = base_types.UninitialisedField(self, 'IssdCertNb', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=NameAndAddress4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssdCertNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))