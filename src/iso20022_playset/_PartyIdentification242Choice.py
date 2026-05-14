# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NameAndAddress8 import NameAndAddress8
from ._PartyIdentification265 import PartyIdentification265
from ._PartyIdentification266 import PartyIdentification266

class PartyIdentification242Choice(base_types._BaseFieldType):

	__slots__ = ["_AnyBIC", "_NmAndAdr", "_PtyId"]
	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if type(value) != base_types.auto else self.make_default("AnyBIC")

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = None

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

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnyBIC', type=PartyIdentification265, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification266, min=0, max=1, mutex_group=1, array=False),
	))