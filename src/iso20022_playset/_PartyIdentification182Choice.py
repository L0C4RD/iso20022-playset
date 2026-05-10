from . import base_types
from .Max35Text import Max35Text
from .AnyBICDec2014Identifier import AnyBICDec2014Identifier
from .NameAndAddress15 import NameAndAddress15
from .GenericIdentification1 import GenericIdentification1

class PartyIdentification182Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtryId", "_NtlRegnNb", "_NmAndAdr", "_TaxIdNb", "_AnyBIC"]
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
	def TaxIdNb(self):
		return self._TaxIdNb

	@TaxIdNb.setter
	def TaxIdNb(self, value):
		self._TaxIdNb = value if type(value) != base_types.auto else self.make_default("TaxIdNb")

	@TaxIdNb.deleter
	def TaxIdNb(self):
		del self._TaxIdNb
		self._TaxIdNb = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtlRegnNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress15, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TaxIdNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
	))

