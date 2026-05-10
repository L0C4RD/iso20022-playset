import base_types
import Header70
import ContentInformationType37
import AcceptorAuthorisationRequest14

class AcceptorAuthorisationRequestV14(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_AuthstnReq", "_SctyTrlr"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def AuthstnReq(self):
		return self._AuthstnReq

	@AuthstnReq.setter
	def AuthstnReq(self, value):
		self._AuthstnReq = value if type(value) != auto else self.make_default("AuthstnReq")

	@AuthstnReq.deleter
	def AuthstnReq(self):
		del self._AuthstnReq
		self._AuthstnReq = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnReq', type=AcceptorAuthorisationRequest14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
	))

