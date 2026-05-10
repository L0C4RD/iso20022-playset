import base_types
import AcquirerToAcceptorFileBody2
import ResponseType11
import Header56
import ContentInformationType38

class AcquirerToAcceptorBatchFileExchangeV02(base_types._BaseFieldType):

	__slots__ = ["_BodyElmt", "_Rspn", "_SctyTrlr", "_Hdr"]
	@property
	def BodyElmt(self):
		return self._BodyElmt

	@BodyElmt.setter
	def BodyElmt(self, value):
		self._BodyElmt = value if type(value) != auto else self.make_default("BodyElmt")

	@BodyElmt.deleter
	def BodyElmt(self):
		del self._BodyElmt
		self._BodyElmt = None

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if type(value) != auto else self.make_default("Rspn")

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = None

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
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BodyElmt', type=AcquirerToAcceptorFileBody2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header56, min=1, max=1, mutex_group=None, array=False),
	))

