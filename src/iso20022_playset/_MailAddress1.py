# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max256Text
from . import PostalAddress1

class MailAddress1(base_types._BaseFieldType):

	__slots__ = ["_Crspdc", "_EmailAdr"]
	@property
	def Crspdc(self):
		return self._Crspdc

	@Crspdc.setter
	def Crspdc(self, value):
		self._Crspdc = value if value is not None else base_types.UninitialisedField(self, 'Crspdc', PostalAddress1, True)

	@Crspdc.deleter
	def Crspdc(self):
		del self._Crspdc
		self._Crspdc = base_types.UninitialisedField(self, 'Crspdc', PostalAddress1, True)

	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if value is not None else base_types.UninitialisedField(self, 'EmailAdr', Max256Text, True)

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = base_types.UninitialisedField(self, 'EmailAdr', Max256Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Crspdc', type=PostalAddress1, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=5, mutex_group=None, array=True),
	))