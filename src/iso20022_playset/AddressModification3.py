from . import base_types
import Modification1Code
import PostalAddress27

class AddressModification3(base_types._BaseFieldType):

	__slots__ = ["_ModCd", "_Adr"]
	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if type(value) != auto else self.make_default("ModCd")

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = None

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
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=PostalAddress27, min=1, max=1, mutex_group=None, array=False),
	))

