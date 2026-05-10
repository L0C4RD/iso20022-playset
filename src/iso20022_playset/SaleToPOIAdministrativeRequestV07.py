import base_types
import Header41
import AdministrativeRequest8
import ContentInformationType38

class SaleToPOIAdministrativeRequestV07(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_AdmstvReq"]
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
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def AdmstvReq(self):
		return self._AdmstvReq

	@AdmstvReq.setter
	def AdmstvReq(self, value):
		self._AdmstvReq = value if type(value) != auto else self.make_default("AdmstvReq")

	@AdmstvReq.deleter
	def AdmstvReq(self):
		del self._AdmstvReq
		self._AdmstvReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdmstvReq', type=AdministrativeRequest8, min=1, max=1, mutex_group=None, array=False),
	))

