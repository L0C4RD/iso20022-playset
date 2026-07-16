# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IssuerAndSerialNumber1
from . import KEKIdentifier2

class Recipient5Choice(base_types._BaseFieldType):

	__slots__ = ["_IssrAndSrlNb", "_KeyIdr"]
	@property
	def IssrAndSrlNb(self):
		return self._IssrAndSrlNb

	@IssrAndSrlNb.setter
	def IssrAndSrlNb(self, value):
		self._IssrAndSrlNb = value if value is not None else base_types.UninitialisedField(self, 'IssrAndSrlNb', IssuerAndSerialNumber1, False)

	@IssrAndSrlNb.deleter
	def IssrAndSrlNb(self):
		del self._IssrAndSrlNb
		self._IssrAndSrlNb = base_types.UninitialisedField(self, 'IssrAndSrlNb', IssuerAndSerialNumber1, False)

	@property
	def KeyIdr(self):
		return self._KeyIdr

	@KeyIdr.setter
	def KeyIdr(self, value):
		self._KeyIdr = value if value is not None else base_types.UninitialisedField(self, 'KeyIdr', KEKIdentifier2, False)

	@KeyIdr.deleter
	def KeyIdr(self):
		del self._KeyIdr
		self._KeyIdr = base_types.UninitialisedField(self, 'KeyIdr', KEKIdentifier2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IssrAndSrlNb', type=IssuerAndSerialNumber1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyIdr', type=KEKIdentifier2, min=0, max=1, mutex_group=1, array=False),
	))