# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max350Text import Max350Text
from ._PostalAddress26 import PostalAddress26

class PersonName1(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_FrstNm", "_Srnm"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def FrstNm(self):
		return self._FrstNm

	@FrstNm.setter
	def FrstNm(self, value):
		self._FrstNm = value if type(value) != base_types.auto else self.make_default("FrstNm")

	@FrstNm.deleter
	def FrstNm(self):
		del self._FrstNm
		self._FrstNm = None

	@property
	def Srnm(self):
		return self._Srnm

	@Srnm.setter
	def Srnm(self, value):
		self._Srnm = value if type(value) != base_types.auto else self.make_default("Srnm")

	@Srnm.deleter
	def Srnm(self):
		del self._Srnm
		self._Srnm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=PostalAddress26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Srnm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))