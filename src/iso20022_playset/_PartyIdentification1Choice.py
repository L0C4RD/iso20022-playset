# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICIdentifier
from . import GenericIdentification1
from . import NameAndAddress2

class PartyIdentification1Choice(base_types._BaseFieldType):

	__slots__ = ["_BICOrBEI", "_NmAndAdr", "_PrtryId"]
	@property
	def BICOrBEI(self):
		return self._BICOrBEI

	@BICOrBEI.setter
	def BICOrBEI(self, value):
		self._BICOrBEI = value if value is not None else base_types.UninitialisedField(self, 'BICOrBEI', AnyBICIdentifier, False)

	@BICOrBEI.deleter
	def BICOrBEI(self):
		del self._BICOrBEI
		self._BICOrBEI = base_types.UninitialisedField(self, 'BICOrBEI', AnyBICIdentifier, False)

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if value is not None else base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress2, False)

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress2, False)

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if value is not None else base_types.UninitialisedField(self, 'PrtryId', GenericIdentification1, False)

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = base_types.UninitialisedField(self, 'PrtryId', GenericIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BICOrBEI', type=AnyBICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
	))