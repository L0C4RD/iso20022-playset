# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AnyBICDec2014Identifier import AnyBICDec2014Identifier
from ._GenericIdentification36 import GenericIdentification36
from ._LEIIdentifier import LEIIdentifier
from ._Max35Text import Max35Text
from ._Max50Text import Max50Text

class PartyIdentification198Choice(base_types._BaseFieldType):

	__slots__ = ["_AnyBIC", "_ClntId", "_LEI", "_NtlRegnNb", "_PrtryId"]
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
	def ClntId(self):
		return self._ClntId

	@ClntId.setter
	def ClntId(self, value):
		self._ClntId = value if type(value) != base_types.auto else self.make_default("ClntId")

	@ClntId.deleter
	def ClntId(self):
		del self._ClntId
		self._ClntId = None

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def NtlRegnNb(self):
		return self._NtlRegnNb

	@NtlRegnNb.setter
	def NtlRegnNb(self, value):
		self._NtlRegnNb = value if type(value) != base_types.auto else self.make_default("NtlRegnNb")

	@NtlRegnNb.deleter
	def NtlRegnNb(self):
		del self._NtlRegnNb
		self._NtlRegnNb = None

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
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ClntId', type=Max50Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtlRegnNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
	))