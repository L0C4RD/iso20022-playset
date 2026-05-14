# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AnyBICIdentifier import AnyBICIdentifier
from ._GenericIdentification1 import GenericIdentification1
from ._NameAndAddress5 import NameAndAddress5

class PartyIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_BICOrBEI", "_NmAndAdr", "_PrtryId"]
	@property
	def BICOrBEI(self):
		return self._BICOrBEI

	@BICOrBEI.setter
	def BICOrBEI(self, value):
		self._BICOrBEI = value if type(value) != base_types.auto else self.make_default("BICOrBEI")

	@BICOrBEI.deleter
	def BICOrBEI(self):
		del self._BICOrBEI
		self._BICOrBEI = None

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
		base_types.FieldEntry(name='BICOrBEI', type=AnyBICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
	))