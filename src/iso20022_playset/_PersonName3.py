# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import NamePrefix2Code
from . import PostalAddress26

class PersonName3(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_FrstNm", "_NmPrfx", "_Srnm"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', PostalAddress26, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', PostalAddress26, False)

	@property
	def FrstNm(self):
		return self._FrstNm

	@FrstNm.setter
	def FrstNm(self, value):
		self._FrstNm = value if value is not None else base_types.UninitialisedField(self, 'FrstNm', Max350Text, False)

	@FrstNm.deleter
	def FrstNm(self):
		del self._FrstNm
		self._FrstNm = base_types.UninitialisedField(self, 'FrstNm', Max350Text, False)

	@property
	def NmPrfx(self):
		return self._NmPrfx

	@NmPrfx.setter
	def NmPrfx(self, value):
		self._NmPrfx = value if value is not None else base_types.UninitialisedField(self, 'NmPrfx', NamePrefix2Code, False)

	@NmPrfx.deleter
	def NmPrfx(self):
		del self._NmPrfx
		self._NmPrfx = base_types.UninitialisedField(self, 'NmPrfx', NamePrefix2Code, False)

	@property
	def Srnm(self):
		return self._Srnm

	@Srnm.setter
	def Srnm(self, value):
		self._Srnm = value if value is not None else base_types.UninitialisedField(self, 'Srnm', Max350Text, False)

	@Srnm.deleter
	def Srnm(self):
		del self._Srnm
		self._Srnm = base_types.UninitialisedField(self, 'Srnm', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=PostalAddress26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmPrfx', type=NamePrefix2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Srnm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))