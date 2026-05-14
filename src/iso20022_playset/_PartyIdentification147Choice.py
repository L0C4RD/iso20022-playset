# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BICFIDec2014Identifier import BICFIDec2014Identifier
from ._GenericIdentification84 import GenericIdentification84
from ._NameAndAddress12 import NameAndAddress12

class PartyIdentification147Choice(base_types._BaseFieldType):

	__slots__ = ["_BICFI", "_NmAndAdr", "_PrtryId"]
	@property
	def BICFI(self):
		return self._BICFI

	@BICFI.setter
	def BICFI(self, value):
		self._BICFI = value if type(value) != base_types.auto else self.make_default("BICFI")

	@BICFI.deleter
	def BICFI(self):
		del self._BICFI
		self._BICFI = None

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
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != base_types.auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BICFI', type=BICFIDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification84, min=0, max=1, mutex_group=1, array=False),
	))