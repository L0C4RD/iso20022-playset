# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Modification1Code
from . import PostalAddress27

class AddressModification3(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_ModCd"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', PostalAddress27, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', PostalAddress27, False)

	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if value is not None else base_types.UninitialisedField(self, 'ModCd', Modification1Code, False)

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = base_types.UninitialisedField(self, 'ModCd', Modification1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=PostalAddress27, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
	))