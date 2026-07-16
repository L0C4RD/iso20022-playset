# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max10KBinary
from . import Max140Binary
from . import Max35Binary
from . import Max35Text
from . import NetworkParameters9

class NetworkParameters7(base_types._BaseFieldType):

	__slots__ = ["_AccsCd", "_Adr", "_ClntCert", "_SctyPrfl", "_SvrCert", "_SvrCertIdr", "_UsrNm"]
	@property
	def AccsCd(self):
		return self._AccsCd

	@AccsCd.setter
	def AccsCd(self, value):
		self._AccsCd = value if value is not None else base_types.UninitialisedField(self, 'AccsCd', Max35Binary, False)

	@AccsCd.deleter
	def AccsCd(self):
		del self._AccsCd
		self._AccsCd = base_types.UninitialisedField(self, 'AccsCd', Max35Binary, False)

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', NetworkParameters9, True)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', NetworkParameters9, True)

	@property
	def ClntCert(self):
		return self._ClntCert

	@ClntCert.setter
	def ClntCert(self, value):
		self._ClntCert = value if value is not None else base_types.UninitialisedField(self, 'ClntCert', Max10KBinary, True)

	@ClntCert.deleter
	def ClntCert(self):
		del self._ClntCert
		self._ClntCert = base_types.UninitialisedField(self, 'ClntCert', Max10KBinary, True)

	@property
	def SctyPrfl(self):
		return self._SctyPrfl

	@SctyPrfl.setter
	def SctyPrfl(self, value):
		self._SctyPrfl = value if value is not None else base_types.UninitialisedField(self, 'SctyPrfl', Max35Text, False)

	@SctyPrfl.deleter
	def SctyPrfl(self):
		del self._SctyPrfl
		self._SctyPrfl = base_types.UninitialisedField(self, 'SctyPrfl', Max35Text, False)

	@property
	def SvrCert(self):
		return self._SvrCert

	@SvrCert.setter
	def SvrCert(self, value):
		self._SvrCert = value if value is not None else base_types.UninitialisedField(self, 'SvrCert', Max10KBinary, True)

	@SvrCert.deleter
	def SvrCert(self):
		del self._SvrCert
		self._SvrCert = base_types.UninitialisedField(self, 'SvrCert', Max10KBinary, True)

	@property
	def SvrCertIdr(self):
		return self._SvrCertIdr

	@SvrCertIdr.setter
	def SvrCertIdr(self, value):
		self._SvrCertIdr = value if value is not None else base_types.UninitialisedField(self, 'SvrCertIdr', Max140Binary, True)

	@SvrCertIdr.deleter
	def SvrCertIdr(self):
		del self._SvrCertIdr
		self._SvrCertIdr = base_types.UninitialisedField(self, 'SvrCertIdr', Max140Binary, True)

	@property
	def UsrNm(self):
		return self._UsrNm

	@UsrNm.setter
	def UsrNm(self, value):
		self._UsrNm = value if value is not None else base_types.UninitialisedField(self, 'UsrNm', Max35Text, False)

	@UsrNm.deleter
	def UsrNm(self):
		del self._UsrNm
		self._UsrNm = base_types.UninitialisedField(self, 'UsrNm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccsCd', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=NetworkParameters9, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClntCert', type=Max10KBinary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyPrfl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvrCert', type=Max10KBinary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvrCertIdr', type=Max140Binary, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UsrNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))