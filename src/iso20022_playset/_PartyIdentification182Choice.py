# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICDec2014Identifier
from . import GenericIdentification1
from . import Max35Text
from . import NameAndAddress15

class PartyIdentification182Choice(base_types._BaseFieldType):

	__slots__ = ["_AnyBIC", "_NmAndAdr", "_NtlRegnNb", "_PrtryId", "_TaxIdNb"]
	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if value is not None else base_types.UninitialisedField(self, 'AnyBIC', AnyBICDec2014Identifier, False)

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = base_types.UninitialisedField(self, 'AnyBIC', AnyBICDec2014Identifier, False)

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if value is not None else base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress15, False)

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress15, False)

	@property
	def NtlRegnNb(self):
		return self._NtlRegnNb

	@NtlRegnNb.setter
	def NtlRegnNb(self, value):
		self._NtlRegnNb = value if value is not None else base_types.UninitialisedField(self, 'NtlRegnNb', Max35Text, False)

	@NtlRegnNb.deleter
	def NtlRegnNb(self):
		del self._NtlRegnNb
		self._NtlRegnNb = base_types.UninitialisedField(self, 'NtlRegnNb', Max35Text, False)

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

	@property
	def TaxIdNb(self):
		return self._TaxIdNb

	@TaxIdNb.setter
	def TaxIdNb(self, value):
		self._TaxIdNb = value if value is not None else base_types.UninitialisedField(self, 'TaxIdNb', Max35Text, False)

	@TaxIdNb.deleter
	def TaxIdNb(self):
		del self._TaxIdNb
		self._TaxIdNb = base_types.UninitialisedField(self, 'TaxIdNb', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress15, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtlRegnNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TaxIdNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))