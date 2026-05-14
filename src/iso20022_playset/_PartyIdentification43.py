# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContactDetails2 import ContactDetails2
from ._CountryCode import CountryCode
from ._Max140Text import Max140Text
from ._Party11Choice import Party11Choice
from ._PostalAddress6 import PostalAddress6

class PartyIdentification43(base_types._BaseFieldType):

	__slots__ = ["_CtctDtls", "_CtryOfRes", "_Id", "_Nm", "_PstlAdr"]
	@property
	def CtctDtls(self):
		return self._CtctDtls

	@CtctDtls.setter
	def CtctDtls(self, value):
		self._CtctDtls = value if type(value) != base_types.auto else self.make_default("CtctDtls")

	@CtctDtls.deleter
	def CtctDtls(self):
		del self._CtctDtls
		self._CtctDtls = None

	@property
	def CtryOfRes(self):
		return self._CtryOfRes

	@CtryOfRes.setter
	def CtryOfRes(self, value):
		self._CtryOfRes = value if type(value) != base_types.auto else self.make_default("CtryOfRes")

	@CtryOfRes.deleter
	def CtryOfRes(self):
		del self._CtryOfRes
		self._CtryOfRes = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if type(value) != base_types.auto else self.make_default("PstlAdr")

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctDtls', type=ContactDetails2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfRes', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Party11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress6, min=0, max=1, mutex_group=None, array=False),
	))