# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PlaceType1Code
from . import PostalAddress1

class LocationFormat1Choice(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_LctnCd"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', PostalAddress1, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', PostalAddress1, False)

	@property
	def LctnCd(self):
		return self._LctnCd

	@LctnCd.setter
	def LctnCd(self, value):
		self._LctnCd = value if value is not None else base_types.UninitialisedField(self, 'LctnCd', PlaceType1Code, False)

	@LctnCd.deleter
	def LctnCd(self):
		del self._LctnCd
		self._LctnCd = base_types.UninitialisedField(self, 'LctnCd', PlaceType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=PostalAddress1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LctnCd', type=PlaceType1Code, min=0, max=1, mutex_group=1, array=False),
	))