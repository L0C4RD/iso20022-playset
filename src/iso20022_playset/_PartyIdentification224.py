# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max256Text import Max256Text
from ._PartyIdentification198Choice import PartyIdentification198Choice
from ._PersonName2 import PersonName2

class PartyIdentification224(base_types._BaseFieldType):

	__slots__ = ["_EmailAdr", "_Id", "_NmAndAdr"]
	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if type(value) != base_types.auto else self.make_default("EmailAdr")

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = None

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
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != base_types.auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification198Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=PersonName2, min=1, max=1, mutex_group=None, array=False),
	))