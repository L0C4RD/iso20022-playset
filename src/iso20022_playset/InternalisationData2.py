import base_types
import InternalisationDataVolume1

class InternalisationData2(base_types._BaseFieldType):

	__slots__ = ["_Faild", "_Ttl", "_Sttld"]
	@property
	def Faild(self):
		return self._Faild

	@Faild.setter
	def Faild(self, value):
		self._Faild = value if type(value) != auto else self.make_default("Faild")

	@Faild.deleter
	def Faild(self):
		del self._Faild
		self._Faild = None

	@property
	def Ttl(self):
		return self._Ttl

	@Ttl.setter
	def Ttl(self, value):
		self._Ttl = value if type(value) != auto else self.make_default("Ttl")

	@Ttl.deleter
	def Ttl(self):
		del self._Ttl
		self._Ttl = None

	@property
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if type(value) != auto else self.make_default("Sttld")

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Faild', type=InternalisationDataVolume1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ttl', type=InternalisationDataVolume1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttld', type=InternalisationDataVolume1, min=1, max=1, mutex_group=None, array=False),
	))

