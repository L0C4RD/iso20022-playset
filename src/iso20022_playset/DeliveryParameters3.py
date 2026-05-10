import base_types
import Max35Text
import NameAndAddress4

class DeliveryParameters3(base_types._BaseFieldType):

	__slots__ = ["_IssdCertNb", "_Adr"]
	@property
	def IssdCertNb(self):
		return self._IssdCertNb

	@IssdCertNb.setter
	def IssdCertNb(self, value):
		self._IssdCertNb = value if type(value) != auto else self.make_default("IssdCertNb")

	@IssdCertNb.deleter
	def IssdCertNb(self):
		del self._IssdCertNb
		self._IssdCertNb = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IssdCertNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=NameAndAddress4, min=1, max=1, mutex_group=None, array=False),
	))

