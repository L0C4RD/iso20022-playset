import base_types
import Max35Text
import NetworkParameters9
import Max35Binary
import Max140Binary
import Max10KBinary

class NetworkParameters7(base_types._BaseFieldType):

	__slots__ = ["_AccsCd", "_SvrCertIdr", "_SctyPrfl", "_ClntCert", "_SvrCert", "_UsrNm", "_Adr"]
	@property
	def AccsCd(self):
		return self._AccsCd

	@AccsCd.setter
	def AccsCd(self, value):
		self._AccsCd = value if type(value) != auto else self.make_default("AccsCd")

	@AccsCd.deleter
	def AccsCd(self):
		del self._AccsCd
		self._AccsCd = None

	@property
	def SvrCertIdr(self):
		return self._SvrCertIdr

	@SvrCertIdr.setter
	def SvrCertIdr(self, value):
		self._SvrCertIdr = value if type(value) != auto else self.make_default("SvrCertIdr")

	@SvrCertIdr.deleter
	def SvrCertIdr(self):
		del self._SvrCertIdr
		self._SvrCertIdr = None

	@property
	def SctyPrfl(self):
		return self._SctyPrfl

	@SctyPrfl.setter
	def SctyPrfl(self, value):
		self._SctyPrfl = value if type(value) != auto else self.make_default("SctyPrfl")

	@SctyPrfl.deleter
	def SctyPrfl(self):
		del self._SctyPrfl
		self._SctyPrfl = None

	@property
	def ClntCert(self):
		return self._ClntCert

	@ClntCert.setter
	def ClntCert(self, value):
		self._ClntCert = value if type(value) != auto else self.make_default("ClntCert")

	@ClntCert.deleter
	def ClntCert(self):
		del self._ClntCert
		self._ClntCert = None

	@property
	def SvrCert(self):
		return self._SvrCert

	@SvrCert.setter
	def SvrCert(self, value):
		self._SvrCert = value if type(value) != auto else self.make_default("SvrCert")

	@SvrCert.deleter
	def SvrCert(self):
		del self._SvrCert
		self._SvrCert = None

	@property
	def UsrNm(self):
		return self._UsrNm

	@UsrNm.setter
	def UsrNm(self, value):
		self._UsrNm = value if type(value) != auto else self.make_default("UsrNm")

	@UsrNm.deleter
	def UsrNm(self):
		del self._UsrNm
		self._UsrNm = None

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
		base_types.FieldEntry(name='AccsCd', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvrCertIdr', type=Max140Binary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyPrfl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntCert', type=Max10KBinary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvrCert', type=Max10KBinary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UsrNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=NetworkParameters9, min=1, max=None, mutex_group=None, array=True),
	))

